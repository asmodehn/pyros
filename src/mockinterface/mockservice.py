from __future__ import absolute_import

from collections import deque, namedtuple

ServiceType = namedtuple("ServiceType", "reqtype resptype")

statusecho_service = ServiceType("StatusMsg", "StatusMsg")


"""
MockService is a mock for the class handling conversion from python API to Service call
"""
class MockService:
    def __init__(self, service_name, service_type):
        # service_type is a composition of python standard builtin types that still make sense outside of
        # the python environment where there originated from :
        # int, float, long, complex, str, unicode, list, tuple, bytearray, buffer, xrange, set, frozenset, dict
        self.name = service_name
        # setting the fullname to make sure we start with /
        self.fullname = self.name if self.name.startswith('/') else '/' + self.name

        self.srvtype = (service_type.reqtype, service_type.resptype)

    def call(self, rosreq = None):

        # simulating echo
        return rosreq
