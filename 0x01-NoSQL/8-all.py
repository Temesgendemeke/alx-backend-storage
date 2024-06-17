#!/usr/bin/env python3
""" 
     lists all documents in a collection
"""

def list_all(mongo_collection):
    """list all documents in a collection"""
    if mongo_collection is None:
        return []
    doc = mongo_collection.find()
    
    return list(doc)
    