#!/usr/bin/env python
import pika
import requests
import json

credentials = pika.PlainCredentials('signals', 'insecure')
parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       'vhost',
                                       credentials)

def callback(ch, method, properties, body):
    body = json.loads(body)
    # print(body)

    payload = {
            "location": {"geometrie": {"type":"Point","coordinates": [4.99054263,52.29994823]},
        			     "address": {"openbare_ruimte":"Anne Kooistrahof","huisnummer":"1","postcode":"1106WG","woonplaats":"Amsterdam"},"stadsdeel":"T"},
            "category":{"category_url":"http://localhost:8000/signals/v1/public/terms/categories/Afval/Afvalbakken/Afvalbak/Vol"},
            "reporter":{"phone":body["users"][0]["mobile"], "email":body["users"][0]["emailId"], "sharing_allowed":True},
            "incident_date_start": body["reports"][0]["createdAt"],
            "text":body["reports"][0]["comment"],
            "country":{"country_name": "Netherland"},
            "city":{"city_name": "Almere"}
        }

    response = requests.post(
        'http://localhost:8000/signals/v1/private/signals/',
        json=payload,
        headers={'Authorization': 'Bearer ' + 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjgzYTgxZjNmYjI1NmJkZGMyNGUwNzRjNTFhZWY5Yzg1NjA0MzFlZTEifQ.eyJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjU1NTYiLCJzdWIiOiJDZ0V4RWdWc2IyTmhiQSIsImF1ZCI6InNpZ25hbHMiLCJleHAiOjE1OTgwOTc5MjUsImlhdCI6MTU5ODAxMTUyNSwibm9uY2UiOiJyYW5kb20tbm9uY2UiLCJhdF9oYXNoIjoiTEQwcGRLNnh4VEd0cldQb3pkbHZEZyIsImVtYWlsIjoic2lnbmFscy5hZG1pbkBleGFtcGxlLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiYWRtaW4ifQ.r2C9Pc6KVtPKpe9U_F6ah8VgHdJL4rxEJO-CRUoL1ZFRACNuMIEy4VYohB-n1DoEXVLqG1U2I7ypM_D-jU_MUXmvTX5xxJjAqOGglcrVt-U5G0YZtWkdsRgX9FyNeSa-7PdpuiX071UFPB7-OfQoO_2IRg_5Cjx9EZtA0T9aE2Ki60M2SPx10ejDmTxxfCn9sq7slsqG9edZHbCcwViM12WZdAtDVuGhsKIUImYcb_Sl8ju8WhEK8oH95dMkg8r8F1bfrfb_qkQwmKDcGv3KH0d-uRy0b9zgn-Wdrrn05STQdSXbrUU1QyuEOzZ4LtiqDj9E6NSWEdhZEiDHp2itCA'}
        )

    # print(response.status_code)
    id = response.json()["id"]
    print(f"Signal added: {response.status_code}, id is {id} !!")
    # print(response.json())

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello1', durable=True)

channel.basic_consume(queue='hello1', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()





# with open('file.json', mode='wb') as localfile:
    # localfile.write(response.content)

# print(" [x] Received %r" % body)
