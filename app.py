from flask import Flask,request,jsonify
import numpy as np
import datetime 

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    if request.headers.get('Authorization') != 'secret_key':
        return jsonify({"status": "Error","message":"Unauthorization!"}), 401
    data = request.json
    try:
        nums = data['args']
        sumOfNumbers = sum(nums)
    except KeyError:
        return jsonify({"status":"error","message": "Missing 'args' in request"}), 400
    except TypeError:
        return jsonify({"status":"error","message": "Invalid 'args' in request. Expected list of numbers"}), 400

    response = {
        "status": "success",
        "response":{
            "datetime": datetime.datetime.now(),
            "args": data['args'],
            "sum": sumOfNumbers
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True,port=3003)