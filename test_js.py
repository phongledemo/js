import json

same = []
sum = []
X = 0
Y = ''
Model = [['CAT4k', 'CAT6k', 'N7k', '9200', '9300',\
    '9500', '9500', 'C94', 'C96'], ['ISR', 'ASR'], ['9800', '5520', '5504'], \
        ['CDB', 'IE-3', 'IE-44', 'IE-5', "IE-"]\
        , ['AIR', 'AXE', 'AXI', 'I', 'C91']]

Special_model = [['38'],[],[],['35'],[]]
Product = {'Switch':[], 'Router':[], 'Controller':[], 'IoT':[], "Access Point":[]}
type_Product = ['Switch', 'Router', 'Controller', 'IoT', "Access Point"]
list_item = ["Switch", "Point"]

def check(same:list, i):
        if i == 49:
            return same
        f_json = open(f"./metajson/meta ({i}).json")
        data = json.load(f_json)
        device_version = data["device_version"]
        for j in device_version:
            platform = j["platform"]
            type = j["type"]
            sum.append(platform)
            if platform[0:4] == "AIR-":
                test_two = platform[4:8]
                for index, models in enumerate(Model):
                    for model in models:
                        if model in test_two:
                            same.append(platform)
            if platform[0:4]=="WS-C":
                test = platform[4:6]
                for index, models in enumerate(Special_model):
                    for model in models:
                        if model in test:
                            same.append(platform)
                            Product[list(Product.keys())[index]] = list(set(Product[list(Product.keys())[index]]))
                            Product[list(Product.keys())[index]].append(platform)
            else:
                for index, models in enumerate(Model):
                    for model in models:
                        if model in platform:
                            same.append(platform)
                            Product[list(Product.keys())[index]] = list(set(Product[list(Product.keys())[index]]))
                            Product[list(Product.keys())[index]].append(platform)
        return check((same), i + 1)


def check_type(type:str, i = -1):
    if i == -len(type.split(" ")):
        return type_split
    type_split = type.split(" ")[i]
    if type_split in list_item:
        if (type.split(" ")[i-2]+ " " + type.split(" ")[i-1])\
             == "Industrial Ethernet":
            type_split = "IoT"
        elif type_split == "Point":
            type_split = type.split(" ")[i-1] + " " + type_split
        return type_split
    else:   
        return check(type,(i-1))



check(same, 1)
same = list(set(same))
sum = list(set(sum))
print(len(same), len(sum))
for i in range(0,len(same)):
    if same[i] in sum:
        sum.remove(str(same[i]))
print(sum)
print(Product)



# print(same)
# print(sum)
# # x = []
# # for i in sum:
# #     if i[0] == "C":
# #         i = i[1:]
# #         x.append(i)
# # print(x)

# print(set(sum))


      
