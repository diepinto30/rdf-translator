from rdfextras.sparql2sql.bison.Util import ListRedirect

class ParsedFilter(object):
    def __init__(self, filter):
        self.filter = filter

    def __repr__(self):
        return "FILTER %s" % self.filter

class ParsedExpressionFilter(ParsedFilter):
    def __repr__(self):
        return "FILTER %s" % (
            isinstance(self.filter, ListRedirect) \
                and self.filter.reduce() \
                or self.filter)

class ParsedFunctionFilter(ParsedFilter):
    pass

# Convenience
# from rdfextras.sparql2sql.bison.Filter import ParsedFilter
# from rdfextras.sparql2sql.bison.Filter import ParsedExpressionFilter
# from rdfextras.sparql2sql.bison.Filter import ParsedFunctionFilter
