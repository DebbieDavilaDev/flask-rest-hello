from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    firstname = db.Column(db.String(120), unique=True, nullable=True)
    lastname = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(80), unique=False, nullable=True)
    username = db.Column(db.String(120), unique=True, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username,
        }
            # do not serialize the password, its a security breach

    
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    habitantSpecies = db.Column(db.String(120), unique=True, nullable=False)
    size = db.Column(db.Integer, unique=True, nullable=False)
    url = db.Column(db.String(80), unique=False, nullable=False)


    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "habitantSpecies": self.habitantSpecies,
            "size": self.size,
            "url": self.url
            # do not serialize the password, its a security breach
        }
    
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    birthyear = db.Column(db.String, unique=False, nullable=False)
    eyecolor = db.Column(db.String(80), unique=False, nullable=False)
    films = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    homeworld = db.Column(db.String(80), unique=False, nullable=False)
    url = db.Column(db.String(80), unique=False, nullable=False)    

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birthyear": self.birthyear,
            "eyecolor": self.eyecolor,
            "films": self.films,
            "height": self.height,
            "homeworld": self.homeworld,
            "url": self.url
            # do not serialize the password, its a security breach
        }

    
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    entity_type = db.Column(db.String(80), unique=False, nullable=False)
    entity_id = db.Column(db.Integer, unique=False, nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Favorite id=%r>' %    (self.id, 
                                        self.name, 
                                        self.entity_type, 
                                        self.entity_id, 
                                        self.owner) #finish this with all columns
                                                            
                                                              

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "entity_type": self.entity_type,
            "entity_id": self.entity_id,
            "owner": self.owner

            # Continue these to end
            # do not serialize the password, its a security breach
        }
    



