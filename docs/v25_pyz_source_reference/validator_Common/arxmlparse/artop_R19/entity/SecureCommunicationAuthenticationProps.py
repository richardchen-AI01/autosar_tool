# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SecureCommunicationAuthenticationProps.py
from .Identifiable import Identifiable

class SecureCommunicationAuthenticationProps(Identifiable):

    def __init__(self):
        super().__init__()
        from .SecureCommunicationPropsSet import SecureCommunicationPropsSet
        self._artop_authAlgorithm = None
        self._artop_authInfoTxLength = None
        self._artop_secureCommunicationPropsSet = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_secureCommunicationPropsSet": "SECURE-COMMUNICATION-PROPS-SET"})

    @property
    def authAlgorithm_(self):
        return self._artop_authAlgorithm

    @property
    def authInfoTxLength_(self):
        return self._artop_authInfoTxLength

    @property
    def ref_secureCommunicationPropsSet_(self):
        return self._artop_secureCommunicationPropsSet

    @property
    def secureCommunicationPropsSet_(self):
        if self._artop_secureCommunicationPropsSet is not None:
            if hasattr(self._artop_secureCommunicationPropsSet, "uuid"):
                return self._artop_secureCommunicationPropsSet.uuid
        return
