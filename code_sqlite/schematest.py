from jsonschema import validate

SCHEMA ={
    "title": "PETS",
    "description": "A pets from Acme's catalog",
    "type": "object",
    "properties": {
        "id": {
            "description": "The unique identifier for a product",
            "type": "number"
              },
        "name": {
            "description": "The name for a product",
            "type": "string"
              },

        "price": {
            "description": "The price for a product",
            "type": "number",
            "minimum":1
              }


                     },
    "required": ['name','price']
}


validate({'name':"vinod",'price':45},SCHEMA)

