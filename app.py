from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://testeaprendizado.commercesuite.com.br/web_api/products"

@app.route('/')
def index():
  
    page = request.args.get('page', 1, type=int)
    limit = 10  
    params = {
        'page': page,
        'limit': limit
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    products = data.get('Products', [])
    total = data['paging']['total']
    page = data['paging']['page']
    limit = data['paging']['limit']

    return render_template('index.html', products=products, total=total, page=page, limit=limit)

if __name__ == '__main__':
    app.run(debug=True)
