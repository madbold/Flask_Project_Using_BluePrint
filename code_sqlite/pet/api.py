from flask.views import MethodView
from flask import jsonify,request,abort
from flask import Flask,request
from app.decoratores import authorization_required
from pet.models import PetModel


class PetAPI(MethodView):

    decorators=[authorization_required]

    @classmethod
    def get(cls,pet_id):
        if pet_id:
            item=PetModel.getPetbyID(pet_id)
            if item:
                return jsonify({"details":item.json()}),200
            else:
                return jsonify({"MSG":"Item {0} not found".format(pet_id)})

        else:
            print(request.args.get('species'))
            if 'species' in request.args:
                    pet=PetModel.getPetbyName(name=request.args.get('species'))
                    return jsonify({"details":pet.json()}),200

            Petlist= PetModel.getallPets()
            return jsonify({'details':[pet.json() for pet in Petlist ]})
        

    @classmethod
    def post(cls):

        data= request.get_json()
        pet=PetModel.getPetbyName(data["name"])
        if pet:
            return jsonify({"msg":"Item with name {0} already exist".format(data['name'])})

        item=PetModel(data["name"],data["price"],data["store_id"])
        new_item,code = item.AddItem()
        return jsonify({"msg":new_item}),code

    @classmethod
    def put(cls,pet_id):

        data= request.get_json()
        pet=PetModel.getPetbyID(pet_id)
        if pet:
            pet.price=data["price"]
            pet.name=data['name']
        else:
            pet=PetModel(data['name'],data["price"],data["store_id"])
        return pet.AddItem()

    def delete(self,pet_id):

        pet=PetModel.getPetbyID(pet_id)
        if pet:
            pet.delete_from_db()
            return {"msg":"Deleted {0}".format(pet_id)}, 200

        return {"msg":"Item not found to delete"},200
       