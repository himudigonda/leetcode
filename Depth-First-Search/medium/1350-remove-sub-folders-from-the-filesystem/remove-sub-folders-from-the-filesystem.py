# Optimal init
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_subfolder = False


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # # BruteForce
        # result = []
        # for f1 in folder:
        #     is_subfolder = False

        #     for f2 in folder:
        #         if f1 == f2:
        #             continue
        #         if f1.startswith(f2 + "/") and len(f1) > len(f2):
        #             is_subfolder = True
        #             break
        #     if not is_subfolder:
        #         result.append(f1)
        # return result

        trie_root = TrieNode()

        for path in folder:
            node = trie_root
            components = path.split("/")
            for comp in components[1:]:
                if comp not in node.children:
                    node.children[comp] = TrieNode()
                node = node.children[comp]
            node.is_subfolder = True
        result = []

        def dfs(node, cur_path):
            if node.is_subfolder:
                result.append("/" + "/".join(cur_path))
                return
            for comp, child_node in node.children.items():
                cur_path.append(comp)
                dfs(child_node, cur_path)
                cur_path.pop()

        dfs(trie_root, [])
        return result
