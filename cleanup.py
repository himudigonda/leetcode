#!/usr/bin/env python3

import os
import re
import json
import shutil
import urllib.request
import urllib.error
from tqdm import tqdm

LC_ENDPOINT = "https://leetcode.com/graphql"
GQL_QUERY = """
query getQuestionDetail($titleSlug:String!){
  question(titleSlug:$titleSlug){
    difficulty
    topicTags { name }
  }
}
"""
SLUG_RE = re.compile(r"https?://leetcode\.com/problems/([\w-]+)/?")
HEADERS = {
    "Content-Type": "application/json",
    "Referer": None,
    "Origin": "https://leetcode.com",
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json, text/plain, */*",
}


def sanitize(name):
    return re.sub(r"[^A-Za-z0-9-]", "", name.replace(" ", "-"))


def extract_slug(readme_path):
    with open(readme_path, encoding="utf-8") as f:
        m = SLUG_RE.search(f.read())
        return m.group(1) if m else None


def fetch_metadata(slug):
    payload = json.dumps({"query": GQL_QUERY, "variables": {"titleSlug": slug}}).encode(
        "utf-8"
    )
    HEADERS["Referer"] = f"https://leetcode.com/problems/{slug}/"
    req = urllib.request.Request(LC_ENDPOINT, data=payload, headers=HEADERS)
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode("utf-8"))
    q = data.get("data", {}).get("question")
    if not q:
        raise RuntimeError("No question data for slug")
    return q["difficulty"].lower(), [t.get("name") for t in q.get("topicTags", [])]


def main():
    cwd = os.getcwd()
    metadata = {}
    unique_problems = {}
    difficulty_counts = {}
    tag_counts = {}

    # Collect all candidate folders
    all_dirs = []
    for root, _, files in os.walk(cwd):
        if root == cwd or "/.git" in root or "/.vscode" in root:
            continue
        if any(f.lower() == "readme.md" for f in files):
            all_dirs.append(root)

    for root in tqdm(all_dirs, desc="📂 Organizing Problems"):
        entry = os.path.basename(root)
        readme = next(
            (
                os.path.join(root, fn)
                for fn in ("README.md", "readme.md", "Readme.md")
                if os.path.isfile(os.path.join(root, fn))
            ),
            None,
        )
        if not readme:
            continue

        slug = extract_slug(readme)
        if not slug or slug in unique_problems:
            continue

        try:
            diff, tags = fetch_metadata(slug)
        except Exception:
            continue
        if not tags:
            continue

        unique_problems[slug] = {"difficulty": diff, "tags": tags, "entry": entry}
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
                if os.path.abspath(dest) != os.path.abspath(root):
                    if os.path.exists(dest):
                        shutil.rmtree(dest)
                    shutil.move(root, dest)
                first_dest = dest
            else:
                if first_dest:
                    if os.path.exists(dest):
                        shutil.rmtree(dest)
                    shutil.copytree(first_dest, dest)
            metadata.setdefault(tag, []).append(
                {"entry": entry, "difficulty": diff.capitalize(), "slug": slug}
            )

    readme_path = os.path.join(cwd, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# LeetCode Solutions Overview\n\n")
        f.write("## 🧮 Summary Stats\n\n")
        f.write(f"**Total Problems Solved:** {len(unique_problems)}\n\n")
        f.write("**By Difficulty:**\n\n")
        f.write("| Difficulty | Count |\n|---|---|\n")
        for d in ["easy", "medium", "hard"]:
            f.write(f"| {d.capitalize()} | {difficulty_counts.get(d, 0)} |\n")
        f.write("\n**By Tag:**\n\n")
        f.write("| Tag | Count |\n|---|---|\n")
        for tag, count in sorted(tag_counts.items(), key=lambda x: -x[1]):
            f.write(f"| {tag} | {count} |\n")
        f.write("\n## Solutions by Tag\n\n")
        for tag, items in metadata.items():
            f.write(f"### {tag}\n\n")
            f.write("| Problem | Difficulty | Code | LeetCode |\n|---|---|---|---|\n")
            for itm in items:
                entry = itm["entry"]
                diff = itm["difficulty"]
                slug = itm["slug"]
                t = sanitize(tag)
                code_link = f"./{t}/{diff.lower()}/{entry}"
                lc_link = f"https://leetcode.com/problems/{slug}/"
                f.write(
                    f"| {entry} | {diff} | [code]({code_link}) | [leetcode]({lc_link}) |\n"
                )
            f.write("\n")

    # Cleanup pass
    for entry in os.listdir(cwd):
        path = os.path.join(cwd, entry)
        if os.path.isdir(path) and not entry.startswith(".") and entry not in metadata:
            if any(
                os.path.isfile(os.path.join(path, f))
                for f in ("README.md", "readme.md", "Readme.md")
            ):
                shutil.rmtree(path)


if __name__ == "__main__":
    main()
