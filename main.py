from flask import Flask, jsonify, redirect, url_for, request, render_template

app = Flask(__name__)

customers = [{'customer_id' : "0",
             'name' : "Praveen S",
             'account_number' : "123456789",
             'accoount_type' : "Savings",
             'balance_available' : "10000"},
             {'customer_id' : "1",
             'name' : "Ragul M",
             'account_number' : "123456788",
             'accoount_type' : "Savings",
             'balance_available' : "10000"}
            ]

@app.route('/')
def index():
    return 'Welcome to Banking Application'


@app.route('/customers', methods=['GET'])
def get():
    return jsonify(customers)

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    return jsonify(customers[customer_id])

#for creation open create html

@app.route('/new',methods = ['POST'])
def new():
    customer = {'customer_id': request.form['cid'],
                'name': request.form['nm'],
                'account_number': request.form['ac'],
                'account_type': request.form['at'],
                'balance_available': request.form['bal']}
    customers.append(customer)
    return jsonify({'Created': customer})

#for updation open update1.html

@app.route('/customers/update', methods=['PUT'])
def customer_update(customer_id):
    customer = {'customer_id': request.form['cid'],
                'name': request.form['nm'],
                'account_number': request.form['ac'],
                'account_type': request.form['at'],
                'balance_available': request.form['bal']}
    customers[customer_id] = customer
    return jsonify(customers[customer_id])

@app.route('/customers/delete/<int:customer_id>', methods=['DELETE'])
def delete(customer_id):
    customers.remove(customers[customer_id])
    return jsonify({'result': True})



if __name__ == '__main__':
    app.run(debug = True)

