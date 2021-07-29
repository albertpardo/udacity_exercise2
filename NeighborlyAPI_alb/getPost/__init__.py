import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

import sys
sys.path.insert(0, '../')

from db import MyDbConnection

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('_id')

    logging.info('--> MyDbConnection :' + MyDbConnection)
    logging.info('--> _id :' + id)

    if id:
        try:
            url = MyDbConnection  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['neighborly']
            collection = database['posts']


            result = collection.find_one({"_id": ObjectId(id)})
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        logging.info('--- NO id')
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)