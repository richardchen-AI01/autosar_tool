# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ApplicationAssocMapElementValueSpecification.py
from .ARObject import ARObject

class ApplicationAssocMapElementValueSpecification(ARObject):

    def __init__(self):
        super().__init__()
        from .ApplicationAssocMapValueSpecification import ApplicationAssocMapValueSpecification
        from .ValueSpecification import ValueSpecification
        self._artop_applicationAssocMapValueSpecification = None
        self._artop_key = None
        self._artop_value = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_applicationAssocMapValueSpecification':"APPLICATION-ASSOC-MAP-VALUE-SPECIFICATION", 
         '_artop_key':"VALUE-SPECIFICATION", 
         '_artop_value':"VALUE-SPECIFICATION"})

    @property
    def ref_applicationAssocMapValueSpecification_(self):
        return self._artop_applicationAssocMapValueSpecification

    @property
    def applicationAssocMapValueSpecification_(self):
        if self._artop_applicationAssocMapValueSpecification is not None:
            if hasattr(self._artop_applicationAssocMapValueSpecification, "uuid"):
                return self._artop_applicationAssocMapValueSpecification.uuid
        return

    @property
    def ref_key_(self):
        return self._artop_key

    @property
    def key_(self):
        if self._artop_key is not None:
            if hasattr(self._artop_key, "uuid"):
                return self._artop_key.uuid
        return

    @property
    def ref_value_(self):
        return self._artop_value

    @property
    def value_(self):
        if self._artop_value is not None:
            if hasattr(self._artop_value, "uuid"):
                return self._artop_value.uuid
        return
