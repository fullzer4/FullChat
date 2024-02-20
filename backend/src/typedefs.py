from ariadne import gql
from typedef.hello import hello_type_def

type_defs = gql("""
    {} {}
""".format(hello_type_def))