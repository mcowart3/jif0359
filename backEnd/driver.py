import database
from bson.objectid import ObjectId

if __name__ == '__main__':
    db = database.Database(url='localhost', port=27017, db_name='donne_documents')
    db.db_init([database.DOC_1, database.DOC_2, database.DOC_3, database.DOC_4, database.DOC_5, database.DOC_6])
