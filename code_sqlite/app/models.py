
from db import DB
class UserModel(DB.Model):

    __tablename__="user"
    id=DB.Column(DB.Integer,primary_key=True)
    username=DB.Column(DB.String(80))
    password=DB.Column(DB.String(40))

    def __init__(self,username,password):

        self.username=username
        self.password=password


    def json(self):
        return {"name": self.username,"id":self.id}

    def save_to_db(self):
        DB.session.add(self)
        DB.session.commit()

    def delete_from_db(self):
        DB.session.delete(self)
        DB.session.commit()

    @classmethod
    def find_user_by_name(cls,name):
        return cls.query.filter_by(username=name).first()


    @classmethod
    def find_user_by_id(cls,id):
        return cls.query.filter_by(id=id).first()


class TokenModel(DB.Model):

    __tablename__="token"
    id=DB.Column(DB.Integer,primary_key=True)
    token=DB.Column(DB.String(80))
    expires=DB.Column(DB.String(40))

    def __init__(self,token,expires):

        self.token=token
        self.expires=expires

    def json(self):
        return {"token": self.token,"expires":self.expires,"id":self.id}

    def save_to_db(self):
        DB.session.add(self)
        DB.session.commit()

    def delete_from_db(self):
        DB.session.delete(self)
        DB.session.commit()


    @classmethod
    def find_token_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
