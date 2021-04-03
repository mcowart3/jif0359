import os
from flask import Flask, send_from_directory
from api import documents, search, sort, tag

app = Flask(__name__, static_folder='build/')
app.register_blueprint(documents.doc_bp)
app.register_blueprint(search.doc_bp)
app.register_blueprint(sort.doc_bp)
app.register_blueprint(tag.doc_bp)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    return {}
