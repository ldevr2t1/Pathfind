import connexion
import json
from flask import jsonify
from swagger_server.models.error import Error
from swagger_server.models.generic_object import GenericObject
from swagger_server.models.uid_info import UidInfo
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from pymongo import MongoClient


client = MongoClient()
db = client.path_db

def create_json(uid, body):
    #gotta check if the body is valid jsonc
    return jsonify({"uid":str(uid), "body":str(body)})

def insert_json(uid, body):
    db.posts.insert_one({"uid": str(uid), "body":str(body)})
    
def return_uid(uid):
    return db.posts.find_one({"uid": str(uid)})

def root_get():
    return 'This is version 1.0'


def root_post():
    #need to create a method to give better uid ... this method will give an error if a user deletes any uid thats not the last...lulz
    db_size = db.posts.count()+1
    insert_json(db_size, {"data": 'empty'})
    return jsonify({"uid": db_size})


def uid_delete(uid):
    db.posts.delete_one({"uid": str(uid)})
    return jsonify({"Status": 200, "Message": "Successfully posted"})


def uid_get(uid):
    #run a check to see if the uid exists
    ret_object = db.posts.find_one({"uid": str(uid)})
    #if the uid doesn't exist then just go ahead return error status
    return jsonify(ret_object['body'])


def uid_post(uid, body):
    #this checks if incoming data is valid json
    print()
    print("body" + str(body))
    if connexion.request.is_json:
        print("inside connextion")
        body = GenericObject.from_dict(connexion.request.get_json())
        db.posts.find_one_and_update({"uid":str(uid)}, {"$set": {"body": str(body)}})
    #need to write better messages to return for a success
        return jsonify({"Status": 200, "Message": "Successfully posted"})
    else:
        return jsonify({"Status": 500, "Message": "Unexpected Error"})
    

def uid_put(uid, body):
    #this checks if incoming data is valid json
    if connexion.request.is_json:
        body = GenericObject.from_dict(connexion.request.get_json())
        db.posts.find_one_and_update({"uid":str(uid)}, {"$set": {"body": str(body)}})
    #need to write better messages to return for a success
        return jsonify({"Status": 200, "Message": "Successfully posted"})
    else:
        return jsonify({"Status": 500, "Message": "Unexpected Error"})
