import os

MONGO_DB_URI='mongodb+srv://admin:313001@cluster0.6jr3w.mongodb.net/app?retryWrites=true&w=majority'

# make collections named questions, answers , responses

os.environ['MONGO_DB_URI'] = MONGO_DB_URI
