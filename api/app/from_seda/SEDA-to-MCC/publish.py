import pika
import json
from pymongo import MongoClient
from bson import ObjectId
import psycopg2

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


# Function to connect to MongoDB
def connectPostgresql():
    try:
        connection = psycopg2.connect(user='signals', password='insecure', host='localhost', port='5409', database = "signals")

        cursor = connection.cursor()
        print(connection.get_dsn_parameters(),"\n")

        postgreSQL_select_Query = "select * from users_profile"
        cursor.execute(postgreSQL_select_Query)
        user_records = cursor.fetchall()
        # print(user_records)
        # print("You are connected to - ", record,"\n")

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    
    return user_records


data = connectPostgresql()
# print(data)


# Function to publish data to rabbitmq
def connectRabbitMQ():
    credentials = pika.PlainCredentials('signals', 'insecure')
    parameters = pika.ConnectionParameters('localhost', 5672, 'vhost', credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='hello1', durable=True)

    channel.basic_publish(exchange='hello-exchange', routing_key='hello', body=json.dumps(data, indent=4, sort_keys=True, default=str))

    print("SEND: ", data)
    connection.close()

connectRabbitMQ()
