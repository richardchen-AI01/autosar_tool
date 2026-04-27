# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RestHttpPortPrototypeMapping.py
from .UploadablePackageElement import UploadablePackageElement

class RestHttpPortPrototypeMapping(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .HttpAcceptEncoding import HttpAcceptEncoding
        from .NetworkEndpoint import NetworkEndpoint
        from .PortPrototypeInExecutableInstanceRef import PortPrototypeInExecutableInstanceRef
        from .Process import Process
        from .TlsSecureComProps import TlsSecureComProps
        self._artop_portPrototypeSlugFragment = None
        self._artop_tcpPort = None
        self._artop_acceptsEncoding = []
        self._artop_hostRef = None
        self._artop_portPrototypeIref = None
        self._artop_processRef = None
        self._artop_tlsSecureComPropsRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_acceptsEncoding': '"HTTP-ACCEPT-ENCODING"', 
         '_artop_hostRef': '"NETWORK-ENDPOINT"', 
         '_artop_portPrototypeIref': '"PORT-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF"', 
         '_artop_processRef': '"PROCESS"', 
         '_artop_tlsSecureComPropsRef': '"TLS-SECURE-COM-PROPS"'})

    @property
    def portPrototypeSlugFragment_(self):
        return self._artop_portPrototypeSlugFragment

    @property
    def tcpPort_(self):
        return self._artop_tcpPort

    @property
    def acceptsEncodings_HttpAcceptEncoding(self):
        return self._artop_acceptsEncoding

    @property
    def ref_host_(self):
        return self._artop_hostRef

    @property
    def host_(self):
        if self._artop_hostRef is not None:
            if hasattr(self._artop_hostRef, "uuid"):
                return self._artop_hostRef.uuid
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

    @property
    def ref_tlsSecureComProps_(self):
        return self._artop_tlsSecureComPropsRef

    @property
    def tlsSecureComProps_(self):
        if self._artop_tlsSecureComPropsRef is not None:
            if hasattr(self._artop_tlsSecureComPropsRef, "uuid"):
                return self._artop_tlsSecureComPropsRef.uuid
        return
