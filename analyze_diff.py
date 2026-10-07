diff = open('diff_b6f3b6a.txt', 'r', encoding='utf-16le', errors='ignore').read()

import re
# We just want to find what was removed from the CSS
removed_lines = [line for line in diff.splitlines() if line.startswith('-') and not line.startswith('---')]

for line in removed_lines:
    if 'autoptimize_65cbc9' in line:
        # The CSS file diff!
        if 'background' in line or 'url' in line:
            print("CSS REMOVED:", line[:200])
