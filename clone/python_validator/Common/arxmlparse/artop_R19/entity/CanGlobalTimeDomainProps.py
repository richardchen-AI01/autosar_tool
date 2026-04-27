# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanGlobalTimeDomainProps.py
from .AbstractGlobalTimeDomainProps import AbstractGlobalTimeDomainProps

class CanGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):

    def __init__(self):
        super().__init__()
        self._artop_fupDataIdList = None
        self._artop_ofnsDataIdList = None
        self._artop_ofsDataIdList = None
        self._artop_syncDataIdList = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def fupDataIdList_(self):
        return self._artop_fupDataIdList

    @property
    def ofnsDataIdList_(self):
        return self._artop_ofnsDataIdList

    @property
    def ofsDataIdList_(self):
        return self._artop_ofsDataIdList

    @property
    def syncDataIdList_(self):
        return self._artop_syncDataIdList
