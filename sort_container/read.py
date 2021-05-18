data = "data/0001.txt"
with open(data, "r", encoding="utf-8") as datas:
    for row in datas:
        print(row)
        data_container = row.strip('\n').split("\t")
        print(data_container)