import connexion
from swagger_server.models.error import Error
from swagger_server.models.generic_object import GenericObject
from swagger_server.models.uid_info import UidInfo
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def root_get():
    """
    Returns the current versions information
    Get all of the details of the current version

    :rtype: List[GenericObject]
    """
    return 'do some magic!'


def root_post():
    """
    creates a new uid
    return the new generated

    :rtype: int
    """
    return 'do some magic!'


def uid_delete(uid):
    """
    delete a uid
    delete a uid 
    :param uid: the UID
    :type uid: int

    :rtype: None
    """
    return 'do some magic!'


def uid_get(uid):
    """
    get the particular uid for the version
    Will return the current object(s) stored for the uid 
    :param uid: the UID
    :type uid: int

    :rtype: UidInfo
    """
    return 'do some magic!'


def uid_post(uid, body):
    """
    creates a new uid
    return the new generated uid
    :param uid: the UID
    :type uid: int
    :param body: Information/object for the uid
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = GenericObject.from_dict(connexion.request.get_json())
    return 'do some magic!'


def uid_put(uid, body):
    """
    update an existing uid
    Will return the current object(s) stored for the uid 
    :param uid: the uid
    :type uid: int
    :param body: Information/object for the uid
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = GenericObject.from_dict(connexion.request.get_json())
    return 'do some magic!'
