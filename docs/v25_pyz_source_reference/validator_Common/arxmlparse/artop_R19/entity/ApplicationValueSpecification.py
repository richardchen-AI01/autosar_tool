# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ApplicationValueSpecification.py
from .ValueSpecification import ValueSpecification

class ApplicationValueSpecification(ValueSpecification):

    def __init__(self):
        super().__init__()
        from .SwAxisCont import SwAxisCont
        from .SwValueCont import SwValueCont
        self._artop_category = None
        self._artop_swAxisCont = []
        self._artop_swValueCont = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_swAxisCont':"SW-AXIS-CONT", 
         '_artop_swValueCont':"SW-VALUE-CONT"})

    @property
    def category_(self):
        return self._artop_category

    @property
    def swAxisConts_SwAxisCont(self):
        return self._artop_swAxisCont

    @property
    def ref_swValueCont_(self):
        return self._artop_swValueCont

    @property
    def swValueCont_(self):
        if self._artop_swValueCont is not None:
            if hasattr(self._artop_swValueCont, "uuid"):
                return self._artop_swValueCont.uuid
        return
