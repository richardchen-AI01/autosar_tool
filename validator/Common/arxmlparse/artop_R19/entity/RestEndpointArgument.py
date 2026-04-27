# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RestEndpointArgument.py
from .ARObject import ARObject

class RestEndpointArgument(ARObject):

    def __init__(self):
        super().__init__()
        from .RestAbstractEndpoint import RestAbstractEndpoint
        from .RestAbstractPropertyDef import RestAbstractPropertyDef
        self._artop_mandatory = None
        self._artop_restAbstractEndpoint = None
        self._artop_parameter = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_restAbstractEndpoint':"REST-ABSTRACT-ENDPOINT", 
         '_artop_parameter':"REST-ABSTRACT-PROPERTY-DEF"})

    @property
    def mandatory_(self):
        if self._artop_mandatory:
            if self._artop_mandatory == "true":
                return True
            return False
        else:
            return self._artop_mandatory

    @property
    def ref_restAbstractEndpoint_(self):
        return self._artop_restAbstractEndpoint

    @property
    def restAbstractEndpoint_(self):
        if self._artop_restAbstractEndpoint is not None:
            if hasattr(self._artop_restAbstractEndpoint, "uuid"):
                return self._artop_restAbstractEndpoint.uuid
        return

    @property
    def ref_parameter_(self):
        return self._artop_parameter

    @property
    def parameter_(self):
        if self._artop_parameter is not None:
            if hasattr(self._artop_parameter, "uuid"):
                return self._artop_parameter.uuid
        return
