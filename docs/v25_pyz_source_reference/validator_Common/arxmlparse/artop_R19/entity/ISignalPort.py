# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ISignalPort.py
from .CommConnectorPort import CommConnectorPort

class ISignalPort(CommConnectorPort):

    def __init__(self):
        super().__init__()
        from .DataFilter import DataFilter
        self._artop_firstTimeout = None
        self._artop_handleInvalid = None
        self._artop_timeout = None
        self._artop_dataFilter = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_dataFilter": "DATA-FILTER"})

    @property
    def firstTimeout_(self):
        return self._artop_firstTimeout

    @property
    def handleInvalid_(self):
        return self._artop_handleInvalid

    @property
    def timeout_(self):
        return self._artop_timeout

    @property
    def ref_dataFilter_(self):
        return self._artop_dataFilter

    @property
    def dataFilter_(self):
        if self._artop_dataFilter is not None:
            if hasattr(self._artop_dataFilter, "uuid"):
                return self._artop_dataFilter.uuid
        return
