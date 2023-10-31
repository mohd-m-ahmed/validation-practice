import json

Jsondata ="""{"name":"jane doe","salary":9000,"email":"jane.doe@pynative.com"}"""


def jsonValidate(JsonFile):
    try:
        json.loads(JsonFile)
    except ValueError as err:
        return False
    return True
print(jsonValidate(Jsondata))