#!/usr/bin/env python3
"""
insert a new document in a collection based on kwargs
mongo_collection will be the pymongo collection object
"""
from typing import List


def insert_school(mongo_collection, **kwargs) -> List:
    """
    returns the new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
