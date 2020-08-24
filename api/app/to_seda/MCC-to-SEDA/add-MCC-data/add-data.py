import pika
import json
from pymongo import MongoClient
from bson import ObjectId
import dateutil.parser


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


# Function to connect to MongoDB
def connectMongo(db, collection, data):
    client = MongoClient("mongodb://Shoaib0023:00011122@cluster0-shard-00-00-zpshz.mongodb.net:27017,cluster0-shard-00-01-zpshz.mongodb.net:27017,cluster0-shard-00-02-zpshz.mongodb.net:27017/Facilitator?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

    db = client[db]
    collection = db[collection]
    collection.insert_one(data)
    return data


def add_report_data():
    {
        "_id":  "5d91e6778c1cfcfc0d000031",
        "updatedAt": {
                "date": {
                        "numberLong": "1569842807000"
                }
        },
        "createdAt": {
                "date": {
                        "numberLong": "1569842807000"
                }
        },
        "comment": "Test",
        "oracComment": "Test",
        "oracCode": {
                "$oid": "599bfffbe95e3f0bb00ec48c"
        },
        "reportedBy": {
                "$oid": "5d26f64fd1dbfb8a027b23ce"
        },
        "issueNameD": "Afval naast de container",
        "rewardingUser": {
                "$oid": "5d26f64fd1dbfb8a027b23ce"
        },
        "oracCategory": "Rubbish beside container",
        "oracType": "Restafval",
        "issueType": "Rubbish beside container",
        "issueLocation": [
                {
                        "$numberDouble": "4.3203715"
                },
                {
                        "$numberDouble": "52.0770469"
                }
        ],
        "postcode": "2511XZ",
        "isSubscribed": true,
        "isPrimary": false,
        "issuePicture": "1569842807.jpg",
        "complainId": "ORC1457",
        "complainIdall": "ORC1455",
        "isOrac": true,
        "deptCode": "",
        "facilitatorComment": "",
        "isFacilitator": false,
        "isCurrentLocation": true,
        "streetInfo": {
                "$oid": "5960d3c4a79cb21f3ca8e4a1"
        },
        "streetName": "Ammunitiehaven",
        "resolvedTime": "",
        "reportStatus": {
                "$numberInt": "0"
        },
        "reportCount": {
                "$numberInt": "1"
        },
        "sentNotification": [],
        "receiveNotification": [],
        "otherOracReport": [],
        "__v": {
                "$numberInt": "0"
        },
        "emailmordate": "",
        "hmshandleddate": "",
        "morupdateddate": ""
    }

    data = connectMongo('MyCleanCity', 'reports', payload)
    print("Success")
