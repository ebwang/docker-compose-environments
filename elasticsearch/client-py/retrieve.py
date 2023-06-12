from datetime import datetime
from elasticsearch import Elasticsearch
from faker import Faker

es = Elasticsearch('http://localhost:9200')
fake = Faker()

for i in range(1000):
    resp = es.get(index="bank", id=i)
    print(resp['_source'])


