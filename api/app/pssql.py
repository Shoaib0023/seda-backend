# import psycopg2
import csv
from signals.apps.signals.models import Category
#
#
# def connect():
#     conn = None
#     dsn = "host=ec2-52-200-189-81.compute-1.amazonaws.com dbname=signals user=signals password=insecure"
#
#     try:
#         conn = psycopg2.connect(dsn)
#
#         return conn
#
#     except (Exception) as Error:
#         print(Error)
#         return None
#
# conn = connect()
#
# def readcsv():
#     data = None
# with open('category.csv', newline='') as csvfile:
#     data = csv.reader(csvfile)
#     line_count = -1
#     for row in data:
#         line_count += 1
#         if line_count == 0:
#             continue
#
#         country = {
#             'country_name': "Netherland",
#         }
#
#         city = {
#             'city_name': "Hague",
#         }
#
#         cat1, cat2, cat3, cat4, dept = row
#         if not Category.objects.filter(name=cat1, category_level_name2=cat2, category_level_name3=cat3, category_level_name4=cat4).exists():
#             if not Department.objects.filter(name=dept.strip()).exists():
#                 dept = Department.objects.create(name=dept.strip(), code=dept.strip())
#             else:
#                 dept = Department.objects.get(name=dept.strip())
#
#             category = Category.objects.create(name=cat1.strip(), category_level_name1=cat1.strip(), category_level_name2=cat2.strip(), category_level_name3=cat3.strip(), category_level_name4=cat4.strip(), country=country, city=city)
#
#             category.departments.add(dept)
