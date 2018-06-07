
from flask import Flask
from flask import Blueprint
from db import DB
app= Flask(__name__)


app.config.from_pyfile('setting.py')

@app.before_first_request
def create_table():
    DB.create_all()


def create_app():

            # DB intialize
            
            DB.init_app(app)

            # import blueprint
            
            from app.views import app_app
            from pet.views import pet_app
            from stores.views import stores_app
            

            #register Blueprint

            app.register_blueprint(pet_app)
            app.register_blueprint(app_app)
            app.register_blueprint(stores_app)

            return app

if __name__=="__main__":
    create_app().run(port=5000)
