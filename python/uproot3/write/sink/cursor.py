#!/usr/bin/env python

# BSD 3-Clause License; see https://github.com/scikit-hep/uproot3/blob/master/LICENSE

from __future__ import absolute_import

import struct
import sys

from uproot3._util import _tobytes

class Cursor(object):
    def __init__(self, index):
        self.index = index

    def skip(self, numbytes):
        self.index += numbytes

    def update_fields(self, sink, format, *args):
        sink.write(format.pack(*args), self.index)

    def write_fields(self, sink, format, *args):
        self.update_fields(sink, format, *args)
        self.index += format.size

    def put_fields(self, format, *args):
        self.index += format.size
        return format.pack(*args)

    @staticmethod
    def length_string(string):
        if len(string) < 255:
            return len(string) + 1
        else:
            return len(string) + 5

    @staticmethod
    def length_strings(strings):
        return sum(Cursor.length_string(x) for x in strings)

    _format_byte = struct.Struct("B")
    _format_byteint = struct.Struct(">Bi")
    def update_string(self, sink, data):
        if len(data) < 255:
            sink.write(self._format_byte.pack(len(data)), self.index)
            sink.write(data, self.index + 1)
        else:
            sink.write(self._format_byteint.pack(255, len(data)), self.index)
            sink.write(data, self.index + 5)

    def write_string(self, sink, data):
        self.update_string(sink, data)
        self.index += self.length_string(data)

    def put_string(self, data):
        self.index += self.length_string(data)
        if len(data) < 255:
            return self._format_byte.pack(len(data)) + data
        else:
            return self._format_byteint.pack(255, len(data)) + data

    def update_cstring(self, sink, data):
        sink.write(data, self.index)
        sink.write(b"\x00")

    def write_cstring(self, sink, data):
        self.update_cstring(sink, data)
        self.index += len(data) + 1

    def put_cstring(self, data):
        self.index += len(data) + 1
        return data.encode("utf-8") + b"\x00"

    def update_data(self, sink, data):
        sink.write(data, self.index)

    def write_data(self, sink, data):
        self.update_data(sink, data)
        self.index += len(data)

    def put_data(self, data):
        self.index += len(data)
        return data

    def put_array(self, data):
        self.index += data.nbytes
        return _tobytes(data)

    def update_array(self, sink, data):
        sink.write(_tobytes(data), self.index)

    def write_array(self, sink, data):
        self.update_array(sink, data)
        self.index += data.nbytes
