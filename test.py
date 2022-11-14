import json

Model = [['CAT4k', 'CAT6k', 'N7k', '9200L', '9300', '9300L', \
    '9400', '9500-H', '9600', '9500-X'], ['ISR', 'ASR'], ['9300', '9400', '9800', '5520', '5504'], \
        ['CDB', '3560CX', 'IE-3', 'IE-44', 'IE-5', "IE-"]\
        , ['AIR-3702', 'AIR-3802', 'AIR-1800S', 'AIR-9124', 'AIR-9130', 'AIR-']]

Product = ['Switch', 'Router', 'Controller', 'IoT', "Access Point"]
list_item = ["Switch", "Point"]


same = []

sum = []


def check(platform:str ,type:str, i = -1):
    if i == -len(type.split(" ")):
        return None
    for index, models in enumerate(Model):
        for model in models:
            if model in platform:
                return Product[index]
    type_split = type.split(" ")[i]
    if type_split in list_item:
        if (type.split(" ")[i-2]+ " " + type.split(" ")[i-1])\
             == "Industrial Ethernet":
            type_split = "IoT"
        elif type_split == "Point":
            type_split = type.split(" ")[i-1] + " " + type_split
        return type_split
    else:   
        return check(platform,type,(i-1))

for i in range(1,49):
    f_json = open(f"./metajson/meta ({i}).json")
    data = json.load(f_json)
    device_version = data["device_version"]
    for j in device_version:
        platform = j["platform"]
        type = j["type"]
        sum.append(platform)
        for index, models in enumerate(Model):
            for model in models:
                if model in platform:
                    same.append(platform)

for i in range(0,len(same)-1):
    if same[i] in sum:
        sum.remove(str(same[i]))

print(set(sum))
      





# print(check("C9130AXI-B","Cisco Catalyst 9130AXI Unified Access Point"))
# print(check("C9124AXI-B","Cisco Catalyst 9124AXI Unified Access Point"))
# print(check("AIR-AP1800S-B-K9","Cisco Aironet 1800S Active Sensor"))
# print(check("CDB-8P","Cisco Catalyst CDB-8P Switch"))
# print(check("C9200-24PB","Cisco Catalyst 9200-PB Switch Stack"))
# print(check("C9300-48UXM","Cisco Catalyst 9300 Switch"))
# print(check("WS-C3560CX-12PC-S","Cisco Catalyst 3560CX-12PC-S Switch"))
# print(check("C9200L-24P-4G","Cisco Catalyst 9200L Switch Stack"))
# print(check("IE-5000-12S12P-10G","Cisco IE-5000-12S12P-10G Industrial Ethernet Switch"))

