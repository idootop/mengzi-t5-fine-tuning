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
