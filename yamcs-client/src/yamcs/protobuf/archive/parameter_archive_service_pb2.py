# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/archive/parameter_archive_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yamcs.api import annotations_pb2 as yamcs_dot_api_dot_annotations__pb2
from yamcs.protobuf.archive import archive_pb2 as yamcs_dot_protobuf_dot_archive_dot_archive__pb2
from yamcs.protobuf.pvalue import pvalue_pb2 as yamcs_dot_protobuf_dot_pvalue_dot_pvalue__pb2
from yamcs.protobuf import yamcs_pb2 as yamcs_dot_protobuf_dot_yamcs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/archive/parameter_archive_service.proto',
  package='yamcs.protobuf.archive',
  syntax='proto2',
  serialized_options=_b('\n\022org.yamcs.protobufB\034ParameterArchiveServiceProtoP\001'),
  serialized_pb=_b('\n6yamcs/protobuf/archive/parameter_archive_service.proto\x12\x16yamcs.protobuf.archive\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1byamcs/api/annotations.proto\x1a$yamcs/protobuf/archive/archive.proto\x1a\"yamcs/protobuf/pvalue/pvalue.proto\x1a\x1ayamcs/protobuf/yamcs.proto\"|\n\x13RebuildRangeRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12)\n\x05start\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04stop\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x8c\x02\n\x19GetParameterRangesRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12)\n\x05start\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04stop\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06minGap\x18\x05 \x01(\x03\x12\x0e\n\x06maxGap\x18\x06 \x01(\x03\x12\x12\n\nnorealtime\x18\x07 \x01(\x08\x12\x11\n\tprocessor\x18\x08 \x01(\t\x12\x0e\n\x06source\x18\t \x01(\t\x12\x10\n\x08minRange\x18\n \x01(\x03\x12\x11\n\tmaxValues\x18\x0b \x01(\x05\"^\n GetArchivedParametersInfoRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\t\n\x01q\x18\x02 \x01(\t\x12\x0e\n\x06system\x18\x03 \x01(\t\x12\r\n\x05limit\x18\x07 \x01(\x05\"\x99\x01\n#GetArchivedParameterSegmentsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0b\n\x03pid\x18\x02 \x01(\r\x12)\n\x05start\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04stop\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x99\x01\n\x15\x41rchivedParameterInfo\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x0b\n\x03\x66qn\x18\x02 \x01(\t\x12+\n\x07rawType\x18\x03 \x01(\x0e\x32\x1a.yamcs.protobuf.Value.Type\x12+\n\x07\x65ngType\x18\x04 \x01(\x0e\x32\x1a.yamcs.protobuf.Value.Type\x12\x0c\n\x04gids\x18\x05 \x03(\r\"c\n\x1e\x41rchivedParametersInfoResponse\x12\x41\n\nparameters\x18\x01 \x03(\x0b\x32-.yamcs.protobuf.archive.ArchivedParameterInfo\"\x91\x01\n\x1b\x41rchiveParameterSegmentInfo\x12\x0f\n\x07groupId\x18\x01 \x01(\r\x12)\n\x05start\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05\x63ount\x18\x04 \x01(\r\"\xb0\x01\n!ArchivedParameterSegmentsResponse\x12\x44\n\rparameterInfo\x18\x01 \x01(\x0b\x32-.yamcs.protobuf.archive.ArchivedParameterInfo\x12\x45\n\x08segments\x18\x02 \x03(\x0b\x32\x33.yamcs.protobuf.archive.ArchiveParameterSegmentInfo\"A\n GetArchivedParameterGroupRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0b\n\x03gid\x18\x02 \x01(\r\"p\n\x1e\x41rchivedParameterGroupResponse\x12\x0b\n\x03gid\x18\x01 \x01(\r\x12\x41\n\nparameters\x18\x02 \x03(\x0b\x32-.yamcs.protobuf.archive.ArchivedParameterInfo2\xb9\n\n\x13ParameterArchiveApi\x12\x90\x01\n\x0cRebuildRange\x12+.yamcs.protobuf.archive.RebuildRangeRequest\x1a\x16.google.protobuf.Empty\";\x8a\x92\x03\x37\x1a\x30/api/archive/{instance}/parameterArchive:rebuild:\x01*H\x01\x12\xae\x01\n\x13GetParameterSamples\x12\x32.yamcs.protobuf.archive.GetParameterSamplesRequest\x1a!.yamcs.protobuf.pvalue.TimeSeries\"@\x8a\x92\x03<\n2/api/archive/{instance}/parameters/{name*}/samplesR\x06sample\x12\xa6\x01\n\x12GetParameterRanges\x12\x31.yamcs.protobuf.archive.GetParameterRangesRequest\x1a\x1d.yamcs.protobuf.pvalue.Ranges\">\x8a\x92\x03:\n1/api/archive/{instance}/parameters/{name*}/rangesR\x05range\x12\xb3\x01\n\x14ListParameterHistory\x12\x33.yamcs.protobuf.archive.ListParameterHistoryRequest\x1a\x34.yamcs.protobuf.archive.ListParameterHistoryResponse\"0\x8a\x92\x03,\n*/api/archive/{instance}/parameters/{name*}\x12\xcd\x01\n\x19GetArchivedParametersInfo\x12\x38.yamcs.protobuf.archive.GetArchivedParametersInfoRequest\x1a\x36.yamcs.protobuf.archive.ArchivedParametersInfoResponse\">\x8a\x92\x03:\n8/api/archive/{instance}/parameterArchive/info/parameters\x12\xdb\x01\n\x1cGetArchivedParameterSegments\x12;.yamcs.protobuf.archive.GetArchivedParameterSegmentsRequest\x1a\x39.yamcs.protobuf.archive.ArchivedParameterSegmentsResponse\"C\x8a\x92\x03?\n=/api/archive/{instance}/parameterArchive/info/segments/{pid*}\x12\xd0\x01\n\x19GetArchivedParameterGroup\x12\x38.yamcs.protobuf.archive.GetArchivedParameterGroupRequest\x1a\x36.yamcs.protobuf.archive.ArchivedParameterGroupResponse\"A\x8a\x92\x03=\n;/api/archive/{instance}/parameterArchive/info/groups/{gid*}B4\n\x12org.yamcs.protobufB\x1cParameterArchiveServiceProtoP\x01')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yamcs_dot_api_dot_annotations__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_archive_dot_archive__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_pvalue_dot_pvalue__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_yamcs__pb2.DESCRIPTOR,])




_REBUILDRANGEREQUEST = _descriptor.Descriptor(
  name='RebuildRangeRequest',
  full_name='yamcs.protobuf.archive.RebuildRangeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.archive.RebuildRangeRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.archive.RebuildRangeRequest.start', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.archive.RebuildRangeRequest.stop', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=275,
  serialized_end=399,
)


_GETPARAMETERRANGESREQUEST = _descriptor.Descriptor(
  name='GetParameterRangesRequest',
  full_name='yamcs.protobuf.archive.GetParameterRangesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.start', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.stop', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minGap', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.minGap', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxGap', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.maxGap', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='norealtime', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.norealtime', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processor', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.processor', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.source', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minRange', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.minRange', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxValues', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.maxValues', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=402,
  serialized_end=670,
)


_GETARCHIVEDPARAMETERSINFOREQUEST = _descriptor.Descriptor(
  name='GetArchivedParametersInfoRequest',
  full_name='yamcs.protobuf.archive.GetArchivedParametersInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.archive.GetArchivedParametersInfoRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='q', full_name='yamcs.protobuf.archive.GetArchivedParametersInfoRequest.q', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system', full_name='yamcs.protobuf.archive.GetArchivedParametersInfoRequest.system', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='yamcs.protobuf.archive.GetArchivedParametersInfoRequest.limit', index=3,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=672,
  serialized_end=766,
)


_GETARCHIVEDPARAMETERSEGMENTSREQUEST = _descriptor.Descriptor(
  name='GetArchivedParameterSegmentsRequest',
  full_name='yamcs.protobuf.archive.GetArchivedParameterSegmentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.archive.GetArchivedParameterSegmentsRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pid', full_name='yamcs.protobuf.archive.GetArchivedParameterSegmentsRequest.pid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.archive.GetArchivedParameterSegmentsRequest.start', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.archive.GetArchivedParameterSegmentsRequest.stop', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=769,
  serialized_end=922,
)


_ARCHIVEDPARAMETERINFO = _descriptor.Descriptor(
  name='ArchivedParameterInfo',
  full_name='yamcs.protobuf.archive.ArchivedParameterInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='yamcs.protobuf.archive.ArchivedParameterInfo.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fqn', full_name='yamcs.protobuf.archive.ArchivedParameterInfo.fqn', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rawType', full_name='yamcs.protobuf.archive.ArchivedParameterInfo.rawType', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='engType', full_name='yamcs.protobuf.archive.ArchivedParameterInfo.engType', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gids', full_name='yamcs.protobuf.archive.ArchivedParameterInfo.gids', index=4,
      number=5, type=13, cpp_type=3, label=3,
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
  serialized_start=925,
  serialized_end=1078,
)


_ARCHIVEDPARAMETERSINFORESPONSE = _descriptor.Descriptor(
  name='ArchivedParametersInfoResponse',
  full_name='yamcs.protobuf.archive.ArchivedParametersInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameters', full_name='yamcs.protobuf.archive.ArchivedParametersInfoResponse.parameters', index=0,
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
  serialized_start=1080,
  serialized_end=1179,
)


_ARCHIVEPARAMETERSEGMENTINFO = _descriptor.Descriptor(
  name='ArchiveParameterSegmentInfo',
  full_name='yamcs.protobuf.archive.ArchiveParameterSegmentInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='groupId', full_name='yamcs.protobuf.archive.ArchiveParameterSegmentInfo.groupId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.archive.ArchiveParameterSegmentInfo.start', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='yamcs.protobuf.archive.ArchiveParameterSegmentInfo.end', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='yamcs.protobuf.archive.ArchiveParameterSegmentInfo.count', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1182,
  serialized_end=1327,
)


_ARCHIVEDPARAMETERSEGMENTSRESPONSE = _descriptor.Descriptor(
  name='ArchivedParameterSegmentsResponse',
  full_name='yamcs.protobuf.archive.ArchivedParameterSegmentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameterInfo', full_name='yamcs.protobuf.archive.ArchivedParameterSegmentsResponse.parameterInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='segments', full_name='yamcs.protobuf.archive.ArchivedParameterSegmentsResponse.segments', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1330,
  serialized_end=1506,
)


_GETARCHIVEDPARAMETERGROUPREQUEST = _descriptor.Descriptor(
  name='GetArchivedParameterGroupRequest',
  full_name='yamcs.protobuf.archive.GetArchivedParameterGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.archive.GetArchivedParameterGroupRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gid', full_name='yamcs.protobuf.archive.GetArchivedParameterGroupRequest.gid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1508,
  serialized_end=1573,
)


_ARCHIVEDPARAMETERGROUPRESPONSE = _descriptor.Descriptor(
  name='ArchivedParameterGroupResponse',
  full_name='yamcs.protobuf.archive.ArchivedParameterGroupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gid', full_name='yamcs.protobuf.archive.ArchivedParameterGroupResponse.gid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='yamcs.protobuf.archive.ArchivedParameterGroupResponse.parameters', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1575,
  serialized_end=1687,
)

_REBUILDRANGEREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REBUILDRANGEREQUEST.fields_by_name['stop'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETPARAMETERRANGESREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETPARAMETERRANGESREQUEST.fields_by_name['stop'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETARCHIVEDPARAMETERSEGMENTSREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETARCHIVEDPARAMETERSEGMENTSREQUEST.fields_by_name['stop'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ARCHIVEDPARAMETERINFO.fields_by_name['rawType'].enum_type = yamcs_dot_protobuf_dot_yamcs__pb2._VALUE_TYPE
_ARCHIVEDPARAMETERINFO.fields_by_name['engType'].enum_type = yamcs_dot_protobuf_dot_yamcs__pb2._VALUE_TYPE
_ARCHIVEDPARAMETERSINFORESPONSE.fields_by_name['parameters'].message_type = _ARCHIVEDPARAMETERINFO
_ARCHIVEPARAMETERSEGMENTINFO.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ARCHIVEPARAMETERSEGMENTINFO.fields_by_name['end'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ARCHIVEDPARAMETERSEGMENTSRESPONSE.fields_by_name['parameterInfo'].message_type = _ARCHIVEDPARAMETERINFO
_ARCHIVEDPARAMETERSEGMENTSRESPONSE.fields_by_name['segments'].message_type = _ARCHIVEPARAMETERSEGMENTINFO
_ARCHIVEDPARAMETERGROUPRESPONSE.fields_by_name['parameters'].message_type = _ARCHIVEDPARAMETERINFO
DESCRIPTOR.message_types_by_name['RebuildRangeRequest'] = _REBUILDRANGEREQUEST
DESCRIPTOR.message_types_by_name['GetParameterRangesRequest'] = _GETPARAMETERRANGESREQUEST
DESCRIPTOR.message_types_by_name['GetArchivedParametersInfoRequest'] = _GETARCHIVEDPARAMETERSINFOREQUEST
DESCRIPTOR.message_types_by_name['GetArchivedParameterSegmentsRequest'] = _GETARCHIVEDPARAMETERSEGMENTSREQUEST
DESCRIPTOR.message_types_by_name['ArchivedParameterInfo'] = _ARCHIVEDPARAMETERINFO
DESCRIPTOR.message_types_by_name['ArchivedParametersInfoResponse'] = _ARCHIVEDPARAMETERSINFORESPONSE
DESCRIPTOR.message_types_by_name['ArchiveParameterSegmentInfo'] = _ARCHIVEPARAMETERSEGMENTINFO
DESCRIPTOR.message_types_by_name['ArchivedParameterSegmentsResponse'] = _ARCHIVEDPARAMETERSEGMENTSRESPONSE
DESCRIPTOR.message_types_by_name['GetArchivedParameterGroupRequest'] = _GETARCHIVEDPARAMETERGROUPREQUEST
DESCRIPTOR.message_types_by_name['ArchivedParameterGroupResponse'] = _ARCHIVEDPARAMETERGROUPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RebuildRangeRequest = _reflection.GeneratedProtocolMessageType('RebuildRangeRequest', (_message.Message,), dict(
  DESCRIPTOR = _REBUILDRANGEREQUEST,
  __module__ = 'yamcs.protobuf.archive.parameter_archive_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.RebuildRangeRequest)
  ))
_sym_db.RegisterMessage(RebuildRangeRequest)

GetParameterRangesRequest = _reflection.GeneratedProtocolMessageType('GetParameterRangesRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPARAMETERRANGESREQUEST,
  __module__ = 'yamcs.protobuf.archive.parameter_archive_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.GetParameterRangesRequest)
  ))
_sym_db.RegisterMessage(GetParameterRangesRequest)

GetArchivedParametersInfoRequest = _reflection.GeneratedProtocolMessageType('GetArchivedParametersInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETARCHIVEDPARAMETERSINFOREQUEST,
  __module__ = 'yamcs.protobuf.archive.parameter_archive_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.GetArchivedParametersInfoRequest)
  ))
_sym_db.RegisterMessage(GetArchivedParametersInfoRequest)

GetArchivedParameterSegmentsRequest = _reflection.GeneratedProtocolMessageType('GetArchivedParameterSegmentsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETARCHIVEDPARAMETERSEGMENTSREQUEST,
  __module__ = 'yamcs.protobuf.archive.parameter_archive_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.GetArchivedParameterSegmentsRequest)
  ))
_sym_db.RegisterMessage(GetArchivedParameterSegmentsRequest)

ArchivedParameterInfo = _reflection.GeneratedProtocolMessageType('ArchivedParameterInfo', (_message.Message,), dict(
  DESCRIPTOR = _ARCHIVEDPARAMETERINFO,
  __module__ = 'yamcs.protobuf.archive.parameter_archive_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.ArchivedParameterInfo)
  ))
_sym_db.RegisterMessage(ArchivedParameterInfo)

ArchivedParametersInfoResponse = _reflection.GeneratedProtocolMessageType('ArchivedParametersInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _ARCHIVEDPARAMETERSINFORESPONSE,
  __module__ = 'yamcs.protobuf.archive.parameter_archive_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.ArchivedParametersInfoResponse)
  ))
_sym_db.RegisterMessage(ArchivedParametersInfoResponse)

ArchiveParameterSegmentInfo = _reflection.GeneratedProtocolMessageType('ArchiveParameterSegmentInfo', (_message.Message,), dict(
  DESCRIPTOR = _ARCHIVEPARAMETERSEGMENTINFO,
  __module__ = 'yamcs.protobuf.archive.parameter_archive_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.ArchiveParameterSegmentInfo)
  ))
_sym_db.RegisterMessage(ArchiveParameterSegmentInfo)

ArchivedParameterSegmentsResponse = _reflection.GeneratedProtocolMessageType('ArchivedParameterSegmentsResponse', (_message.Message,), dict(
  DESCRIPTOR = _ARCHIVEDPARAMETERSEGMENTSRESPONSE,
  __module__ = 'yamcs.protobuf.archive.parameter_archive_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.ArchivedParameterSegmentsResponse)
  ))
_sym_db.RegisterMessage(ArchivedParameterSegmentsResponse)

GetArchivedParameterGroupRequest = _reflection.GeneratedProtocolMessageType('GetArchivedParameterGroupRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETARCHIVEDPARAMETERGROUPREQUEST,
  __module__ = 'yamcs.protobuf.archive.parameter_archive_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.GetArchivedParameterGroupRequest)
  ))
_sym_db.RegisterMessage(GetArchivedParameterGroupRequest)

ArchivedParameterGroupResponse = _reflection.GeneratedProtocolMessageType('ArchivedParameterGroupResponse', (_message.Message,), dict(
  DESCRIPTOR = _ARCHIVEDPARAMETERGROUPRESPONSE,
  __module__ = 'yamcs.protobuf.archive.parameter_archive_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.ArchivedParameterGroupResponse)
  ))
_sym_db.RegisterMessage(ArchivedParameterGroupResponse)


DESCRIPTOR._options = None

_PARAMETERARCHIVEAPI = _descriptor.ServiceDescriptor(
  name='ParameterArchiveApi',
  full_name='yamcs.protobuf.archive.ParameterArchiveApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1690,
  serialized_end=3027,
  methods=[
  _descriptor.MethodDescriptor(
    name='RebuildRange',
    full_name='yamcs.protobuf.archive.ParameterArchiveApi.RebuildRange',
    index=0,
    containing_service=None,
    input_type=_REBUILDRANGEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\212\222\0037\0320/api/archive/{instance}/parameterArchive:rebuild:\001*H\001'),
  ),
  _descriptor.MethodDescriptor(
    name='GetParameterSamples',
    full_name='yamcs.protobuf.archive.ParameterArchiveApi.GetParameterSamples',
    index=1,
    containing_service=None,
    input_type=yamcs_dot_protobuf_dot_archive_dot_archive__pb2._GETPARAMETERSAMPLESREQUEST,
    output_type=yamcs_dot_protobuf_dot_pvalue_dot_pvalue__pb2._TIMESERIES,
    serialized_options=_b('\212\222\003<\n2/api/archive/{instance}/parameters/{name*}/samplesR\006sample'),
  ),
  _descriptor.MethodDescriptor(
    name='GetParameterRanges',
    full_name='yamcs.protobuf.archive.ParameterArchiveApi.GetParameterRanges',
    index=2,
    containing_service=None,
    input_type=_GETPARAMETERRANGESREQUEST,
    output_type=yamcs_dot_protobuf_dot_pvalue_dot_pvalue__pb2._RANGES,
    serialized_options=_b('\212\222\003:\n1/api/archive/{instance}/parameters/{name*}/rangesR\005range'),
  ),
  _descriptor.MethodDescriptor(
    name='ListParameterHistory',
    full_name='yamcs.protobuf.archive.ParameterArchiveApi.ListParameterHistory',
    index=3,
    containing_service=None,
    input_type=yamcs_dot_protobuf_dot_archive_dot_archive__pb2._LISTPARAMETERHISTORYREQUEST,
    output_type=yamcs_dot_protobuf_dot_archive_dot_archive__pb2._LISTPARAMETERHISTORYRESPONSE,
    serialized_options=_b('\212\222\003,\n*/api/archive/{instance}/parameters/{name*}'),
  ),
  _descriptor.MethodDescriptor(
    name='GetArchivedParametersInfo',
    full_name='yamcs.protobuf.archive.ParameterArchiveApi.GetArchivedParametersInfo',
    index=4,
    containing_service=None,
    input_type=_GETARCHIVEDPARAMETERSINFOREQUEST,
    output_type=_ARCHIVEDPARAMETERSINFORESPONSE,
    serialized_options=_b('\212\222\003:\n8/api/archive/{instance}/parameterArchive/info/parameters'),
  ),
  _descriptor.MethodDescriptor(
    name='GetArchivedParameterSegments',
    full_name='yamcs.protobuf.archive.ParameterArchiveApi.GetArchivedParameterSegments',
    index=5,
    containing_service=None,
    input_type=_GETARCHIVEDPARAMETERSEGMENTSREQUEST,
    output_type=_ARCHIVEDPARAMETERSEGMENTSRESPONSE,
    serialized_options=_b('\212\222\003?\n=/api/archive/{instance}/parameterArchive/info/segments/{pid*}'),
  ),
  _descriptor.MethodDescriptor(
    name='GetArchivedParameterGroup',
    full_name='yamcs.protobuf.archive.ParameterArchiveApi.GetArchivedParameterGroup',
    index=6,
    containing_service=None,
    input_type=_GETARCHIVEDPARAMETERGROUPREQUEST,
    output_type=_ARCHIVEDPARAMETERGROUPRESPONSE,
    serialized_options=_b('\212\222\003=\n;/api/archive/{instance}/parameterArchive/info/groups/{gid*}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_PARAMETERARCHIVEAPI)

DESCRIPTOR.services_by_name['ParameterArchiveApi'] = _PARAMETERARCHIVEAPI

# @@protoc_insertion_point(module_scope)
