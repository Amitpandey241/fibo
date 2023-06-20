from flask import Flask, request, make_response, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

dict1 = {}

class Register(Resource):
    def post(self):
        userinfo = request.get_json()
        username = userinfo.get("username")
        password = userinfo.get("password")
        if username and password:
            b = {"username": username, "password": password}
            print(b)

            res = dict1.update(b)
        return make_response(jsonify({"message": "User created successfully"}))
api.add_resource(Register, '/')

if __name__ == '__main__':
    app.run(debug=True)

print(dict1)