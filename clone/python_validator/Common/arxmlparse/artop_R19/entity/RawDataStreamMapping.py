# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RawDataStreamMapping.py
from .UploadablePackageElement import UploadablePackageElement

class RawDataStreamMapping(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .RawDataStreamDeployment import RawDataStreamDeployment
        from .RPortPrototypeInExecutableInstanceRef import RPortPrototypeInExecutableInstanceRef
        from .Process import Process
        self._artop_deploymentRef = None
        self._artop_portPrototypeIref = None
        self._artop_processRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_deploymentRef':"RAW-DATA-STREAM-DEPLOYMENT", 
         '_artop_portPrototypeIref':"R-PORT-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF", 
         '_artop_processRef':"PROCESS"})

    @property
    def ref_deployment_(self):
        return self._artop_deploymentRef

    @property
    def deployment_(self):
        if self._artop_deploymentRef is not None:
            if hasattr(self._artop_deploymentRef, "uuid"):
                return self._artop_deploymentRef.uuid
        return

    @property
    def ref_portPrototype_(self):
        return self._artop_portPrototypeIref

    @property
    def portPrototype_(self):
        if self._artop_portPrototypeIref is not None:
            if hasattr(self._artop_portPrototypeIref, "uuid"):
                return self._artop_portPrototypeIref.uuid
        return

    @property
    def ref_process_(self):
        return self._artop_processRef

    @property
    def process_(self):
        if self._artop_processRef is not None:
            if hasattr(self._artop_processRef, "uuid"):
                return self._artop_processRef.uuid
        return
