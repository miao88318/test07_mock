import yaml

data_list = []
with open("./seripts.yml", "r",encoding="utf-8")as f:
    data = yaml.safe_load(f)
    # print(data.values())
    for i in data.values():
        # print(i.get("input"))
        # print(i.get("exp"))
        # print((i.get("input"),i.get("exp")))
        data_list.append((i.get("input"),i.get("exp")))
print(data_list)