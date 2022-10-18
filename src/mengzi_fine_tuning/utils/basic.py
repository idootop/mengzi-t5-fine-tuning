from pathlib import Path


def isEmpty(obj):
    """
    判断元素是否为 None 或空白字符串
    """
    if not obj:
        return True
    if isinstance(obj, str):
        if obj.isspace():
            return True
    return False


def isNotEmpty(obj):
    return not isEmpty(obj)


def exists(path: str):
    """
    判断文件路径是否存在
    """
    return Path(path).exists()


def makeDir(dir="", filePath=""):
    """
    自动补全文件所在的文件夹路径，如果父级文件夹不存在
    """
    if isNotEmpty(dir):
        Path(dir).mkdir(parents=True, exist_ok=True)
    else:
        Path(filePath).parent.mkdir(parents=True, exist_ok=True)
