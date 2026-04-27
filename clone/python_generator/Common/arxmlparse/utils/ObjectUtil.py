# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\utils\ObjectUtil.py


def isNotNull(obj):
    if obj:
        return True
    return False


def isNull(obj):
    if obj is None or len(obj) <= 0:
        return True
    return False


def isNone(obj):
    if obj is None:
        return True
    return False


def isNotNone(obj):
    if obj is not None:
        return True
    return False


def hasLength(obj):
    if len(obj) > 0:
        return True
    return False
