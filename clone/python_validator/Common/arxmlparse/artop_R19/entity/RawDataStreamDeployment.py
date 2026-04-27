# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RawDataStreamDeployment.py
from .UploadablePackageElement import UploadablePackageElement

class RawDataStreamDeployment(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .RawDataStreamMethodDeployment import RawDataStreamMethodDeployment
        from .RawDataStreamInterface import RawDataStreamInterface
        self._artop_methodDeployment = []
        self._artop_rawDataStreamInterfaceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_methodDeployment':"RAW-DATA-STREAM-METHOD-DEPLOYMENT", 
         '_artop_rawDataStreamInterfaceRef':"RAW-DATA-STREAM-INTERFACE"})

    @property
    def methodDeployments_RawDataStreamMethodDeployment(self):
        return self._artop_methodDeployment

    @property
    def ref_rawDataStreamInterface_(self):
        return self._artop_rawDataStreamInterfaceRef

    @property
    def rawDataStreamInterface_(self):
        if self._artop_rawDataStreamInterfaceRef is not None:
            if hasattr(self._artop_rawDataStreamInterfaceRef, "uuid"):
                return self._artop_rawDataStreamInterfaceRef.uuid
        return
