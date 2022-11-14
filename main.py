
import json

same = []
sum = []
X = 0
Y = ''
Model = [['CAT4k', 'CAT6k', 'N7k', '9200', '9300',\
    '9500', 'C94', 'C96'], ['ISR', 'ASR'], ['9800', '5520', '5504'], \
        ['CDB', 'IE-3', 'IE-44', 'IE-5', "IE-"]\
        , ['AIR', 'AXE', 'AXI', 'I', 'C91']]

Special_model = [['38'],[],[],['35'],[]]
Product = {'Switch':[], 'Router':[], 'Controller':[], 'IoT':[], "Access Point":[]}
type_Product = ['Switch', 'Router', 'Controllers', 'IoT', "Access Point"]
type_Product_1 = ['Switch', 'Router', 'Controller', 'IoT', "Access Point"]
list_item = ["Switch", "Point"]




def check_platform(platform):
    if platform[0:4] == "AIR-":
        test_two = platform[6:10]
        for index, models in enumerate(Model):
            for model in models:
                if model in test_two:
                    return type_Product[index]
        return type_Product[4]
    elif platform[0:4]=="WS-C":
        test = platform[4:6]
        for index, models in enumerate(Special_model):
            for model in models:
                if model in test:
                    return type_Product[index]
    else:
        for index, models in enumerate(Model):
            for model in models:
                if model in platform:
                    return type_Product[index]

def check_type(type:str, i = -1):
    if i == -len(type.split(" ")):
        return None
    type_split = type.split(" ")[i]
    if type_split in type_Product_1:
        return type_split
    if type_split in list_item:
        if (type.split(" ")[i-2]+ " " + type.split(" ")[i-1])\
             == "Industrial Ethernet":
            type_split = "IoT"
        elif type_split == "Point":
            type_split = type.split(" ")[i-1] + " " + type_split
        else:
            pass
        return type_split
    else:   
        return check_type(type,(i-1))


def check(i):
        if i == 49:
            return same
        f_json = open(f"./metajson/meta ({i}).json")
        data = json.load(f_json)
        device_version = data["device_version"]
        for j in device_version:
            platform = j["platform"]
            type = j["type"]
            print(check_platform(platform))
            print(check_type(type))
        return check(i + 1)

check(1)
