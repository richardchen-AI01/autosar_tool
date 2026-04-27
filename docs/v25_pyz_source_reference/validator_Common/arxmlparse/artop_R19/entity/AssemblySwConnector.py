# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AssemblySwConnector.py
from .SwConnector import SwConnector

class AssemblySwConnector(SwConnector):

    def __init__(self):
        super().__init__()
        from .PPortInCompositionInstanceRef import PPortInCompositionInstanceRef
        from .RPortInCompositionInstanceRef import RPortInCompositionInstanceRef
        self._artop_providerIref = None
        self._artop_requesterIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_providerIref':"P-PORT-IN-COMPOSITION-INSTANCE-REF", 
         '_artop_requesterIref':"R-PORT-IN-COMPOSITION-INSTANCE-REF"})

    @property
    def ref_provider_(self):
        return self._artop_providerIref

    @property
    def provider_(self):
        if self._artop_providerIref is not None:
            if hasattr(self._artop_providerIref, "uuid"):
                return self._artop_providerIref.uuid
        return

    @property
    def ref_requester_(self):
        return self._artop_requesterIref

    @property
    def requester_(self):
        if self._artop_requesterIref is not None:
            if hasattr(self._artop_requesterIref, "uuid"):
                return self._artop_requesterIref.uuid
        return
