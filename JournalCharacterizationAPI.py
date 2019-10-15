from flask import Flask
from flask_restful import Resource, Api
import json

from ControllerJournalCharacterization import ControllerJournalCharacterization

app = Flask(__name__)
api = Api(app)


class QueryJournalsApi(Resource):
    def get(self, nom):
        journals = ControllerJournalCharacterization.update_journals(nombre=nom)

        return json.dumps(journals)


api.add_resource(QueryJournalsApi, '/<string:nom>')

if __name__ == '__main__':
    app.run(debug=True)