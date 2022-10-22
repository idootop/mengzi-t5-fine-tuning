from mengzi_fine_tuning.utils.csv_tool import readCSV, writeCSV

kTestData = "./tests/data/csv"

datas = readCSV(f"{kTestData}/test.csv", split="｜")
print(datas)
writeCSV(f"{kTestData}/test1", datas, split="｜")
writeCSV(f"{kTestData}/test2.csv", datas, split="｜")
