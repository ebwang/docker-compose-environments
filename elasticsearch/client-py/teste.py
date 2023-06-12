from elasticsearch import Elasticsearch
from flask import Flask, render_template, request

app = Flask(__name__)
es = Elasticsearch('http://localhost:9200')

@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/show_all')
def show_all():
    page = request.args.get('page', 1, type=int)
    per_page = 15
    start = (page - 1) * per_page
    search_result = es.search(index='bank', from_=start, size=per_page)
    records = search_result['hits']['hits']
    return render_template('show_all.html', records=records, page=page)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        search_result = es.search(index='bank', body={"query": {"query_string": {"query": query}}})
        records = search_result['hits']['hits']
        return render_template('search_results.html', records=records)
    return render_template('search.html')

    
@app.route('/add')
def add():
    # Add your add logic here
    pass

@app.route('/delete')
def delete():
    # Add your delete logic here
    pass

if __name__ == '__main__':
    app.run()

