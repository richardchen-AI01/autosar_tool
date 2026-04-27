# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Ieee1722TpEthernetFrame.py
from .AbstractEthernetFrame import AbstractEthernetFrame

class Ieee1722TpEthernetFrame(AbstractEthernetFrame):

    def __init__(self):
        super().__init__()
        self._artop_relativeRepresentationTime = None
        self._artop_streamIdentifier = None
        self._artop_subType = None
        self._artop_version = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def relativeRepresentationTime_(self):
        return self._artop_relativeRepresentationTime

    @property
    def streamIdentifier_(self):
        return self._artop_streamIdentifier

    @property
    def subType_(self):
        return self._artop_subType

    @property
    def version_(self):
        return self._artop_version
