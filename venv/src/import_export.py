import os
import pymongo

# connection = pymongo.MongoClient('localhost:27010')
# db = connection.get_database('cw')

def export_collection(db_name="cw", collection="guitars", filepath="guitars.json", host="localhost:27010"):
    print(os.getcwd())
    command = "mongoexport --db {} --collection {} --out ./{} --host {}".format(db_name, collection, filepath, host)
    os.system(command)
    return "{}.collection {} exported to file {}".format(db_name, collection, filepath)
 
 
def import_collection(db_name="cw", collection="guitars", filepath="guitars.json", host="localhost:27010"):
    print(os.getcwd())
    command = "mongoimport --db {} --collection {} --file ./{} --host {}".format(db_name, collection, filepath, host)
    os.system(command)
    return "{}.collection {} imported to file {}".format(db_name, collection, filepath)