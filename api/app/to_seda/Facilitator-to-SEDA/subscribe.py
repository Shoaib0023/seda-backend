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
    # print([int(coord) for coord in body["reports"][0]["location"]])
    body = json.loads(body)
    # print(body["reports"][0]["location"])
    category_level_name1 = body["reports"][0]["category"]
    category_level_name2 = body["reports"][0]["sub_category"]
    category_level_name3 = body["reports"][0]["sub_category1"]
    category_level_name4 = body["reports"][0]["sub_category2"]

    # print(f"http://localhost:8000/signals/v1/public/terms/categories/{category_level_name1}/{category_level_name2}/{category_level_name3}/{category_level_name4}")

    payload = {
            "location": {"geometrie": {"type":"Point","coordinates":[4.99054263,52.29994823]},
        			     "address": {"openbare_ruimte":"Anne Kooistrahof","huisnummer":"1","postcode":"1106WG","woonplaats":"Amsterdam"},"stadsdeel":"T"},
            "category":{"category_url":f"http://localhost:8000/signals/v1/public/terms/categories/{category_level_name1}/{category_level_name2}/{category_level_name3}/{category_level_name4}" },
            "reporter":{"phone":body["users"][0]["mobile"], "email":body["users"][0]["emailId"], "sharing_allowed":True},
            "incident_date_start": body["reports"][0]["created_at"],
            "text":body["reports"][0]["description"][0],
            "country":{"country_name": "Netherland"},
            "city":{"city_name": "Almere"}
        }

    response = requests.post(
        'http://localhost:8000/signals/v1/private/signals/',
        json=payload,
        headers={'Authorization': 'Bearer ' + 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjgzYTgxZjNmYjI1NmJkZGMyNGUwNzRjNTFhZWY5Yzg1NjA0MzFlZTEifQ.eyJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjU1NTYiLCJzdWIiOiJDZ0V4RWdWc2IyTmhiQSIsImF1ZCI6InNpZ25hbHMiLCJleHAiOjE1OTgwOTc5MjUsImlhdCI6MTU5ODAxMTUyNSwibm9uY2UiOiJyYW5kb20tbm9uY2UiLCJhdF9oYXNoIjoiTEQwcGRLNnh4VEd0cldQb3pkbHZEZyIsImVtYWlsIjoic2lnbmFscy5hZG1pbkBleGFtcGxlLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiYWRtaW4ifQ.r2C9Pc6KVtPKpe9U_F6ah8VgHdJL4rxEJO-CRUoL1ZFRACNuMIEy4VYohB-n1DoEXVLqG1U2I7ypM_D-jU_MUXmvTX5xxJjAqOGglcrVt-U5G0YZtWkdsRgX9FyNeSa-7PdpuiX071UFPB7-OfQoO_2IRg_5Cjx9EZtA0T9aE2Ki60M2SPx10ejDmTxxfCn9sq7slsqG9edZHbCcwViM12WZdAtDVuGhsKIUImYcb_Sl8ju8WhEK8oH95dMkg8r8F1bfrfb_qkQwmKDcGv3KH0d-uRy0b9zgn-Wdrrn05STQdSXbrUU1QyuEOzZ4LtiqDj9E6NSWEdhZEiDHp2itCA'}
        )

    # print(response.status_code, response.json())
    id_ = response.json()["id"]
    print(f"Signal added: {response.status_code}, id is {id_} !! Creating signals_plan report ------------------------")
    # print(response.json())

    data = body["signals_plan"][0]
    data["signal_id"] = response.json()["id"]
    data["reporter_id"] = response.json()["reporter"]["id"]
    # print(data)

    response1 = requests.post(
        'http://localhost:8000/signals/v1/private/signals_plan/',
        json=data,
        headers={'Authorization': 'Bearer ' + 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImIzMjY2MGZhZDRmNWI1Y2ZlZGI5NzczNmMyMmE5ZmU0ZjdmY2YwOTkifQ.eyJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjU1NTYiLCJzdWIiOiJDZ0V4RWdWc2IyTmhiQSIsImF1ZCI6InNpZ25hbHMiLCJleHAiOjE1OTgwNzg0NjQsImlhdCI6MTU5Nzk5MjA2NCwibm9uY2UiOiJyYW5kb20tbm9uY2UiLCJhdF9oYXNoIjoid2pEazY2WGR6NGpwVUlIMm9HSXRaUSIsImVtYWlsIjoic2lnbmFscy5hZG1pbkBleGFtcGxlLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiYWRtaW4ifQ.LsBxXJBcRurpdWFw7bk2bF2c5eGN5NHgopxBHwsIouvimg_8IpG9FFUpQ8M6rLXasnLbQPh1sn7cb82jVpJCCV4qNiWD8zkLhDv2iAEcCK6hQct5W91djH9nMioLTvRTT3uWoxUSU0mtjcPPVxPx925vdcKwYZgFqAVs6c4pQ-_ZmP2ow0gFqfRj9wpiHK2bptUaUvB4hPcimpNKN3GmxSrfmZkVc78ge52IVxKudx5mjLq4sKwSQkSqMG8IPg7ZJ74iSgCjU0oRPZkGmSlUklVxlsGI4iZ-9Hm5_RnzihSbXqOdHP2WQ5NMTcr3zgrO48EQA2ZxjyBO6toTW907ig'}
    )

    # print(response1.status_code)
    id_ = response1.json()["id"]
    print(f"Signals Report Created Successfully {response1.status_code} with id {id_} !!!" if response1.status_code == 201 else response1.status_code)


connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello1', durable=True)

channel.basic_consume(queue='hello1', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()



# with open('file.json', mode='wb') as localfile:
    # localfile.write(response.content)

# print(" [x] Received %r" % body)
