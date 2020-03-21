from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='List Sum API', description='A restAPI to sum a list of integers', ordered=True)
ns = api.namespace('total', description='Sum List Operations', ordered=True)


@ns.route('/')
class Total(Resource):
    def get(self):
        total = 6  # TODO Method required --> If List of [1, 2, 3] passed OUT 6
        return {"Total:": total}, 200


if __name__ == '__main__':
    app.run(debug=True)
