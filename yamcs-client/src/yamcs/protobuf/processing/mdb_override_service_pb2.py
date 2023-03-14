# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/processing/mdb_override_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from yamcs.api import annotations_pb2 as yamcs_dot_api_dot_annotations__pb2
from yamcs.protobuf.mdb import mdb_pb2 as yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/processing/mdb_override_service.proto',
  package='yamcs.protobuf.processing',
  syntax='proto2',
  serialized_options=_b('\n\022org.yamcs.protobufB\027MdbOverrideServiceProtoP\001'),
  serialized_pb=_b('\n4yamcs/protobuf/processing/mdb_override_service.proto\x12\x19yamcs.protobuf.processing\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1byamcs/api/annotations.proto\x1a\x1cyamcs/protobuf/mdb/mdb.proto\">\n\x17ListMdbOverridesRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x11\n\tprocessor\x18\x02 \x01(\t\"Y\n\x18ListMdbOverridesResponse\x12=\n\toverrides\x18\x01 \x03(\x0b\x32*.yamcs.protobuf.processing.MdbOverrideInfo\"Q\n\x1cGetAlgorithmOverridesRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x11\n\tprocessor\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"g\n\x1dGetAlgorithmOverridesResponse\x12\x46\n\x0ctextOverride\x18\x01 \x01(\x0b\x32\x30.yamcs.protobuf.processing.AlgorithmTextOverride\"\xcd\x01\n\x0fMdbOverrideInfo\x12\x45\n\x04type\x18\x01 \x01(\x0e\x32\x37.yamcs.protobuf.processing.MdbOverrideInfo.OverrideType\x12O\n\x15\x61lgorithmTextOverride\x18\x02 \x01(\x0b\x32\x30.yamcs.protobuf.processing.AlgorithmTextOverride\"\"\n\x0cOverrideType\x12\x12\n\x0e\x41LGORITHM_TEXT\x10\x00\"8\n\x15\x41lgorithmTextOverride\x12\x11\n\talgorithm\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"\xab\x04\n\x16UpdateParameterRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x11\n\tprocessor\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12L\n\x06\x61\x63tion\x18\x04 \x01(\x0e\x32<.yamcs.protobuf.processing.UpdateParameterRequest.ActionType\x12=\n\x11\x64\x65\x66\x61ultCalibrator\x18\x05 \x01(\x0b\x32\".yamcs.protobuf.mdb.CalibratorInfo\x12\x44\n\x11\x63ontextCalibrator\x18\x06 \x03(\x0b\x32).yamcs.protobuf.mdb.ContextCalibratorInfo\x12\x33\n\x0c\x64\x65\x66\x61ultAlarm\x18\x07 \x01(\x0b\x32\x1d.yamcs.protobuf.mdb.AlarmInfo\x12:\n\x0c\x63ontextAlarm\x18\x08 \x03(\x0b\x32$.yamcs.protobuf.mdb.ContextAlarmInfo\"\x99\x01\n\nActionType\x12\t\n\x05RESET\x10\x00\x12\x15\n\x11RESET_CALIBRATORS\x10\x01\x12\x1a\n\x16SET_DEFAULT_CALIBRATOR\x10\x02\x12\x13\n\x0fSET_CALIBRATORS\x10\x03\x12\x10\n\x0cRESET_ALARMS\x10\x04\x12\x16\n\x12SET_DEFAULT_ALARMS\x10\x05\x12\x0e\n\nSET_ALARMS\x10\x06\"\xf1\x01\n\x16UpdateAlgorithmRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x11\n\tprocessor\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12L\n\x06\x61\x63tion\x18\x04 \x01(\x0e\x32<.yamcs.protobuf.processing.UpdateAlgorithmRequest.ActionType\x12\x34\n\talgorithm\x18\x06 \x01(\x0b\x32!.yamcs.protobuf.mdb.AlgorithmInfo\" \n\nActionType\x12\t\n\x05RESET\x10\x00\x12\x07\n\x03SET\x10\x01\x32\xef\x06\n\x0eMdbOverrideApi\x12\xac\x01\n\x10ListMdbOverrides\x12\x32.yamcs.protobuf.processing.ListMdbOverridesRequest\x1a\x33.yamcs.protobuf.processing.ListMdbOverridesResponse\"/\x8a\x92\x03+\n)/api/mdb-overrides/{instance}/{processor}\x12\xce\x01\n\x15GetAlgorithmOverrides\x12\x37.yamcs.protobuf.processing.GetAlgorithmOverridesRequest\x1a\x38.yamcs.protobuf.processing.GetAlgorithmOverridesResponse\"B\x8a\x92\x03>\n</api/mdb-overrides/{instance}/{processor}/algorithms/{name*}\x12\xeb\x01\n\x0fUpdateParameter\x12\x31.yamcs.protobuf.processing.UpdateParameterRequest\x1a%.yamcs.protobuf.mdb.ParameterTypeInfo\"~\x8a\x92\x03z*</api/mdb-overrides/{instance}/{processor}/parameters/{name*}:\x01*Z7*2/api/mdb/{instance}/{processor}/parameters/{name*}:\x01*\x12\xdc\x01\n\x0fUpdateAlgorithm\x12\x31.yamcs.protobuf.processing.UpdateAlgorithmRequest\x1a\x16.google.protobuf.Empty\"~\x8a\x92\x03z*</api/mdb-overrides/{instance}/{processor}/algorithms/{name*}:\x01*Z7*2/api/mdb/{instance}/{processor}/algorithms/{name*}:\x01*\x1a\x10\x82\x80\x01\x0cMDB OverrideB/\n\x12org.yamcs.protobufB\x17MdbOverrideServiceProtoP\x01')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,yamcs_dot_api_dot_annotations__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2.DESCRIPTOR,])



_MDBOVERRIDEINFO_OVERRIDETYPE = _descriptor.EnumDescriptor(
  name='OverrideType',
  full_name='yamcs.protobuf.processing.MdbOverrideInfo.OverrideType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALGORITHM_TEXT', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=686,
  serialized_end=720,
)
_sym_db.RegisterEnumDescriptor(_MDBOVERRIDEINFO_OVERRIDETYPE)

_UPDATEPARAMETERREQUEST_ACTIONTYPE = _descriptor.EnumDescriptor(
  name='ActionType',
  full_name='yamcs.protobuf.processing.UpdateParameterRequest.ActionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESET_CALIBRATORS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_DEFAULT_CALIBRATOR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_CALIBRATORS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESET_ALARMS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_DEFAULT_ALARMS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_ALARMS', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1183,
  serialized_end=1336,
)
_sym_db.RegisterEnumDescriptor(_UPDATEPARAMETERREQUEST_ACTIONTYPE)

_UPDATEALGORITHMREQUEST_ACTIONTYPE = _descriptor.EnumDescriptor(
  name='ActionType',
  full_name='yamcs.protobuf.processing.UpdateAlgorithmRequest.ActionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1548,
  serialized_end=1580,
)
_sym_db.RegisterEnumDescriptor(_UPDATEALGORITHMREQUEST_ACTIONTYPE)


_LISTMDBOVERRIDESREQUEST = _descriptor.Descriptor(
  name='ListMdbOverridesRequest',
  full_name='yamcs.protobuf.processing.ListMdbOverridesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.processing.ListMdbOverridesRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processor', full_name='yamcs.protobuf.processing.ListMdbOverridesRequest.processor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=233,
)


_LISTMDBOVERRIDESRESPONSE = _descriptor.Descriptor(
  name='ListMdbOverridesResponse',
  full_name='yamcs.protobuf.processing.ListMdbOverridesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='overrides', full_name='yamcs.protobuf.processing.ListMdbOverridesResponse.overrides', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=324,
)


_GETALGORITHMOVERRIDESREQUEST = _descriptor.Descriptor(
  name='GetAlgorithmOverridesRequest',
  full_name='yamcs.protobuf.processing.GetAlgorithmOverridesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.processing.GetAlgorithmOverridesRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processor', full_name='yamcs.protobuf.processing.GetAlgorithmOverridesRequest.processor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.processing.GetAlgorithmOverridesRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=407,
)


_GETALGORITHMOVERRIDESRESPONSE = _descriptor.Descriptor(
  name='GetAlgorithmOverridesResponse',
  full_name='yamcs.protobuf.processing.GetAlgorithmOverridesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='textOverride', full_name='yamcs.protobuf.processing.GetAlgorithmOverridesResponse.textOverride', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=409,
  serialized_end=512,
)


_MDBOVERRIDEINFO = _descriptor.Descriptor(
  name='MdbOverrideInfo',
  full_name='yamcs.protobuf.processing.MdbOverrideInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='yamcs.protobuf.processing.MdbOverrideInfo.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='algorithmTextOverride', full_name='yamcs.protobuf.processing.MdbOverrideInfo.algorithmTextOverride', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MDBOVERRIDEINFO_OVERRIDETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=515,
  serialized_end=720,
)


_ALGORITHMTEXTOVERRIDE = _descriptor.Descriptor(
  name='AlgorithmTextOverride',
  full_name='yamcs.protobuf.processing.AlgorithmTextOverride',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='yamcs.protobuf.processing.AlgorithmTextOverride.algorithm', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='yamcs.protobuf.processing.AlgorithmTextOverride.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=722,
  serialized_end=778,
)


_UPDATEPARAMETERREQUEST = _descriptor.Descriptor(
  name='UpdateParameterRequest',
  full_name='yamcs.protobuf.processing.UpdateParameterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.processing.UpdateParameterRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processor', full_name='yamcs.protobuf.processing.UpdateParameterRequest.processor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.processing.UpdateParameterRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='yamcs.protobuf.processing.UpdateParameterRequest.action', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultCalibrator', full_name='yamcs.protobuf.processing.UpdateParameterRequest.defaultCalibrator', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contextCalibrator', full_name='yamcs.protobuf.processing.UpdateParameterRequest.contextCalibrator', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultAlarm', full_name='yamcs.protobuf.processing.UpdateParameterRequest.defaultAlarm', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contextAlarm', full_name='yamcs.protobuf.processing.UpdateParameterRequest.contextAlarm', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UPDATEPARAMETERREQUEST_ACTIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=781,
  serialized_end=1336,
)


_UPDATEALGORITHMREQUEST = _descriptor.Descriptor(
  name='UpdateAlgorithmRequest',
  full_name='yamcs.protobuf.processing.UpdateAlgorithmRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.processing.UpdateAlgorithmRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processor', full_name='yamcs.protobuf.processing.UpdateAlgorithmRequest.processor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.processing.UpdateAlgorithmRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='yamcs.protobuf.processing.UpdateAlgorithmRequest.action', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='yamcs.protobuf.processing.UpdateAlgorithmRequest.algorithm', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UPDATEALGORITHMREQUEST_ACTIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1339,
  serialized_end=1580,
)

_LISTMDBOVERRIDESRESPONSE.fields_by_name['overrides'].message_type = _MDBOVERRIDEINFO
_GETALGORITHMOVERRIDESRESPONSE.fields_by_name['textOverride'].message_type = _ALGORITHMTEXTOVERRIDE
_MDBOVERRIDEINFO.fields_by_name['type'].enum_type = _MDBOVERRIDEINFO_OVERRIDETYPE
_MDBOVERRIDEINFO.fields_by_name['algorithmTextOverride'].message_type = _ALGORITHMTEXTOVERRIDE
_MDBOVERRIDEINFO_OVERRIDETYPE.containing_type = _MDBOVERRIDEINFO
_UPDATEPARAMETERREQUEST.fields_by_name['action'].enum_type = _UPDATEPARAMETERREQUEST_ACTIONTYPE
_UPDATEPARAMETERREQUEST.fields_by_name['defaultCalibrator'].message_type = yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2._CALIBRATORINFO
_UPDATEPARAMETERREQUEST.fields_by_name['contextCalibrator'].message_type = yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2._CONTEXTCALIBRATORINFO
_UPDATEPARAMETERREQUEST.fields_by_name['defaultAlarm'].message_type = yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2._ALARMINFO
_UPDATEPARAMETERREQUEST.fields_by_name['contextAlarm'].message_type = yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2._CONTEXTALARMINFO
_UPDATEPARAMETERREQUEST_ACTIONTYPE.containing_type = _UPDATEPARAMETERREQUEST
_UPDATEALGORITHMREQUEST.fields_by_name['action'].enum_type = _UPDATEALGORITHMREQUEST_ACTIONTYPE
_UPDATEALGORITHMREQUEST.fields_by_name['algorithm'].message_type = yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2._ALGORITHMINFO
_UPDATEALGORITHMREQUEST_ACTIONTYPE.containing_type = _UPDATEALGORITHMREQUEST
DESCRIPTOR.message_types_by_name['ListMdbOverridesRequest'] = _LISTMDBOVERRIDESREQUEST
DESCRIPTOR.message_types_by_name['ListMdbOverridesResponse'] = _LISTMDBOVERRIDESRESPONSE
DESCRIPTOR.message_types_by_name['GetAlgorithmOverridesRequest'] = _GETALGORITHMOVERRIDESREQUEST
DESCRIPTOR.message_types_by_name['GetAlgorithmOverridesResponse'] = _GETALGORITHMOVERRIDESRESPONSE
DESCRIPTOR.message_types_by_name['MdbOverrideInfo'] = _MDBOVERRIDEINFO
DESCRIPTOR.message_types_by_name['AlgorithmTextOverride'] = _ALGORITHMTEXTOVERRIDE
DESCRIPTOR.message_types_by_name['UpdateParameterRequest'] = _UPDATEPARAMETERREQUEST
DESCRIPTOR.message_types_by_name['UpdateAlgorithmRequest'] = _UPDATEALGORITHMREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListMdbOverridesRequest = _reflection.GeneratedProtocolMessageType('ListMdbOverridesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTMDBOVERRIDESREQUEST,
  __module__ = 'yamcs.protobuf.processing.mdb_override_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.processing.ListMdbOverridesRequest)
  ))
_sym_db.RegisterMessage(ListMdbOverridesRequest)

ListMdbOverridesResponse = _reflection.GeneratedProtocolMessageType('ListMdbOverridesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTMDBOVERRIDESRESPONSE,
  __module__ = 'yamcs.protobuf.processing.mdb_override_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.processing.ListMdbOverridesResponse)
  ))
_sym_db.RegisterMessage(ListMdbOverridesResponse)

GetAlgorithmOverridesRequest = _reflection.GeneratedProtocolMessageType('GetAlgorithmOverridesRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETALGORITHMOVERRIDESREQUEST,
  __module__ = 'yamcs.protobuf.processing.mdb_override_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.processing.GetAlgorithmOverridesRequest)
  ))
_sym_db.RegisterMessage(GetAlgorithmOverridesRequest)

GetAlgorithmOverridesResponse = _reflection.GeneratedProtocolMessageType('GetAlgorithmOverridesResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETALGORITHMOVERRIDESRESPONSE,
  __module__ = 'yamcs.protobuf.processing.mdb_override_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.processing.GetAlgorithmOverridesResponse)
  ))
_sym_db.RegisterMessage(GetAlgorithmOverridesResponse)

MdbOverrideInfo = _reflection.GeneratedProtocolMessageType('MdbOverrideInfo', (_message.Message,), dict(
  DESCRIPTOR = _MDBOVERRIDEINFO,
  __module__ = 'yamcs.protobuf.processing.mdb_override_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.processing.MdbOverrideInfo)
  ))
_sym_db.RegisterMessage(MdbOverrideInfo)

AlgorithmTextOverride = _reflection.GeneratedProtocolMessageType('AlgorithmTextOverride', (_message.Message,), dict(
  DESCRIPTOR = _ALGORITHMTEXTOVERRIDE,
  __module__ = 'yamcs.protobuf.processing.mdb_override_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.processing.AlgorithmTextOverride)
  ))
_sym_db.RegisterMessage(AlgorithmTextOverride)

UpdateParameterRequest = _reflection.GeneratedProtocolMessageType('UpdateParameterRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEPARAMETERREQUEST,
  __module__ = 'yamcs.protobuf.processing.mdb_override_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.processing.UpdateParameterRequest)
  ))
_sym_db.RegisterMessage(UpdateParameterRequest)

UpdateAlgorithmRequest = _reflection.GeneratedProtocolMessageType('UpdateAlgorithmRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEALGORITHMREQUEST,
  __module__ = 'yamcs.protobuf.processing.mdb_override_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.processing.UpdateAlgorithmRequest)
  ))
_sym_db.RegisterMessage(UpdateAlgorithmRequest)


DESCRIPTOR._options = None

_MDBOVERRIDEAPI = _descriptor.ServiceDescriptor(
  name='MdbOverrideApi',
  full_name='yamcs.protobuf.processing.MdbOverrideApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\202\200\001\014MDB Override'),
  serialized_start=1583,
  serialized_end=2462,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListMdbOverrides',
    full_name='yamcs.protobuf.processing.MdbOverrideApi.ListMdbOverrides',
    index=0,
    containing_service=None,
    input_type=_LISTMDBOVERRIDESREQUEST,
    output_type=_LISTMDBOVERRIDESRESPONSE,
    serialized_options=_b('\212\222\003+\n)/api/mdb-overrides/{instance}/{processor}'),
  ),
  _descriptor.MethodDescriptor(
    name='GetAlgorithmOverrides',
    full_name='yamcs.protobuf.processing.MdbOverrideApi.GetAlgorithmOverrides',
    index=1,
    containing_service=None,
    input_type=_GETALGORITHMOVERRIDESREQUEST,
    output_type=_GETALGORITHMOVERRIDESRESPONSE,
    serialized_options=_b('\212\222\003>\n</api/mdb-overrides/{instance}/{processor}/algorithms/{name*}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateParameter',
    full_name='yamcs.protobuf.processing.MdbOverrideApi.UpdateParameter',
    index=2,
    containing_service=None,
    input_type=_UPDATEPARAMETERREQUEST,
    output_type=yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2._PARAMETERTYPEINFO,
    serialized_options=_b('\212\222\003z*</api/mdb-overrides/{instance}/{processor}/parameters/{name*}:\001*Z7*2/api/mdb/{instance}/{processor}/parameters/{name*}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateAlgorithm',
    full_name='yamcs.protobuf.processing.MdbOverrideApi.UpdateAlgorithm',
    index=3,
    containing_service=None,
    input_type=_UPDATEALGORITHMREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\212\222\003z*</api/mdb-overrides/{instance}/{processor}/algorithms/{name*}:\001*Z7*2/api/mdb/{instance}/{processor}/algorithms/{name*}:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_MDBOVERRIDEAPI)

DESCRIPTOR.services_by_name['MdbOverrideApi'] = _MDBOVERRIDEAPI

# @@protoc_insertion_point(module_scope)
