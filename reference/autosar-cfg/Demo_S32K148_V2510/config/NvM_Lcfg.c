/**
 * COPYRIGHT
 * ---------------------------------------------------------------------------------------------------------------------
 * Copyright (c) iSOFT INFRASTRUCTURE SOFTWARE CO., LTD. This software is proprietary to
 * iSOFT INFRASTRUCTURE SOFTWARE CO., LTD., and all rights are reserved by iSOFT INFRASTRUCTURE SOFTWARE CO., LTD.
 * Without the express written permission of the company, no organization or individual may copy, install, trial,
 * distribute, or reverse engineer this software. For terms of use and further details, please refer to the End User
 * License Agreement (EULA) or contact us business@i-soft.com.cn for more assistance.
 *
 * This file contains code from iSoft, which is licensed under the LGPL-2.1. However, due to a special exception,
 * you are not required to comply with the provisions of section 6a of LGPL-2.1. Specifically, you may distribute
 * your software, including this file, under terms of your choice, including proprietary licenses, without needing to
 * provide the source code or object code as specified in section 6a. For more details, please refer to the project's
 * LICENSE and EXCEPTION files and the specific exception statement.
 * ---------------------------------------------------------------------------------------------------------------------
 * FILE DESCRIPTION
 * ---------------------------------------------------------------------------------------------------------------------
 * @MCU         : S32K148
 * @file        : NvM_Lcfg.c
 * @licence     : 
 * @date        : 2026-05-04 00:09:17
 * @customer    : iSoft
 * @description : Link time definitions of NvM
 * @generator   : AUTOSAR classic Platform R23-11
 * @toolVersion : for EasyXMen V25.10
 **********************************************************************************************************************/

/* =================================================== inclusions =================================================== */
#include "Rte_NvMApp.h"
#include "Dem_Cbk.h"
#include "NvM_Types.h"
#include "NvM_Lcfg.h"
#include "Rte_NvM.h"

/* ===================================================== macros ===================================================== */

/* ================================================ type definitions ================================================ */

/* ========================================== internal function declarations ======================================== */

/* ============================================ internal data definitions =========================================== */

/* ============================================ external data definitions =========================================== */
#define NVM_START_SEC_CONFIG_DATA_PTR
#include "NvM_MemMap.h"
/**
 * @brief Container for NvmMultiBlockCallback
 */
/* PRQA S 1502 ++ */ /* VL_NvM_1502 */
const NvM_MultiBlockCallbackType NvmMultiBlockCallback = NULL_PTR;
/* PRQA S 1502 -- */
#define NVM_STOP_SEC_CONFIG_DATA_PTR
#include "NvM_MemMap.h"

/* PRQA S 3132 ++ */ /* VL_QAC_MagicNum */
/* PRQA S 1504,1751 ++ */ /* VL_QAC_OneRefSymbol */
#define NVM_START_SEC_VAR_CLEARED_8
#include "NvM_MemMap.h"
/**
 * @brief Buffer of RAM block
 */
uint8 NvMBlockRamBuffer1[2];
uint8 NvMBlockRamBuffer2[1];
uint8 NvMBlockRamBuffer3[1];
uint8 NvMBlockRamBuffer4[17];
uint8 NvMBlockRamBuffer5[4];
#define NVM_STOP_SEC_VAR_CLEARED_8
#include "NvM_MemMap.h"

#define NVM_START_SEC_VAR_CLEARED_32
#include "NvM_MemMap.h"
uint32 NvMCrcBuf_NvMBlock_ConfigID[1];
uint32 NvMCrcBuf_NvMBlock_SecurityLevel01[1];
uint32 NvMCrcBuf_NvMBlock_SecurityLevel02[1];
uint32 NvMCrcBuf_NvMBlock_DIDF190[1];
uint32 NvMCrcBuf_NvMBlock_DIDF183[1];
uint32 NvMCrcBuf_NvMBlock_Primary_0[1];
uint32 NvMCrcBuf_NvMBlock_Primary_1[1];
uint32 NvMCrcBuf_NvMBlock_Primary_2[1];
uint32 NvMCrcBuf_NvMBlock_Primary_3[1];
uint32 NvMCrcBuf_NvMBlock_Primary_4[1];
uint32 NvMCrcBuf_NvMBlock_Primary_5[1];
uint32 NvMCrcBuf_NvMBlock_Primary_6[1];
uint32 NvMCrcBuf_NvMBlock_Primary_7[1];
uint32 NvMCrcBuf_NvMBlock_Primary_8[1];
uint32 NvMCrcBuf_NvMBlock_Primary_9[1];
uint32 NvMCrcBuf_NvMBlock_Primary_10[1];
uint32 NvMCrcBuf_NvMBlock_Primary_11[1];
uint32 NvMCrcBuf_NvMBlock_Primary_12[1];
uint32 NvMCrcBuf_NvMBlock_Primary_13[1];
uint32 NvMCrcBuf_NvMBlock_Primary_14[1];
uint32 NvMCrcBuf_NvMBlock_Primary_15[1];
uint32 NvMCrcBuf_NvMBlock_Primary_16[1];
uint32 NvMCrcBuf_NvMBlock_AdminData[1];
uint32 NvMCrcBuf_NvMBlock_EventStatusData[1];
#define NVM_STOP_SEC_VAR_CLEARED_32
#include "NvM_MemMap.h"
/* PRQA S 3132 -- */
/* PRQA S 1504,1751 -- */
#define NVM_START_SEC_CONFIG_DATA_UNSPECIFIED
#include "NvM_MemMap.h"

/**
 * @brief Container for a management structure to configure the composition of a given NVRAM Block Management Type
 */
/* PRQA S 1334 ++ */ /* VL_NvM_1334 */
const NvM_BlockDescriptorType NvM_BlockDescriptor[NVM_BLOCK_NUM_ALL] =
{
    /** NvMBlock_ConfigID */
    {
        0u,        /** NvMNvramDeviceId */
        NVM_BLOCK_REDUNDANT,    /** NvmBlockManagementType */
        2u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x3cu, /** FlagGroup */
        1u,   /** NvmNvBlockBaseNumber */
        2u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_ConfigID,    /** NvmBlockCrcBuffAddress */
        (uint8*) NvMBlockRamBuffer1,	/** NvMRamBlockDataAddress */
        NULL_PTR,   /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,   /** NvMInitBlockCallback */
        NULL_PTR,   /** NvMSingleBlockCallback */
        NULL_PTR,   /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,   /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_SecurityLevel01 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x23cu, /** FlagGroup */
        5u,    /** NvmNvBlockBaseNumber */
        1u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_SecurityLevel01,    /** NvmBlockCrcBuffAddress */
        (uint8*) NvMBlockRamBuffer2,    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        NULL_PTR,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_SecurityLevel02 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x23cu, /** FlagGroup */
        6u,    /** NvmNvBlockBaseNumber */
        1u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_SecurityLevel02,    /** NvmBlockCrcBuffAddress */
        (uint8*) NvMBlockRamBuffer3,    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        NULL_PTR,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_DIDF190 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        1u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x21cu, /** FlagGroup */
        7u,    /** NvmNvBlockBaseNumber */
        17u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_DIDF190,    /** NvmBlockCrcBuffAddress */
        (uint8*) NvMBlockRamBuffer4,    /** NvMRamBlockDataAddress */
        (uint8*) NvMBlock_DIDF190_RomAddress,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        NULL_PTR,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_DIDF183 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        1u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x21cu, /** FlagGroup */
        8u,    /** NvmNvBlockBaseNumber */
        4u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_DIDF183,    /** NvmBlockCrcBuffAddress */
        (uint8*) NvMBlockRamBuffer5,    /** NvMRamBlockDataAddress */
        (uint8*) NvMBlock_DIDF183_RomAddress,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        NULL_PTR,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_0 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        9u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_0,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[0],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_1 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        10u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_1,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[1],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_2 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        11u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_2,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[2],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_3 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        12u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_3,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[3],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_4 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        13u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_4,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[4],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_5 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        14u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_5,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[5],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_6 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        15u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_6,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[6],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_7 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        16u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_7,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[7],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_8 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        17u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_8,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[8],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_9 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        18u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_9,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[9],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_10 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        19u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_10,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[10],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_11 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        20u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_11,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[11],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_12 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        21u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_12,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[12],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_13 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        22u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_13,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[13],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_14 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        23u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_14,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[14],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_15 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        24u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_15,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[15],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_Primary_16 */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        25u,    /** NvmNvBlockBaseNumber */
        28u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_Primary_16,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetMemoryEntry()[16],    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        NULL_PTR,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_AdminData */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        26u,    /** NvmNvBlockBaseNumber */
        6u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_AdminData,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetAdminData(),    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        Dem_NvMInitAdminData,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
    /** NvMBlock_EventStatusData */
    {
        0u,	        /** NvMNvramDeviceId */
        NVM_BLOCK_NATIVE,    /** NvmBlockManagementType */
        1u,    /** NvmNvBlockNum */
        0u,    /** NvmRomBlockNum */
        3u, /** NvMMaxNumOfReadRetries */
        3u,  /** NvMMaxNumOfWriteRetries */
        NVM_CRC16,        /** NvmBlockCRCType */
        /*
         * Bit 0:NvmWriteBlockOnce
         * Bit 1:NvmBlockWriteProt
         * Bit 2:NvmCalcRamBlockCrc
         * Bit 3:NvmResistantToChangedSw
         * Bit 4:NvmSelectBlockForReadall
         * Bit 5:NvmSelectBlockForWriteall
         * Bit 6:NvMStaticBlockIDCheck
         * Bit 7:NvMWriteVerification
         * Bit 8:NvMBlockUseAutoValidation
         * Bit 9:NvMBlockUseCRCCompMechanism
         * Bit 10:NvMBlockUseSetRamBlockStatus
         * Bit 11:NvMBlockUseSyncMechanism
         * Bit 12:NvMBswMBlockStatusInformation
         * Bit 13:NvMSelectBlockForFirstInitAll
         * BIt 14:NvMBlockUseCompression
         */
        0x538u, /** FlagGroup */
        27u,    /** NvmNvBlockBaseNumber */
        26u,    /** NvmNvBlockLength */
        0u, /** NvMWriteVerificationDataSize */
        0u, /** RepairIndex */
        /* PRQA S 3432, 0306++ */ /* VL_NvM_3432, VL_NvM_0306 */
        NvMCrcBuf_NvMBlock_EventStatusData,    /** NvmBlockCrcBuffAddress */
        (uint8*) &Dem_GetEventStatusData(),    /** NvMRamBlockDataAddress */
        NULL_PTR,       /** NvMRomBlockDataAddress */
        /* PRQA S 3432, 0306 -- */
        Dem_NvMInitStatusData,       /** NvMInitBlockCallback */
        Dem_NvMJobFinished,    /** NvmSingleBlockCallback */
        NULL_PTR,       /** NvM_ReadRamBlockFromNvmCallbackType */
        NULL_PTR,       /** NvM_WriteRamBlockToNvmCallbackType */
    },
};
/* PRQA S 1334 -- */
#define NVM_STOP_SEC_CONFIG_DATA_UNSPECIFIED
#include "NvM_MemMap.h"


/* ========================================== external function definitions ========================================= */

/* ========================================== internal function definitions ========================================= */

