import connexion
import json
from flask import jsonify
from flask.ext.api import status
from swagger_server.models.error import Error
from swagger_server.models.generic_object import GenericObject
from swagger_server.models.uid_info import UidInfo
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from pymongo import MongoClient
from flask.ext.api import status

client = MongoClient()
db = client.path_db

def create_json(uid, body):
	#gotta check if the body is valid jsonc
	return jsonify({"uid":str(uid), "body":str(body)})

def insert_json(uid, body):
	db.posts.insert_one({"uid": str(uid), "body":str(body)})
	
def find_uid(uid):
	return db.posts.find({"uid": str(uid)}).count() != 0

def get_status(status, message):
	return jsonify({"Status": status, "Message": message})


def root_get():
	return 'This is version 1.0'


def root_post():
	#need to create a method to give better uid ... this method will give an error if a user deletes any uid thats not the last...lulz
	db_size = db.posts.count()+1
	for i in range(1, db_size):
		if(db.posts.find_one({"uid":str(i)}) == None):
			insert_json(i, {"data": 'empty'})
			return jsonify({"uid": i})
	insert_json(db_size, {"data": 'empty'})
	return jsonify({"uid": db_size})


def uid_delete(uid):
	if db.posts.delete_many({"uid": str(uid)}).deleted_count == 0:
		return get_status(404, "NOT FOUND"), status.HTTP_404_NOT_FOUND
	else:
		return get_status(200, "Successfully Deleted")


def uid_get(uid):
	#run a check to see if the uid exists
	if not find_uid(uid):
		return get_status(404, "COULD NOT FIND"), status.HTTP_404_NOT_FOUND
	#if the uid doesn't exist then just go ahead return error status
	ret_object = db.posts.find_one({"uid": str(uid)})
	return jsonify(ret_object['body'])


def uid_post(uid, body):
	#this checks if incoming data is valid json
	if connexion.request.is_json:
		if not find_uid(uid):
			return get_status(404, "COULD NOT FIND"), status.HTTP_404_NOT_FOUND
		body = GenericObject.from_dict(connexion.request.get_json())
		db.posts.find_one_and_update({"uid":str(uid)}, {"$set": {"body": str(body)}})
	#need to write better messages to return for a success
		return get_status(200, "Successfully POSTED")
	else:
		return get_status(500, "Unexpected ERROR"), status.HTTP_500_INTERNAL_SERVER_ERROR
	

def uid_put(uid, body):
	#this checks if incoming data is valid json and for valid uid
	if connexion.request.is_json:
		if(find_uid(uid) == False):
			return get_status(404, "COULD NOT FIND"), status.HTTP_404_NOT_FOUND
		body = GenericObject.from_dict(connexion.request.get_json())
		db.posts.find_one_and_update({"uid":str(uid)}, {"$set": {"body": str(body)}})
	#need to write better messages to return for a success
		return get_status(200, "Successfully PUT/UPDATED")
	else:
		return get_status(500, "Unexpected ERROR"), status.HTTP_500_INTERNAL_SERVER_ERROR