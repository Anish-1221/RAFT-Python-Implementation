# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: raft.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'raft.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nraft.proto\"<\n\x10heartbeatMessage\x12\x13\n\x0bleader_name\x18\x01 \x01(\t\x12\x13\n\x0bleader_port\x18\x02 \x01(\x05\"L\n\nlogMessage\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x13\n\x0binstruction\x18\x04 \x01(\t\".\n\nackMessage\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2a\n\x08RaftNode\x12.\n\x0c\x61\x63kHeartbeat\x12\x11.heartbeatMessage\x1a\x0b.ackMessage\x12%\n\tlogAppend\x12\x0b.logMessage\x1a\x0b.ackMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'raft_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HEARTBEATMESSAGE']._serialized_start=14
  _globals['_HEARTBEATMESSAGE']._serialized_end=74
  _globals['_LOGMESSAGE']._serialized_start=76
  _globals['_LOGMESSAGE']._serialized_end=152
  _globals['_ACKMESSAGE']._serialized_start=154
  _globals['_ACKMESSAGE']._serialized_end=200
  _globals['_RAFTNODE']._serialized_start=202
  _globals['_RAFTNODE']._serialized_end=299
# @@protoc_insertion_point(module_scope)
