#!/usr/bin/env python3
"""
Lits all documents
"""


def list_all(mongo_collection):
    """
    function
    """
    return list(mongo_collection.find())

