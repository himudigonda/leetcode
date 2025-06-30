#!/usr/bin/env python3
# 
# @AUTHOR: Himansh Mudigonda
# 
# This script organizes LeetCode problem directories, fetches metadata,
# and generates a comprehensive README.md file.
#
# It scans the current directory for problem folders, extracts the LeetCode
# slug from their README.md files, and then queries the LeetCode API
# to get difficulty and topic tags.
#
# Problem directories are then moved/copied into a new structure:
# ./<tag>/<difficulty>/<problem_name>/
#
# Finally, it generates a README.md at the root with a summary of solved
# problems by difficulty and tags, and a detailed list of problems
# categorized by their tags, including links to the code and LeetCode problem page.

import os
import re
import json
import shutil
import urllib.request
import urllib.error

# Configuration
LC_ENDPOINT = "https://leetcode.com/graphql"
GQL_QUERY = '''
query getQuestionDetail($titleSlug:String!){
  question(titleSlug:$titleSlug){
    difficulty
    topicTags { name }
  }
}
'''
# Regex to extract slug
SLUG_RE = re.compile(r"https?://leetcode\.com/problems/([\w-]+)/?")
# HTTP headers to avoid 403
HEADERS = {
    "Content-Type": "application/json",
    "Referer": None,  # set per request
    "Origin": "https://leetcode.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
}

def sanitize(name):
    """
    Sanitize a tag or folder name: spaces to hyphens, remove unsafe chars.
    """
    return re.sub(r"[^A-Za-z0-9-]", "", name.replace(' ', '-'))


def extract_slug(readme_path):
    text = open(readme_path, encoding="utf-8").read()
    m = SLUG_RE.search(text)
    return m.group(1) if m else None


def fetch_metadata(slug):
    payload = json.dumps({
        "query": GQL_QUERY,
        "variables": {"titleSlug": slug}
    }).encode('utf-8')
    HEADERS["Referer"] = f"https://leetcode.com/problems/{slug}/"
    req = urllib.request.Request(LC_ENDPOINT, data=payload, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.reason}")
    q = data.get("data", {}).get("question")
    if not q:
        raise RuntimeError("No question data for slug")
    diff = q["difficulty"].lower()
    tags = [t.get("name") for t in q.get("topicTags", [])]
    return diff, tags


def main():
    cwd = os.getcwd()
    metadata = {}  # tag -> [{entry, diff, slug}]
    unique_problems = {}  # slug -> {difficulty, tags, entry}
    difficulty_counts = {}
    tag_counts = {}

    print(f"\n📂 Scanning directory: {cwd}\n")

    for root, dirs, files in os.walk(cwd):
        # Skip the root itself and hidden/system folders
        if root == cwd or '/.git' in root or '/.vscode' in root:
            continue
        entry = os.path.basename(root)
        print(f"➡️ Scanning: {root}")

        # Locate README
        readme = None
        for fn in ("README.md", "readme.md", "Readme.md"):
            candidate = os.path.join(root, fn)
            if os.path.isfile(candidate):
                readme = candidate
                break
        if not readme:
            print(f"  ⛔ Skipped: No README found in {root}")
            continue

        slug = extract_slug(readme)
        if not slug:
            print(f"  ⚠️ Skipped: No slug found in {readme}")
            continue
        if slug in unique_problems:
            print(f"  🔁 Already counted slug: {slug}, skipping stats")
            continue
        print(f"  ✅ Found slug: {slug}")

        try:
            diff, tags = fetch_metadata(slug)
            print(f"     ↪ difficulty: {diff}, tags: {tags}")
        except Exception as e:
            print(f"  ❌ Fetch error for slug '{slug}': {e}")
            import traceback; traceback.print_exc()
            continue

        if not tags:
            print(f"  ⚠️ No tags returned for {slug}")
            continue

        unique_problems[slug] = {
            'difficulty': diff,
            'tags': tags,
            'entry': entry
        }
        # Count once per unique slug
        difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1
        for tag in tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

        first_dest = None
        for i, tag in enumerate(tags):
            t = sanitize(tag)
            target_dir = os.path.join(cwd, t, diff)
            os.makedirs(target_dir, exist_ok=True)
            dest = os.path.join(target_dir, entry)
            if i == 0:
                if not os.path.exists(dest):
                    shutil.move(root, dest)
                    first_dest = dest
                    print(f"     ✅ Moved to: {t}/{diff}/{entry}")
                else:
                    print(f"     ⚠️ Already exists: {t}/{diff}/{entry}")
                    first_dest = dest
            else:
                if first_dest:
                    if not os.path.exists(dest):
                        shutil.copytree(first_dest, dest)
                        print(f"     📄 Copied to: {t}/{diff}/{entry}")
                    else:
                        print(f"     ⚠️ Skipped copy: {t}/{diff}/{entry} already exists")
            metadata.setdefault(tag, []).append({
                'entry': entry,
                'difficulty': diff.capitalize(),
                'slug': slug
            })

    # Check metadata
    print(f"\n📊 Metadata contains entries for {len(metadata)} tags\n")

    readme_path = os.path.join(cwd, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("# LeetCode Solutions Overview\n\n")
        f.write("## 🧮 Summary Stats\n\n")
        f.write(f"**Total Problems Solved:** {len(unique_problems)}\n\n")
        f.write("**By Difficulty:**\n\n")
        f.write("| Difficulty | Count |\n|---|---|\n")
        for d in ["easy", "medium", "hard"]:
            count = difficulty_counts.get(d, 0)
            f.write(f"| {d.capitalize()} | {count} |\n")
        f.write("\n")
        f.write("**By Tag:**\n\n")
        f.write("| Tag | Count |\n|---|---|\n")
        for tag, count in sorted(tag_counts.items(), key=lambda x: -x[1]):
            f.write(f"| {tag} | {count} |\n")
        f.write("\n")
        f.write("## Solutions by Tag\n\n")
        for tag, items in metadata.items():
            f.write(f"### {tag}\n\n")
            f.write("| Problem | Difficulty | Code | LeetCode |\n")
            f.write("|---|---|---|---|\n")
            for itm in items:
                entry = itm['entry']
                diff = itm['difficulty']
                slug = itm['slug']
                t = sanitize(tag)
                code_link = f"./{t}/{diff.lower()}/{entry}"
                lc_link = f"https://leetcode.com/problems/{slug}/"
                f.write(f"| {entry} | {diff} | [code]({code_link}) | [leetcode]({lc_link}) |\n")
            f.write("\n")

    print("✅ README.md generated.\n")

if __name__ == '__main__':
    main()
