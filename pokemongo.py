import pymongo, json


'''
The chosen dataset is the Pokedex, which contains information about all of the
original 150 Pokemon, including names, types, evolutions, biological data,
and data from the game (like spawn chance).

Link: https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json

The file was transferred to a JSON file which was translated into a dictionary
to be uploaded to the MongoDB server.


'''
###CODE FOR UPLOADING DB DATA

f = open('pokemon.json','rU')
datastring = f.read()
dic = json.loads(datastring)

connection = pymongo.MongoClient('homer.stuy.edu')
db = connection['elsharawyM']
collection = db['pokemon']

collection.insert_many(dic['pokemon'])

###SEARCH FUNCTIONALITY
def find_id(pokeid):
    cursor = collection.find({'id': pokeid})
    print 'POKEMON WITH ID ' + str(pokeid) + ':\n'
    result = []
    for i in cursor:
        result.append(i)
        print i
    return result

#find_id(136)

def find_type(poketype):
    cursor = collection.find({'type': poketype})
    print 'POKEMON WITH TYPE ' + poketype + ':\n'
    result = []
    for i in cursor:
        result.append(i)
        print i
    return result

#find_type('Bug')


def find_type_and_minspawnchance(poketype,spawnchance):
    cursor = collection.find({'type': poketype, 'spawn_chance' : {'$gt' : spawnchance}})
    print 'POKEMON WITH TYPE ' + poketype + ' AND SPAWN CHANCE GREATER THAN  ' + str(spawnchance) + ':\n'
    result = []
    for i in cursor:
        result.append(i)
        print i['name']
    return result

#find_type_and_minspawnchance('Bug', 0.1)

def find_name(name):
    cursor = collection.find({'name': name})
    print 'POKEMON WITH NAME ' + str(name) + ':\n'
    result = []
    for i in cursor:
        result.append(i)
        print i
    return result


connection.drop_database('elsharawyM')
