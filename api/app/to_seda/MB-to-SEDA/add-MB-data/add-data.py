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
        "_id" : ObjectId("5dad5eb317a8dc697f27d6ff"),
        "issue_image" : "seda1571643059.png",
        "address" : "Sumahi Village Rd, Taruanwa, Uttar Pradesh 274401, India",
        "description" : "Test",
        "category" : "Afval",
        "sub_category" : "",
        "sub_category1" : "",
        "sub_category2" : "",
        "category_id" : "5d8f1da6decf62a41c00002d",
        "sub_category_id" : "",
        "sub_category1_id" : "",
        "sub_category2_id" : "",
        "location" : [
            26.6279453,
            84.0350811
        ],
        "user_id" : "5db9c67317a8dc313c7b23c7",
        "reported_by_data" : [
            {
                "_id" : ObjectId("5db9c67317a8dc313c7b23c7"),
                "updated_at" : dateutil.parser.parse("2019-10-30T17:20:51.000+0000"),
                "created_at" : dateutil.parser.parse("2019-10-30T17:20:51.000+0000"),
                "first_name" : "R",
                "last_name" : "a",
                "email_id" : "rahulmanit5@gmail.com",
                "mobile" : "88404069843",
                "password" : "$2y$10$5qVzVRfaF.cI.aUoSr0CFuSTfmcrCYMcaz/KpzksyHUPTW364Z2Va",
                "district" : ObjectId("5c4bece1798064240800002c"),
                "neighbourhood" : ObjectId("5db9c67317a8dc313c7b23c6"),
                "role_id" : "Groen",
                "verification_code" : 369089,
                "profile_pic" : "",
                "is_verified" : True,
                "is_approved" : True,
                "device" : {
                    "platform" : "",
                    "token" : "",
                    "language" : 1,
                    "last_logged_in" : dateutil.parser.parse("2019-11-10T13:01:42.000+0000"),
                    "is_logged_out" : False
                }
            }
        ],
        "created_at" : dateutil.parser.parse("2019-10-21T07:30:59.000+0000"),
        "updated_at" : dateutil.parser.parse("2019-11-10T15:41:59.000+0000"),
        "report_id" : 1108,
        "status" : 1,
        "re_route" : 1,
        "finished_by" : "5db9c67317a8dc313c7b23c7",
        "issue_desc" : "",
        "issue_image_finish" : "seda1573400519.png"
    }

    data = connectMongo('Mobile-Beheereder', 'reports', payload)
    print("Success")


def add_users_data():
    payload = {
        "_id" : ObjectId("5db9b44617a8dc95367b23c7"),
        "updated_at" : dateutil.parser.parse("2019-10-30T16:03:18.000+0000"),
        "created_at" : dateutil.parser.parse("2019-10-30T16:03:18.000+0000"),
        "first_name" : "MIchael",
        "last_name" : "Schaap",
        "email_id" : "michael.savana1+1@gmail.com",
        "mobile" : "0637378373",
        "password" : "$2y$10$INuRxDoCOg3RuHEIu1MHvecXxBuVR2KWHRQr3T.6.zy7bg.7ny8Em",
        "district" : ObjectId("5c4bece1798064240800002c"),
        "neighbourhood" : ObjectId("5db9b44617a8dc95367b23c6"),
        "role_id" : "Groen",
        "verification_code" : 172299,
        "profile_pic" : "",
        "is_verified" : True,
        "is_approved" : True,
        "device" : {
        "platform" : "",
        "token" : "",
        "language" : 1,
        "last_logged_in" : dateutil.parser.parse("2019-10-30T16:05:00.000+0000"),
        "is_logged_out" : False
        }
    }

    data = connectMongo('Mobile-Beheereder', 'users', payload)
    print("Success")


def add_districts_data():
    payload = {
        "_id" : ObjectId("5c4bece1798064240800002c"),
        "updated_at" : dateutil.parser.parse("2019-01-29T14:06:34.000+0000"),
        "created_at" : dateutil.parser.parse("2019-01-29T14:06:34.000+0000"),
        "is_active" : True,
        "district_id" : "STA1003",
        "district_name" : "Centrum",
        "district_map" : "1548770794.jpg",
        "district_location" : [
            52.3717,
            4.9021
        ]
    }

    data = connectMongo('Mobile-Beheereder', 'districts', payload)
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

    data = connectMongo('Mobile-Beheereder', 'neighbourhoods', payload)
    print("Success")


def add_categories_data():
    payload = {
        "_id" : ObjectId("5d8f1da6decf62a41c00002d"),
        "cat_type" : 0,
        "category_name" : "Afval",
        "createdAt" : dateutil.parser.parse("2019-09-28T08:45:26.000+0000"),
        "is_active" : True,
        "parent_id" : "",
        "updatedAt" : dateutil.parser.parse("2019-09-28T08:45:26.000+0000")
    }

    data = connectMongo('Mobile-Beheereder', 'categories', payload)
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
    data = connectMongo('Mobile-Beheereder', 'reports_plan', payload)
    print("Success")


# add_report_data()
# add_users_data()
# add_districts_data()
# add_neighbourhoods_data()
# add_categories_data()
add_reports_plan_data()
