import os
import pymongo
from pymongo import MongoClient

DOC_5 = {
    "author": "John Donne",
    "text": "SIR, more than kisses, letters mingle souls,\nFor thus, friends absent speak. This ease controls\nThe tediousness of my life ; but for these\nI could ideate nothing which could please ;\nBut I should wither in one day, and pass\nTo a bottle of hay, that am a lock of grass.\nLife is a voyage, and in our lives' ways\nCountries, courts, towns are rocks, or remoras ;\nThey break or stop all ships, yet our state's such,\nThat though than pitch they stain worse, we must touch.\nIf in the furnace of the raging line,\nOr under th' adverse icy pole thou pine,\nThou know'st two temperate regions, girded in,\nDwell there ; but O, what refuge canst thou win\nParch'd in the court, and in the country frozen ?\nShall cities built of both extremes be chosen ?\nCan dung or garlic be perfume ? Or can\nA scorpion or torpedo cure a man ?\nCities are worst of all three ; of all three ?\nO knotty riddle !  ; each is worst equally.\nCities are sepulchres ; they who dwell there\nAre carcases, as if no such there were.\nAnd courts are theatres, where some men play\nPrinces, some slaves, all to one end, of one clay.\nThe country is a desert, where the good,\nGain'd, inhabits not, born, is not understood.\nThere men become beasts, and prone to more evils ;\nIn cities blocks, and in a lewd court devils.\nAs in the first chaos, confusedly,\nEach element's qualities were in th' other three,\nSo pride, lust, covetise, being several\nTo these three places, yet all are in all,\nAnd mingled thus, their issue is incestuous.\nFalsehood is denizen'd ; virtue is barbarous.\nLet no man say there, “ Virtue's flinty wall\nShall lock vice in me, I'll do none, but know all.”\nMen are sponges, which, to pour out, receive ;\nWho know false play, rather than lose, deceive.\nFor in best understandings sin began,\nAngels sinn'd first, then devils, and then man.\nOnly perchance beasts sin not ; wretched we\nAre beasts in all but white integrity.\nI think if men, which in these place live,\nDurst look in themselves, and themselves retrieve,\nThey would like strangers greet themselves, seeing then\nUtopian youth grown old Italian.\n\tBe then thine own home, and in thyself dwell ;\nInn anywhere ; continuance maketh hell.\nAnd seeing the snail, which everywhere doth roam,\nCarrying his own house still, still is at home ;\nFollow—for he is easy paced—this snail,\nBe thine own palace, or the world's thy gaol.\nAnd in the world's sea do not like cork sleep\nUpon the water's face ; nor in the deep\nSink like a lead without a line ; but as\nFishes glide, leaving no print where they pass,\nNor making sound ; so closely thy course go,\nLet men dispute, whether thou breathe or no.\nOnly in this be no Galenist—to make\nCourts' hot ambitions wholesome, do not take\nA dram of country's dullness ; do not add\nCorrectives, but, as chemics, purge the bad.\nBut, sir, I advise not you, I rather do\nSay o'er those lessons, which I learn'd of you ;\nWhom, free from Germany's schisms, and lightness\nOf France, and fair Italy's faithlessness,\nHaving from these suck'd all they had of worth,\nAnd brought home that faith which you carried forth,\nI thoroughly love ; but if myself I've won\nTo know my rules, I have, and you have DONNE.",
    "title": "To Sir Henry Wotton" ,
    "tags": ["poetic", "friendship"],
    "correspondent": "Wotton"
    }



#client = pymongo.MongoClient("mongodb://localhost:5000/")
#db = client["database"]
#col = db["documents"]

class Database:
    db_up = False

    def __init__(self):
        if not self.db_up:
            conn_str = "mongodb://{user_name}:{pwd}@{host_name}:{port}".format(
                user_name=os.environ["MONGO_INITDB_ROOT_USERNAME"],
                pwd=os.environ["MONGO_INITDB_ROOT_PASSWORD"],
                host_name="db",
                port=27017
            )
            self.client = MongoClient(conn_str)
            self.db = self.client["donne_documents"]
            self.documents = self.db["documents"]
            self.db_up = True

    def db_init(self, documents):
        self.clear_db()

        
        self.add_doc(documents)

    def clear_db(self):
        docs = self.get_all_docs()

        for doc in docs:
            self.documents.delete_one(doc)

    def get_doc(self, query):
        #EX: db.get_doc({'author': 'John Donne'})
        doc = self.documents.find(query)
        return doc

    def get_multi_doc(self, query):
        #EX: db.get_multi_doc({'author': 'John Donne'})
        doc = self.documents.find(query)
        return doc

    def get_all_docs(self):
        #If we make this larger, we will remove the list() and just leave it as a cursor
        return list(self.documents.find())

    def get_all_docs_sorted(self, sortCriteria, ascending):
        return list(self.documents.find().sort(sortCriteria, ascending))

    def filter(self, which, criteria):
        if which == "date":
            return list(self.documents.find({"year": criteria}))
        elif which == "correspondent":
            return list(self.documents.find({"correspondent":criteria}))

    #def add_doc(self, new_doc):
       # docs = self.db.documents
        #new_doc_id = docs.insert_one(new_doc).inserted_id
        #return new_doc_id
    def add_doc(self, new_doc):
        docs = self.db.documents
        new_doc_id = docs.insert_many(new_doc)
        return new_doc_id
