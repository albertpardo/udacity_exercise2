import azure.functions as func
import pymongo
from bson.objectid import ObjectId

import sys
sys.path.insert(1, '../')

from db import MyDbConnection

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('_id')

    if id:
        try:
            url = MyDbConnection  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['neighborly']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
