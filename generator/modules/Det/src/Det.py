from Common.arxmlparse.constant.BswPathConstant import BswPath as BP
from Common.arxmlparse.cache.BswModuleCache import getBswContainerByEnum
from Det.src.DetGeneral import *
from Det.src.DetNotification import *
from Det.src.DetConfigSet import *
import uuid

class Det:
    def __init__(self):
        tempDetGeneral = getBswContainerByEnum(BP.Det_DetGeneral)
        tempDetNotification = getBswContainerByEnum(BP.Det_DetNotification)
        tempDetConfigSet = getBswContainerByEnum(BP.Det_DetConfigSet)
        tempDetModule = getBswContainerByEnum(BP.Det_DetModule)
        tempDetModuleInstance = getBswContainerByEnum(BP.Det_DetModuleInstance)
        # 将Det模块下的容器实例化
        self.DetGeneral = DetGeneral(tempDetGeneral[0]) if tempDetGeneral else []
        self.DetConfigSet = DetGeneral(tempDetConfigSet[0]) if tempDetConfigSet else []
        self.DetNotification = [DetNotification(detNotification) for detNotification in tempDetNotification] if tempDetNotification else []
        self.DetModule = [DetModule(detModule) for detModule in tempDetModule] if tempDetModule else []
        self.DetModuleInstance = [DetModuleInstance(detModuleInstance) for detModuleInstance in tempDetModuleInstance] if tempDetModuleInstance else []

    @property
    def ErrorHookTable(self):
        """
        返回 DetErrorHook下拉编辑框中 ErrorHook 通知回调函数的列表
        """
        errorHookList = []
        for detNotification in self.DetNotification:
            if detNotification.DetErrorHook:
                errorHookList.extend(detNotification.DetErrorHook)
        return errorHookList

    @property
    def RuntimeErrorCalloutTable(self):
        """
        返回 DetReportRuntimeErrorCallout下拉编辑框中ErrorHook通知回调函数的列表,
        """
        runtimeErrorCalloutList = []
        for detNotification in self.DetNotification:
            if detNotification.DetReportRuntimeErrorCallout:
                runtimeErrorCalloutList.extend(detNotification.DetReportRuntimeErrorCallout)
        return runtimeErrorCalloutList

    @property
    def TransientFaultCalloutTable(self):
        """
        返回 DetReportTransientFaultCallout下拉编辑框中ErrorHook通知回调函数的列表,
        """
        transientFaultCalloutList = []
        for detNotification in self.DetNotification:
            if detNotification.DetReportTransientFaultCallout:
                transientFaultCalloutList.extend(detNotification.DetReportTransientFaultCallout)
        return transientFaultCalloutList
    
    @staticmethod
    def getModuleId(module):
        """
        返回 DetModule的 DetModuleId列表
        """
        idList = []
        for module1 in module.DetModule:
            idList.append(module1.DetModuleId)
        return idList

    @staticmethod
    def getInstanceId(module):
        """
        返回 DetModuleInstance的 DetInstanceId列表
        """
        idList = []
        for instance in module.DetModuleInstance:
            idList.append(instance.DetInstanceId)
        return idList
    
    @property
    def DetGetuuid(self):
        return uuid.uuid4()

