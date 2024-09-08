from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/client")
def client():
    return jsonify(client) 


@app.route("/api/clients")
def clients():
    return jsonify(clients)


## Data hard code 

client = { "name":"Jacobs","sur_name":"Feldman"}

clients =  [ { "name": "Dan","surName": "Feldman"},{"name": "Joseph","surName": "Feldman"},{ "name": "Mark","surName": "Feldman" } ]

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8075')