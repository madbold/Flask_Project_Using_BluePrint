from flask import Blueprint
from stores.api import StoreAPI

stores_app=Blueprint('stores_app',__name__)

stores_app.add_url_rule('/stores/',view_func = StoreAPI.as_view('stores'),defaults={'store_id': None},methods=['GET',])
stores_app.add_url_rule('/stores/<int:store_id>/',view_func = StoreAPI.as_view('store'),methods=['GET','PUT','DELETE'])
stores_app.add_url_rule('/stores/',view_func = StoreAPI.as_view('add store'),methods=['POST'])
stores_app.add_url_rule('/stores/<int:store_id>/pets/',view_func = StoreAPI.as_view('get store'),methods=['GET'])



 