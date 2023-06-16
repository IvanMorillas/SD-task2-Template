# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: KVStore/protos/kv-store.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dKVStore/protos/kv-store.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x19\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\r\"+\n\x0bGetResponse\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_value\"(\n\nPutRequest\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t\"+\n\rAppendRequest\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t\"W\n\x13RedistributeRequest\x12\x1a\n\x12\x64\x65stination_server\x18\x01 \x01(\t\x12\x11\n\tlower_val\x18\x02 \x01(\r\x12\x11\n\tupper_val\x18\x03 \x01(\r\"&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t\"1\n\x0fTransferRequest\x12\x1e\n\x0bkeys_values\x18\x01 \x03(\x0b\x32\t.KeyValue\"\x1f\n\rServerRequest\x12\x0e\n\x06server\x18\x01 \x01(\t\"\r\n\x0bLockRequest\"\x10\n\x0eReleaseRequest2\xb8\x04\n\x07KVStore\x12\"\n\x03Get\x12\x0b.GetRequest\x1a\x0c.GetResponse\"\x00\x12#\n\x04LPop\x12\x0b.GetRequest\x1a\x0c.GetResponse\"\x00\x12#\n\x04RPop\x12\x0b.GetRequest\x1a\x0c.GetResponse\"\x00\x12,\n\x03Put\x12\x0b.PutRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x32\n\x06\x41ppend\x12\x0e.AppendRequest\x1a\x16.google.protobuf.Empty\"\x00\x12>\n\x0cRedistribute\x12\x14.RedistributeRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x36\n\x08Transfer\x12\x10.TransferRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x36\n\nAddReplica\x12\x0e.ServerRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x39\n\rRemoveReplica\x12\x0e.ServerRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x35\n\x0bLockReplica\x12\x0c.LockRequest\x1a\x16.google.protobuf.Empty\"\x00\x12;\n\x0eReleaseReplica\x12\x0f.ReleaseRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'KVStore.protos.kv_store_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETREQUEST._serialized_start=62
  _GETREQUEST._serialized_end=87
  _GETRESPONSE._serialized_start=89
  _GETRESPONSE._serialized_end=132
  _PUTREQUEST._serialized_start=134
  _PUTREQUEST._serialized_end=174
  _APPENDREQUEST._serialized_start=176
  _APPENDREQUEST._serialized_end=219
  _REDISTRIBUTEREQUEST._serialized_start=221
  _REDISTRIBUTEREQUEST._serialized_end=308
  _KEYVALUE._serialized_start=310
  _KEYVALUE._serialized_end=348
  _TRANSFERREQUEST._serialized_start=350
  _TRANSFERREQUEST._serialized_end=399
  _SERVERREQUEST._serialized_start=401
  _SERVERREQUEST._serialized_end=432
  _LOCKREQUEST._serialized_start=434
  _LOCKREQUEST._serialized_end=447
  _RELEASEREQUEST._serialized_start=449
  _RELEASEREQUEST._serialized_end=465
  _KVSTORE._serialized_start=468
  _KVSTORE._serialized_end=1036
# @@protoc_insertion_point(module_scope)