.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017-2024 Lele Gaifax
..

============================================================================
 :mod:`pglast.enums.primnodes` --- Constants extracted from `primnodes.h`__
============================================================================

__ https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h

.. module:: pglast.enums.primnodes
   :synopsis: Constants extracted from primnodes.h


.. class:: pglast.enums.primnodes.BoolExprType

   Corresponds to the `BoolExprType enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L856>`__.

   .. data:: AND_EXPR

   .. data:: OR_EXPR

   .. data:: NOT_EXPR


.. class:: pglast.enums.primnodes.BoolTestType

   Corresponds to the `BoolTestType enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L1705>`__.

   .. data:: IS_TRUE

   .. data:: IS_NOT_TRUE

   .. data:: IS_FALSE

   .. data:: IS_NOT_FALSE

   .. data:: IS_UNKNOWN

   .. data:: IS_NOT_UNKNOWN


.. class:: pglast.enums.primnodes.CoercionContext

   Corresponds to the `CoercionContext enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L639>`__.

   .. data:: COERCION_IMPLICIT

   .. data:: COERCION_ASSIGNMENT

   .. data:: COERCION_PLPGSQL

   .. data:: COERCION_EXPLICIT


.. class:: pglast.enums.primnodes.CoercionForm

   Corresponds to the `CoercionForm enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L659>`__.

   .. data:: COERCE_EXPLICIT_CALL

   .. data:: COERCE_EXPLICIT_CAST

   .. data:: COERCE_IMPLICIT_CAST

   .. data:: COERCE_SQL_SYNTAX


.. class:: pglast.enums.primnodes.JsonConstructorType

   Corresponds to the `JsonConstructorType enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L1611>`__.

   .. data:: JSCTOR_JSON_OBJECT

   .. data:: JSCTOR_JSON_ARRAY

   .. data:: JSCTOR_JSON_OBJECTAGG

   .. data:: JSCTOR_JSON_ARRAYAGG


.. class:: pglast.enums.primnodes.JsonEncoding

   Corresponds to the `JsonEncoding enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L1551>`__.

   .. data:: JS_ENC_DEFAULT

   .. data:: JS_ENC_UTF8

   .. data:: JS_ENC_UTF16

   .. data:: JS_ENC_UTF32


.. class:: pglast.enums.primnodes.JsonFormatType

   Corresponds to the `JsonFormatType enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L1563>`__.

   .. data:: JS_FORMAT_DEFAULT

   .. data:: JS_FORMAT_JSON

   .. data:: JS_FORMAT_JSONB


.. class:: pglast.enums.primnodes.JsonValueType

   Corresponds to the `JsonValueType enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L1640>`__.

   .. data:: JS_TYPE_ANY

   .. data:: JS_TYPE_OBJECT

   .. data:: JS_TYPE_ARRAY

   .. data:: JS_TYPE_SCALAR


.. class:: pglast.enums.primnodes.MinMaxOp

   Corresponds to the `MinMaxOp enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L1427>`__.

   .. data:: IS_GREATEST

   .. data:: IS_LEAST


.. class:: pglast.enums.primnodes.NullTestType

   Corresponds to the `NullTestType enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L1681>`__.

   .. data:: IS_NULL

   .. data:: IS_NOT_NULL


.. class:: pglast.enums.primnodes.OnCommitAction

   Corresponds to the `OnCommitAction enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L47>`__.

   .. data:: ONCOMMIT_NOOP

   .. data:: ONCOMMIT_PRESERVE_ROWS

   .. data:: ONCOMMIT_DELETE_ROWS

   .. data:: ONCOMMIT_DROP


.. class:: pglast.enums.primnodes.ParamKind

   Corresponds to the `ParamKind enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L343>`__.

   .. data:: PARAM_EXTERN

   .. data:: PARAM_EXEC

   .. data:: PARAM_SUBLINK

   .. data:: PARAM_MULTIEXPR


.. class:: pglast.enums.primnodes.RowCompareType

   Corresponds to the `RowCompareType enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L1379>`__.

   .. data:: ROWCOMPARE_LT

   .. data:: ROWCOMPARE_LE

   .. data:: ROWCOMPARE_EQ

   .. data:: ROWCOMPARE_GE

   .. data:: ROWCOMPARE_GT

   .. data:: ROWCOMPARE_NE


.. class:: pglast.enums.primnodes.SQLValueFunctionOp

   Corresponds to the `SQLValueFunctionOp enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L1461>`__.

   .. data:: SVFOP_CURRENT_DATE

   .. data:: SVFOP_CURRENT_TIME

   .. data:: SVFOP_CURRENT_TIME_N

   .. data:: SVFOP_CURRENT_TIMESTAMP

   .. data:: SVFOP_CURRENT_TIMESTAMP_N

   .. data:: SVFOP_LOCALTIME

   .. data:: SVFOP_LOCALTIME_N

   .. data:: SVFOP_LOCALTIMESTAMP

   .. data:: SVFOP_LOCALTIMESTAMP_N

   .. data:: SVFOP_CURRENT_ROLE

   .. data:: SVFOP_CURRENT_USER

   .. data:: SVFOP_USER

   .. data:: SVFOP_SESSION_USER

   .. data:: SVFOP_CURRENT_CATALOG

   .. data:: SVFOP_CURRENT_SCHEMA


.. class:: pglast.enums.primnodes.SubLinkType

   Corresponds to the `SubLinkType enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L922>`__.

   .. data:: EXISTS_SUBLINK

   .. data:: ALL_SUBLINK

   .. data:: ANY_SUBLINK

   .. data:: ROWCOMPARE_SUBLINK

   .. data:: EXPR_SUBLINK

   .. data:: MULTIEXPR_SUBLINK

   .. data:: ARRAY_SUBLINK

   .. data:: CTE_SUBLINK


.. class:: pglast.enums.primnodes.XmlExprOp

   Corresponds to the `XmlExprOp enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L1505>`__.

   .. data:: IS_XMLCONCAT

   .. data:: IS_XMLELEMENT

   .. data:: IS_XMLFOREST

   .. data:: IS_XMLPARSE

   .. data:: IS_XMLPI

   .. data:: IS_XMLROOT

   .. data:: IS_XMLSERIALIZE

   .. data:: IS_DOCUMENT


.. class:: pglast.enums.primnodes.XmlOptionType

   Corresponds to the `XmlOptionType enum <https://github.com/pganalyze/libpg_query/blob/680f5ee/src/postgres/include/nodes/primnodes.h#L1517>`__.

   .. data:: XMLOPTION_DOCUMENT

   .. data:: XMLOPTION_CONTENT
