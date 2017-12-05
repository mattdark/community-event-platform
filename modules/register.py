import json

def newspeaker(name, org, mail):
    a_dict = {}

    with open('./speakers.json') as data_file:
        data = json.load(data_file)
        id = len(data["speakers"]) + 1
        temp_list = []
        for dicObj in data["speakers"]:
            temp_list.append(dicObj)
        temp_list.append( {"id": str(id), "name": name, "org": org, "mail": mail})
        data["speakers"] = temp_list
        a_dict["speakers"] = data["speakers"]
        with open('./speakers.json', mode='w', encoding='utf-8') as f:
            f.write(json.dumps(a_dict, indent=4, sort_keys=True, ensure_ascii=False))
