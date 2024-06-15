#!/usr/bin/env python3
"""insert new documents"""


def insert_school(mongo_collection, **kwargs):
    newdoc = mongo_collection.insert_one(kwargs)
    return newdoc.inserted_id
    