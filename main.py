from flask import Flask
from flask_restful import Api, Resource
# import time

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self, mame):
        return {"name": name, "test": test}


api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)
