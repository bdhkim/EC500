import json
import numpy as np
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['airport-database']



with open('airports.json') as data_file:
    data = json.load(data_file)

    for index, value in enumerate(data):  # iterate through the json document
        posts = db.posts
        post_data = {

            "code": data[index]['code'],
            "lat": data[index]['lat'],
            "lon": data[index]['lon'],
            "name": data[index]['name'],
            "city": data[index]['city'],
            "state": data[index]['state'],
            "country": data[index]['country'],
            "woeid": data[index]['woeid'],
            "tz": data[index]['tz'],
            "phone": data[index]['phone'],
            "type": data[index]['type'],
            "email": data[index]['email'],
            "url": data[index]['url'],
            "runway_length": data[index]['runway_length'],
            "elev": data[index]['elev'],
            "icao": data[index]['icao'],
            "direct_flights": data[index]['direct_flights'],
            "carriers": data[index]['carriers']
        }
        result = posts.insert_one(post_data)
        print("successfully appeneded! " + str(index))


# for i in range(0,5):
#     commandString = "data[" + str(i) + "]" + "[\'code\']"
#     print(commandString)
#

# a = np.array
# print(data[0]['code'])