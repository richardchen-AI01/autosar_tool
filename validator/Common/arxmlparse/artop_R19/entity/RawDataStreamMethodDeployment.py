# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RawDataStreamMethodDeployment.py
from .Identifiable import Identifiable

class RawDataStreamMethodDeployment(Identifiable):

    def __init__(self):
        super().__init__()
        from .RawDataStreamDeployment import RawDataStreamDeployment
        from .ClientServerOperation import ClientServerOperation
        self._artop_callTimeout = None
        self._artop_rawDataStreamDeployment = None
        self._artop_methodRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_rawDataStreamDeployment':"RAW-DATA-STREAM-DEPLOYMENT", 
         '_artop_methodRef':"CLIENT-SERVER-OPERATION"})

    @property
    def callTimeout_(self):
        return self._artop_callTimeout

    @property
    def ref_rawDataStreamDeployment_(self):
        return self._artop_rawDataStreamDeployment

    @property
    def rawDataStreamDeployment_(self):
        if self._artop_rawDataStreamDeployment is not None:
            if hasattr(self._artop_rawDataStreamDeployment, "uuid"):
                return self._artop_rawDataStreamDeployment.uuid
        return

    @property
    def ref_methods_(self):
        return self._artop_methodRef

    @property
    def methods_(self):
        return self._artop_methodRef
