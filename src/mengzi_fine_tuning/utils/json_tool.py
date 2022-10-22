import json
from typing import Any

from .string_tool import readLines, readString, writeLines, writeString


def jsonEncode(data: Any, pretty=True):
    indent = 4 if pretty else None
    return json.dumps(data, ensure_ascii=False, indent=indent)


def jsonDecode(string: str):
    return json.loads(string)


def readJSON(nameOrPath: str):
    return jsonDecode(readString(nameOrPath))


def writeJSON(nameOrPath: str, data):
    writeString(nameOrPath, jsonEncode(data))


def readJSONs(nameOrPath: str) -> list[Any]:
    return [jsonDecode(line) for line in readLines(nameOrPath)]


def writeJSONs(nameOrPath: str, datas: list[Any]):
    writeLines(nameOrPath, [jsonEncode(data, pretty=False) for data in datas])
