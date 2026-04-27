# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Collection.py
from .ARElement import ARElement

class Collection(ARElement):

    def __init__(self):
        super().__init__()
        from .Identifiable import Identifiable
        from .AnyInstanceRef import AnyInstanceRef
        self._artop_autoCollect = None
        self._artop_elementRole = None
        self._artop_elementRef = []
        self._artop_sourceElementRef = []
        self._artop_collectedInstanceIref = []
        self._artop_sourceInstanceIref = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_elementRef': '"IDENTIFIABLE"', 
         '_artop_sourceElementRef': '"IDENTIFIABLE"', 
         '_artop_collectedInstanceIref': '"ANY-INSTANCE-REF-IREF"', 
         '_artop_sourceInstanceIref': '"ANY-INSTANCE-REF-IREF"'})

    @property
    def autoCollect_(self):
        return self._artop_autoCollect

    @property
    def elementRole_(self):
        return self._artop_elementRole

    @property
    def ref_elements_(self):
        return self._artop_elementRef

    @property
    def elements_(self):
        return self._artop_elementRef

    @property
    def ref_sourceElements_(self):
        return self._artop_sourceElementRef

    @property
    def sourceElements_(self):
        return self._artop_sourceElementRef

    @property
    def collectedInstances_AnyInstanceRef(self):
        return self._artop_collectedInstanceIref

    @property
    def sourceInstances_AnyInstanceRef(self):
        return self._artop_sourceInstanceIref
