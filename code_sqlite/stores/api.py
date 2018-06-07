from flask.views import MethodView
from flask import jsonify,request,abort
from flask import Flask,request
from app.decoratores import authorization_required
from stores.models import StoresModel
from pet.models import PetModel

from jsonschema import Draft4Validator
from jsonschema.exceptions import best_match
from app.decoratores import authorization_required
from stores.schema  import SCHEMA


class StoreAPI(MethodView):

    decoratores=[authorization_required]

    @classmethod
    def get(cls,**kwargs):
        store_id=kwargs.get('store_id')
        if store_id:
            store=StoresModel.getStorebyID(store_id)
            if store:

                if 'species' in request.args:
                    store=PetModel.getPetbyName(request.args.get('species'))

                return jsonify({"details":store.json()}),200
            else:
                return jsonify({"MSG":"Item {0} not found".format(store_id)}),404

        else:
            Storelist= StoresModel.getallStores()
            return jsonify({'details':[store.json() for store in Storelist ]}),200

    @classmethod    
    def post(cls):

        data = request.get_json()
        store=StoresModel.getStorebyName(data['name'])
        if store:
            return jsonify({"msg":"Store {0} already exist".format(data['name'])})

        store=StoresModel(data.get('name'),data.get('address'),data.get('phone'))
        obj=store.AddStore()
        

        return jsonify({"detals":obj.json()}),200


    def delete(self,store_id):
        store=StoresModel.getStorebyID(store_id)
        if not store:
            return {"msg":"unbale to deleted. {0}: store not found".format(store_id)}
        store.delete_from_db()
        return jsonify({"msg":"deleted successfully"}),200
    
    def put(self,store_id):

        data= request.get_json()
        store=StoresModel.getStorebyID(store_id)
        if store:
            store.name=data["name"]
            store.address=data["address"]
            store.phone = data['phone']

        else:
            store=StoresModel(data.get('name'),data.get('address'),data.get('phone'))
        return store.AddItem()



    


        



  
  