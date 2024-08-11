import sys
import re
from collections import defaultdict

def read_config(config_file):
    replacements = {}
    with open(config_file, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            replacements[key] = value
    return replacements

def replace_values(line, replacements):
    replaced_line = line
    replaced_count = 0
    for key, value in replacements.items():
        replaced_line, count = re.subn(re.escape(key), value, replaced_line)
        replaced_count += count
    return replaced_line, replaced_count

def main():
    if len(sys.argv) != 3:
        print("Use: python cqg_test.py <config_file> <text_file>")
        return
    config_file = sys.argv[1]
    text_file = sys.argv[2]

    replacements = read_config(config_file)

    changed_lines = []

    with open(text_file, 'r') as f:
        for line in f:
            replaced_line, replaced_count = replace_values(line.strip(), replacements)
            changed_lines.append((replaced_line, replaced_count))

    sorted_changed_lines = sorted(changed_lines, key=lambda x: x[1], reverse=True)

    for replaced_line, replaced_count in sorted_changed_lines:
        print(f"{replaced_line} (Replaced: {replaced_count} symbols)")

if __name__ == "__main__":
    main()