
from functools import wraps
from flask import request,abort,jsonify
from app.models import TokenModel,UserModel
from datetime import datetime
import app

def authorization_required(f):
    
    def inside_function(*args,**kwargs):

        if not request.headers.get('token'):
            abort(403)
        # check if payload has proper attribute
        if  not request.headers.get("username") :
            return jsonify({"Error":"MISSING USER_NAME"}),403
        
        token= TokenModel.find_token_by_id( UserModel.find_user_by_name( request.headers.get("username")).id if UserModel.find_user_by_name( request.headers.get("username")) else None)
        if not token:
            return jsonify({"Error":"MISSING TOKEN"}),403
        

        if token.token!=request.headers.get("token") or (datetime.strptime(token.expires,"%Y-%m-%d %H:%M") < datetime.utcnow().replace(second=0,microsecond=0)):
            return jsonify({"msg":"token expires :{0}".format(token.expires)}),403

        
        return f(*args,**kwargs)
    return inside_function
