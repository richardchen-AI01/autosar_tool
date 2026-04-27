# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DltMessage.py
from .Identifiable import Identifiable

class DltMessage(Identifiable):

    def __init__(self):
        super().__init__()
        from .DltMessageCollectionSet import DltMessageCollectionSet
        from .DltArgument import DltArgument
        self._artop_messageId = None
        self._artop_messageLineNumber = None
        self._artop_messageSourceFile = None
        self._artop_messageTypeInfo = None
        self._artop_dltMessageCollectionSet = None
        self._artop_dltArgument = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dltMessageCollectionSet':"DLT-MESSAGE-COLLECTION-SET", 
         '_artop_dltArgument':"DLT-ARGUMENT"})

    @property
    def messageId_(self):
        return self._artop_messageId

    @property
    def messageLineNumber_(self):
        return self._artop_messageLineNumber

    @property
    def messageSourceFile_(self):
        return self._artop_messageSourceFile

    @property
    def messageTypeInfo_(self):
        return self._artop_messageTypeInfo

    @property
    def ref_dltMessageCollectionSet_(self):
        return self._artop_dltMessageCollectionSet

    @property
    def dltMessageCollectionSet_(self):
        if self._artop_dltMessageCollectionSet is not None:
            if hasattr(self._artop_dltMessageCollectionSet, "uuid"):
                return self._artop_dltMessageCollectionSet.uuid
        return

    @property
    def dltArguments_DltArgument(self):
        return self._artop_dltArgument
