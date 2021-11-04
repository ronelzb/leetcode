import os
from typing import List


def getFiles(directory: str, output: str = "", level: int = 0) -> List[str]:
    global toc_links
    dir_files = os.listdir(directory)
    files_full_path = []

    for file in dir_files:
        if file in exclude:
            continue

        link_str = os.path.splitext(file)[0].split("_")
        link_str[0] = str(int(link_str[0])) + "." if link_str[0].isdigit() else link_str[0]
        toc_links.append((" " * (level * 4)) + "* " +
                         "[" + " ".join(link_str) + "]" +
                         "(" + github_repo_branch + output + "/" + file + ")")

        file_path = os.path.join(directory, file)
        if os.path.isdir(file_path):
            files_full_path = files_full_path + getFiles(file_path, output + "/" + file, level + 1)
        else:
            files_full_path.append(file_path)

    return files_full_path


exclude = {"venv", "node_modules", ".idea", ".git", ".gitignore", "work_in_progress", "test", "README.md",
           "utils"}
dirName = os.path.dirname(os.getcwd())
github_repo_branch = "https://github.com/ronelzb/leetcode/tree/master"
toc_links = []
files = getFiles(dirName)
print("\n".join(toc_links))
