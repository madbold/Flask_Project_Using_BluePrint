from flask import Blueprint
from pet.api import PetAPI

pet_app=Blueprint('pet_app',__name__)

pet_app.add_url_rule('/pets/',view_func = PetAPI.as_view('pets'),defaults={'pet_id': None},methods=['GET'])
pet_app.add_url_rule('/pets/<int:pet_id>',view_func = PetAPI.as_view('pet'),methods=['GET','PUT'])
pet_app.add_url_rule('/pets/<int:pet_id>',view_func = PetAPI.as_view('pet delete'),methods=['DELETE'])
pet_app.add_url_rule('/pets/',view_func = PetAPI.as_view('add pets'),methods=['POST'])


