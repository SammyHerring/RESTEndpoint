from flask import Flask
from flask_restplus import Api, Resource, fields

#   START   |   API CONFIG

app = Flask(__name__)
api = Api(app, version='1.0', title='List Sum API', description='A restAPI to sum a list of integers',
          contact='Sam Herring', contact_email='sammy@traveller.coffee', ordered=True)
ns = api.namespace('total', description='Sum List Operations')  # Define 'total' namespace in API

#   END     |   API CONFIG


#   START   |   API MODELS CONFIG

# Total Model expected upon return of sum
total_model = api.model('Total', {
    "Total": fields.Integer(description='Sum of passed list'),
})

# List Model expected when posting list of integers
list_model = api.model('List', {
    "List": fields.List(fields.Integer(description='Item (Integer)'), description="List of Integers"),
})


#   END     |   API MODELS CONFIG


#   START   |   API BLUEPRINT

# Define 'total' namespace main api  route
@ns.route('/')
@ns.response(200, 'Success. OK')
@ns.response(400, 'Not ALL List Items of Type Int. BAD')
class Total(Resource):
    # GET Default List Sum
    @ns.doc('list_total')
    @ns.marshal_with(total_model)
    def get(self):
        numbers = generateNumberList()
        if checkListItemsAreInt(numbers):
            return {"Total": sum(numbers)}, 200
        else:
            api.abort(400, "Not ALL List Items of Type Int")

    # POST List of Integers and Return Sum
    @ns.doc('list_total')
    @ns.marshal_with(total_model)
    @ns.expect(list_model)
    def post(self):
        numbers = api.payload['List']
        if checkListItemsAreInt(numbers):
            return {"Total": sum(numbers)}, 200
        else:
            api.abort(400, "Not ALL List Items of Type Int")


#   END     |   API BLUEPRINT


#   START   |   APP LOGIC

def generateNumberList() -> list:
    numbers_to_add = list(range(10000001))  # Function required by client scenario
    return numbers_to_add


# Validate list items are all of type int
def checkListItemsAreInt(listData: list) -> bool:
    try:
        if all(isinstance(item, int) for item in listData):
            return True
        else:
            return False
    except TypeError:
        assert "Object passed not iterable"
        return False


#   END     |   APP LOGIC

if __name__ == '__main__':
    app.run(debug=True)
