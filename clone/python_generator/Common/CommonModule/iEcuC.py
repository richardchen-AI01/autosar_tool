# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\CommonModule\iEcuC.py
from Common.arxmlparse.cache.BswModuleCache import *
import Common.BswBase as BswBase
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP
from Common.Utils import singletonFunc
from Common import logger

class iEcuC:

    def GetPdu(self, vid=None):
        """
        返回pdu列表
        """
        logger.info(type(vid))
        PduList = getBswContainerByEnum(BP.EcuC_Pdu, vid)
        if PduList:
            return [pdu(tmpPdu) for tmpPdu in PduList]
        return []

    @property
    def GetMetaItem(self):
        """
        返回MetaDataItem列表
        """
        metaItemList = getBswContainerByEnum(BP.EcuC_MetaDataType)
        if metaItemList:
            return [MetaDataItem(metaItem) for metaItem in metaItemList]

    @property
    def SupportMultipleCore(self):
        """
        - return: STD_ON/STD_OFF
        - description: 是否支持多核
        """
        coreList = getBswContainerByEnum(BP.EcuC_EcucCoreDefinition)
        if len(coreList) > 0:
            return "STD_ON"
        return "STD_OFF"

    @property
    def SupportMultiplePartition(self):
        """
        - return: STD_ON/STD_OFF
        - description: 是否支持多partition
        """
        partitionList = getBswContainerByEnum(BP.EcuC_EcucPartition)
        if len(partitionList) > 0:
            return "STD_ON"
        return "STD_OFF"


class ecuCGeneral(BswBase):

    def __init__(self, Container):
        super().__init__(Container)

    @property
    def GetByteOrder(self):
        """
        返回当前机器大小端情况
        """
        byteOrder = self.getAttrValue(BP.EcuC_ByteOrder)
        return byteOrder


class pdu(BswBase):

    def DynamicLength(self, vid=None):
        """
        返回pdu的属性DynamicLength
        """
        return self.getAttrValue(BP.EcuC_DynamicLength, vid)

    def J1939Requestable(self, vid=None):
        return self.getAttrValue(BP.EcuC_J1939Requestable, vid)

    @property
    def KeepLocalPduBuffer(self):
        return self.getAttrValue(BP.EcuC_KeepLocalPduBuffer)

    def PduLength(self, vid=None):
        """
        返回pdu的属性PduLength
        """
        return self.getAttrValue(BP.EcuC_PduLength, vid)

    @property
    def EcucPduDefaultPartitionRef(self):
        """
        返回pdu的属性EcucPduDefaultPartitionRef
        """
        return self.getAttrValue(BP.EcuC_EcucPduDefaultPartitionRef)

    @property
    def MetaDataTypeRef(self, ItemTypeList=[]):
        """
        返回pdu的属性MetaDataTypeRef或MetaDataTypeRef子容器列表
        """
        MetaData = self.getAttrValue(BP.EcuC_MetaDataTypeRef)
        if MetaData:
            if ItemTypeList != []:
                result = 0
                for metaDataItem in MetaData.getSubContainer("MetaDataItem"):
                    if metaDataItem.getAttrValue(BP.EcuC_MetaDataItemType) in ItemTypeList:
                        result += 1
                    return result

        return MetaData

    def SysTPduToFrameTriggeringRef(self, vid=None):
        """
        返回pdu的属性SysTPduToFrameTriggeringRef
        """
        return self.getAttrValue(BP.EcuC_SysTPduToFrameTriggeringRef, vid)

    def SysTPduToPduTriggeringRef(self, vid=None):
        """
        返回pdu的属性SysTPduToPduTriggeringRef
        """
        return self.getAttrValue(BP.EcuC_SysTPduToPduTriggeringRef, vid)


class MetaDataItem(BswBase):

    @property
    def MetaDataItemType(self):
        """
        返回MetaDataItem的属性MetaDataItemType
        """
        return self.getAttrValue(BP.EcuC_MetaDataItemType)

    @property
    def MetaDataItemLength(self):
        """
        返回MetaDataItem的属性MetaDataItemLength
        """
        return self.getAttrValue(BP.EcuC_MetaDataItemLength)

    @property
    def getMetaDataLengthNum(self):
        """
        统计关联的ECUC中Pdu的MetaDataItem->MetaDataItemLength（0-N个）之和
        """
        num = 0
        MetaData = self.getAttrValue(BP.EcuC_MetaDataTypeRef)
        if MetaData:
            for MetaDataItem in MetaData.getSubContainer("MetaDataItem"):
                num += MetaDataItem(MetaDataItem).MetaDataItemLength

        return num


class partition(BswBase):

    @property
    def GetIndexofEcucPartition(self, partition):
        """
        获取partition在EcucPartition中的index
        """
        partitionList = getBswContainerByEnum(BP.EcuC_EcucPartition)
        return partitionList.index(partition)

    @property
    def EcucDefaultBswPartition(self):
        """
        返回EcucPartition的属性MetaDataItemLength
        """
        return self.getAttrValue(BP.EcuC_EcucDefaultBswPartition)

    @property
    def EcucPartitionId(self):
        """
        返回EcucPartition的属性EcucPartitionId
        """
        return self.getAttrValue(BP.EcuC_EcucPartitionId)

    @property
    def EcucEcuPartitionRef(self):
        """
        返回EcucPartition的属性EcucEcuPartitionRef
        """
        return self.getAttrValue(BP.EcuC_EcucEcuPartitionRef)

    @property
    def EcucPartitionCoreRef(self):
        """
        返回EcucPartition的属性EcucPartitionCoreRef
        """
        return self.getAttrValue(BP.EcuC_EcucPartitionCoreRef)

    @property
    def PartitionCanBeRestarted(self):
        """
        返回EcucPartition的属性PartitionCanBeRestarted
        """
        return self.getAttrValue(BP.EcuC_PartitionCanBeRestarted)

    @property
    def EcucPartitionBswModuleDistinguishedPartition(self, isGetNum):
        """
        返回EcucPartition的属性EcucPartitionBswModuleDistinguishedPartition列表或总数
        """
        partitionList = self.getAttrValue(BP.EcuC_EcucPartitionBswModuleDistinguishedPartition)
        if isGetNum:
            return len(partitionList)
        return partitionList

    @property
    def EcucPartitionSoftwareComponentInstanceRef(self, isGetNum):
        """
        返回EcucPartition的属性EcucPartitionSoftwareComponentInstanceRef列表或总数
        """
        partitionList = self.getAttrValue(BP.EcuC_EcucPartitionSoftwareComponentInstanceRef)
        if isGetNum:
            return len(partitionList)
        return partitionList


class CoreInfo(BswBase):

    @property
    def EcucCoreHwRef(self):
        return self.getAttrValue(BP.EcuC_EcucCoreHwRef)

    @property
    def EcucCoreId(self):
        return self.getAttrValue(BP.EcuC_EcucCoreId)


@singletonFunc
class PduInfo(BswBase):

    def __init__(self):
        self.pduDict = {}

    def setDict(self):
        self.pduDict.update({pdu.getAttrValue(BP.CanIf_CanIfRxPduRef).shortName_: ["CanIf", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.CanIf_CanIfRxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.CanIf_CanIfRxPduCfg) if pdu.getAttrValue(BP.CanIf_CanIfRxPduRef)})
        self.pduDict.update({pdu.getAttrValue(BP.CanIf_CanIfTxPduRef).shortName_: ["CanIf", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.CanIf_CanIfTxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.CanIf_CanIfTxPduCfg) if pdu.getAttrValue(BP.CanIf_CanIfTxPduRef)})
        self.pduDict.update({pdu.getAttrValue(BP.CanTp_CanTpRxNSduRef).shortName_: ["CanTp", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.CanTp_CanTpRxNSduRef).shortName_] for pdu in getBswContainerByEnum(BP.CanTp_CanTpRxNSdu) if pdu.getAttrValue(BP.CanTp_CanTpRxNSduRef)})
        self.pduDict.update({pdu.getAttrValue(BP.CanTp_CanTpTxNSduRef).shortName_: ["CanTp", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.CanTp_CanTpTxNSduRef).shortName_] for pdu in getBswContainerByEnum(BP.CanTp_CanTpTxNSdu) if pdu.getAttrValue(BP.CanTp_CanTpTxNSduRef)})
        self.pduDict.update({pdu.getAttrValue(BP.J1939Tp_J1939TpRxNSduRef).shortName_: ["J1939Tp", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.J1939Tp_J1939TpRxNSduRef).shortName_] for pdu in getBswContainerByEnum(BP.J1939Tp_J1939TpRxNSdu) if pdu.getAttrValue(BP.J1939Tp_J1939TpRxNSduRef)})
        self.pduDict.update({pdu.getAttrValue(BP.J1939Tp_J1939TpTxNSduRef).shortName_: ["J1939Tp", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.J1939Tp_J1939TpTxNSduRef).shortName_] for pdu in getBswContainerByEnum(BP.J1939Tp_J1939TpTxNSdu) if pdu.getAttrValue(BP.J1939Tp_J1939TpTxNSduRef)})
        self.pduDict.update({pdu.getAttrValue(BP.CanNm_CanNmTxUserDataPduRef).shortName_: ["CanNm", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.CanNm_CanNmTxUserDataPduRef).shortName_] for pdu in getBswContainerByEnum(BP.CanNm_CanNmUserDataTxPdu) if pdu.getAttrValue(BP.CanNm_CanNmTxUserDataPduRef)})
        for pdu in getBswContainerByEnum(BP.Com_ComIPdu):
            if pdu.getAttrValue(BP.Com_ComPduIdRef):
                if pdu.getAttrValue(BP.Com_ComIPduDirection) == "Receive":
                    self.pduDict[pdu.getAttrValue(BP.Com_ComPduIdRef).shortName_] = [
                     "Com", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.Com_ComPduIdRef).shortName_]
                else:
                    self.pduDict[pdu.getAttrValue(BP.Com_ComPduIdRef).shortName_] = [
                     "Com", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.Com_ComPduIdRef).shortName_]
        else:
            self.pduDict.update({pdu.getAttrValue(BP.Dcm_DcmDslProtocolRxPduRef).shortName_: ["Dcm", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.Dcm_DcmDslProtocolRxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.Dcm_DcmDslProtocolRx) if pdu.getAttrValue(BP.Dcm_DcmDslProtocolRxPduRef)})
            self.pduDict.update({pdu.getAttrValue(BP.Dcm_DcmDslProtocolTxPduRef).shortName_: ["Dcm", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.Dcm_DcmDslProtocolTxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.Dcm_DcmDslProtocolTx) if pdu.getAttrValue(BP.Dcm_DcmDslProtocolTxPduRef)})
            self.pduDict.update({pdu.getAttrValue(BP.Dcm_DcmDslPeriodicTxPduRef).shortName_: ["Dcm", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.Dcm_DcmDslPeriodicTxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.Dcm_DcmDslPeriodicConnection) if pdu.getAttrValue(BP.Dcm_DcmDslPeriodicTxPduRef)})
            for pdu in getBswContainerByEnum(BP.Dcm_DcmDslPeriodicConnection):
                if pdu.getAttrValue(BP.Dcm_DcmDslPeriodicTxPduRef):
                    self.pduDict[pdu.getAttrValue(BP.Dcm_DcmDslPeriodicTxPduRef).shortName_] = [
                     "Dcm", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.Dcm_DcmDslPeriodicTxPduRef).shortName_]
            else:
                self.pduDict.update({pdu.getAttrValue(BP.Dlt_DltRxPduIdRef).shortName_: ["Dlt", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.Dlt_DltRxPduIdRef).shortName_] for pdu in getBswContainerByEnum(BP.Dlt_DltRxPdu) if pdu.getAttrValue(BP.Dlt_DltRxPduIdRef)})
                self.pduDict.update({pdu.getAttrValue(BP.Dlt_DltTxPduRef).shortName_: ["Dlt", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.Dlt_DltTxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.Dlt_DltTxPdu) if pdu.getAttrValue(BP.Dlt_DltTxPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.DoIP_DoIPPduRRxPduRef).shortName_: ["DoIP", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.DoIP_DoIPPduRRxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.DoIP_DoIPPduRRxPdu) if pdu.getAttrValue(BP.DoIP_DoIPPduRRxPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.DoIP_DoIPPduRTxPduRef).shortName_: ["DoIP", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.DoIP_DoIPPduRTxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.DoIP_DoIPPduRTxPdu) if pdu.getAttrValue(BP.DoIP_DoIPPduRTxPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.IpduM_IpduMContainedRxPduRef).shortName_: ["IpduM", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.IpduM_IpduMContainedRxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.IpduM_IpduMContainedRxPdu) if pdu.getAttrValue(BP.IpduM_IpduMContainedRxPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.IpduM_IpduMContainedTxPduRef).shortName_: ["IpduM", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.IpduM_IpduMContainedTxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.IpduM_IpduMContainedTxPdu) if pdu.getAttrValue(BP.IpduM_IpduMContainedTxPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.IpduM_IpduMContainerRxPduRef).shortName_: ["IpduM", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.IpduM_IpduMContainerRxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.IpduM_IpduMContainerRxPdu) if pdu.getAttrValue(BP.IpduM_IpduMContainerRxPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.IpduM_IpduMContainerTxPduRef).shortName_: ["IpduM", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.IpduM_IpduMContainerTxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.IpduM_IpduMContainerTxPdu) if pdu.getAttrValue(BP.IpduM_IpduMContainerTxPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.IpduM_IpduMRxIndicationPduRef).shortName_: ["IpduM", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.IpduM_IpduMRxIndicationPduRef).shortName_] for pdu in getBswContainerByEnum(BP.IpduM_IpduMRxIndication) if pdu.getAttrValue(BP.IpduM_IpduMRxIndicationPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.IpduM_IpduMOutgoingDynamicPduRef).shortName_: ["IpduM", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.IpduM_IpduMOutgoingDynamicPduRef).shortName_] for pdu in getBswContainerByEnum(BP.IpduM_IpduMRxDynamicPart) if pdu.getAttrValue(BP.IpduM_IpduMOutgoingDynamicPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.IpduM_IpduMOutgoingStaticPduRef).shortName_: ["IpduM", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.IpduM_IpduMOutgoingStaticPduRef).shortName_] for pdu in getBswContainerByEnum(BP.IpduM_IpduMRxStaticPart) if pdu.getAttrValue(BP.IpduM_IpduMOutgoingStaticPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.IpduM_IpduMOutgoingPduRef).shortName_: ["IpduM", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.IpduM_IpduMOutgoingPduRef).shortName_] for pdu in getBswContainerByEnum(BP.IpduM_IpduMTxRequest) if pdu.getAttrValue(BP.IpduM_IpduMOutgoingPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.IpduM_IpduMTxDynamicPduRef).shortName_: ["IpduM", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.IpduM_IpduMTxDynamicPduRef).shortName_] for pdu in getBswContainerByEnum(BP.IpduM_IpduMTxDynamicPart) if pdu.getAttrValue(BP.IpduM_IpduMTxDynamicPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.IpduM_IpduMTxStaticPduRef).shortName_: ["IpduM", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.IpduM_IpduMTxStaticPduRef).shortName_] for pdu in getBswContainerByEnum(BP.IpduM_IpduMTxStaticPart) if pdu.getAttrValue(BP.IpduM_IpduMTxStaticPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.J1939Dcm_J1939DcmRxPduRef).shortName_: ["J1939Dcm", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.J1939Dcm_J1939DcmRxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.J1939Dcm_J1939DcmRxPdu) if pdu.getAttrValue(BP.J1939Dcm_J1939DcmRxPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.J1939Dcm_J1939DcmTxPduRef).shortName_: ["J1939Dcm", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.J1939Dcm_J1939DcmTxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.J1939Dcm_J1939DcmTxPdu) if pdu.getAttrValue(BP.J1939Dcm_J1939DcmTxPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.J1939Rm_J1939RmAckmRxPduRef).shortName_: ["J1939Rm", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.J1939Rm_J1939RmAckmRxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.J1939Rm_J1939RmAckmRxPdu) if pdu.getAttrValue(BP.J1939Rm_J1939RmAckmRxPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.J1939Rm_J1939RmAckmTxPduRef).shortName_: ["J1939Rm", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.J1939Rm_J1939RmAckmTxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.J1939Rm_J1939RmAckmTxPdu) if pdu.getAttrValue(BP.J1939Rm_J1939RmAckmTxPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.J1939Rm_J1939RmRqst2RxPduRef).shortName_: ["J1939Rm", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.J1939Rm_J1939RmRqst2RxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.J1939Rm_J1939RmRqst2RxPdu) if pdu.getAttrValue(BP.J1939Rm_J1939RmRqst2RxPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.J1939Rm_J1939RmRqst2TxPduRef).shortName_: ["J1939Rm", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.J1939Rm_J1939RmRqst2TxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.J1939Rm_J1939RmRqst2TxPdu) if pdu.getAttrValue(BP.J1939Rm_J1939RmRqst2TxPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.J1939Rm_J1939RmRqstRxPduRef).shortName_: ["J1939Rm", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.J1939Rm_J1939RmRqstRxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.J1939Rm_J1939RmRqstRxPdu) if pdu.getAttrValue(BP.J1939Rm_J1939RmRqstRxPduRef)})
                self.pduDict.update({pdu.getAttrValue(BP.J1939Rm_J1939RmRqstTxPduRef).shortName_: ["J1939Rm", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.J1939Rm_J1939RmRqstTxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.J1939Rm_J1939RmRqstTxPdu) if pdu.getAttrValue(BP.J1939Rm_J1939RmRqstTxPduRef)})
                for pdu in getBswContainerByEnum(BP.LdCom_LdComIPdu):
                    if pdu.getAttrValue(BP.LdCom_LdComPduRef):
                        if pdu.getAttrValue(BP.LdCom_LdComIPduDirection) == "LDCOM_RECEIVE":
                            self.pduDict[pdu.getAttrValue(BP.LdCom_LdComPduRef).shortName_] = [
                             "LdCom", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.LdCom_LdComPduRef).shortName_]
                        else:
                            self.pduDict[pdu.getAttrValue(BP.LdCom_LdComPduRef).shortName_] = [
                             "LdCom", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.LdCom_LdComPduRef).shortName_]
                else:
                    for pdu in getBswContainerByEnum(BP.LinIf_LinIfRxPdu):
                        if pdu.getAttrValue(BP.LinIf_LinIfRxPduRef):
                            self.pduDict[pdu.getAttrValue(BP.LinIf_LinIfRxPduRef).shortName_] = [
                             "LinIf", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.LinIf_LinIfRxPduRef).shortName_]
                    else:
                        for pdu in getBswContainerByEnum(BP.LinIf_LinIfTxPdu):
                            if pdu.getAttrValue(BP.LinIf_LinIfTxPduRef):
                                self.pduDict[pdu.getAttrValue(BP.LinIf_LinIfTxPduRef).shortName_] = [
                                 "LinIf", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.LinIf_LinIfTxPduRef).shortName_]
                        else:
                            self.pduDict.update({pdu.getAttrValue(BP.LinTp_LinTpRxNSduPduRef).shortName_: ["LinTp", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.LinTp_LinTpRxNSduPduRef).shortName_] for pdu in getBswContainerByEnum(BP.LinTp_LinTpRxNSdu) if pdu.getAttrValue(BP.LinTp_LinTpRxNSduPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.LinTp_LinTpTxNSduPduRef).shortName_: ["LinTp", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.LinTp_LinTpTxNSduPduRef).shortName_] for pdu in getBswContainerByEnum(BP.LinTp_LinTpTxNSdu) if pdu.getAttrValue(BP.LinTp_LinTpTxNSduPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.OsekNm_OsekNmTxUserDataPduRef).shortName_: ["OsekNm", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.OsekNm_OsekNmTxUserDataPduRef).shortName_] for pdu in getBswContainerByEnum(BP.OsekNm_OsekNmUserDataTxPdu) if pdu.getAttrValue(BP.OsekNm_OsekNmTxUserDataPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.SecOC_SecOCRxAuthenticLayerPduRef).shortName_: ["SecOC", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.SecOC_SecOCRxAuthenticLayerPduRef).shortName_] for pdu in getBswContainerByEnum(BP.SecOC_SecOCRxAuthenticPduLayer) if pdu.getAttrValue(BP.SecOC_SecOCRxAuthenticLayerPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.SecOC_SecOCRxSecuredLayerPduRef).shortName_: ["SecOC", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.SecOC_SecOCRxSecuredLayerPduRef).shortName_] for pdu in getBswContainerByEnum(BP.SecOC_SecOCRxSecuredPdu) if pdu.getAttrValue(BP.SecOC_SecOCRxSecuredLayerPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.SecOC_SecOCRxAuthenticPduRef).shortName_: ["SecOC", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.SecOC_SecOCRxAuthenticPduRef).shortName_] for pdu in getBswContainerByEnum(BP.SecOC_SecOCRxAuthenticPdu) if pdu.getAttrValue(BP.SecOC_SecOCRxAuthenticPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.SecOC_SecOCRxCryptographicPduRef).shortName_: ["SecOC", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.SecOC_SecOCRxCryptographicPduRef).shortName_] for pdu in getBswContainerByEnum(BP.SecOC_SecOCRxCryptographicPdu) if pdu.getAttrValue(BP.SecOC_SecOCRxCryptographicPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.SecOC_SecOCTxAuthenticLayerPduRef).shortName_: ["SecOC", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.SecOC_SecOCTxAuthenticLayerPduRef).shortName_] for pdu in getBswContainerByEnum(BP.SecOC_SecOCTxAuthenticPduLayer) if pdu.getAttrValue(BP.SecOC_SecOCTxAuthenticLayerPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.SecOC_SecOCTxSecuredLayerPduRef).shortName_: ["SecOC", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.SecOC_SecOCTxSecuredLayerPduRef).shortName_] for pdu in getBswContainerByEnum(BP.SecOC_SecOCTxSecuredPdu) if pdu.getAttrValue(BP.SecOC_SecOCTxSecuredLayerPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.SecOC_SecOCTxAuthenticPduRef).shortName_: ["SecOC", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.SecOC_SecOCTxAuthenticPduRef).shortName_] for pdu in getBswContainerByEnum(BP.SecOC_SecOCTxAuthenticPdu) if pdu.getAttrValue(BP.SecOC_SecOCTxAuthenticPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.SecOC_SecOCTxCryptographicPduRef).shortName_: ["SecOC", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.SecOC_SecOCTxCryptographicPduRef).shortName_] for pdu in getBswContainerByEnum(BP.SecOC_SecOCTxCryptographicPdu) if pdu.getAttrValue(BP.SecOC_SecOCTxCryptographicPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.SoAd_SoAdTxPduRef).shortName_: ["SoAd", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.SoAd_SoAdTxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.SoAd_SoAdPduRoute) if pdu.getAttrValue(BP.SoAd_SoAdTxPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.SoAd_SoAdRxPduRef).shortName_: ["SoAd", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.SoAd_SoAdRxPduRef).shortName_] for pdu in getBswContainerByEnum(BP.SoAd_SoAdSocketRouteDest) if pdu.getAttrValue(BP.SoAd_SoAdRxPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.SomeIpTp_SomeIpTpRxSduRef).shortName_: ["SomeIpTp", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.SomeIpTp_SomeIpTpRxSduRef).shortName_] for pdu in getBswContainerByEnum(BP.SomeIpTp_SomeIpTpRxNSdu) if pdu.getAttrValue(BP.SomeIpTp_SomeIpTpRxSduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.SomeIpTp_SomeIpTpRxNPduRef).shortName_: ["SomeIpTp", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.SomeIpTp_SomeIpTpRxNPduRef).shortName_] for pdu in getBswContainerByEnum(BP.SomeIpTp_SomeIpTpRxNPdu) if pdu.getAttrValue(BP.SomeIpTp_SomeIpTpRxNPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.SomeIpTp_SomeIpTpTxNSduRef).shortName_: ["SomeIpTp", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.SomeIpTp_SomeIpTpTxNSduRef).shortName_] for pdu in getBswContainerByEnum(BP.SomeIpTp_SomeIpTpTxNSdu) if pdu.getAttrValue(BP.SomeIpTp_SomeIpTpTxNSduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.SomeIpTp_SomeIpTpTxNPduRef).shortName_: ["SomeIpTp", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.SomeIpTp_SomeIpTpTxNPduRef).shortName_] for pdu in getBswContainerByEnum(BP.SomeIpTp_SomeIpTpTxNPdu) if pdu.getAttrValue(BP.SomeIpTp_SomeIpTpTxNPduRef)})
                            self.pduDict.update({pdu.getAttrValue(BP.UdpNm_UdpNmTxUserDataPduRef).shortName_: ["UdpNm", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.UdpNm_UdpNmTxUserDataPduRef).shortName_] for pdu in getBswContainerByEnum(BP.UdpNm_UdpNmUserDataTxPdu) if pdu.getAttrValue(BP.UdpNm_UdpNmTxUserDataPduRef)})
                            for pdu in getBswContainerByEnum(BP.FrIf_FrIfRxPdu):
                                if pdu.getAttrValue(BP.FrIf_FrIfUserRxIndicationUL) == "PDUR" and pdu.getAttrValue(BP.FrIf_FrIfRxPduRef):
                                    self.pduDict[pdu.getAttrValue(BP.FrIf_FrIfRxPduRef).shortName_] = [
                                     "FrIf", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.FrIf_FrIfRxPduRef).shortName_]
                            else:
                                for pdu in getBswContainerByEnum(BP.FrIf_FrIfTxPdu):
                                    if pdu.getAttrValue(BP.FrIf_FrIfUserTxUL) == "PDUR" and pdu.getAttrValue(BP.FrIf_FrIfTxPduRef):
                                        self.pduDict[pdu.getAttrValue(BP.FrIf_FrIfTxPduRef).shortName_] = [
                                         "FrIf", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.FrIf_FrIfTxPduRef).shortName_]
                                else:
                                    self.pduDict.update({pdu.getAttrValue(BP.FrArTp_FrArTpRxSduRef).shortName_: ["FrArTp", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.FrArTp_FrArTpRxSduRef).shortName_] for pdu in getBswContainerByEnum(BP.FrArTp_FrArTpRxSdu) if pdu.getAttrValue(BP.FrArTp_FrArTpRxSduRef)})
                                    self.pduDict.update({pdu.getAttrValue(BP.FrArTp_FrArTpTxSduRef).shortName_: ["FrArTp", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.FrArTp_FrArTpTxSduRef).shortName_] for pdu in getBswContainerByEnum(BP.FrArTp_FrArTpTxSdu) if pdu.getAttrValue(BP.FrArTp_FrArTpTxSduRef)})
                                    if [] != getBswContainerByEnum(BP.FrNm_FrNmGlobalFeatures):
                                        pdu = getBswContainerByEnum(BP.FrNm_FrNmGlobalFeatures)[0]
                                        if pdu.getAttrValue(BP.FrNm_FrNmPnEiraRxNSduRef):
                                            self.pduDict[pdu.getAttrValue(BP.FrNm_FrNmPnEiraRxNSduRef).shortName_] = [
                                             "FrNm", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.FrNm_FrNmPnEiraRxNSduRef).shortName_]
                                    for pdu in getBswContainerByEnum(BP.FrNm_FrNmChannelIdentifiers):
                                        if pdu.getAttrValue(BP.FrNm_FrNmPnEraRxNSduRef):
                                            self.pduDict[pdu.shortName_] = [
                                             "FrNm", "Receive", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.FrNm_FrNmPnEraRxNSduRef).shortName_]
                                    else:
                                        self.pduDict.update({pdu.getAttrValue(BP.FrNm_FrNmTxUserDataPduRef).shortName_: ["FrNm", "Transmit", BswBase(pdu).symbolicName, "PDUR_SRCPDU_" + pdu.getAttrValue(BP.FrNm_FrNmTxUserDataPduRef).shortName_] for pdu in getBswContainerByEnum(BP.FrNm_FrNmUserDataTxPdu) if pdu.getAttrValue(BP.FrNm_FrNmTxUserDataPduRef)})

    @property
    def GetPduModuleName(self, pdu):
        """
        获取每个pdu所属的模块名
        """
        if pdu == "":
            logger.error("this pdu is not set.")
            return
        if pdu.shortName_ not in self.pduDict.keys():
            logger.error("pdu [%s] is not found", pdu.shortName_)
            return
        return self.pduDict[pdu.shortName_][0]

    @property
    def GetPduDirect(self, pdu):
        """
        获取每个pdu的方向
        """
        if pdu == "":
            logger.error("this pdu is not set.")
            return
        if pdu.shortName_ not in self.pduDict.keys():
            logger.error("pdu [%s] is not found", pdu.shortName_)
            return
        return self.pduDict[pdu.shortName_][1]

    @property
    def GetPduSymbolicName(self, pdu):
        """
        获取每个pdu的SymbolicName
        """
        if pdu == "":
            logger.error("this pdu is not set.")
            return
        if pdu.shortName_ not in self.pduDict.keys():
            logger.error("pdu [%s] is not found", pdu.shortName_)
            return
        return self.pduDict[pdu.shortName_][2]

    @property
    def GetPduOldPdurName(self, pdu):
        """
        获取每个pdu的PdurName
        """
        if pdu == "":
            logger.error("this pdu is not set.")
            return
        if pdu.shortName_ not in self.pduDict.keys():
            logger.error("pdu [%s] is not found", pdu.shortName_)
            return
        return self.pduDict[pdu.shortName_][3]

    @property
    def GetByteOrder(self):
        """
        获取当前机器的大小端情况，返回“LITTLE_ENDIAN”或“BIG_ENDIAN”
        """
        ecuCGeneralTmp = getBswContainerByEnum(BP.EcuC_EcuCGeneral)
        if ecuCGeneralTmp:
            return ecuCGeneral(ecuCGeneralTmp[0]).GetByteOrder
        return ""


EcuCPduInfo = PduInfo()
