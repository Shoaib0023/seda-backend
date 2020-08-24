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
    payload = {
        "_id" : ObjectId("5d4e798a8c1cfcf033000029"),
        "updated_at" : dateutil.parser.parse("2019-08-10T10:26:42.000+0000"),
        "created_at" : dateutil.parser.parse("2019-08-10T08:00:10.000+0000"),
        "team_id" : 0,
        "tool_id" : "5c5aada3b068ca4411000029",
        "locations" : "52.084660794429574&4.281838723278729",
        "report_type" : "1,2,3",
        "language" : "1",
        "description" : [
            ""
        ],
        "location_type" : 0,
        "reported_by" : ObjectId("5a27fa52289e6e6a06a9f701"),
        "user_district" : ObjectId("5c4bece1798064240800002c"),
        "user_neighbourhood" : ObjectId("5c4bea6e7980641808000029"),
        "report_status" : 0,
        "issue_image" : [
            ""
        ],
        "report_id" : 1069,
        "map_image_name" : "1565424001.png",
        "report_status_date" : [
            dateutil.parser.parse("2019-08-10T08:00:10.000+0000")
        ],
        "assign_to" : ObjectId("5c7cf64eb068ca783700002a")
    }
    data = connectMongo('Facilitator', 'reports', payload)
    print("Success")


def add_users_data():
    payload = {
         "_id" : ObjectId("5a27fa52289e6e6a06a9f701"),
        "updatedAt" : dateutil.parser.parse("2018-01-04T13:33:58.109+0000"),
        "createdAt" : dateutil.parser.parse("2017-12-06T14:10:26.834+0000"),
        "password" : "$2a$08$edup3e8YJW61Ed23VhgXxeepiYIcEs4y/NitF/PdQqvru0hMbehbK",
        "firstName" : "Pr",
        "lastName" : "Sh",
        "emailId" : "prashant.shukla.in+123@gmail.com",
        "mobile" : "0611039076",
        "volunteerFor" : "Adopt a Container",
        "lastLogin" : "native",
        "dob" : dateutil.parser.parse("1990-12-06T00:00:00.000+0000"),
        "loggedIn" : dateutil.parser.parse("2018-01-04T12:04:54.177+0000"),
        "language" : 1,
        "receiveReport" : True,
        "receiveCommunity" : True,
        "isAccepted" : False,
        "redeemdedPoints" : 0,
        "points" : 10,
        "isLoggedOut" : False,
        "isFacilitator" : False,
        "isNotification" : True,
        "isActive" : True,
        "oracSelected" : True,
        "myOrac" : [
            ObjectId("599c0007e95e3f0bb00ed5cd"),
            ObjectId("599c0007e95e3f0bb00ed5cb"),
            ObjectId("599c0007e95e3f0bb00ed5ca")
        ],
        "myReports" : [
            ObjectId("5d4e798a8c1cfcf033000029")
        ],
        "fbId" : "",
        "phoneNotification" : False,
        "emailNotification" : False,
        "isVerified" : True,
        "profilePic" : "",
        "facilitated" : [

        ],
        "address" : {
            "postcode" : "2511CB",
            "street" : "Kalvermarkt",
            "city" : "'s-Gravenhage",
            "houseNo" : "53"
        },
        "device" : {
            "platform" : "android",
            "token" : "ddwf-9cr2DE:APA91bHuApc23MKLE7qBW4QhXOnRaxXmJDPinkN16c6vOxu6VYwWVW6mvJgmSsHXk6bRkRIQGbbxzh6OCvA-4McCLZUld0vChs0VUXShZGUREzElpnOQ7nFxnG8jLqLnl2s_1TsAfpZV"
        },
        "verificationCode" : 924135,
        "__v" : 1,
        "referal" : 0.0,
        "redeemedreferal" : 0.0
    }

    data = connectMongo('Facilitator', 'users', payload)
    print("Success")


def add_districts_data():
    payload = {
        "_id" : ObjectId("5c4bece1798064240800002c"),
        "updated_at" : dateutil.parser.parse("2019-01-29T14:06:34.000+0000"),
        "created_at" : dateutil.parser.parse("2019-01-29T14:06:34.000+0000"),
        "is_active" : True,
        "district_id" : "STA1003",
        "district_name" : "Centrum",
        "district_map" : "1548770794.jpg"
    }

    data = connectMongo('Facilitator', 'districts', payload)
    print("Success")


def add_neighbourhoods_data():
    payload = {
        "_id" : ObjectId("5c4bea6e7980641808000029"),
        "updated_at" : dateutil.parser.parse("2019-01-29T14:08:23.000+0000"),
        "created_at" : dateutil.parser.parse("2019-01-29T14:08:23.000+0000"),
        "is_active" : True,
        "neighbourhood_id" : "",
        "district_id" : ObjectId("5c4bece1798064240800002c"),
        "neighbourhood_name" : "Centrum",
        "neighbourhood_map" : "1548770903.jpg",
        "coordinates" : [
            [
                52.085386,
                4.2820533
            ],
            [
                52.0662438,
                4.3286678
            ]
        ]
    }

    data = connectMongo('Facilitator', 'neighbourhoods', payload)
    print("Success")


def add_reports_plan_data():
    payload = {
        "_id" : ObjectId("5d9700a18c1cfcd43300002a"),
        "report_id" : ObjectId("5d4e798a8c1cfcf033000029"),
        "created_at" : dateutil.parser.parse("2019-10-04T08:19:45.000+0000"),
        "emp_id" : "",
        "team_id" : "5c59422e798064842700002a",
        "report_days" : "0",
        "report_time" : 4,
        "urgency" : 0,
        "forman_email" : ""
    }
    data = connectMongo('Facilitator', 'reports_plan', payload)
    print("Success")


# add_neighbourhoods_data()
add_reports_plan_data()
