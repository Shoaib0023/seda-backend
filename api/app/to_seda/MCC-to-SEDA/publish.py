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
def connectMongo():
    client = MongoClient("mongodb://Shoaib0023:00011122@cluster0-shard-00-00-zpshz.mongodb.net:27017,cluster0-shard-00-01-zpshz.mongodb.net:27017,cluster0-shard-00-02-zpshz.mongodb.net:27017/Facilitator?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

    db = client.MyCleanCity

    data = {"reports": [], "users": []}
    for document in db.reports.find() :
        data["reports"].append(document)

    for document in db.users.find():
        data["users"].append(document)

    return data


data = connectMongo()
# print("data")


# Function to publish data to rabbitmq
def connectRabbitMQ():
    credentials = pika.PlainCredentials('signals', 'insecure')
    parameters = pika.ConnectionParameters('localhost', 5672, 'vhost', credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='hello1', durable=True)

    channel.basic_publish(exchange='hello-exchange', routing_key='hello', body=json.dumps(data, indent=4, sort_keys=True, default=str))

    print("Success: Data is published to queue")
    print(data)
    connection.close()

connectRabbitMQ()
