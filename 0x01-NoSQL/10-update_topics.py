#!/usr/bin/env python3
"""
change all topics of a school document based on the name
Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) will be the school name to update
topics (list of strings) will be the list of topics approached in the school
"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List) -> List:
    """
    return list of changed topics of a school document
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
