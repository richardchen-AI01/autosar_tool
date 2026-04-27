# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TlsSecureComProps.py
from .SecureComProps import SecureComProps

class TlsSecureComProps(SecureComProps):

    def __init__(self):
        super().__init__()
        from .EthernetRawDataStreamMapping import EthernetRawDataStreamMapping
        from .CryptoServicePrimitive import CryptoServicePrimitive
        from .TlsCryptoCipherSuite import TlsCryptoCipherSuite
        self._artop_ethernetRawDataStreamMapping = None
        self._artop_keyExchangeRef = []
        self._artop_tlsCipherSuite = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ethernetRawDataStreamMapping':"ETHERNET-RAW-DATA-STREAM-MAPPING", 
         '_artop_keyExchangeRef':"CRYPTO-SERVICE-PRIMITIVE", 
         '_artop_tlsCipherSuite':"TLS-CRYPTO-CIPHER-SUITE"})

    @property
    def ref_ethernetRawDataStreamMapping_(self):
        return self._artop_ethernetRawDataStreamMapping

    @property
    def ethernetRawDataStreamMapping_(self):
        if self._artop_ethernetRawDataStreamMapping is not None:
            if hasattr(self._artop_ethernetRawDataStreamMapping, "uuid"):
                return self._artop_ethernetRawDataStreamMapping.uuid
        return

    @property
    def ref_keyExchanges_(self):
        return self._artop_keyExchangeRef

    @property
    def keyExchanges_(self):
        return self._artop_keyExchangeRef

    @property
    def tlsCipherSuites_TlsCryptoCipherSuite(self):
        return self._artop_tlsCipherSuite
