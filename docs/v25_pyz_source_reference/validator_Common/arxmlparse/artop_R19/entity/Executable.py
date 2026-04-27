# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Executable.py
from .AtpClassifier import AtpClassifier
from .ARElement import ARElement

class Executable(ARElement, AtpClassifier):

    def __init__(self):
        super().__init__()
        from .RootSwComponentPrototype import RootSwComponentPrototype
        self._artop_buildType = None
        self._artop_loggingBehavior = None
        self._artop_minimumTimerGranularity = None
        self._artop_reportingBehavior = None
        self._artop_version = None
        self._artop_rootSwComponentPrototype = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_rootSwComponentPrototype": "ROOT-SW-COMPONENT-PROTOTYPE"})

    @property
    def buildType_(self):
        return self._artop_buildType

    @property
    def loggingBehavior_(self):
        return self._artop_loggingBehavior

    @property
    def minimumTimerGranularity_(self):
        return self._artop_minimumTimerGranularity

    @property
    def reportingBehavior_(self):
        return self._artop_reportingBehavior

    @property
    def version_(self):
        return self._artop_version

    @property
    def ref_rootSwComponentPrototype_(self):
        return self._artop_rootSwComponentPrototype

    @property
    def rootSwComponentPrototype_(self):
        if self._artop_rootSwComponentPrototype is not None:
            if hasattr(self._artop_rootSwComponentPrototype, "uuid"):
                return self._artop_rootSwComponentPrototype.uuid
        return
