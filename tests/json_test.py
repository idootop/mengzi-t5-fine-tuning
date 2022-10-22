from mengzi_fine_tuning.utils.json_tool import (
    readJSON,
    writeJSON,
    readJSONs,
    writeJSONs,
    jsonEncode,
    jsonDecode,
)

kTestData = "./tests/data/json"

print(">>> 读取JSON")
datas = readJSON(f"{kTestData}/test.json")
print(datas)

writeJSON(f"{kTestData}/test1.json", datas)


writeJSONs(f"{kTestData}/tests.json", [datas, datas, datas])

print(">>> 读取JSONs")
datas = readJSONs(f"{kTestData}/tests.json")
print("\n".join([jsonEncode(data) for data in datas]))

print(">>> json 编解码 list")
jsonStr = jsonEncode(["1哈哈哈", 2, 3])
print(jsonStr)
print(jsonDecode(jsonStr)[0])

print(">>> json 编解码 map")
jsonStr = jsonEncode(
    {
        "help": "sos哈哈哈",
    }
)
print(jsonStr)
print(jsonDecode(jsonStr)["help"])
