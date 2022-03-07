from flask import Flask,jsonify,request

app = Flask(__name__)

data = [
    {
        "id": 1,
        "Contact": '9657432149',
        "Name" : "Rajesh",
        "done": "False"

    },
    {
        "id" : '2',
        "Name": 'George',
        "Contact": '9803562348',
        "done" : 'False'

    }   
]

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data!"
        }, 400)
    
    list = {
        "id": data[-1]["id"] + 1,
        "Name":request.json["title"], 
        "Contact": request.json["description"],
        "done": False
    }

    data.append(list)
    return jsonify({
            "status": "success",
            "message": "List added successfully!"
        })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": list
    })


if __name__ == "__main__":
    app.run(debug = True)                