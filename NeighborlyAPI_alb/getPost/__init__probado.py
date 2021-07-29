import logging
import azure.functions as func
import pymongo
import os
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('*** Python getPosts trigger function processed a request.')
    
    id = req.params.get('_id')

    try:
        url = "mongodb://myazurecosmosdblab22:LMUfola32AH1g6wwKgepwM5F2dpnrbw71f3Zruh63khcP2JUypCV8exvVaWcnSxe3TGPDE9F73tWWzZ8do3FXQ==@myazurecosmosdblab22.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@myazurecosmosdblab22@"
        client = pymongo.MongoClient(url)
        database = client['lab1db']
        collection = database['posts']

        result = collection.find_one({"_id":ObjectId(id)})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        return func.HttpResponse("Could not connect to mongodb",
                                 status_code=400)