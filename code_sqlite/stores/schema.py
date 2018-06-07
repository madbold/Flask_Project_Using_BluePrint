from jsonschema import validate

SCHEMA ={
    "title": "stores",
    "description": "A store from Acme's catalog",
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

        "address": {
            "description": "The price for a product",
            "type": "string",
           
              },
        "phone": {
            "description": "The price for a product",
            "type": "number",
           
              }


                     },
    "required": ['name','address','phone']
}


