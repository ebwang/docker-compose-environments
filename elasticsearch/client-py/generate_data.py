from datetime import datetime
from elasticsearch import Elasticsearch
from faker import Faker

es = Elasticsearch('http://localhost:9200')
fake = Faker()

def generate_fake_data():
    data = {
        "account_number": fake.random_int(min=0, max=9999),
        "balance": fake.random_int(min=0, max=999999),
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "age": fake.random_int(min=18, max=100),
        "gender": fake.random_element(elements=('M', 'F')),
        "address": fake.street_address(),
        "employer": fake.company(),
        "email": fake.email(),
        "city": fake.city(),
        "state": fake.state_abbr()
    }
    return data

data_list = []

for i in range(1000):
    data = generate_fake_data()
    data_list.append(data)

for data in data_list:
    es.index(index='bank', body=data)