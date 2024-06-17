#!/usr/bin/env python3
"""log stats"""

from pymongo import mongo_client


def log_stats():
    """log stats"""
    client = mongo_client.MongoClient("mongodb://localhost:27017")
    collection = client.logs.nginx
    print(f'{collection.estimated_document_count()} logs')
    print("Methods:")
    print(f'\tmethod GET: {collection.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {collection.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {collection.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {collection.count_documents({"method": "PATCH"})}')
    print('\tmethod DELETE: {}'.format(collection.count_documents({"method": "DELETE"})))
    print(f'{collection.count_documents({"method": "GET", "path": "/status"})} status check')
    

if __name__ == "__main__":
    log_stats()