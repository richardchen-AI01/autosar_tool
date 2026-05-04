package cn.com.myorg.bswbuilder.modules.nvm.functionextensions;

import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMBlockCrcTypeEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMBlockDescriptorEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMBlockJobPriorityEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMBlockManagementType;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMBlockManagementTypeEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMBlockUseAutoValidationEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMBlockUseCRCCompMechanismEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMBlockUseCrcEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMBlockUseSetRamBlockStatusEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMBlockUseSyncMechanismEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMBlockWriteProtEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMBswMBlockStatusInformationEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMCalcRamBlockCrcEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMInitBlockCallbackEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMNvBlockBaseNumberCount;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMNvBlockLengthEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMNvBlockNumEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMNvramBlockIdentifier;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMNvramDeviceIdCount;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMRamBlockDataAddressEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMReadRamBlockFromNvCallback;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMReadRamBlockFromNvCallbackEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMResistantToChangedSwEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMRomBlockNumEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMSelectBlockForReadAllEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMSelectBlockForWriteAllEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMWriteBlockOnceEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMWriteRamBlockToNvCallback;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMWriteRamBlockToNvmCallbackEnable;
import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMWriteVerificationDataSize;
import cn.com.myorg.bswbuilder.modules.nvm.common.functionextensions.NvMJobPrioritizationEnable;
import cn.com.myorg.bswbuilder.modules.nvm.common.functionextensions.NvMSizeImmediateJobQueueEnable;
import cn.com.myorg.mal.interfaces.IFunctionExtension;
import cn.com.myorg.mal.interfaces.IModuleInit;
import cn.com.myorg.mal.uidefinition.IUIDefinition;
import cn.com.myorg.mal.uidefinition.UIDefinitionMap;
import java.util.HashMap;
import java.util.Map;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.nvm.functionextensions.NvMFunctionExtension.
 * 99% paraphrase. Registers 32 hooks (M1a scope).
 */
public class NvMFunctionExtension implements IFunctionExtension {

    public static final String NvMMultiBlockCallback = "NvMMultiBlockCallback";
    public static final String NvMSizeImmediateJobQueue = "NvMSizeImmediateJobQueue";
    public static final String NvMBlockManagementType = "NvMBlockManagementType";
    public static final String NvMBlockJobPriority = "NvMBlockJobPriority";
    public static final String NvMWriteBlockOnce = "NvMWriteBlockOnce";
    public static final String NvMBlockWriteProt = "NvMBlockWriteProt";
    public static final String NvMCalcRamBlockCrc = "NvMCalcRamBlockCrc";
    public static final String NvMResistantToChangedSw = "NvMResistantToChangedSw";
    public static final String NvMSelectBlockForReadAll = "NvMSelectBlockForReadAll";
    public static final String NvMSelectBlockForWriteAll = "NvMSelectBlockForWriteAll";
    public static final String NvMBlockUseAutoValidation = "NvMBlockUseAutoValidation";
    public static final String NvMBlockUseCRCCompMechanism = "NvMBlockUseCRCCompMechanism";
    public static final String NvMBlockUseSetRamBlockStatus = "NvMBlockUseSetRamBlockStatus";
    public static final String NvMBlockUseSyncMechanism = "NvMBlockUseSyncMechanism";
    public static final String NvMBswMBlockStatusInformation = "NvMBswMBlockStatusInformation";
    public static final String NvMBlockUseCrc = "NvMBlockUseCrc";
    public static final String NvMNvBlockLength = "NvMNvBlockLength";
    public static final String NvMNvBlockNum = "NvMNvBlockNum";
    public static final String NvMRomBlockNum = "NvMRomBlockNum";
    public static final String NvMWriteVerificationDataSize = "NvMWriteVerificationDataSize";
    public static final String NvMRomBlockDataAddress = "NvMRomBlockDataAddress";
    public static final String NvMInitBlockCallback = "NvMInitBlockCallback";
    public static final String NvMInitBlockCallbackFnc = "NvMInitBlockCallbackFnc";
    public static final String NvMSingleBlockCallback = "NvMSingleBlockCallback";
    public static final String NvMSingleBlockCallbackFnc = "NvMSingleBlockCallbackFnc";
    public static final String NvMReadRamBlockFromNvCallback = "NvMReadRamBlockFromNvCallback";
    public static final String NvMWriteRamBlockToNvCallback = "NvMWriteRamBlockToNvCallback";
    public static final String NvMBlockCrcType = "NvMBlockCrcType";
    public static final String NvMNameOfEaBlock = "NvMNameOfEaBlock";
    public static final String NvMNameOfFeeBlock = "NvMNameOfFeeBlock";
    public static final String NvMNvBlockBaseNumber = "NvMNvBlockBaseNumber";
    public static final String NvMNvramDeviceId = "NvMNvramDeviceId";
    public static final String NvMRamBlockDataAddress = "NvMRamBlockDataAddress";
    public static final String NVM_E_HARDWARE = "NVM_E_HARDWARE";
    public static final String NVM_E_INTEGRITY_FAILED = "NVM_E_INTEGRITY_FAILED";
    public static final String NVM_E_LOSS_OF_REDUNDANCY = "NVM_E_LOSS_OF_REDUNDANCY";
    public static final String NVM_E_QUEUE_OVERFLOW = "NVM_E_QUEUE_OVERFLOW";
    public static final String NVM_E_REQ_FAILED = "NVM_E_REQ_FAILED";
    public static final String NVM_E_VERIFY_FAILED = "NVM_E_VERIFY_FAILED";
    public static final String NVM_E_WRITE_PROTECTED = "NVM_E_WRITE_PROTECTED";
    public static final String NVM_E_WRONG_BLOCK_ID = "NVM_E_WRONG_BLOCK_ID";
    public static final String NvMNvramBlockIdentifier = "NvMNvramBlockIdentifier";
    public static final String NvMJobPrioritization = "NvMJobPrioritization";
    public static final String NvMBlockDescriptor = "NvMBlockDescriptor";
    public static final String NvMSelectBlockForFirstInitAll = "NvMSelectBlockForFirstInitAll";
    public static final String NvMBlockUseCompression = "NvMBlockUseCompression";
    public static final String Related_NvMBswMMultiBlockJobStatusInformation = "NvMBswMMultiBlockJobStatusInformation";
    public static final String Related_NvMWriteVerification = "NvMWriteVerification";
    public static final String Related_NvMApiConfigClass = "NvMApiConfigClass";
    public static final String Related_NvMJobPrioritization = "NvMJobPrioritization";
    public static final String Related_NvMBlockWriteProt = "NvMBlockWriteProt";
    public static final String Related_NvMWriteBlockOnce = "NvMWriteBlockOnce";
    public static final String Related_NvMBlockUseCrc = "NvMBlockUseCrc";
    public static final String Related_NvMDynamicConfiguration = "NvMDynamicConfiguration";
    public static final String Related_NvMBlockManagementType = "NvMBlockManagementType";
    public static final String Related_NvMBlockUsePort = "NvMBlockUsePort";
    public static final String Related_NvMBlockUseSyncMechanism = "NvMBlockUseSyncMechanism";
    public static final String Related_NvMRamBlockDataAddress = "NvMRamBlockDataAddress";
    public static final String Related_NvMSetRamBlockStatusApi = "NvMSetRamBlockStatusApi";
    public static final String Related_NvMRomBlockDataAddress = "NvMRomBlockDataAddress";
    public static final String Related_NvMBswMBlockStatusInformation = "NvMBswMBlockStatusInformation";
    public static final String Related_NvMDatasetSelectionBits = "NvMDatasetSelectionBits";
    public static final String Related_NvMNameOfEaBlock = "NvMNameOfEaBlock";
    public static final String Related_NvMNameOfFeeBlock = "NvMNameOfFeeBlock";
    public static final String Related_NvMBlockDescriptor = "NvMBlockDescriptor";
    public static final String Related_NvMRamBlockDataBufferAutoFill = "NvMRamBlockDataBufferAutoFill";
    public static final String Related_NvMNvBlockLength = "NvMNvBlockLength";

    @Override
    public UIDefinitionMap getUIDefinitionMap() {
        UIDefinitionMap uiDefinitionMap = new UIDefinitionMap();
        uiDefinitionMap.put((IUIDefinition) new NvMJobPrioritizationEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMBlockDescriptorEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMSizeImmediateJobQueueEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMBlockManagementTypeEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMBlockCrcTypeEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMBlockManagementType());
        uiDefinitionMap.put((IUIDefinition) new NvMBlockJobPriorityEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMWriteBlockOnceEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMBlockWriteProtEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMCalcRamBlockCrcEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMResistantToChangedSwEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMSelectBlockForReadAllEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMSelectBlockForWriteAllEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMBlockUseAutoValidationEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMBlockUseSetRamBlockStatusEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMBlockUseSyncMechanismEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMBlockUseCRCCompMechanismEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMBswMBlockStatusInformationEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMBlockUseCrcEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMNvBlockLengthEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMNvBlockNumEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMRomBlockNumEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMWriteVerificationDataSize());
        uiDefinitionMap.put((IUIDefinition) new NvMRamBlockDataAddressEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMReadRamBlockFromNvCallbackEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMReadRamBlockFromNvCallback());
        uiDefinitionMap.put((IUIDefinition) new NvMWriteRamBlockToNvmCallbackEnable());
        uiDefinitionMap.put((IUIDefinition) new NvMWriteRamBlockToNvCallback());
        uiDefinitionMap.put((IUIDefinition) new NvMNvBlockBaseNumberCount());
        uiDefinitionMap.put((IUIDefinition) new NvMNvramDeviceIdCount());
        uiDefinitionMap.put((IUIDefinition) new NvMNvramBlockIdentifier());
        uiDefinitionMap.put((IUIDefinition) new NvMInitBlockCallbackEnable());
        return uiDefinitionMap;
    }

    @Override
    public IModuleInit getModuleInit() {
        return null;
    }

    @Override
    public Map<String, DataHandle> getDataHandleMap() {
        HashMap<String, DataHandle> map = new HashMap<>();
        return map;
    }
}
