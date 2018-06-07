from db import DB

class StoresModel(DB.Model):

    __tablename__="stores"
    id=DB.Column(DB.Integer,primary_key=True)
    name=DB.Column(DB.String(80))
    address=DB.Column(DB.String)
    phone= DB.Column(DB.Integer)
    pets= DB.relationship("PetModel" ,lazy="dynamic")

    def __init__(self,name,address,phone):
        self.address= address
        self.phone=phone
        self.name=name


    def json(self):
        return {"Name":self.name,"Phone":self.phone,"id":self.id,'address':self.address ,'pets': [pet.json() for pet in self.pets.all()]}


    @classmethod
    def getallStores(cls):
        stores=cls.query.all()
        return stores

    @classmethod
    def getStorebyName(cls,name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def getStorebyID(cls,pet_id):
        return cls.query.filter_by(id=pet_id).first()



    def save_to_db(self):
        DB.session.add(self)
        DB.session.commit()


    def delete_from_db(self):
        DB.session.delete(self)
        DB.session.commit()


    def AddStore(self):
        try:
                   
            self.save_to_db()
        except:
            return {"msg":"unable to add. internal server error"},500
        return self
       
            
       
