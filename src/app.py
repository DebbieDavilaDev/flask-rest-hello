"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, Characters, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/users', methods=['POST'])
def post_user():
    new_user = request.json
    person = User( 
        username = new_user['username'], 
        email = new_user['email'],
        firstname = new_user['firstname'],
        lastname = new_user['lastname'],
        password = new_user['password']

    ) #finish this line with proper email source
    db.session.add(person)
    db.session.commit()
    return jsonify(new_user), 200

@app.route('/favorites', methods=['POST'])
def post_favorite():
    new_favorite = request.json
    person = Favorites( 
        owner = new_favorite['owner'], 
        name = new_favorite['name'],
        entity_type = new_favorite['entity_type'],
        entity_id = new_favorite['entity_id']

    ) #finish this line with proper email source
    db.session.add(person)
    db.session.commit()
    return jsonify(new_favorite), 200




@app.route('/characters', methods=['POST'])
def post_character():
    new_character = request.json
    person = Characters( 
        name = new_character['name'],
        birthyear = new_character['birthyear'],
        eyecolor = new_character['eyecolor'],
        films = "various",
        height = new_character['height'],
        homeworld = new_character['homeworld'],
        url = new_character['url']
    ) #finish this line with proper email source
    db.session.add(person)
    db.session.commit()
    return jsonify(new_character), 200






@app.route('/planets', methods=['POST'])
def post_planet():
    new_planet = request.json
    planet = Planets( 
        name = new_planet['name'],
        habitantSpecies = new_planet['habitantSpecies'],
        size = new_planet['size'],
        url = new_planet['url']
    ) #finish this line with proper email source
    db.session.add(planet)
    db.session.commit()
    return jsonify(new_planet), 200
        



@app.route('/users', methods=['GET']) # Finished
def get_users():
    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))
    return jsonify(all_users), 200

# CREATE GET ROUTE FOR FAVORITES

@app.route('/favorites', methods=['GET']) # Finished
def get_favorites():
    favorites = Favorites.query.all()
    all_favorites = list(map(lambda x: x.serialize(), favorites))
    return jsonify(all_favorites), 200


@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Characters.query.all() # GET from Favorite class
    all_characters = list(map(lambda x: x.serialize(), characters))
    return jsonify(all_characters), 200

@app.route('/planets', methods=['GET'])
def get_planets():
    planets_favorites = Planets.query.all() # GET from Favorite class
    all_planets = list(map(lambda x: x.serialize(), planets))
    return jsonify(all_planets), 200


@app.route('/users/<id>', methods=['DELETE'])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    test_user = User.query.get(id)
    if(test_user is None):
        return f"User with id: {id} was deleted"
    else:  
        return f"User was not deleted - possible error"




@app.route('/favorites/<id>', methods=['DELETE'])
def favorites_delete(id):
    favorite = Favorites.query.get(id)
    db.session.delete(favorite)
    db.session.commit()

    updated_favorites = Favorites.query.all()
    updated_favorites = list(map(lambda x: x.serialize(), updated_favorites))

    test_favorite = Favorites.query.get(id)
    if(test_favorite is None):
        return jsonify(
            {
                "msg":f"Favorite with id: {id} was deleted",
                "updated_list": updated_favorites
            }
        )
    
    
    else:
        return f"Favorite was not deleted - possible error"







# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)


    

    


