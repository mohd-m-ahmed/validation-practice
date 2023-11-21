import jsonschema
import json
path= "dummy4.json"
with open(path) as file:
    data= json.load(file)
schema= {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "gender": {
      "type": "string"
    },
    "age": {
      "type": "integer"
    },
    "degree": {
      "type": "string"
    },
    "subjects": {
      "type": "array",
      "items": [
        {
          "type": "string"
        },
        {
          "type": "string"
        },
        {
          "type": "string"
        },
        {
          "type": "string"
        }
      ]
    }
  },
  "required": [
    "name",
    "gender",
    "age",
    "degree",
    "subjects"
  ]
}
validator = jsonschema.Draft7Validator(schema)

errors = validator.iter_errors(data)
error_list=[]
for error in errors:
   error_list.append(error)
   print(error_list)