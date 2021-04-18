import json
import csv

with open('../users.json', 'r') as json_file:
    users = json.loads(json_file.read())
with open('../books.csv', 'r') as csv_file:
    books = csv.reader(csv_file)
    header = next(books)
    for index in range(len(users)):
        users[index]['books'] = [dict(zip(header, next(books)))]
with open('../new_json.json', 'w') as file:
    result = json.dumps(users, indent=4)
    file.write(result)
