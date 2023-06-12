#!/usr/bin/env python

# BSD 3-Clause License; see https://github.com/scikit-hep/uproot3/blob/master/LICENSE

from __future__ import absolute_import

import math

import numpy

import uproot3.cache
import uproot3.source.source


class ChunkedSource(uproot3.source.source.Source):
    # makes __doc__ attribute mutable before Python 3.3
    __metaclass__ = type.__new__(type, "type", (uproot3.source.source.Source.__metaclass__,), {})

    def __init__(self, path, chunkbytes, limitbytes, parallel):
        from uproot3.rootio import _memsize
        m = _memsize(chunkbytes)
        if m is not None:
            chunkbytes = int(math.ceil(m))
        m = _memsize(limitbytes)
        if m is not None:
            limitbytes = int(math.ceil(m))
        self.path = path
        self._chunkbytes = chunkbytes
        self._limitbytes = limitbytes
        if limitbytes is None:
            self.cache = {}
        else:
            self.cache = uproot3.cache.ThreadSafeArrayCache(limitbytes)
        self._source = None
        self._setup_futures(parallel)

    def parent(self):
        return self

    def threadlocal(self):
        return self

    def __del__(self):
        self.dismiss()

    def _read(self, chunkindex):
        raise NotImplementedError

    def close(self):
        super(ChunkedSource, self).close()
        self.cache.clear()

    def dismiss(self):
        if self._futures is not None:
            for future in self._futures.values():
                future.cancel()
            self._futures = {}

    def _setup_futures(self, parallel):
        if parallel is not None and parallel > 1:
            try:
                import concurrent.futures
            except ImportError:
                raise ImportError("Install futures package (for parallel > 1) with:\n    pip install futures\nor\n    conda install -c conda-forge futures")
            self._executor = concurrent.futures.ThreadPoolExecutor(parallel)
            self._futures = {}
        else:
            self._executor = None
            self._futures = None

    def _preload(self, chunkindex):
        try:
            chunk = self.cache[chunkindex]
        except KeyError:
            return self._read(chunkindex)
        else:
            return chunk

    def preload(self, starts):
        self._open()
        limitnum = self._limitbytes // self._chunkbytes
        if self._executor is not None:
            for start in starts:
                if len(self._futures) > limitnum:
                    break
                chunkindex = start // self._chunkbytes
                if chunkindex not in self._futures:
                    self._futures[chunkindex] = self._executor.submit(self._preload, chunkindex)

    def data(self, start, stop, dtype=None):
        if dtype is None:
            thedtype = numpy.dtype(numpy.uint8)
        else:
            thedtype = dtype

        # assert start >= 0
        # assert stop >= 0
        # assert stop >= start

        chunkstart = start // self._chunkbytes
        if stop % self._chunkbytes == 0:
            chunkstop = stop // self._chunkbytes
        else:
            chunkstop = stop // self._chunkbytes + 1

        out = numpy.empty((stop - start) // thedtype.itemsize, dtype=thedtype)

        for chunkindex in range(chunkstart, chunkstop):
            chunk = None
            if self._futures is not None:
                future = self._futures.pop(chunkindex, None)
                if future is not None:
                    chunk = future.result()

            if chunk is None:
                try:
                    chunk = self.cache[chunkindex]
                except KeyError:
                    self._open()
                    chunk = self._read(chunkindex)

            cstart = 0
            cstop = self._chunkbytes
            gstart = chunkindex * self._chunkbytes
            gstop = (chunkindex + 1) * self._chunkbytes

            if len(chunk) > self._chunkbytes:
                if not numpy.array_equal(chunk[:4], list(b"root")):
                    raise NotImplementedError("Expected {0} or fewer bytes but received {1} and data does not appear to be an entire ROOT file.".format(self._chunkbytes, len(chunk)))
                self.cache = {}
                for i in range(0, len(chunk), self._chunkbytes):
                    self.cache[i // self._chunkbytes] = chunk[i:i+self._chunkbytes]
                chunk = self.cache[chunkindex]
                # Dismiss any pending futures as everything has already been loaded
                self.dismiss()
            else:
                self.cache[chunkindex] = chunk

            if gstart < start:
                cstart += start - gstart
                gstart += start - gstart
            if gstop > stop:
                cstop -= gstop - stop
                gstop -= gstop - stop

            if cstop - cstart > len(chunk):
                raise IndexError("indexes {0}:{1} are beyond the end of data source {2}".format(gstart + len(chunk), stop, repr(self.path)))

            if dtype is None:
                out[gstart - start : gstop - start] = chunk[cstart:cstop]
            else:
                out.view(numpy.uint8)[gstart - start : gstop - start] = chunk[cstart:cstop]

        return out
