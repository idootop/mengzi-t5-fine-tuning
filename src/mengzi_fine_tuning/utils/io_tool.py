from pathlib import Path

from .basic import isNotEmpty


# 数据存放路径
kDataRoot = "./data"


def exists(path: str):
    """
    判断文件路径是否存在
    """
    return Path(path).exists()


def makeDir(_dir="", filePath=""):
    """
    自动补全文件所在的文件夹路径，如果父级文件夹不存在
    """
    if isNotEmpty(_dir):
        Path(_dir).mkdir(parents=True, exist_ok=True)
    else:
        Path(filePath).parent.mkdir(parents=True, exist_ok=True)


def getFilePath(nameOrPath: str):
    """
    获取文件路径，默认目录为 `./data`

    ```python
    - getFilePath('test.csv') # ./data/test.csv
    - getFilePath('subdir/test.csv') # ./data/subdir/test.csv
    - getFilePath('./data/test.csv') # ./data/test.csv
    - getFilePath('/Users/desktop/test.csv') # /Users/desktop/test.csv
    - getFilePath('C:\\Users\\desktop\\test.csv') # C:\\Users\\desktop\\test.csv
    ```
    """
    splits = nameOrPath.split(".")
    suffix = splits[-1] if len(splits) > 1 else ""
    nameOrPath = nameOrPath.replace("\\", "/").replace(f".{suffix}", "")
    isPath = (
        nameOrPath.startswith("/") or nameOrPath.startswith("./") or ":/" in nameOrPath
    )
    if isPath:
        path = f"{nameOrPath}.{suffix}"
    else:
        path = f"{kDataRoot}/{nameOrPath}.{suffix}"
    return path


def readString(nameOrPath: str):
    path = getFilePath(nameOrPath)
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    return data


def writeString(nameOrPath: str, text: str, append=False):
    path = getFilePath(nameOrPath)
    # 文件读写模式参考 https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
    mode = "a" if append else "w"
    with open(path, mode, encoding="utf-8") as f:
        f.write(text)


def readLines(nameOrPath: str):
    path = getFilePath(nameOrPath)
    with open(path, "r", encoding="utf-8") as f:
        data = f.readlines()
    return data


def writeLines(nameOrPath: str, lines: list[str], append=False):
    path = getFilePath(nameOrPath)
    mode = "a+" if append else "w"
    with open(path, mode, encoding="utf-8") as f:
        f.seek(0)  # 回到文件顶部
        data = f.read(100)
        if len(data) > 0:
            f.write("\n")  # 如果文件内容非空，自动换行
        f.writelines(f"{s}\n" for s in lines)
