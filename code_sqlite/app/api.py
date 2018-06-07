from flask.views import MethodView
from flask import jsonify,request,abort
from flask import Flask,request
from app.decoratores import authorization_required
from app.models import TokenModel,UserModel
#import bcrypt
import uuid
import app
from datetime import datetime ,timedelta


class UserAPI(MethodView):

    def post(self):

        # check if payload has proper attribute
        if  not  request.get_json().get("username") or not request.get_json().get('usersceret'):
            return jsonify({"Error":"MISSING USER_ID_OR_MISSING_USER_SCERET"}),403

        # check if user is already exist

        user=UserModel.find_user_by_name(request.get_json().get("username"))
        if user:
            return jsonify({"Error":"USER ALREADY EXISTING"}),403
        
        # add user in USERS List
        # encrypting password using hash
        # commenting bcrypt code as unable to install py-bcrypt lib
        #salt = bcrypt.gensalt()
        #hashed = bcrypt.hashpw(request.json.get('app_secret'),salt)
        hashed = 'abcdefg12356'
        new_user= UserModel(request.get_json().get("username"),hashed)
        
        
        #store encrypted password
        new_user.save_to_db()
        print(new_user.json())
        return jsonify({"msg":"added"}),200


class TokenGen(MethodView):

    def post(self):

        # check if payload has proper attribute
        if  not  request.get_json().get("username") or not request.get_json().get('usersceret'):
            return jsonify({"Error":"MISSING USER_ID_OR_MISSING_USER_SCERET"}),403

        # check user is authenticated or not
        user=UserModel.find_user_by_name(request.get_json().get("username"))
       
        if not user:
            return jsonify({"msg":"Invalid credentials"}),403

        # check password
           
        #if  userfound.get('password') != bcrypt.hashpw(request.get('app_sceret'),userfound.get('password')):
        
        if  user.password != 'abcdefg12356':    
            jsonify({"msg":"invalid credential"}),403
        
        #generate token
        token=str(uuid.uuid4())
        now=datetime.utcnow().replace(second=0,microsecond=0)
        expires= now+ timedelta(days=20)

        # store in db

        token= TokenModel(token,expires.strftime("%Y-%m-%d %H:%M"))
        token.save_to_db()

        expires_3999= expires.isoformat("T")+"Z"
        print(token.json())
        return jsonify({"token":token.token,"expires":expires_3999}),200






        
        

        

        
