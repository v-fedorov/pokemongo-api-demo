# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gyms.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gyms.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\ngyms.proto\"\x87\x05\n\x11RequestEnvelopGym\x12\x10\n\x08unknown1\x18\x01 \x02(\x05\x12\x0e\n\x06rpc_id\x18\x03 \x01(\x03\x12-\n\x08requests\x18\x04 \x03(\x0b\x32\x1b.RequestEnvelopGym.Requests\x12-\n\x08unknown6\x18\x06 \x01(\x0b\x32\x1b.RequestEnvelopGym.Unknown6\x12\x10\n\x08latitude\x18\x07 \x01(\x06\x12\x11\n\tlongitude\x18\x08 \x01(\x06\x12\x10\n\x08\x61ltitude\x18\t \x01(\x06\x12)\n\x04\x61uth\x18\n \x01(\x0b\x32\x1b.RequestEnvelopGym.AuthInfo\x12\x11\n\tunknown12\x18\x0c \x01(\x03\x1a)\n\x08Requests\x12\x0c\n\x04type\x18\x01 \x02(\x05\x12\x0f\n\x07message\x18\x02 \x01(\x0c\x1a\x19\n\x08\x66our2int\x12\r\n\x05value\x18\x01 \x01(\x04\x1aI\n\x0b\x66our2string\x12\x11\n\x05\x63\x65lls\x18\x01 \x03(\x04\x42\x02\x10\x01\x12\r\n\x05\x64unno\x18\x02 \x01(\x06\x12\x0b\n\x03lat\x18\x03 \x01(\x06\x12\x0b\n\x03lon\x18\x04 \x01(\x06\x1ar\n\x08Unknown6\x12\x10\n\x08unknown1\x18\x01 \x02(\x05\x12\x36\n\x08unknown2\x18\x02 \x02(\x0b\x32$.RequestEnvelopGym.Unknown6.Unknown2\x1a\x1c\n\x08Unknown2\x12\x10\n\x08unknown1\x18\x01 \x02(\x0c\x1ax\n\x08\x41uthInfo\x12\x10\n\x08provider\x18\x01 \x02(\t\x12.\n\x05token\x18\x02 \x02(\x0b\x32\x1f.RequestEnvelopGym.AuthInfo.JWT\x1a*\n\x03JWT\x12\x10\n\x08\x63ontents\x18\x01 \x02(\t\x12\x11\n\tunknown13\x18\x02 \x02(\x05\"\xf0\x05\n\x12ResponseEnvelopGym\x12\x10\n\x08unknown1\x18\x01 \x02(\x05\x12\x10\n\x08unknown2\x18\x02 \x01(\x03\x12\x0f\n\x07\x61pi_url\x18\x03 \x01(\t\x12.\n\x08unknown6\x18\x06 \x01(\x0b\x32\x1c.ResponseEnvelopGym.Unknown6\x12.\n\x08unknown7\x18\x07 \x01(\x0b\x32\x1c.ResponseEnvelopGym.Unknown7\x12,\n\x07payload\x18\x64 \x03(\x0b\x32\x1b.ResponseEnvelopGym.Payload\x1as\n\x08Unknown6\x12\x10\n\x08unknown1\x18\x01 \x02(\x05\x12\x37\n\x08unknown2\x18\x02 \x02(\x0b\x32%.ResponseEnvelopGym.Unknown6.Unknown2\x1a\x1c\n\x08Unknown2\x12\x10\n\x08unknown1\x18\x01 \x02(\x0c\x1a\x43\n\x08Unknown7\x12\x11\n\tunknown71\x18\x01 \x01(\x0c\x12\x11\n\tunknown72\x18\x02 \x01(\x03\x12\x11\n\tunknown73\x18\x03 \x01(\x0c\x1a@\n\x07Payload\x12\x35\n\x05\x63\x65lls\x18\x01 \x03(\x0b\x32&.ResponseEnvelopGym.ClientMapCellProto\x1a\x9a\x02\n\x12\x43lientMapCellProto\x12\x10\n\x08S2CellId\x18\x01 \x01(\x04\x12\x12\n\nAsOfTimeMs\x18\x02 \x01(\x03\x12\x45\n\x04\x46ort\x18\x03 \x03(\x0b\x32\x37.ResponseEnvelopGym.ClientMapCellProto.PokemonFortProto\x1a\x96\x01\n\x10PokemonFortProto\x12\x0e\n\x06\x46ortId\x18\x01 \x01(\t\x12\x16\n\x0eLastModifiedMs\x18\x02 \x01(\x03\x12\x10\n\x08Latitude\x18\x03 \x01(\x06\x12\x11\n\tLongitude\x18\x04 \x01(\x06\x12\x0f\n\x07\x45nabled\x18\x08 \x01(\x05\x12\x12\n\nIsInBattle\x18\x0b \x01(\x05\x12\x10\n\x08\x46ortType\x18\t \x01(\x05*>\n\x10\x43ustom_TeamColor\x12\x0b\n\x07NEUTRAL\x10\x00\x12\x08\n\x04\x42LUE\x10\x01\x12\x07\n\x03RED\x10\x02\x12\n\n\x06YELLOW\x10\x03*#\n\x08\x46ortType\x12\x07\n\x03GYM\x10\x00\x12\x0e\n\nCHECKPOINT\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CUSTOM_TEAMCOLOR = _descriptor.EnumDescriptor(
  name='Custom_TeamColor',
  full_name='Custom_TeamColor',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NEUTRAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLUE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YELLOW', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1419,
  serialized_end=1481,
)
_sym_db.RegisterEnumDescriptor(_CUSTOM_TEAMCOLOR)

Custom_TeamColor = enum_type_wrapper.EnumTypeWrapper(_CUSTOM_TEAMCOLOR)
_FORTTYPE = _descriptor.EnumDescriptor(
  name='FortType',
  full_name='FortType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GYM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECKPOINT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1483,
  serialized_end=1518,
)
_sym_db.RegisterEnumDescriptor(_FORTTYPE)

FortType = enum_type_wrapper.EnumTypeWrapper(_FORTTYPE)
NEUTRAL = 0
BLUE = 1
RED = 2
YELLOW = 3
GYM = 0
CHECKPOINT = 1



_REQUESTENVELOPGYM_REQUESTS = _descriptor.Descriptor(
  name='Requests',
  full_name='RequestEnvelopGym.Requests',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='RequestEnvelopGym.Requests.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='RequestEnvelopGym.Requests.message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=322,
)

_REQUESTENVELOPGYM_FOUR2INT = _descriptor.Descriptor(
  name='four2int',
  full_name='RequestEnvelopGym.four2int',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='RequestEnvelopGym.four2int.value', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=349,
)

_REQUESTENVELOPGYM_FOUR2STRING = _descriptor.Descriptor(
  name='four2string',
  full_name='RequestEnvelopGym.four2string',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cells', full_name='RequestEnvelopGym.four2string.cells', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='dunno', full_name='RequestEnvelopGym.four2string.dunno', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat', full_name='RequestEnvelopGym.four2string.lat', index=2,
      number=3, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lon', full_name='RequestEnvelopGym.four2string.lon', index=3,
      number=4, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=424,
)

_REQUESTENVELOPGYM_UNKNOWN6_UNKNOWN2 = _descriptor.Descriptor(
  name='Unknown2',
  full_name='RequestEnvelopGym.Unknown6.Unknown2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='RequestEnvelopGym.Unknown6.Unknown2.unknown1', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=512,
  serialized_end=540,
)

_REQUESTENVELOPGYM_UNKNOWN6 = _descriptor.Descriptor(
  name='Unknown6',
  full_name='RequestEnvelopGym.Unknown6',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='RequestEnvelopGym.Unknown6.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='RequestEnvelopGym.Unknown6.unknown2', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOPGYM_UNKNOWN6_UNKNOWN2, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=540,
)

_REQUESTENVELOPGYM_AUTHINFO_JWT = _descriptor.Descriptor(
  name='JWT',
  full_name='RequestEnvelopGym.AuthInfo.JWT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contents', full_name='RequestEnvelopGym.AuthInfo.JWT.contents', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown13', full_name='RequestEnvelopGym.AuthInfo.JWT.unknown13', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=620,
  serialized_end=662,
)

_REQUESTENVELOPGYM_AUTHINFO = _descriptor.Descriptor(
  name='AuthInfo',
  full_name='RequestEnvelopGym.AuthInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='RequestEnvelopGym.AuthInfo.provider', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='RequestEnvelopGym.AuthInfo.token', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOPGYM_AUTHINFO_JWT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=542,
  serialized_end=662,
)

_REQUESTENVELOPGYM = _descriptor.Descriptor(
  name='RequestEnvelopGym',
  full_name='RequestEnvelopGym',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='RequestEnvelopGym.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpc_id', full_name='RequestEnvelopGym.rpc_id', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requests', full_name='RequestEnvelopGym.requests', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown6', full_name='RequestEnvelopGym.unknown6', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='RequestEnvelopGym.latitude', index=4,
      number=7, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='RequestEnvelopGym.longitude', index=5,
      number=8, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='RequestEnvelopGym.altitude', index=6,
      number=9, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth', full_name='RequestEnvelopGym.auth', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown12', full_name='RequestEnvelopGym.unknown12', index=8,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOPGYM_REQUESTS, _REQUESTENVELOPGYM_FOUR2INT, _REQUESTENVELOPGYM_FOUR2STRING, _REQUESTENVELOPGYM_UNKNOWN6, _REQUESTENVELOPGYM_AUTHINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=662,
)


_RESPONSEENVELOPGYM_UNKNOWN6_UNKNOWN2 = _descriptor.Descriptor(
  name='Unknown2',
  full_name='ResponseEnvelopGym.Unknown6.Unknown2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='ResponseEnvelopGym.Unknown6.Unknown2.unknown1', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=512,
  serialized_end=540,
)

_RESPONSEENVELOPGYM_UNKNOWN6 = _descriptor.Descriptor(
  name='Unknown6',
  full_name='ResponseEnvelopGym.Unknown6',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='ResponseEnvelopGym.Unknown6.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='ResponseEnvelopGym.Unknown6.unknown2', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSEENVELOPGYM_UNKNOWN6_UNKNOWN2, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=882,
  serialized_end=997,
)

_RESPONSEENVELOPGYM_UNKNOWN7 = _descriptor.Descriptor(
  name='Unknown7',
  full_name='ResponseEnvelopGym.Unknown7',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown71', full_name='ResponseEnvelopGym.Unknown7.unknown71', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown72', full_name='ResponseEnvelopGym.Unknown7.unknown72', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown73', full_name='ResponseEnvelopGym.Unknown7.unknown73', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=999,
  serialized_end=1066,
)

_RESPONSEENVELOPGYM_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='ResponseEnvelopGym.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cells', full_name='ResponseEnvelopGym.Payload.cells', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1068,
  serialized_end=1132,
)

_RESPONSEENVELOPGYM_CLIENTMAPCELLPROTO_POKEMONFORTPROTO = _descriptor.Descriptor(
  name='PokemonFortProto',
  full_name='ResponseEnvelopGym.ClientMapCellProto.PokemonFortProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FortId', full_name='ResponseEnvelopGym.ClientMapCellProto.PokemonFortProto.FortId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LastModifiedMs', full_name='ResponseEnvelopGym.ClientMapCellProto.PokemonFortProto.LastModifiedMs', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Latitude', full_name='ResponseEnvelopGym.ClientMapCellProto.PokemonFortProto.Latitude', index=2,
      number=3, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Longitude', full_name='ResponseEnvelopGym.ClientMapCellProto.PokemonFortProto.Longitude', index=3,
      number=4, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Enabled', full_name='ResponseEnvelopGym.ClientMapCellProto.PokemonFortProto.Enabled', index=4,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IsInBattle', full_name='ResponseEnvelopGym.ClientMapCellProto.PokemonFortProto.IsInBattle', index=5,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FortType', full_name='ResponseEnvelopGym.ClientMapCellProto.PokemonFortProto.FortType', index=6,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1267,
  serialized_end=1417,
)

_RESPONSEENVELOPGYM_CLIENTMAPCELLPROTO = _descriptor.Descriptor(
  name='ClientMapCellProto',
  full_name='ResponseEnvelopGym.ClientMapCellProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='S2CellId', full_name='ResponseEnvelopGym.ClientMapCellProto.S2CellId', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AsOfTimeMs', full_name='ResponseEnvelopGym.ClientMapCellProto.AsOfTimeMs', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Fort', full_name='ResponseEnvelopGym.ClientMapCellProto.Fort', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSEENVELOPGYM_CLIENTMAPCELLPROTO_POKEMONFORTPROTO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1135,
  serialized_end=1417,
)

_RESPONSEENVELOPGYM = _descriptor.Descriptor(
  name='ResponseEnvelopGym',
  full_name='ResponseEnvelopGym',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='ResponseEnvelopGym.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='ResponseEnvelopGym.unknown2', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='api_url', full_name='ResponseEnvelopGym.api_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown6', full_name='ResponseEnvelopGym.unknown6', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown7', full_name='ResponseEnvelopGym.unknown7', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='ResponseEnvelopGym.payload', index=5,
      number=100, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSEENVELOPGYM_UNKNOWN6, _RESPONSEENVELOPGYM_UNKNOWN7, _RESPONSEENVELOPGYM_PAYLOAD, _RESPONSEENVELOPGYM_CLIENTMAPCELLPROTO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=665,
  serialized_end=1417,
)

_REQUESTENVELOPGYM_REQUESTS.containing_type = _REQUESTENVELOPGYM
_REQUESTENVELOPGYM_FOUR2INT.containing_type = _REQUESTENVELOPGYM
_REQUESTENVELOPGYM_FOUR2STRING.containing_type = _REQUESTENVELOPGYM
_REQUESTENVELOPGYM_UNKNOWN6_UNKNOWN2.containing_type = _REQUESTENVELOPGYM_UNKNOWN6
_REQUESTENVELOPGYM_UNKNOWN6.fields_by_name['unknown2'].message_type = _REQUESTENVELOPGYM_UNKNOWN6_UNKNOWN2
_REQUESTENVELOPGYM_UNKNOWN6.containing_type = _REQUESTENVELOPGYM
_REQUESTENVELOPGYM_AUTHINFO_JWT.containing_type = _REQUESTENVELOPGYM_AUTHINFO
_REQUESTENVELOPGYM_AUTHINFO.fields_by_name['token'].message_type = _REQUESTENVELOPGYM_AUTHINFO_JWT
_REQUESTENVELOPGYM_AUTHINFO.containing_type = _REQUESTENVELOPGYM
_REQUESTENVELOPGYM.fields_by_name['requests'].message_type = _REQUESTENVELOPGYM_REQUESTS
_REQUESTENVELOPGYM.fields_by_name['unknown6'].message_type = _REQUESTENVELOPGYM_UNKNOWN6
_REQUESTENVELOPGYM.fields_by_name['auth'].message_type = _REQUESTENVELOPGYM_AUTHINFO
_RESPONSEENVELOPGYM_UNKNOWN6_UNKNOWN2.containing_type = _RESPONSEENVELOPGYM_UNKNOWN6
_RESPONSEENVELOPGYM_UNKNOWN6.fields_by_name['unknown2'].message_type = _RESPONSEENVELOPGYM_UNKNOWN6_UNKNOWN2
_RESPONSEENVELOPGYM_UNKNOWN6.containing_type = _RESPONSEENVELOPGYM
_RESPONSEENVELOPGYM_UNKNOWN7.containing_type = _RESPONSEENVELOPGYM
_RESPONSEENVELOPGYM_PAYLOAD.fields_by_name['cells'].message_type = _RESPONSEENVELOPGYM_CLIENTMAPCELLPROTO
_RESPONSEENVELOPGYM_PAYLOAD.containing_type = _RESPONSEENVELOPGYM
_RESPONSEENVELOPGYM_CLIENTMAPCELLPROTO_POKEMONFORTPROTO.containing_type = _RESPONSEENVELOPGYM_CLIENTMAPCELLPROTO
_RESPONSEENVELOPGYM_CLIENTMAPCELLPROTO.fields_by_name['Fort'].message_type = _RESPONSEENVELOPGYM_CLIENTMAPCELLPROTO_POKEMONFORTPROTO
_RESPONSEENVELOPGYM_CLIENTMAPCELLPROTO.containing_type = _RESPONSEENVELOPGYM
_RESPONSEENVELOPGYM.fields_by_name['unknown6'].message_type = _RESPONSEENVELOPGYM_UNKNOWN6
_RESPONSEENVELOPGYM.fields_by_name['unknown7'].message_type = _RESPONSEENVELOPGYM_UNKNOWN7
_RESPONSEENVELOPGYM.fields_by_name['payload'].message_type = _RESPONSEENVELOPGYM_PAYLOAD
DESCRIPTOR.message_types_by_name['RequestEnvelopGym'] = _REQUESTENVELOPGYM
DESCRIPTOR.message_types_by_name['ResponseEnvelopGym'] = _RESPONSEENVELOPGYM
DESCRIPTOR.enum_types_by_name['Custom_TeamColor'] = _CUSTOM_TEAMCOLOR
DESCRIPTOR.enum_types_by_name['FortType'] = _FORTTYPE

RequestEnvelopGym = _reflection.GeneratedProtocolMessageType('RequestEnvelopGym', (_message.Message,), dict(

  Requests = _reflection.GeneratedProtocolMessageType('Requests', (_message.Message,), dict(
    DESCRIPTOR = _REQUESTENVELOPGYM_REQUESTS,
    __module__ = 'gyms_pb2'
    # @@protoc_insertion_point(class_scope:RequestEnvelopGym.Requests)
    ))
  ,

  four2int = _reflection.GeneratedProtocolMessageType('four2int', (_message.Message,), dict(
    DESCRIPTOR = _REQUESTENVELOPGYM_FOUR2INT,
    __module__ = 'gyms_pb2'
    # @@protoc_insertion_point(class_scope:RequestEnvelopGym.four2int)
    ))
  ,

  four2string = _reflection.GeneratedProtocolMessageType('four2string', (_message.Message,), dict(
    DESCRIPTOR = _REQUESTENVELOPGYM_FOUR2STRING,
    __module__ = 'gyms_pb2'
    # @@protoc_insertion_point(class_scope:RequestEnvelopGym.four2string)
    ))
  ,

  Unknown6 = _reflection.GeneratedProtocolMessageType('Unknown6', (_message.Message,), dict(

    Unknown2 = _reflection.GeneratedProtocolMessageType('Unknown2', (_message.Message,), dict(
      DESCRIPTOR = _REQUESTENVELOPGYM_UNKNOWN6_UNKNOWN2,
      __module__ = 'gyms_pb2'
      # @@protoc_insertion_point(class_scope:RequestEnvelopGym.Unknown6.Unknown2)
      ))
    ,
    DESCRIPTOR = _REQUESTENVELOPGYM_UNKNOWN6,
    __module__ = 'gyms_pb2'
    # @@protoc_insertion_point(class_scope:RequestEnvelopGym.Unknown6)
    ))
  ,

  AuthInfo = _reflection.GeneratedProtocolMessageType('AuthInfo', (_message.Message,), dict(

    JWT = _reflection.GeneratedProtocolMessageType('JWT', (_message.Message,), dict(
      DESCRIPTOR = _REQUESTENVELOPGYM_AUTHINFO_JWT,
      __module__ = 'gyms_pb2'
      # @@protoc_insertion_point(class_scope:RequestEnvelopGym.AuthInfo.JWT)
      ))
    ,
    DESCRIPTOR = _REQUESTENVELOPGYM_AUTHINFO,
    __module__ = 'gyms_pb2'
    # @@protoc_insertion_point(class_scope:RequestEnvelopGym.AuthInfo)
    ))
  ,
  DESCRIPTOR = _REQUESTENVELOPGYM,
  __module__ = 'gyms_pb2'
  # @@protoc_insertion_point(class_scope:RequestEnvelopGym)
  ))
_sym_db.RegisterMessage(RequestEnvelopGym)
_sym_db.RegisterMessage(RequestEnvelopGym.Requests)
_sym_db.RegisterMessage(RequestEnvelopGym.four2int)
_sym_db.RegisterMessage(RequestEnvelopGym.four2string)
_sym_db.RegisterMessage(RequestEnvelopGym.Unknown6)
_sym_db.RegisterMessage(RequestEnvelopGym.Unknown6.Unknown2)
_sym_db.RegisterMessage(RequestEnvelopGym.AuthInfo)
_sym_db.RegisterMessage(RequestEnvelopGym.AuthInfo.JWT)

ResponseEnvelopGym = _reflection.GeneratedProtocolMessageType('ResponseEnvelopGym', (_message.Message,), dict(

  Unknown6 = _reflection.GeneratedProtocolMessageType('Unknown6', (_message.Message,), dict(

    Unknown2 = _reflection.GeneratedProtocolMessageType('Unknown2', (_message.Message,), dict(
      DESCRIPTOR = _RESPONSEENVELOPGYM_UNKNOWN6_UNKNOWN2,
      __module__ = 'gyms_pb2'
      # @@protoc_insertion_point(class_scope:ResponseEnvelopGym.Unknown6.Unknown2)
      ))
    ,
    DESCRIPTOR = _RESPONSEENVELOPGYM_UNKNOWN6,
    __module__ = 'gyms_pb2'
    # @@protoc_insertion_point(class_scope:ResponseEnvelopGym.Unknown6)
    ))
  ,

  Unknown7 = _reflection.GeneratedProtocolMessageType('Unknown7', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSEENVELOPGYM_UNKNOWN7,
    __module__ = 'gyms_pb2'
    # @@protoc_insertion_point(class_scope:ResponseEnvelopGym.Unknown7)
    ))
  ,

  Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSEENVELOPGYM_PAYLOAD,
    __module__ = 'gyms_pb2'
    # @@protoc_insertion_point(class_scope:ResponseEnvelopGym.Payload)
    ))
  ,

  ClientMapCellProto = _reflection.GeneratedProtocolMessageType('ClientMapCellProto', (_message.Message,), dict(

    PokemonFortProto = _reflection.GeneratedProtocolMessageType('PokemonFortProto', (_message.Message,), dict(
      DESCRIPTOR = _RESPONSEENVELOPGYM_CLIENTMAPCELLPROTO_POKEMONFORTPROTO,
      __module__ = 'gyms_pb2'
      # @@protoc_insertion_point(class_scope:ResponseEnvelopGym.ClientMapCellProto.PokemonFortProto)
      ))
    ,
    DESCRIPTOR = _RESPONSEENVELOPGYM_CLIENTMAPCELLPROTO,
    __module__ = 'gyms_pb2'
    # @@protoc_insertion_point(class_scope:ResponseEnvelopGym.ClientMapCellProto)
    ))
  ,
  DESCRIPTOR = _RESPONSEENVELOPGYM,
  __module__ = 'gyms_pb2'
  # @@protoc_insertion_point(class_scope:ResponseEnvelopGym)
  ))
_sym_db.RegisterMessage(ResponseEnvelopGym)
_sym_db.RegisterMessage(ResponseEnvelopGym.Unknown6)
_sym_db.RegisterMessage(ResponseEnvelopGym.Unknown6.Unknown2)
_sym_db.RegisterMessage(ResponseEnvelopGym.Unknown7)
_sym_db.RegisterMessage(ResponseEnvelopGym.Payload)
_sym_db.RegisterMessage(ResponseEnvelopGym.ClientMapCellProto)
_sym_db.RegisterMessage(ResponseEnvelopGym.ClientMapCellProto.PokemonFortProto)


_REQUESTENVELOPGYM_FOUR2STRING.fields_by_name['cells'].has_options = True
_REQUESTENVELOPGYM_FOUR2STRING.fields_by_name['cells']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)