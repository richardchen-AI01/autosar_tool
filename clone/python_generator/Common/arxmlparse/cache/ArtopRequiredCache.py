# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\cache\ArtopRequiredCache.py
from typing import TypeVar
T = TypeVar("T")
cache = {}

def getCacheInstance() -> dict:
    global cache
    return cache


def values() -> list:
    return list(cache.values())


def keys() -> list:
    return list(cache.keys())


def put(uuid_elements):
    global cache
    if uuid_elements:
        cache = uuid_elements


def updateCache(key, val):
    if key is None:
        return
    cache[key] = val


def getCache(key):
    if key in cache:
        return cache[key]


def get_len():
    return len(cache.keys())
