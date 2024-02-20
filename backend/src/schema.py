from ariadne import make_executable_schema
from querys import querys
from typedefs import type_defs

schema = make_executable_schema(type_defs, querys)