import json
import jsonschema
from jsonschema import validate 
schema = {
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
validate(instance={
    "name":"Mohd Ahmed",
    "gender":"male",
    "age":22,
    "degree":"B.E.",
    "subjects":["maths","dsp","emw","NT"]
}, schema=schema)
