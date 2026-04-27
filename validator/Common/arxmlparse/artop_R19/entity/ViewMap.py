# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ViewMap.py
from .Identifiable import Identifiable

class ViewMap(Identifiable):

    def __init__(self):
        super().__init__()
        from .ViewMapSet import ViewMapSet
        from .Referrable import Referrable
        from .AnyInstanceRef import AnyInstanceRef
        self._artop_role = None
        self._artop_viewMapSet = None
        self._artop_firstElementRef = []
        self._artop_secondElementRef = []
        self._artop_firstElementInstanceIref = []
        self._artop_secondElementInstanceIref = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_viewMapSet': '"VIEW-MAP-SET"', 
         '_artop_firstElementRef': '"REFERRABLE"', 
         '_artop_secondElementRef': '"REFERRABLE"', 
         '_artop_firstElementInstanceIref': '"ANY-INSTANCE-REF-IREF"', 
         '_artop_secondElementInstanceIref': '"ANY-INSTANCE-REF-IREF"'})

    @property
    def role_(self):
        return self._artop_role

    @property
    def ref_viewMapSet_(self):
        return self._artop_viewMapSet

    @property
    def viewMapSet_(self):
        if self._artop_viewMapSet is not None:
            if hasattr(self._artop_viewMapSet, "uuid"):
                return self._artop_viewMapSet.uuid
        return

    @property
    def ref_firstElements_(self):
        return self._artop_firstElementRef

    @property
    def firstElements_(self):
        return self._artop_firstElementRef

    @property
    def ref_secondElements_(self):
        return self._artop_secondElementRef

    @property
    def secondElements_(self):
        return self._artop_secondElementRef

    @property
    def firstElementInstances_AnyInstanceRef(self):
        return self._artop_firstElementInstanceIref

    @property
    def secondElementInstances_AnyInstanceRef(self):
        return self._artop_secondElementInstanceIref
