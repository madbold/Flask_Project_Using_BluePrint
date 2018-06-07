from db import DB

class PetModel(DB.Model):

    __tablename__="pets"
    id=DB.Column(DB.Integer,primary_key=True)
    name=DB.Column(DB.String(80))
    price=DB.Column(DB.Float(precision=2))
    store_id=DB.Column(DB.Integer,DB.ForeignKey("stores.id"))
    store=DB.relationship("StoresModel")
    
    def __init__(self,name,price,storeid):

        self.name= name
        self.price=price
        self.store_id=storeid
        

    def json(self):
        return {"Name":self.name,"Price":self.price,"store_id":self.store_id}


    @classmethod
    def getallPets(cls):
        pets=cls.query.all()
        return pets

    @classmethod
    def getPetbyName(cls,name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def getPetbyID(cls,pet_id):
        return cls.query.filter_by(id=pet_id).first()



    def save_to_db(self):
        DB.session.add(self)
        DB.session.commit()


    def delete_from_db(self):
        DB.session.delete(self)
        DB.session.commit()


    def AddItem(self):
        try:
            self.save_to_db()
        except:
            return {"msg":"unable to add. internal server error"},500
        return {"added data":self.json()} ,201
