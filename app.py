from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='List Sum API', description='A restAPI to sum a list of integers', ordered=True)
ns = api.namespace('total', description='Sum List Operations', ordered=True)  # Define 'total' namespace in API


# Define namespace 'total' main route
@ns.route('/')
@ns.response(200, 'Success. OK')
@ns.response(400, 'Not ALL List Items of Type Int. BAD')
class Total(Resource):
    def get(self):
        numbers = generateNumberList()
        if checkListItemsAreInt(numbers):
            total = sum(numbers)
            return {"Total:": total}, 200
        else:
            api.abort(400, "Not ALL List Items of Type Int")


#   START   |   APP LOGIC

def generateNumberList() -> list:
    numbers_to_add = list(range(10000001))  # Function required by client scenario
    return numbers_to_add


# Validate list items are all of type int
def checkListItemsAreInt(listData: list) -> bool:
    if all(isinstance(item, int) for item in listData):
        return True
    else:
        return False


#   END     |   APP LOGIC

if __name__ == '__main__':
    app.run(debug=True)
