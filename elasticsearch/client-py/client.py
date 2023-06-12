from datetime import datetime
from elasticsearch import Elasticsearch
from faker import Faker

es = Elasticsearch('https://localhost:9200')
fake = Faker()

for i in range(100):
    doc = {
        'author': fake.name(),
        'text': fake.text(),
        'timestamp': datetime.now(),
    }
    resp = es.index(index="test-inde", id=i, document=doc)
    print(resp['result'])