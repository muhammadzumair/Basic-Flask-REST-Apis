from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': "Alpha Store",
        'items': [
            {
                'name': 'Item-1',
                'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/store', methods=['POST'])
def create_store():
    requestData = request.get_json()
    newStore = {
        'name': requestData['name'],
        'items': []
    }
    stores.append(newStore)
    return jsonify(newStore)


@app.route('/store/<string:name>')
def getStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'error': 'no store found with name: ${name}'})


@app.route('/store')
def getStores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def createItemInStore(name):
    requestData = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : requestData['name'],
                'price' : requestData['price']
            }
        store['items'].append(new_item)
        return jsonify(new_item)
    return jsonify({'error': 'no store found with name: ${name}'})


@app.route('/store/<string:name>/item')
def getItemsInStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'error': 'no store found with name: ${name}'})


app.run(port=5000)
