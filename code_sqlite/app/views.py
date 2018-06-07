from flask import Blueprint
from app.api import UserAPI, TokenGen

app_app=Blueprint('app',__name__)

app_app.add_url_rule('/register/',view_func = UserAPI.as_view('user_api'),methods=['POST'])
app_app.add_url_rule('/gentoken/',view_func = TokenGen.as_view('token_api'),methods=['POST'])
