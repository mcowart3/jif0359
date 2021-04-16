import os
import flask
import database

from flask import Flask, send_from_directory
from api import documents, search, sort, tag

app = Flask(__name__, static_folder='build/')
app.register_blueprint(documents.doc_bp)
app.register_blueprint(search.doc_bp)
app.register_blueprint(sort.doc_bp)
app.register_blueprint(tag.doc_bp)

db = database.Database()
db.db_init([database.DOC_1, database.DOC_2, database.DOC_3, database.DOC_4, database.DOC_5, database.DOC_6])

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    response = flask.jsonify({})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    apprun(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
