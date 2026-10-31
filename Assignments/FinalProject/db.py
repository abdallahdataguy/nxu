"""MongoDB connection helper shared by the Flask app and the scripts."""

from pymongo import MongoClient

import config

_client = None


def get_collection():
    """Return the survey collection, creating the client on first use."""
    global _client
    if _client is None:
        _client = MongoClient(config.MONGO_URI, serverSelectionTimeoutMS=5000)
    return _client[config.MONGO_DB_NAME][config.MONGO_COLLECTION]
