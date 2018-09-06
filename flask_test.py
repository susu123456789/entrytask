from flask import Flask, jsonify, request
import time

app = Flask(__name__)

data = {}


@app.route('/shopee/test', methods=['GET', 'POST','PUT','DELETE'])
def entre_task():
    if request.method == 'GET':

        if request.args.get('a') and request.args.get('b'):
            if request.args.get('a').isdigit() and request.args.get('b').isalpha():

                if request.args.get('a') == '9999':
                    data['error_code'] = "11"
                    data['error_message'] = "system error"
                    data['refernce'] = request.args.get('a')
                    resp = jsonify(data)
                    resp.headers['content-type'] = 'application/json'
                    time.sleep(5)
                    return resp

                elif len(request.args.get('a')) < 10 and len(request.args.get('b')) < 10:
                    data['error_code'] = "0"
                    data['error_message'] = "success"
                    data['refernce'] = request.args.get('a')
                    resp = jsonify(data)
                    resp.headers['content-type'] = 'application/json'
                    return resp
                else:
                    data['error_code'] = "11"
                    data['error_message'] = "system error"
                    data['refernce'] = request.args.get('a')
                    resp = jsonify(data)
                    resp.headers['content-type'] = 'application/json'
                    return resp


            else:
                data['error_code'] = "21"
                data['error_message'] = "empty or wrong params"
                data['refernce'] = request.args.get('a')
                resp = jsonify(data)
                resp.headers['content-type'] = 'application/json'
                return resp

        else:
            data['error_code'] = "21"
            data['error_message'] = "empty or wrong params"
            data['refernce'] = request.args.get('a')
            resp = jsonify(data)
            resp.headers['content-type'] = 'application/json'
            return resp


    else:
        data['error_code'] = "11"
        data['error_message'] = "system error"
        data['refernce'] = request.args.get('a')
        resp = jsonify(data)
        resp.headers['content-type'] = 'application/json'
        return resp


if __name__ == '__main__':
    app.run()
