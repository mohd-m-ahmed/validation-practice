import json

Jsondata ="""{
	"_id": "YZXCK7HHHQV2H9J1",
	"name": "Reita Oquendo",
	"dob": "2021-01-24",
	"address": {
		"street": "6108 Sergeants Road",
		"town": "Wirksworth",
		"postode": "TW9 2TR"
	},
	"telephone": "+591-1312-250-037",
	"pets": [
		"Simba",
		"Harley"
	],
	"score": 7.8,
	"email": "jazmin_hedges29@yahoo.com",
	"url": "https://www.denial.today",
	"description": "previous border grades bracket hydrocodone immunology blair why bedrooms referenced vatican tournament grave bios love relation visitor one continue responsible",
	"verified": false,
	"salary": 26650
}"""


def jsonValidate(JsonFile):
    try:
        json.loads(JsonFile)
    except ValueError as err:
        return False
    return True
print(jsonValidate(Jsondata))