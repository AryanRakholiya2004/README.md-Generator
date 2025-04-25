from collections import defaultdict
from pathlib import Path

def build_file_tree(paths):
    def insert(path_parts, tree):
        part = path_parts[0]
        if len(path_parts) == 1:
            tree[part] = None
        else:
            if part not in tree:
                tree[part] = {}
            insert(path_parts[1:], tree[part])

    file_tree = {}
    for file_path in paths:
        parts = Path(file_path).parts
        insert(list(parts), file_tree)

    return file_tree
