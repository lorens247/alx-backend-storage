#!/usr/bin/env python3
"""
mongo list
"""


def schools_by_topic(mongo_collection, topic):
    """
    function
    """
    return mongo_collection.find({"topics": topic})

