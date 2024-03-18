from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    habitantSpecies = db.Column(db.String(120), unique=True, nullable=False)
    size = db.Column(db.String(120), unique=True, nullable=False)
    
    url = db.Column(db.String(80), unique=False, nullable=False)
    
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    birthyear = db.Column(db.String(80), unique=False, nullable=False)
    eyecolor = db.Column(db.String(80), unique=False, nullable=False)
    films = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.String(80), unique=False, nullable=False)
    homeworld = db.Column(db.String(80), unique=False, nullable=False)
    url = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


#     
#     
#    
    
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    characterid = db.Column(db.String(120), unique=True, nullable=False)
    entitytype = db.Column(db.String(80), unique=False, nullable=False)
    favorite = db.Column(db.String(80), unique=False, nullable=False)
    planetid = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    userfavorites = db.Column(db.Integer, db.ForeignKey(User.id))
    

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


