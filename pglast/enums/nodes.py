# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from nodes.h @ 16-latest-0-g680f5ee
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2024 Lele Gaifax
#

from enum import Enum, IntEnum, IntFlag, auto

try:
    from enum import StrEnum
except ImportError:  # pragma: no cover
    # Python < 3.10
    class StrEnum(str, Enum):
        pass


class AggSplit(IntEnum):
    AGGSPLIT_SIMPLE = 0
    AGGSPLIT_INITIAL_SERIAL = 0x02 | 0x04
    AGGSPLIT_FINAL_DESERIAL = 0x01 | 0x08

class AggStrategy(IntEnum):
    AGG_PLAIN = 0
    AGG_SORTED = auto()
    AGG_HASHED = auto()
    AGG_MIXED = auto()

class CmdType(IntEnum):
    CMD_UNKNOWN = 0
    CMD_SELECT = auto()
    CMD_UPDATE = auto()
    CMD_INSERT = auto()
    CMD_DELETE = auto()
    CMD_MERGE = auto()
    CMD_UTILITY = auto()
    CMD_NOTHING = auto()

class JoinType(IntEnum):
    JOIN_INNER = 0
    JOIN_LEFT = auto()
    JOIN_FULL = auto()
    JOIN_RIGHT = auto()
    JOIN_SEMI = auto()
    JOIN_ANTI = auto()
    JOIN_RIGHT_ANTI = auto()
    JOIN_UNIQUE_OUTER = auto()
    JOIN_UNIQUE_INNER = auto()

class LimitOption(IntEnum):
    LIMIT_OPTION_DEFAULT = 0
    LIMIT_OPTION_COUNT = auto()
    LIMIT_OPTION_WITH_TIES = auto()

class NodeTag(IntEnum):
    T_Invalid = 0
    T_List = 1
    T_Alias = 2
    T_RangeVar = 3
    T_TableFunc = 4
    T_IntoClause = 5
    T_Var = 6
    T_Const = 7
    T_Param = 8
    T_Aggref = 9
    T_GroupingFunc = 10
    T_WindowFunc = 11
    T_SubscriptingRef = 12
    T_FuncExpr = 13
    T_NamedArgExpr = 14
    T_OpExpr = 15
    T_DistinctExpr = 16
    T_NullIfExpr = 17
    T_ScalarArrayOpExpr = 18
    T_BoolExpr = 19
    T_SubLink = 20
    T_SubPlan = 21
    T_AlternativeSubPlan = 22
    T_FieldSelect = 23
    T_FieldStore = 24
    T_RelabelType = 25
    T_CoerceViaIO = 26
    T_ArrayCoerceExpr = 27
    T_ConvertRowtypeExpr = 28
    T_CollateExpr = 29
    T_CaseExpr = 30
    T_CaseWhen = 31
    T_CaseTestExpr = 32
    T_ArrayExpr = 33
    T_RowExpr = 34
    T_RowCompareExpr = 35
    T_CoalesceExpr = 36
    T_MinMaxExpr = 37
    T_SQLValueFunction = 38
    T_XmlExpr = 39
    T_JsonFormat = 40
    T_JsonReturning = 41
    T_JsonValueExpr = 42
    T_JsonConstructorExpr = 43
    T_JsonIsPredicate = 44
    T_NullTest = 45
    T_BooleanTest = 46
    T_CoerceToDomain = 47
    T_CoerceToDomainValue = 48
    T_SetToDefault = 49
    T_CurrentOfExpr = 50
    T_NextValueExpr = 51
    T_InferenceElem = 52
    T_TargetEntry = 53
    T_RangeTblRef = 54
    T_JoinExpr = 55
    T_FromExpr = 56
    T_OnConflictExpr = 57
    T_Query = 58
    T_TypeName = 59
    T_ColumnRef = 60
    T_ParamRef = 61
    T_A_Expr = 62
    T_A_Const = 63
    T_TypeCast = 64
    T_CollateClause = 65
    T_RoleSpec = 66
    T_FuncCall = 67
    T_A_Star = 68
    T_A_Indices = 69
    T_A_Indirection = 70
    T_A_ArrayExpr = 71
    T_ResTarget = 72
    T_MultiAssignRef = 73
    T_SortBy = 74
    T_WindowDef = 75
    T_RangeSubselect = 76
    T_RangeFunction = 77
    T_RangeTableFunc = 78
    T_RangeTableFuncCol = 79
    T_RangeTableSample = 80
    T_ColumnDef = 81
    T_TableLikeClause = 82
    T_IndexElem = 83
    T_DefElem = 84
    T_LockingClause = 85
    T_XmlSerialize = 86
    T_PartitionElem = 87
    T_PartitionSpec = 88
    T_PartitionBoundSpec = 89
    T_PartitionRangeDatum = 90
    T_PartitionCmd = 91
    T_RangeTblEntry = 92
    T_RTEPermissionInfo = 93
    T_RangeTblFunction = 94
    T_TableSampleClause = 95
    T_WithCheckOption = 96
    T_SortGroupClause = 97
    T_GroupingSet = 98
    T_WindowClause = 99
    T_RowMarkClause = 100
    T_WithClause = 101
    T_InferClause = 102
    T_OnConflictClause = 103
    T_CTESearchClause = 104
    T_CTECycleClause = 105
    T_CommonTableExpr = 106
    T_MergeWhenClause = 107
    T_MergeAction = 108
    T_TriggerTransition = 109
    T_JsonOutput = 110
    T_JsonKeyValue = 111
    T_JsonObjectConstructor = 112
    T_JsonArrayConstructor = 113
    T_JsonArrayQueryConstructor = 114
    T_JsonAggConstructor = 115
    T_JsonObjectAgg = 116
    T_JsonArrayAgg = 117
    T_RawStmt = 118
    T_InsertStmt = 119
    T_DeleteStmt = 120
    T_UpdateStmt = 121
    T_MergeStmt = 122
    T_SelectStmt = 123
    T_SetOperationStmt = 124
    T_ReturnStmt = 125
    T_PLAssignStmt = 126
    T_CreateSchemaStmt = 127
    T_AlterTableStmt = 128
    T_ReplicaIdentityStmt = 129
    T_AlterTableCmd = 130
    T_AlterCollationStmt = 131
    T_AlterDomainStmt = 132
    T_GrantStmt = 133
    T_ObjectWithArgs = 134
    T_AccessPriv = 135
    T_GrantRoleStmt = 136
    T_AlterDefaultPrivilegesStmt = 137
    T_CopyStmt = 138
    T_VariableSetStmt = 139
    T_VariableShowStmt = 140
    T_CreateStmt = 141
    T_Constraint = 142
    T_CreateTableSpaceStmt = 143
    T_DropTableSpaceStmt = 144
    T_AlterTableSpaceOptionsStmt = 145
    T_AlterTableMoveAllStmt = 146
    T_CreateExtensionStmt = 147
    T_AlterExtensionStmt = 148
    T_AlterExtensionContentsStmt = 149
    T_CreateFdwStmt = 150
    T_AlterFdwStmt = 151
    T_CreateForeignServerStmt = 152
    T_AlterForeignServerStmt = 153
    T_CreateForeignTableStmt = 154
    T_CreateUserMappingStmt = 155
    T_AlterUserMappingStmt = 156
    T_DropUserMappingStmt = 157
    T_ImportForeignSchemaStmt = 158
    T_CreatePolicyStmt = 159
    T_AlterPolicyStmt = 160
    T_CreateAmStmt = 161
    T_CreateTrigStmt = 162
    T_CreateEventTrigStmt = 163
    T_AlterEventTrigStmt = 164
    T_CreatePLangStmt = 165
    T_CreateRoleStmt = 166
    T_AlterRoleStmt = 167
    T_AlterRoleSetStmt = 168
    T_DropRoleStmt = 169
    T_CreateSeqStmt = 170
    T_AlterSeqStmt = 171
    T_DefineStmt = 172
    T_CreateDomainStmt = 173
    T_CreateOpClassStmt = 174
    T_CreateOpClassItem = 175
    T_CreateOpFamilyStmt = 176
    T_AlterOpFamilyStmt = 177
    T_DropStmt = 178
    T_TruncateStmt = 179
    T_CommentStmt = 180
    T_SecLabelStmt = 181
    T_DeclareCursorStmt = 182
    T_ClosePortalStmt = 183
    T_FetchStmt = 184
    T_IndexStmt = 185
    T_CreateStatsStmt = 186
    T_StatsElem = 187
    T_AlterStatsStmt = 188
    T_CreateFunctionStmt = 189
    T_FunctionParameter = 190
    T_AlterFunctionStmt = 191
    T_DoStmt = 192
    T_InlineCodeBlock = 193
    T_CallStmt = 194
    T_CallContext = 195
    T_RenameStmt = 196
    T_AlterObjectDependsStmt = 197
    T_AlterObjectSchemaStmt = 198
    T_AlterOwnerStmt = 199
    T_AlterOperatorStmt = 200
    T_AlterTypeStmt = 201
    T_RuleStmt = 202
    T_NotifyStmt = 203
    T_ListenStmt = 204
    T_UnlistenStmt = 205
    T_TransactionStmt = 206
    T_CompositeTypeStmt = 207
    T_CreateEnumStmt = 208
    T_CreateRangeStmt = 209
    T_AlterEnumStmt = 210
    T_ViewStmt = 211
    T_LoadStmt = 212
    T_CreatedbStmt = 213
    T_AlterDatabaseStmt = 214
    T_AlterDatabaseRefreshCollStmt = 215
    T_AlterDatabaseSetStmt = 216
    T_DropdbStmt = 217
    T_AlterSystemStmt = 218
    T_ClusterStmt = 219
    T_VacuumStmt = 220
    T_VacuumRelation = 221
    T_ExplainStmt = 222
    T_CreateTableAsStmt = 223
    T_RefreshMatViewStmt = 224
    T_CheckPointStmt = 225
    T_DiscardStmt = 226
    T_LockStmt = 227
    T_ConstraintsSetStmt = 228
    T_ReindexStmt = 229
    T_CreateConversionStmt = 230
    T_CreateCastStmt = 231
    T_CreateTransformStmt = 232
    T_PrepareStmt = 233
    T_ExecuteStmt = 234
    T_DeallocateStmt = 235
    T_DropOwnedStmt = 236
    T_ReassignOwnedStmt = 237
    T_AlterTSDictionaryStmt = 238
    T_AlterTSConfigurationStmt = 239
    T_PublicationTable = 240
    T_PublicationObjSpec = 241
    T_CreatePublicationStmt = 242
    T_AlterPublicationStmt = 243
    T_CreateSubscriptionStmt = 244
    T_AlterSubscriptionStmt = 245
    T_DropSubscriptionStmt = 246
    T_PlannerGlobal = 247
    T_PlannerInfo = 248
    T_RelOptInfo = 249
    T_IndexOptInfo = 250
    T_ForeignKeyOptInfo = 251
    T_StatisticExtInfo = 252
    T_JoinDomain = 253
    T_EquivalenceClass = 254
    T_EquivalenceMember = 255
    T_PathKey = 256
    T_PathTarget = 257
    T_ParamPathInfo = 258
    T_Path = 259
    T_IndexPath = 260
    T_IndexClause = 261
    T_BitmapHeapPath = 262
    T_BitmapAndPath = 263
    T_BitmapOrPath = 264
    T_TidPath = 265
    T_TidRangePath = 266
    T_SubqueryScanPath = 267
    T_ForeignPath = 268
    T_CustomPath = 269
    T_AppendPath = 270
    T_MergeAppendPath = 271
    T_GroupResultPath = 272
    T_MaterialPath = 273
    T_MemoizePath = 274
    T_UniquePath = 275
    T_GatherPath = 276
    T_GatherMergePath = 277
    T_NestPath = 278
    T_MergePath = 279
    T_HashPath = 280
    T_ProjectionPath = 281
    T_ProjectSetPath = 282
    T_SortPath = 283
    T_IncrementalSortPath = 284
    T_GroupPath = 285
    T_UpperUniquePath = 286
    T_AggPath = 287
    T_GroupingSetData = 288
    T_RollupData = 289
    T_GroupingSetsPath = 290
    T_MinMaxAggPath = 291
    T_WindowAggPath = 292
    T_SetOpPath = 293
    T_RecursiveUnionPath = 294
    T_LockRowsPath = 295
    T_ModifyTablePath = 296
    T_LimitPath = 297
    T_RestrictInfo = 298
    T_PlaceHolderVar = 299
    T_SpecialJoinInfo = 300
    T_OuterJoinClauseInfo = 301
    T_AppendRelInfo = 302
    T_RowIdentityVarInfo = 303
    T_PlaceHolderInfo = 304
    T_MinMaxAggInfo = 305
    T_PlannerParamItem = 306
    T_AggInfo = 307
    T_AggTransInfo = 308
    T_PlannedStmt = 309
    T_Result = 310
    T_ProjectSet = 311
    T_ModifyTable = 312
    T_Append = 313
    T_MergeAppend = 314
    T_RecursiveUnion = 315
    T_BitmapAnd = 316
    T_BitmapOr = 317
    T_SeqScan = 318
    T_SampleScan = 319
    T_IndexScan = 320
    T_IndexOnlyScan = 321
    T_BitmapIndexScan = 322
    T_BitmapHeapScan = 323
    T_TidScan = 324
    T_TidRangeScan = 325
    T_SubqueryScan = 326
    T_FunctionScan = 327
    T_ValuesScan = 328
    T_TableFuncScan = 329
    T_CteScan = 330
    T_NamedTuplestoreScan = 331
    T_WorkTableScan = 332
    T_ForeignScan = 333
    T_CustomScan = 334
    T_NestLoop = 335
    T_NestLoopParam = 336
    T_MergeJoin = 337
    T_HashJoin = 338
    T_Material = 339
    T_Memoize = 340
    T_Sort = 341
    T_IncrementalSort = 342
    T_Group = 343
    T_Agg = 344
    T_WindowAgg = 345
    T_Unique = 346
    T_Gather = 347
    T_GatherMerge = 348
    T_Hash = 349
    T_SetOp = 350
    T_LockRows = 351
    T_Limit = 352
    T_PlanRowMark = 353
    T_PartitionPruneInfo = 354
    T_PartitionedRelPruneInfo = 355
    T_PartitionPruneStepOp = 356
    T_PartitionPruneStepCombine = 357
    T_PlanInvalItem = 358
    T_ExprState = 359
    T_IndexInfo = 360
    T_ExprContext = 361
    T_ReturnSetInfo = 362
    T_ProjectionInfo = 363
    T_JunkFilter = 364
    T_OnConflictSetState = 365
    T_MergeActionState = 366
    T_ResultRelInfo = 367
    T_EState = 368
    T_WindowFuncExprState = 369
    T_SetExprState = 370
    T_SubPlanState = 371
    T_DomainConstraintState = 372
    T_ResultState = 373
    T_ProjectSetState = 374
    T_ModifyTableState = 375
    T_AppendState = 376
    T_MergeAppendState = 377
    T_RecursiveUnionState = 378
    T_BitmapAndState = 379
    T_BitmapOrState = 380
    T_ScanState = 381
    T_SeqScanState = 382
    T_SampleScanState = 383
    T_IndexScanState = 384
    T_IndexOnlyScanState = 385
    T_BitmapIndexScanState = 386
    T_BitmapHeapScanState = 387
    T_TidScanState = 388
    T_TidRangeScanState = 389
    T_SubqueryScanState = 390
    T_FunctionScanState = 391
    T_ValuesScanState = 392
    T_TableFuncScanState = 393
    T_CteScanState = 394
    T_NamedTuplestoreScanState = 395
    T_WorkTableScanState = 396
    T_ForeignScanState = 397
    T_CustomScanState = 398
    T_JoinState = 399
    T_NestLoopState = 400
    T_MergeJoinState = 401
    T_HashJoinState = 402
    T_MaterialState = 403
    T_MemoizeState = 404
    T_SortState = 405
    T_IncrementalSortState = 406
    T_GroupState = 407
    T_AggState = 408
    T_WindowAggState = 409
    T_UniqueState = 410
    T_GatherState = 411
    T_GatherMergeState = 412
    T_HashState = 413
    T_SetOpState = 414
    T_LockRowsState = 415
    T_LimitState = 416
    T_IndexAmRoutine = 417
    T_TableAmRoutine = 418
    T_TsmRoutine = 419
    T_EventTriggerData = 420
    T_TriggerData = 421
    T_TupleTableSlot = 422
    T_FdwRoutine = 423
    T_Bitmapset = 424
    T_ExtensibleNode = 425
    T_ErrorSaveContext = 426
    T_IdentifySystemCmd = 427
    T_BaseBackupCmd = 428
    T_CreateReplicationSlotCmd = 429
    T_DropReplicationSlotCmd = 430
    T_StartReplicationCmd = 431
    T_ReadReplicationSlotCmd = 432
    T_TimeLineHistoryCmd = 433
    T_SupportRequestSimplify = 434
    T_SupportRequestSelectivity = 435
    T_SupportRequestCost = 436
    T_SupportRequestRows = 437
    T_SupportRequestIndexCondition = 438
    T_SupportRequestWFuncMonotonic = 439
    T_SupportRequestOptimizeWindowClause = 440
    T_Integer = 441
    T_Float = 442
    T_Boolean = 443
    T_String = 444
    T_BitString = 445
    T_ForeignKeyCacheInfo = 446
    T_IntList = 447
    T_OidList = 448
    T_XidList = 449
    T_AllocSetContext = 450
    T_GenerationContext = 451
    T_SlabContext = 452
    T_TIDBitmap = 453
    T_WindowObjectData = 454

class OnConflictAction(IntEnum):
    ONCONFLICT_NONE = 0
    ONCONFLICT_NOTHING = auto()
    ONCONFLICT_UPDATE = auto()

class SetOpCmd(IntEnum):
    SETOPCMD_INTERSECT = 0
    SETOPCMD_INTERSECT_ALL = auto()
    SETOPCMD_EXCEPT = auto()
    SETOPCMD_EXCEPT_ALL = auto()

class SetOpStrategy(IntEnum):
    SETOP_SORTED = 0
    SETOP_HASHED = auto()


# #define-ed constants

AGGSPLITOP_COMBINE = 0x01

AGGSPLITOP_SKIPFINAL = 0x02

AGGSPLITOP_SERIALIZE = 0x04

AGGSPLITOP_DESERIALIZE = 0x08
