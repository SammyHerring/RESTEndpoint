from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='List Sum API', description='A restAPI to sum a list of integers', ordered=True)
ns = api.namespace('total', description='Sum List Operations', ordered=True)  # Define 'total' namespace in API


# Define namespace 'total' main route
@ns.route('/')
class Total(Resource):
    def get(self):
        total = 6  # TODO Method required --> If List of [1, 2, 3] passed OUT 6
        return {"Total:": 6}, 200


#   START   |   APP LOGIC

def generateNumberList() -> list:
    numbers_to_add = list(range(10000001))  # Function required by client scenario
    return numbers_to_add


#   END     |   APP LOGIC

if __name__ == '__main__':
    app.run(debug=True)
