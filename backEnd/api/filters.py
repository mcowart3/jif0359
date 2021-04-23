import database
from flask import Blueprint, make_response, json, request
import pymongo
from bson.objectid import ObjectId

# Blueprint Configuration
doc_bp = Blueprint('sort_bp', __name__,
                   template_folder='templates',
                   static_folder='build/',
                   url_prefix='/')

db = database.Database()

@doc_bp.route('/filter/<string:which>/<string:criteria>', methods=['GET'])

def filters(which, criteria):
    docs = db.filter(which, criteria)
    for d in docs:
        d['_id'] = str(d['_id'])
        docs = json.dumps(docs)
        response = make_response(
            docs, 200, {'Content-Type': 'application/json'})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
