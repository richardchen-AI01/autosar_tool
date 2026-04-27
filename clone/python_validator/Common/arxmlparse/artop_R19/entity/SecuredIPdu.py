# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SecuredIPdu.py
from .IPdu import IPdu

class SecuredIPdu(IPdu):

    def __init__(self):
        super().__init__()
        from .SecureCommunicationAuthenticationProps import SecureCommunicationAuthenticationProps
        from .SecureCommunicationFreshnessProps import SecureCommunicationFreshnessProps
        from .PduTriggering import PduTriggering
        from .SecureCommunicationProps import SecureCommunicationProps
        self._artop_useAsCryptographicIPdu = None
        self._artop_useSecuredPduHeader = None
        self._artop_authenticationPropsRef = None
        self._artop_freshnessPropsRef = None
        self._artop_payloadRef = None
        self._artop_secureCommunicationProps = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_authenticationPropsRef': '"SECURE-COMMUNICATION-AUTHENTICATION-PROPS"', 
         '_artop_freshnessPropsRef': '"SECURE-COMMUNICATION-FRESHNESS-PROPS"', 
         '_artop_payloadRef': '"PDU-TRIGGERING"', 
         '_artop_secureCommunicationProps': '"SECURE-COMMUNICATION-PROPS"'})

    @property
    def useAsCryptographicIPdu_(self):
        if self._artop_useAsCryptographicIPdu:
            if self._artop_useAsCryptographicIPdu == "true":
                return True
            return False
        else:
            return self._artop_useAsCryptographicIPdu

    @property
    def useSecuredPduHeader_(self):
        return self._artop_useSecuredPduHeader

    @property
    def ref_authenticationProps_(self):
        return self._artop_authenticationPropsRef

    @property
    def authenticationProps_(self):
        if self._artop_authenticationPropsRef is not None:
            if hasattr(self._artop_authenticationPropsRef, "uuid"):
                return self._artop_authenticationPropsRef.uuid
        return

    @property
    def ref_freshnessProps_(self):
        return self._artop_freshnessPropsRef

    @property
    def freshnessProps_(self):
        if self._artop_freshnessPropsRef is not None:
            if hasattr(self._artop_freshnessPropsRef, "uuid"):
                return self._artop_freshnessPropsRef.uuid
        return

    @property
    def ref_payload_(self):
        return self._artop_payloadRef

    @property
    def payload_(self):
        if self._artop_payloadRef is not None:
            if hasattr(self._artop_payloadRef, "uuid"):
                return self._artop_payloadRef.uuid
        return

    @property
    def ref_secureCommunicationProps_(self):
        return self._artop_secureCommunicationProps

    @property
    def secureCommunicationProps_(self):
        if self._artop_secureCommunicationProps is not None:
            if hasattr(self._artop_secureCommunicationProps, "uuid"):
                return self._artop_secureCommunicationProps.uuid
        return
