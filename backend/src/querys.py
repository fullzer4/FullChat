from ariadne import gql
from query.hello import hello_query

querys = gql("""
    {} {}
""".format(hello_query))