#!/usr/bin/env python3
"""
function that returns the list of school having a specific topic:

Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection will be the pymongo collection object
topic (string) will be topic searched
"""
from typing import List


def schools_by_topic(mongo_collection, topic: str) -> List:
    """
    return list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
