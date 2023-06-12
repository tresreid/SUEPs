#!/usr/bin/env python

# BSD 3-Clause License; see https://github.com/scikit-hep/uproot3/blob/master/LICENSE

from __future__ import absolute_import

import functools
import textwrap

import uproot3
import uproot3._connect._pandas

TEXT_WIDTH = 80


def _method(x):
    if hasattr(x, "__func__"):
        return x.__func__
    else:
        return x


def _join_and_preserve_sequential_indent(lines):
    """Joins lines with newlines while preserving indentation of first line"""
    if not lines:
        return ''
    first_line = lines[0]
    leading_spaces = len(first_line) - len(first_line.lstrip(' '))
    return '\n'.join([first_line] + [' ' * leading_spaces + line for line in lines[1:]])


def wrap(text, width=80):
    """Wraps the text to a given width, preserving indentation"""
    return "\n".join(
        map(_join_and_preserve_sequential_indent,
            map(functools.partial(textwrap.wrap, width=width), text.split('\n'))))


################################################################ uproot3.rootio fragments

open_fragments = {
    # localsource
    "localsource": u"""localsource : function: path \u21d2 :py:class:`Source <uproot3.source.source.Source> or ``dict`` of keyword arguments`
        function that will be applied to the path to produce an uproot3 :py:class:`Source <uproot3.source.source.Source>` object if the path is a local file. Default is ``MemmapSource.defaults`` for memory-mapped files. If a ``dict``, the ``dict`` is passed as keyword arguments to :py:class:`MemmapSource <uproot3.source.memmap.MemmapSource>` constructor.""",

    # xrootdsource
    "xrootdsource": u"""xrootdsource : function: path \u21d2 :py:class:`Source <uproot3.source.source.Source> or ``dict`` of keyword arguments`
        function that will be applied to the path to produce an uproot3 :py:class:`Source <uproot3.source.source.Source>` object if the path is an XRootD URL. Default is ``uproot3.source.xrootd.XRootDSource.defaults`` for XRootD with default chunk size/caching. (See :py:class:`XRootDSource <uproot3.source.xrootd.XRootDSource>` constructor for details.) If a ``dict``, the ``dict`` is passed as keyword arguments to :py:class:`XRootDSource <uproot3.source.xrootd.XRootDSource>` constructor.""",

    # httpsource
    "httpsource": u"""httpsource : function: path \u21d2 :py:class:`Source <uproot3.source.source.Source> or ``dict`` of keyword arguments`
        function that will be applied to the path to produce an uproot3 :py:class:`Source <uproot3.source.source.Source>` object if the path is an HTTP URL. Default is ``uproot3.source.http.HTTPSource.defaults`` for HTTP with default chunk size/caching. (See :py:class:`HTTPSource <uproot3.source.http.HTTPSource>` constructor for details.) If a ``dict``, the ``dict`` is passed as keyword arguments to :py:class:`HTTPSource <uproot3.source.http.HTTPSource>` constructor.""",

    # options
    "options": u"""options
        passed to :py:class:`ROOTDirectory <uproot3.rootio.ROOTDirectory>` constructor.""",
}

rootdirectory_fragments = {
    # recursive
    "recursive": u"""recursive : bool
        if ``False`` *(default)*, only iterate over this directory level; if ``True``, depth-first iterate over all subdirectories as well.""",

    # filtername
    "filtername": u"""filtername : function: str \u21d2 bool
        only keys for which ``filtername(name)`` returns ``True`` are returned (does not eliminate subdirectories if ``recursive=True``). Default returns ``True`` for all input.""",

    # filterclass
    "filterclass": u"""filterclass : function: class object \u21d2 bool
        only keys for which ``filterclass(class object)`` returns ``True`` are returned (does not eliminate subdirectories if ``recursive=True``). Default returns ``True`` for all input. Note that all class objects passed to this function have a ``classname`` attribute for the C++ class name (may differ from the Python class name for syntactic reasons).""",
    }

################################################################ uproot3.rootio.open

uproot3.rootio.open.__doc__ = wrap(
u"""Opens a ROOT file (local or remote), specified by file path.

    Parameters
    ----------
    path : str
        local file path or URL specifying the location of a file (note: not a Python file object!). If the URL schema is "root://", :py:func:`xrootd <uproot3.xrootd>` will be called; if "http://", :py:func:`http <uproot3.http>` will be called.

    {localsource}

    {xrootdsource}

    {httpsource}

    {options}

    Returns
    -------
    :py:class:`ROOTDirectory <uproot3.rootio.ROOTDirectory>`
        top-level directory of the ROOT file.

    Notes
    -----
    The ROOTDirectory returned by this function is not necessarily an open file. File handles are managed internally by :py:class:`Source <uproot3.source.source.Source>` objects to permit parallel reading. Although this function can be used in a ``with`` construct (which protects against unclosed files), the ``with`` construct has no meaning when applied to this function. Files will be opened or closed as needed to read data on demand.
    """.format(**open_fragments), width=TEXT_WIDTH)

################################################################ uproot3.rootio.xrootd

uproot3.rootio.xrootd.__doc__ = wrap(
u"""Opens a remote ROOT file with XRootD (if installed).

    Parameters
    ----------
    path : str
        URL specifying the location of a file.

    {xrootdsource}

    {options}

    Returns
    -------
    :py:class:`ROOTDirectory <uproot3.rootio.ROOTDirectory>`
        top-level directory of the ROOT file.
    """.format(**open_fragments), width=TEXT_WIDTH)

################################################################ uproot3.rootio.http

uproot3.rootio.http.__doc__ = wrap(
u"""Opens a remote ROOT file with HTTP (if ``requests`` is installed).

    Parameters
    ----------
    path : str
        URL specifying the location of a file.

    {httpsource}

    {options}

    Returns
    -------
    :py:class:`ROOTDirectory <uproot3.rootio.ROOTDirectory>`
        top-level directory of the ROOT file.
    """.format(**open_fragments), width=TEXT_WIDTH)

################################################################ uproot3.rootio.ROOTDirectory

uproot3.rootio.ROOTDirectory.__doc__ = wrap(
u"""Represents a ROOT file or directory, an entry point for reading objects.

    Although this class has a constructor that could be called by a user, objects are usually created from ROOT files through :py:func:`open <uproot3.rootio.open>` or :py:func:`xrootd <uproot3.rootio.xrootd>`.

    :py:class:`ROOTDirectory <uproot3.rootio.ROOTDirectory>` objects may be accessed as Python containers:

    - square brackets (``__getitem__``) read objects from the file by key name (see :py:meth:`get <uproot3.rootio.ROOTDirectory.get>`).
    - the ``len`` function (``__len__``) returns the number of keys.
    - iteration (``__iter__``) iterates over the *names* of the keys only (like a ``dict``, see :py:meth:`keys <uproot3.rootio.ROOTDirectory.keys>`).

    **Attributes, properties, and methods:**

    - **name** (*bytes*) name of the file or directory *as read from the ROOT file*. (ROOT files may be imprinted with a different name than they have in the file system.)

    - **compression** (:py:class:`Compression <uproot3.source.compressed.Compression>`) the compression algorithm and level specified in the file header. (Some objects, including TTree branches, may have different compression settings than the global file settings.)

    - :py:meth:`get <uproot3.rootio.ROOTDirectory.get>` read an object from the file, selected by name.

    - :py:meth:`iterkeys <uproot3.rootio.ROOTDirectory.iterkeys>` iterate over key names in this directory.

    - :py:meth:`itervalues <uproot3.rootio.ROOTDirectory.itervalues>` iterate over objects in this directory.

    - :py:meth:`iteritems <uproot3.rootio.ROOTDirectory.iteritems>` iterate over *(key name, object)* pairs in this directory, like a ``dict``.

    - :py:meth:`iterclasses <uproot3.rootio.ROOTDirectory.iterclasses>` iterate over *(key name, class object)* pairs in this directory.

    - :py:meth:`keys <uproot3.rootio.ROOTDirectory.keys>` return key names in this directory.

    - :py:meth:`values <uproot3.rootio.ROOTDirectory.values>` return objects in this directory.

    - :py:meth:`items <uproot3.rootio.ROOTDirectory.items>` return *(key name, object)* pairs in this directory, like a ``dict``.

    - :py:meth:`classes <uproot3.rootio.ROOTDirectory.classes>` return *(key name, class object)* pairs in this directory.

    - :py:meth:`allkeys <uproot3.rootio.ROOTDirectory.allkeys>` return keys at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`keys <uproot3.rootio.ROOTDirectory.keys>`).

    - :py:meth:`allvalues <uproot3.rootio.ROOTDirectory.allvalues>` return objects at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`values <uproot3.rootio.ROOTDirectory.values>`).

    - :py:meth:`allitems <uproot3.rootio.ROOTDirectory.allitems>` return *(key name, object)* pairs at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`items <uproot3.rootio.ROOTDirectory.items>`).

    - :py:meth:`allclasses <uproot3.rootio.ROOTDirectory.allclasses>` return *(key name, class object)* pairs at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`classes <uproot3.rootio.ROOTDirectory.classes>`).
""", width=TEXT_WIDTH)

_method(uproot3.rootio.ROOTDirectory.get).__doc__ = wrap(
u"""Read an object from the ROOT file or directory by name.

    Parameters
    ----------
    name : str (str)
        name of the object. Any text before a "``/``" is interpreted as a subdirectory, and subdirectories of any depth may be searched. A number after a "``;``" indicates a `TKey <uproot3.rootio.TKey>` cycle.

    cycle : ``None`` or int
        `TKey <uproot3.rootio.TKey>` cycle number to disambiguate keys of the same name. This argument overrides a number after a "``;``".

    Returns
    -------
    :py:class:`ROOTStreamedObject <uproot3.rootio.ROOTStreamedObject>`
        a freshly read object from the ROOT file.

    Notes
    -----

    This method, without the ``cycle`` argument, can be accessed more directly through square brackets (``__getitem__``) on the :py:class:`ROOTDirectory <uproot3.rootio.ROOTDirectory>` object.
""".format(**rootdirectory_fragments), width=TEXT_WIDTH)

_method(uproot3.rootio.ROOTDirectory.iterkeys).__doc__ = wrap(
u"""Iterate over key names in this directory.

    This method does not read objects.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filterclass}

    Returns
    -------
    iterator over bytes
        names of objects and subdirectories in the file.

    Notes
    -----

    This method can be accessed more directly by simply iterating over a :py:class:`ROOTDirectory <uproot3.rootio.ROOTDirectory>` object.
""".format(**rootdirectory_fragments), width=TEXT_WIDTH)

_method(uproot3.rootio.ROOTDirectory.itervalues).__doc__ = wrap(
u"""Iterate over objects in this directory.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filterclass}

    Returns
    -------
    iterator over :py:class:`ROOTStreamedObject <uproot3.rootio.ROOTStreamedObject>`
        freshly read objects from the ROOT file.
""".format(**rootdirectory_fragments), width=TEXT_WIDTH)

_method(uproot3.rootio.ROOTDirectory.iteritems).__doc__ = wrap(
u"""Iterate over *(key name, object)* pairs in this directory, like a ``dict``.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filterclass}

    Returns
    -------
    iterator over (bytes, :py:class:`ROOTStreamedObject <uproot3.rootio.ROOTStreamedObject>`)
        name-object pairs from the file.
""".format(**rootdirectory_fragments), width=TEXT_WIDTH)

_method(uproot3.rootio.ROOTDirectory.iterclasses).__doc__ = wrap(
u"""Iterate over *(key name, class object)* pairs in this directory.

    This method does not read objects.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filterclass}

    Returns
    -------
    iterator over (bytes, class object)
        name-class object pairs from the file.
""".format(**rootdirectory_fragments), width=TEXT_WIDTH)

_method(uproot3.rootio.ROOTDirectory.keys).__doc__ = wrap(
u"""Return key names in this directory.

    This method does not read objects.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filterclass}

    Returns
    -------
    list of bytes
        names of objects and subdirectories in the file.
""".format(**rootdirectory_fragments), width=TEXT_WIDTH)

_method(uproot3.rootio.ROOTDirectory.values).__doc__ = wrap(
u"""Return objects in this directory.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filterclass}

    Returns
    -------
    list of :py:class:`ROOTStreamedObject <uproot3.rootio.ROOTStreamedObject>`
        freshly read objects from the ROOT file.
""".format(**rootdirectory_fragments), width=TEXT_WIDTH)

_method(uproot3.rootio.ROOTDirectory.items).__doc__ = wrap(
u"""Return *(key name, object)* pairs in this directory, like a ``dict``.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filterclass}

    Returns
    -------
    list of (bytes, :py:class:`ROOTStreamedObject <uproot3.rootio.ROOTStreamedObject>`)
        name-object pairs from the file.
""".format(**rootdirectory_fragments), width=TEXT_WIDTH)

_method(uproot3.rootio.ROOTDirectory.classes).__doc__ = wrap(
u"""Return *(key name, class object)* pairs in this directory.

    This method does not read objects.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filterclass}

    Returns
    -------
    list of (bytes, class object)
        name-class object pairs from the file.
""".format(**rootdirectory_fragments), width=TEXT_WIDTH)

_method(uproot3.rootio.ROOTDirectory.allkeys).__doc__ = wrap(
u"""Return keys at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`keys <uproot3.rootio.ROOTDirectory.keys>`).

    This method does not read objects.

    Parameters
    ----------
    {filtername}

    {filterclass}

    Returns
    -------
    list of bytes
        names of objects and subdirectories in the file.
""".format(**rootdirectory_fragments), width=TEXT_WIDTH)

_method(uproot3.rootio.ROOTDirectory.allvalues).__doc__ = wrap(
u"""Return objects at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`values <uproot3.rootio.ROOTDirectory.values>`).

    Parameters
    ----------
    {filtername}

    {filterclass}

    Returns
    -------
    list of :py:class:`ROOTStreamedObject <uproot3.rootio.ROOTStreamedObject>`
        freshly read objects from the ROOT file.
""".format(**rootdirectory_fragments), width=TEXT_WIDTH)

_method(uproot3.rootio.ROOTDirectory.allitems).__doc__ = wrap(
u"""Return *(key name, object)* pairs at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`items <uproot3.rootio.ROOTDirectory.items>`).

    Parameters
    ----------
    {filtername}

    {filterclass}

    Returns
    -------
    list of (bytes, :py:class:`ROOTStreamedObject <uproot3.rootio.ROOTStreamedObject>`)
        name-object pairs from the file.
""".format(**rootdirectory_fragments), width=TEXT_WIDTH)

_method(uproot3.rootio.ROOTDirectory.allclasses).__doc__ = wrap(
u"""Return *(key name, class object)* pairs at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`classes <uproot3.rootio.ROOTDirectory.classes>`).

    This method does not read objects.

    Parameters
    ----------
    {filtername}

    {filterclass}

    Returns
    -------
    list of (bytes, class object)
        name-class object pairs from the file.
""".format(**rootdirectory_fragments), width=TEXT_WIDTH)

################################################################ uproot3.rootio.ROOTObject and uproot3.rootio.ROOTStreamedObject

uproot3.rootio.ROOTObject.__doc__ = wrap(
u"""Superclass of all objects read out of a ROOT file (except :py:class:`ROOTDirectory <uproot3.rootio.ROOTDirectory>`).

    If a :py:class:`ROOTObject <uproot3.rootio.ROOTObject>` is not a :py:class:`ROOTStreamedObject <uproot3.rootio.ROOTStreamedObject>`, then its class definition is hard-coded, not derived from the file's *streamer info*.
""", width=TEXT_WIDTH)

uproot3.rootio.ROOTStreamedObject.__doc__ = wrap(
u"""Superclass of all objects read out of a ROOT file with an automatically generated class, derived from the file's *streamer info*.

    Each subclass of a :py:class:`ROOTStreamedObject <uproot3.rootio.ROOTStreamedObject>` has a ``classversion`` attribute, corresponding to the class version in the *streamer info*. If this version does not match the version of the serialized class, an error is raised during the read.
""", width=TEXT_WIDTH)

################################################################ uproot3.tree fragments

tree_fragments = {
    # entrystart
    "entrystart": u"""entrystart : ``None`` or int
        entry at which reading starts (inclusive). If ``None`` *(default)*, start at the beginning of the branch.""",

    # entrystop
    "entrystop": u"""entrystop : ``None`` or int
        entry at which reading stops (exclusive). If ``None`` *(default)*, stop at the end of the branch.""",

    # entrysteps
    "entrysteps": u"""entrysteps : ``None``, positive int, ``float("inf")``, string matching number + /[kMGTPEZY]?B/i, or iterable of *(int, int)* pairs
        if ``None`` *(default)*, iterate in steps of TTree clusters (number of entries for which all branches' baskets align); if an integer, iterate in steps of equal numbers of entries (except at the end of a file); if infinite, take file-sized steps; if a string, iterate in steps of approximately equal memory, given by a memory size string; otherwise, iterate in explicit, user-specified *(start, stop)* intervals ("start" is inclusive and "stop" is exclusive).""",

    # entrysteps_tree
    "entrysteps_tree": u"""entrysteps : ``None``, positive int, ``float("inf")``, string matching number + /[kMGTPEZY]?B/i, or iterable of *(int, int)* pairs
        if ``None`` *(default)*, iterate in steps of TTree clusters (number of entries for which all branches' baskets align); if an integer, iterate in steps of equal numbers of entries; if infinite, iterate over the whole file in one step; if a string, iterate in steps of approximately equal memory, given by a memory size string; otherwise, iterate in explicit, user-specified *(start, stop)* intervals ("start" is inclusive and "stop" is exclusive).""",

    # branch
    "branch": u"""branch : str
        name of the branch to read.""",

    # interpretation
    "interpretation": u"""interpretation : ``None`` or :py:class:`Interpretation <uproot3.interp.interp.Interpretation>`
        the meaning imposed upon the bytes of the file and the ultimate form to instantiate. If ``None`` *(default)*, :py:func:`interpret <uproot3.interp.auto.interpret>` will be applied to the branch to generate an interpretation.""",

    # branches
    "branches": u"""branches
        - if ``None`` *(default)*, select all *interpretable* branches;
        - if a list of str, select branches by name;
        - if a single str, select a single branch (though the return value is still a container type, not a single array). The selection by string can include filename-like glob characters (``*``, ``?``, ``[...]``) or it can be a full regular expression (Python flavored) if surrounded by slashes, like ``/pattern/i`` (where ``i`` is an optional `Python re flag <https://docs.python.org/2/library/re.html>`_);
        - if a function :py:class:`TBranchMethods <uproot3.tree.TBranchMethods>` \u21d2 ``True`` or ``False``, select branches that return ``True``;
        - if a function :py:class:`TBranchMethods <uproot3.tree.TBranchMethods>` \u21d2 ``None`` or :py:class:`Interpretation <uproot3.interp.interp.Interpretation>`, select branches for which the function does not return ``None`` and use the interpretation it returns otherwise;
        - if a ``dict`` of str \u2192 :py:class:`Interpretation <uproot3.interp.interp.Interpretation>`, select branches named by keys and use interpretations from the associated values.""",

    # outputtype
    "outputtype": u"""outputtype : type
        constructor for the desired yield type, such as ``dict`` *(default)*, ``OrderedDict``, ``tuple``, ``namedtuple``, custom user class, etc.""",

    # namedecode
    "namedecode": u"""namedecode : None or str
        if ``None`` *(default)* return names as uninterpreted byte strings (type ``bytes`` in Python 3); if a string like ``"ascii"`` or ``"utf-8"``, decode bytes to a string using the specified encoding.""",

    # reportpath
    "reportpath": u"""reportpath : bool
        if ``True`` *(not default)*, yield the current path (string) before the arrays (and any other reported objects) as a tuple.""",

    # reportfile
    "reportfile": u"""reportfile : bool
        if ``True``, *(not default)*, yield the current file (object) before the arrays (and any other reported objects except reportpath) as a tuple.""",

    # reportentries
    "reportentries": u"""reportentries : bool
        if ``True`` *(not default)*, yield the current entry start and entry stop (integers) before the arrays, where *entry start* is inclusive and *entry stop* is exclusive.""",

    # flatten
    "flatten": u"""flatten : None or bool
        if ``True``, convert JaggedArrays into flat Numpy arrays. If False *(default)*, make JaggedArrays lists. If None, remove JaggedArrays.""",

    # flatname
    "flatname": u"""flatname : None or (branchname, fieldname, index) \u2192 str
        if ``None`` *(default)*, use ``uproot3._connect._pandas.default_flatname`` to convert a branchname with a subfield and regular index number into a Pandas column name; otherwise, take a user-defined function.""",

    # profile
    "profile": u"""profile : None or str
        if a string *(not default)*, format the lazy arrays using a module from uproot3_methods.profiles named by the string.""",

    # awkwardlib
    "awkwardlib": u"""awkwardlib : ``None``, str, or module
        if ``None`` *(default)*, use ``import awkward`` to get Awkward Array constructors. Otherwise, parse the module string name or use the provided module.""",

    # cache
    "cache": u"""cache : ``None`` or ``dict``-like object
        if not ``None`` *(default)*, fully interpreted arrays will be saved in the ``dict``-like object for later use. Accessing the same arrays with a different interpretation or a different entry range results in a cache miss.""",

    # basketcache
    "basketcache": u"""basketcache : ``None`` or ``dict``-like object
        if not ``None`` *(default)*, raw basket data will be saved in the ``dict``-like object for later use. Accessing the same arrays with a different interpretation or a different entry range fully utilizes this cache, since the interpretation/construction from baskets is performed after retrieving data from this cache.""",

    # keycache
    "keycache": u"""keycache : ``None`` or ``dict``-like object
        if not ``None`` *(default)*, basket TKeys will be saved in the ``dict``-like object for later use. TKeys are small, but require file access, so caching them can speed up repeated access.""",

    # executor
    "executor": u"""executor : `concurrent.futures.Executor <https://docs.python.org/3/library/concurrent.futures.html>`_
        if not ``None`` *(default)*, parallelize basket-reading and decompression by scheduling tasks on the executor. Assumes caches are thread-safe.""",

    # blocking
    "blocking": u"""blocking : bool
        if ``True`` *(default)*, do not exit this function until the arrays are read, and return those arrays. If ``False``, exit immediately and return a zero-argument function. That zero-argument function returns the desired array, and it blocks until the array is available. This option is only useful with a non-``None`` executor.""",

    # persistvirtual
    "persistvirtual": u"""persistvirtual : bool
        if ``False`` *(default)*, the resulting awkward0.VirtualArrays would convert themselves into real arrays (materialize) before being saved in Awkward Array's persistence methods; if ``True``, the "virtualness" of the arrays is preserved\u2014that is, only instructions for reconstituting the arrays is saved, not the array data themselves.""",

    # recursive
    "recursive": u"""recursive : bool
        if ``False`` *(default)*, only iterate at this tree/branch level; if ``True``, depth-first iterate over all subbranches as well. If ``'/'``, depth-first iterate over all subbranches and use fully qualified "paths" to the subbranches as keys, with '/' as level separator.""",

    # filtername
    "filtername": u"""filtername : function: str \u21d2 bool
        only branches for which ``filtername(name)`` returns ``True`` are returned. Default returns ``True`` for all input.""",

    # filtertitle
    "filtertitle": u"""filtertitle : function: str \u21d2 bool
        only branches for which ``filtertitle(title)`` returns ``True`` are returned. Default returns ``True`` for all input.""",

    # i
    "i": u"""i : non-negative int
        basket number (must be greater than or equal to zero and strictly less than *numbaskets*).""",

    # chunked
    "chunked": u"""chunked : bool
        if ``True`` *(default)*, produced chunked lazy arrays using awkward0.ChunkedArray.   If ``False``, produce bare VirtualArrays.  This option implies ``entrysteps = float('inf')``.""",

    }

################################################################ uproot3.tree.iterate

uproot3.tree.iterate.__doc__ = wrap(
u"""Opens a series of ROOT files (local or remote), yielding the same number of entries from all selected branches in each step.

    Depending on the "entrysteps" parameter, the number of entries in one step may differ from the number of entries in the next step, but in every step, the same number of entries is retrieved from all *baskets.*

    All but the first two parameters are identical to :py:meth:`uproot3.tree.TreeMethods.iterate`.

    Parameters
    ----------
    path : str or list of str
        glob pattern(s) for local file paths (POSIX wildcards like "``*``") or URLs specifying the locations of the files. A list of filenames are processed in the given order, but glob patterns get pre-sorted to ensure a predictable order.

    treepath : str
        path within each ROOT file to find the TTree (may include "``/``" for subdirectories or "``;``" for cycle numbers).

    {branches}

    {entrysteps}

    {outputtype}

    {namedecode}

    {reportpath}

    {reportfile}

    {reportentries}

    {flatten}

    {flatname}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {executor}

    {blocking}

    {localsource}

    {xrootdsource}

    {httpsource}

    {options}

    Returns
    -------
    iterator over (str, :py:class:`ROOTDirectory <uproot3.rootio.ROOTDirectory>`, int, int, outputtype) (if *reportpath*, *reportfile*, *reportentries*) or just outputtype (otherwise)
        aligned array segments from the files.
    """.format(**dict(list(open_fragments.items()) + list(tree_fragments.items()))), width=TEXT_WIDTH)

################################################################ uproot3.pandas.iterate

uproot3.pandas.iterate.__doc__ = wrap(
u"""Opens a series of ROOT files (local or remote), yielding Pandas DataFrames in each step.

    Depending on the "entrysteps" parameter, the number of entries in one step may differ from the number of entries in the next step, but in every step, the same number of entries is retrieved from all *baskets.*

    Parameters
    ----------
    path : str or list of str
        glob pattern(s) for local file paths (POSIX wildcards like "``*``") or URLs specifying the locations of the files. A list of filenames are processed in the given order, but glob patterns get pre-sorted to ensure a predictable order.

    treepath : str
        path within each ROOT file to find the TTree (may include "``/``" for subdirectories or "``;``" for cycle numbers).

    {branches}

    {entrysteps}

    {namedecode}

    {reportpath}

    {reportfile}

    {flatten}

    {flatname}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {executor}

    {blocking}

    {localsource}

    {xrootdsource}

    {httpsource}

    {options}

    Returns
    -------
    iterator over (str, :py:class:`ROOTDirectory <uproot3.rootio.ROOTDirectory>`, pandas.Dataframe) (if *reportpath* and *reportfile*) or just pandas.DataFrame (otherwise)
        aligned array segments from the files.
    """.format(**dict(list(open_fragments.items()) + list(tree_fragments.items()))), width=TEXT_WIDTH)

################################################################ uproot3.tree.TTreeMethods

uproot3.tree.TTreeMethods.__doc__ = wrap(
u"""Adds array reading methods to TTree objects that have been streamed from a ROOT file.

    - square brackets (``__getitem__``) returns a branch by name (see :py:meth:`get <uproot3.tree.TTreeMethods.get>`).
    - the ``len`` function (``__len__``) returns the number of entries (same as ``numentries``).
    - iteration (``__iter__``) has no implementation. This is to avoid confusion between iterating over all branches (probably not what you want, but fitting the pattern set by :py:class:`ROOTDirectory <uproot3.rootio.ROOTDirectory>` and ``dict``) and iterating over the data.

    **Attributes, properties, and methods:**

    - **name** (*bytes*) name of the TTree.
    - **title** (*bytes*) title of the TTree.
    - **numentries** (*int*) number of entries in the TTree (same as ``len``).
    - **pandas** connector to `Pandas <http://pandas.pydata.org/>`_ functions

    - :py:meth:`get <uproot3.tree.TTreeMethods.get>` return a branch by name (at any level of depth).
    - :py:meth:`iterkeys <uproot3.tree.TTreeMethods.iterkeys>` iterate over branch names.
    - :py:meth:`itervalues <uproot3.tree.TTreeMethods.itervalues>` iterate over branches.
    - :py:meth:`iteritems <uproot3.tree.TTreeMethods.iteritems>` iterate over *(branch name, branch)* pairs.
    - :py:meth:`keys <uproot3.tree.TTreeMethods.keys>` return branch names.
    - :py:meth:`values <uproot3.tree.TTreeMethods.values>` return branches.
    - :py:meth:`items <uproot3.tree.TTreeMethods.items>` return *(branch name, branch)* pairs.
    - :py:meth:`allkeys <uproot3.tree.TTreeMethods.allkeys>` return branch names at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`keys <uproot3.tree.TTreeMethods.keys>`).
    - :py:meth:`allvalues <uproot3.tree.TTreeMethods.allvalues>` return branches at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`values <uproot3.tree.TTreeMethods.values>`).
    - :py:meth:`allitems <uproot3.tree.TTreeMethods.allitems>` return *(branch name, branch)* pairs at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`items <uproot3.tree.TTreeMethods.items>`).
    - :py:meth:`clusters <uproot3.tree.TTreeMethods.clusters>` iterate over *(int, int)* pairs representing cluster entry starts and stops in this TTree.
    - :py:meth:`mempartitions <uproot3.tree.TTreeMethods.mempartitions>` iterate over *(int, int)* pairs representing entry starts and stops that attempt to maintain a constant memory footprint.

    **Methods for reading array data:**

    - :py:meth:`array <uproot3.tree.TTreeMethods.array>` read one branch into an array (or other object if provided an alternate *interpretation*).
    - :py:meth:`arrays <uproot3.tree.TTreeMethods.arrays>` read many branches into arrays (or other objects if provided alternate *interpretations*).
    - :py:meth:`lazyarray <uproot3.tree.TTreeMethods.lazyarray>` create a lazy array that would read the branch as needed.
    - :py:meth:`lazyarrays <uproot3.tree.TTreeMethods.lazyarrays>` create many lazy arrays.
    - :py:meth:`iterate <uproot3.tree.TTreeMethods.iterate>` iterate over many arrays at once, yielding the same number of entries from all selected branches in each step.
""", width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.get).__doc__ = wrap(
u"""Return a branch by name (at any level of depth).

    Parameters
    ----------
    name : str
        name of the branch to return.
        If `name` contains a '/', it is interpreted as path to a specific subbranch and the `recursive` parameter is ignored.

    Returns
    -------
    :py:class:`TBranch <upoot.tree.TBranchMethods>`
        selected branch.

    Notes
    -----

    This method can be accessed more directly through square brackets (``__getitem__``) on the :py:class:`TTree <uproot3.tree.TTreeMethods>` object.
""", width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.iterkeys).__doc__ = wrap(
u"""Iterate over branch names.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filtertitle}

    Returns
    -------
    iterator over bytes
        names of branches.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.itervalues).__doc__ = wrap(
u"""Iterate over branches.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filtertitle}

    Returns
    -------
    iterator over :py:class:`TBranch <uproot3.tree.TBranchMethods>`
        branches.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.iteritems).__doc__ = wrap(
u"""Iterate over *(branch name, branch)* pairs.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filtertitle}

    Returns
    -------
    iterator over (bytes, :py:class:`TBranch <uproot3.tree.TBranchMethods>`)
        name-branch pairs.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.keys).__doc__ = wrap(
u"""Return branch names.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filtertitle}

    Returns
    -------
    list of bytes
        names of branches.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.values).__doc__ = wrap(
u"""Return branches.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filtertitle}

    Returns
    -------
    list of :py:class:`TBranch <uproot3.tree.TBranchMethods>`
        branches.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.items).__doc__ = wrap(
u"""Return *(branch name, branch)* pairs.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filtertitle}

    Returns
    -------
    list of (bytes, :py:class:`TBranch <uproot3.tree.TBranchMethods>`)
        name-branch pairs.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.allkeys).__doc__ = wrap(
u"""Return branch names at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`keys <uproot3.tree.TTreeMethods.keys>`).

    Parameters
    ----------
    {filtername}

    {filtertitle}

    Returns
    -------
    list of bytes
        names of branches.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.allvalues).__doc__ = wrap(
u"""Return branches at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`values <uproot3.tree.TTreeMethods.values>`).

    Parameters
    ----------
    {filtername}

    {filtertitle}

    Returns
    -------
    list of :py:class:`TBranch <uproot3.tree.TBranchMethods>`
        branches.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.allitems).__doc__ = wrap(
u"""Return *(branch name, branch)* pairs at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`items <uproot3.tree.TTreeMethods.items>`).

    Parameters
    ----------
    {filtername}

    {filtertitle}

    Returns
    -------
    list of (bytes, :py:class:`TBranch <uproot3.tree.TBranchMethods>`
        name-branch pairs.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.clusters).__doc__ = wrap(
u"""Return entry starts and stops as *(int, int)* pairs representing clusters for a given set of branches this TTree.

    Rather than using ROOT's self-reported clusters (which don't exist in every ROOT file), this method finds the minimal step sizes in which a given set of branches have basket thresholds for the same entry number. For a single branch, this is exactly the basket boundaries. It is possible for a given set of branches to never line up, in which case, the cluster is the entire file.

    Parameters
    ----------
    {branches}

    {entrystart}

    {entrystop}

    strict : bool
        if ``False`` *(default)*, the potential ``start, stop`` pair must satisfy ``entrystart < stop and start < entrystop``; if ``True``, the potential ``start, stop`` pair must satisfy ``entrystart <= start and stop <= entrystop``.

    Returns
    -------
    list of (int, int)
        start (inclusive) and stop (exclusive) pairs for each cluster.
""", width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.mempartitions).__doc__ = wrap(
u"""Return entry starts and stops as *(int, int)* pairs of (approximately) equal-memory partitions for a given set of branches in this TTree.

    Similar to :py:meth:`clusters <uproot3.tree.TTreeMethods.clusters>` in that it provides a list of (start, stop) entry pairs, but instead of fitting baskets, this method attempts to keep the memory use constant.

    Parameters
    ----------
    numbytes : positive number (int or float) or string matching number + /[kMGTPEZY]?B/i
        target number of bytes in each step (not an upper limit, but an average); if a string, parse the memory size

    {branches}

    {entrystart}

    {entrystop}

    {keycache}

    linear : bool
        if ``True`` *(default)*, the step size is uniform (same number of entries in each step); any variations in entry size as a function of entry number are averaged over. Non-linear steps (``False``), which would take into account bigger entry sizes at the beginning or end of the file, have not been implemented.

    Returns
    -------
    list of (int, int)
        start (inclusive) and stop (exclusive) pairs for each equal-memory partition.
""", width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.array).__doc__ = wrap(
u"""Read one branch into an array (or other object if provided an alternate *interpretation*).

    Parameters
    ----------
    {branch}

    {interpretation}

    {entrystart}

    {entrystop}

    {flatten}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {executor}

    {blocking}

    Returns
    -------
    array or other object, depending on *interpretation*.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.arrays).__doc__ = wrap(
u"""Read many branches into arrays (or other objects if provided alternate *interpretations*).

    Parameters
    ----------
    {branches}

    {outputtype}

    {namedecode}

    {entrystart}

    {entrystop}

    {flatten}

    {flatname}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {executor}

    {blocking}

    Returns
    -------
    outputtype of arrays or other objects, depending on *interpretation*
        branch data.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.lazyarray).__doc__ = wrap(
u"""Create a lazy array that would read the branch as needed.

    Parameters
    ----------
    {branch}

    {interpretation}

    {entrysteps_tree}

    {entrystart}

    {entrystop}

    {flatten}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {executor}

    {persistvirtual}

    {chunked}

    Returns
    -------
    ChunkedArray of VirtualArrays or VirtualArray
        lazy version of the array.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.lazyarrays).__doc__ = wrap(
u"""Create a table of lazy arrays.

    Parameters
    ----------
    {branches}

    {namedecode}

    {entrysteps}

    {entrystart}

    {entrystop}

    {flatten}

    {profile}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {executor}

    {persistvirtual}

    {chunked}

    Returns
    -------
    ChunkedArray of Table of VirtualArrays or Table of VirtualArrays
        lazy branch data.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TTreeMethods.iterate).__doc__ = wrap(
u"""Iterate over many arrays at once, yielding the same number of entries from all selected branches in each step.

    Depending on the "entrysteps" parameter, the number of entries in one step may differ from the number of entries in the next step, but in every step, the same number of entries is retrieved from all *baskets.*

    Parameters
    ----------
    {branches}

    {entrysteps_tree}

    {outputtype}

    {namedecode}

    {reportentries}

    {entrystart}

    {entrystop}

    {flatten}

    {flatname}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {executor}

    {blocking}

    Returns
    -------
    iterator over (int, int, outputtype) (if *reportentries*) or just outputtype (otherwise)
        aligned array segments from the TTree.
""".format(**tree_fragments), width=TEXT_WIDTH)

################################################################ uproot3.tree.TBranchMethods

uproot3.tree.TBranchMethods.__doc__ = wrap(
u"""Adds array reading methods to TBranch objects that have been streamed from a ROOT file.

    - square brackets (``__getitem__``) returns a subbranch by name (see :py:meth:`get <uproot3.tree.TBranchMethods.get>`).
    - the ``len`` function (``__len__``) returns the number of entries (same as ``numentries``).
    - iteration (``__iter__``) has no implementation. This is to avoid confusion between iterating over all subbranches (probably not what you want, but fitting the pattern set by :py:class:`ROOTDirectory <uproot3.rootio.ROOTDirectory>` and ``dict``) and iterating over the data.

    **Attributes, properties, and methods:**

    - **name** (*bytes*) name of the TBranch.
    - **title** (*bytes*) title of the TBranch.
    - **compression** (:py:class:`Compression <uproot3.source.compressed.Compression>`) the compression algorithm and level specified in the TBranch header. (Actual compression used may differ.)
    - :py:meth:`get <uproot3.tree.TBranchMethods.get>` return a subbranch by name (at any level of depth).
    - :py:meth:`iterkeys <uproot3.tree.TBranchMethods.iterkeys>` iterate over subbranch names.
    - :py:meth:`itervalues <uproot3.tree.TBranchMethods.itervalues>` iterate over subbranches.
    - :py:meth:`iteritems <uproot3.tree.TBranchMethods.iteritems>` iterate over *(subbranch name, subbranch)* pairs.
    - :py:meth:`keys <uproot3.tree.TBranchMethods.keys>` return subbranch names.
    - :py:meth:`values <uproot3.tree.TBranchMethods.values>` return subbranches.
    - :py:meth:`items <uproot3.tree.TBranchMethods.items>` return *(subbranch name, subbranch)* pairs.
    - :py:meth:`allkeys <uproot3.tree.TBranchMethods.allkeys>` return subbranch names at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`keys <uproot3.tree.TBranchMethods.keys>`).
    - :py:meth:`allvalues <uproot3.tree.TBranchMethods.allvalues>` return subbranches at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`values <uproot3.tree.TBranchMethods.values>`).
    - :py:meth:`allitems <uproot3.tree.TBranchMethods.allitems>` return *(subbranch name, subbranch)* pairs at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`items <uproot3.tree.TBranchMethods.items>`).

    **Branch information:**

    - **numentries** (*int*) number of entries in the TBranch (same as ``len``).
    - **numbaskets** (*int*) number of baskets in the TBranch.
    - :py:meth:`uncompressedbytes <uproot3.tree.TBranchMethods.uncompressedbytes>` the number of bytes contained in the TBranch (data and offsets; not including any key headers) *after* decompression, if applicable.
    - :py:meth:`compressedbytes <uproot3.tree.TBranchMethods.compressedbytes>` the number of bytes contained in the TBranch (data and offsets; not including any key headers) *before* decompression, if applicable.
    - :py:meth:`compressionratio <uproot3.tree.TBranchMethods.compressionratio>` the uncompressed bytes divided by compressed bytes (greater than or equal to 1).
    - :py:meth:`numitems <uproot3.tree.TBranchMethods.numitems>` the number of items in the TBranch, under a given interpretation.

    **Basket information:**

    - :py:meth:`basket_entrystart <uproot3.tree.TBranchMethods.basket_entrystart>` the starting entry for a given basket (inclusive).
    - :py:meth:`basket_entrystop <uproot3.tree.TBranchMethods.basket_entrystop>` the stopping entry for a given basket (exclusive).
    - :py:meth:`basket_numentries <uproot3.tree.TBranchMethods.basket_numentries>` the number of entries in a given basket.
    - :py:meth:`basket_uncompressedbytes <uproot3.tree.TBranchMethods.basket_uncompressedbytes>` the number of bytes contained in the basket (data and offsets; not including any key headers) *after* decompression, if applicable.
    - :py:meth:`basket_compressedbytes <uproot3.tree.TBranchMethods.basket_compressedbytes>` the number of bytes contained in the basket (data and offsets; not including any key headers) *before* decompression, if applicable.
    - :py:meth:`basket_numitems <uproot3.tree.TBranchMethods.basket_numitems>` the number of items in the basket, under a given interpretation.
    - :py:meth:`mempartitions <uproot3.tree.TBranchMethods.mempartitions>` iterate over *(int, int)* pairs representing entry starts and stops that attempt to maintain a constant memory footprint.

    **Methods for reading array data:**

    - :py:meth:`array <uproot3.tree.TBranchMethods.array>` read the branch into an array (or other object if provided an alternate *interpretation*).
    - :py:meth:`lazyarray <uproot3.tree.TBranchMethods.lazyarray>` create a lazy array that would read the branch as needed.
    - :py:meth:`basket <uproot3.tree.TBranchMethods.basket>` read a single basket into an array.
    - :py:meth:`baskets <uproot3.tree.TBranchMethods.baskets>` read baskets into a list of arrays.
    - :py:meth:`iterate_baskets <uproot3.tree.TBranchMethods.iterate_baskets>` iterate over baskets.
""", width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.get).__doc__ = wrap(
u"""Return a subbranch by name (at any level of depth).

    Parameters
    ----------
    name : str
        name of the subbranch to return.
        If `name` contains a '/', it is interpreted as path to a specific subbranch and the `recursive` parameter is ignored.

    Returns
    -------
    :py:class:`TBranch <upoot.tree.TBranchMethods>`
        branch object.

    Notes
    -----

    This method can be accessed more directly through square brackets (``__getitem__``) on the :py:class:`TBranch <uproot3.tree.TBranchMethods>` object.
""", width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.iterkeys).__doc__ = wrap(
u"""Iterate over subbranch names.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filtertitle}

    Returns
    -------
    iterator over bytes
        subbranch names.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.itervalues).__doc__ = wrap(
u"""Iterate over subbranches.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filtertitle}

    Returns
    -------
    iterator over :py:class:`TBranch <uproot3.tree.TBranchMethods>`
        subbranches.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.iteritems).__doc__ = wrap(
u"""Iterate over *(subbranch name, subbranch)* pairs.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filtertitle}

    Returns
    -------
    iterator over (bytes, :py:class:`TBranch <uproot3.tree.TBranchMethods>`)
        *(subbranch name, subbranch)* pairs.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.keys).__doc__ = wrap(
u"""Return subbranch names.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filtertitle}

    Returns
    -------
    list of bytes
        subbranch names.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.values).__doc__ = wrap(
u"""Return subbranches.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filtertitle}

    Returns
    -------
    list of :py:class:`TBranch <uproot3.tree.TBranchMethods>`
        subbranches.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.items).__doc__ = wrap(
u"""Return *(subbranch name, subbranch)* pairs.

    Parameters
    ----------
    {recursive}

    {filtername}

    {filtertitle}

    Returns
    -------
    list of (bytes, :py:class:`TBranch <uproot3.tree.TBranchMethods>`)
        *(subbranch name, subbranch)* pairs.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.allkeys).__doc__ = wrap(
u"""Return subbranch names at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`keys <uproot3.tree.TBranchMethods.keys>`).

    Parameters
    ----------
    {filtername}

    {filtertitle}

    Returns
    -------
    list of bytes
        subbranch names.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.allvalues).__doc__ = wrap(
u"""Return subbranches at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`values <uproot3.tree.TBranchMethods.values>`).

    Parameters
    ----------
    {filtername}

    {filtertitle}

    Returns
    -------
    list of :py:class:`TBranch <uproot3.tree.TBranchMethods>`
        subbranches.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.allitems).__doc__ = wrap(
u"""Return *(subbranch name, subbranch)* pairs at all levels of depth (shortcut for passing ``recursive=True`` to :py:meth:`items <uproot3.tree.TBranchMethods.items>`).

    Parameters
    ----------
    {filtername}

    {filtertitle}

    Returns
    -------
    list of (bytes, :py:class:`TBranch <uproot3.tree.TBranchMethods>`
        (subbranch name, subbranch)* pairs.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.uncompressedbytes).__doc__ = wrap(
u"""The number of bytes contained in the TBranch (data and offsets; not including any key headers) *after* decompression, if applicable.

    Parameters
    ----------
    {keycache}

    Returns
    -------
    int
        uncompressed bytes.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.compressedbytes).__doc__ = wrap(
u"""The number of bytes contained in the TBranch (data and offsets; not including any key headers) *before* decompression, if applicable.

    Parameters
    ----------
    {keycache}

    Returns
    -------
    int
        compressed bytes.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.compressionratio).__doc__ = wrap(
u"""The uncompressed bytes divided by compressed bytes (greater than or equal to 1).

    Parameters
    ----------
    {keycache}

    Returns
    -------
    float
        compression ratio.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.numitems).__doc__ = wrap(
u"""The number of items in the TBranch, under a given interpretation.

    Parameters
    ----------
    {interpretation}

    {keycache}

    Returns
    -------
    int
        number of items.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.basket_entrystart).__doc__ = wrap(
u"""The starting entry for a given basket (inclusive).

    Parameters
    ----------
    {i}

    Returns
    -------
    int
        starting entry.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.basket_entrystop).__doc__ = wrap(
u"""The stopping entry for a given basket (exclusive).

    Parameters
    ----------
    {i}

    Returns
    -------
    int
        stopping entry.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.basket_numentries).__doc__ = wrap(
u"""The number of entries in a given basket.

    Parameters
    ----------
    {i}

    Returns
    -------
    int
        number of entries.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.basket_uncompressedbytes).__doc__ = wrap(
u"""The number of bytes contained in the basket (data and offsets; not including any key headers) *after* decompression, if applicable.

    Parameters
    ----------
    {i}

    {keycache}

    Returns
    -------
    int
        number of uncompressed bytes.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.basket_compressedbytes).__doc__ = wrap(
u"""The number of bytes contained in the basket (data and offsets; not including any key headers) *before* decompression, if applicable.

    Parameters
    ----------
    {i}

    {keycache}

    Returns
    -------
    int
        number of compressed bytes.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.basket_numitems).__doc__ = wrap(
u"""The number of items in the basket, under a given interpretation.

    Parameters
    ----------
    {i}

    {interpretation}

    {keycache}

    Returns
    -------
    int
        number of items.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.array).__doc__ = wrap(
u"""Read the branch into an array (or other object if provided an alternate *interpretation*).

    Parameters
    ----------
    {interpretation}

    {entrystart}

    {entrystop}

    {flatten}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {executor}

    {blocking}

    Returns
    -------
    array or other object, depending on *interpretation*
        branch data.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.mempartitions).__doc__ = wrap(
u"""Return entry starts and stops as *(int, int)* pairs of (approximately) equal-memory partitions in this TBranch.

    Similar to :py:meth:`clusters <uproot3.tree.TTreeMethods.clusters>` in that it provides a list of (start, stop) entry pairs, but instead of fitting baskets, this method attempts to keep the memory use constant.

    Parameters
    ----------
    numbytes : positive number (int or float) or string matching number + /[kMGTPEZY]?B/i
        target number of bytes in each step (not an upper limit, but an average); if a string, parse the memory size

    {entrystart}

    {entrystop}

    {keycache}

    linear : bool
        if ``True`` *(default)*, the step size is uniform (same number of entries in each step); any variations in entry size as a function of entry number are averaged over. Non-linear steps (``False``), which would take into account bigger entry sizes at the beginning or end of the file, have not been implemented.

    Returns
    -------
    list of (int, int)
        start (inclusive) and stop (exclusive) pairs for each equal-memory partition.
""", width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.lazyarray).__doc__ = wrap(
u"""Create a lazy array that would read the branch as needed.

    Parameters
    ----------
    {interpretation}

    {entrysteps}

    {entrystart}

    {entrystop}

    {flatten}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {executor}

    {persistvirtual}

    {chunked}

    Returns
    -------
    ChunkedArray of VirtualArrays or VirtualArray
        lazy version of branch data.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.basket).__doc__ = wrap(
u"""Read a single basket into an array.

    Parameters
    ----------
    {i}

    {interpretation}

    {entrystart}

    {entrystop}

    {flatten}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    Returns
    -------
    array or other object, depending on *interpretation*
        basket data.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.baskets).__doc__ = wrap(
u"""Read baskets into a list of arrays.

    Parameters
    ----------
    {interpretation}

    {entrystart}

    {entrystop}

    {flatten}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {reportentries}

    {executor}

    {blocking}

    Returns
    -------
    list of arrays or other objects, depending on *interpretation*
        basket data.
""".format(**tree_fragments), width=TEXT_WIDTH)

_method(uproot3.tree.TBranchMethods.iterate_baskets).__doc__ = wrap(
u"""Iterate over baskets.

    Parameters
    ----------
    {interpretation}

    {entrystart}

    {entrystop}

    {flatten}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {reportentries}

    Returns
    -------
    iterator over arrays or other objects, depending on *interpretation*
        basket data.
""".format(**tree_fragments), width=TEXT_WIDTH)

################################################################ uproot3.tree.TTreeMethods.pandas

_method(uproot3._connect._pandas.TTreeMethods_pandas.df).__doc__ = wrap(
u"""Create a Pandas DataFrame from some branches.

    Parameters
    ----------
    {branches}

    namedecode : None or str
        if ``"utf-8"`` *(default)* or other encoding name, decode column names as strings; if ``None``, return names as uninterpreted byte strings (type ``bytes`` in Python 3).

    {entrystart}

    {entrystop}

    flatten : None or bool
        if ``True`` *(default)*, convert JaggedArrays into flat Numpy arrays and turn the DataFrame index into a two-level MultiIndex to represent the structure. If False, make JaggedArrays into lists. If None, remove JaggedArrays.

    {cache}

    {basketcache}

    {keycache}

    {executor}

    Returns
    -------
    Pandas DataFrame
        data frame (`see docs <http://pandas.pydata.org/pandas-docs/stable/api.html#dataframe>`_).
""".format(**tree_fragments), width=TEXT_WIDTH)

################################################################ uproot3.tree.lazyarray(s)

uproot3.tree.lazyarray.__doc__ = wrap(
u"""Create a lazy array that would read from a set of files as needed.

    Parameters
    ----------

    path : str or list of str
        glob pattern(s) for local file paths (POSIX wildcards like "``*``") or URLs specifying the locations of the files. A list of filenames are processed in the given order, but glob patterns get pre-sorted to ensure a predictable order.

    treepath : str
        path within each ROOT file to find the TTree (may include "``/``" for subdirectories or "``;``" for cycle numbers).

    branchname : str
        path within each TTree to find the TBranch

    {interpretation}

    {namedecode}

    {entrysteps}

    {flatten}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {executor}

    {persistvirtual}

    {localsource}

    {xrootdsource}

    {httpsource}

    {options}

    Returns
    -------
    ChunkedArray of VirtualArrays
        lazy files of lazy baskets.
""".format(**dict(list(open_fragments.items()) + list(tree_fragments.items()))), width=TEXT_WIDTH)

uproot3.tree.lazyarrays.__doc__ = wrap(
u"""Create a lazy table that would read from a set of files as needed.

    Parameters
    ----------

    path : str or list of str
        glob pattern(s) for local file paths (POSIX wildcards like "``*``") or URLs specifying the locations of the files. A list of filenames are processed in the given order, but glob patterns get pre-sorted to ensure a predictable order.

    treepath : str
        path within each ROOT file to find the TTree (may include "``/``" for subdirectories or "``;``" for cycle numbers).

    {branches}

    {namedecode}

    {entrysteps}

    {flatten}

    {profile}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {executor}

    {persistvirtual}

    {localsource}

    {xrootdsource}

    {httpsource}

    {options}

    Returns
    -------
    ChunkedArray of Table of VirtualArrays
        lazy files of branches of lazy baskets.
""".format(**dict(list(open_fragments.items()) + list(tree_fragments.items()))), width=TEXT_WIDTH)

################################################################ uproot3.tree.daskarray/daskframe

uproot3.tree.daskarray.__doc__ = wrap(
u"""Create a Dask array that would read from a set of files as needed.

    Parameters
    ----------

    path : str or list of str
        glob pattern(s) for local file paths (POSIX wildcards like "``*``") or URLs specifying the locations of the files. A list of filenames are processed in the given order, but glob patterns get pre-sorted to ensure a predictable order.

    treepath : str
        path within each ROOT file to find the TTree (may include "``/``" for subdirectories or "``;``" for cycle numbers).

    branchname : str
        path within each TTree to find the TBranch

    {interpretation}

    {namedecode}

    {entrysteps}

    {flatten}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {executor}

    {localsource}

    {xrootdsource}

    {httpsource}

    {options}

    Returns
    -------
    dask.array.core.Array
        lazy files of lazy baskets.
""".format(**dict(list(open_fragments.items()) + list(tree_fragments.items()))), width=TEXT_WIDTH)

uproot3.tree.daskframe.__doc__ = wrap(
u"""Create a Dask DataFrame that would read from a set of files as needed.

    Parameters
    ----------

    path : str or list of str
        glob pattern(s) for local file paths (POSIX wildcards like "``*``") or URLs specifying the locations of the files. A list of filenames are processed in the given order, but glob patterns get pre-sorted to ensure a predictable order.

    treepath : str
        path within each ROOT file to find the TTree (may include "``/``" for subdirectories or "``;``" for cycle numbers).

    {branches}

    {namedecode}

    {entrysteps}

    {flatten}

    {awkwardlib}

    {cache}

    {basketcache}

    {keycache}

    {executor}

    {localsource}

    {xrootdsource}

    {httpsource}

    {options}

    Returns
    -------
    dask.dataframe.core.DataFrame
        lazy files of branches of lazy baskets.
""".format(**dict(list(open_fragments.items()) + list(tree_fragments.items()))), width=TEXT_WIDTH)

################################################################ uproot3.tree.numentries

uproot3.tree.numentries.__doc__ = wrap(
u"""Get the number of entries in a TTree without fully opening the file.

    ``uproot3.numentries("file.root", "tree")`` is a shortcut for ``uproot3.open("file.root")["tree"].numentries`` that should be faster, particularly for files with many streamers and/or TTrees with many branches because it skips those steps in getting to the number of entries.

    If a requested file is not found, this raises the appropriate exception. If a requested file does not have the requested TTree, the number of entries is taken to be zero, raising no error.

    Parameters
    ----------
    path : str or list of str
        glob pattern(s) for local file paths (POSIX wildcards like "``*``") or URLs specifying the locations of the files. A list of filenames are processed in the given order, but glob patterns get pre-sorted to ensure a predictable order.

    treepath : str
        path within each ROOT file to find the TTree (may include "``/``" for subdirectories or "``;``" for cycle numbers).

    total : bool
        if ``True`` *(default)*, return an integer: the total number of entries for all files; otherwise, return an ``OrderedDict`` of path (str) \u2192 number of entries.

    {localsource}

    {xrootdsource}

    {httpsource}

    {executor}

    {blocking}

    Returns
    -------
    int or ``OrderedDict``
        total number of entries or number of entries for each file, depending on *total*.
""".format(**dict(list(open_fragments.items()) + list(tree_fragments.items()))), width=TEXT_WIDTH)

################################################################ uproot3.interp.interp.Interpretation

uproot3.interp.interp.Interpretation.__doc__ = wrap(
u"""Interface for interpretations.

    Interpretations do not need to inherit from this class, but they do need to satisfy the interface described below.

    Arrays and other collections are filled from ROOT in two stages: raw bytes from each basket are interpreted as a "source" and sources are copied into a branch-wide collection called the "destination" (often swapping bytes from big-endian to native-endian in the process). Public functions return a finalized destination. The distinction between source and destination (a) compactifies disparate baskets into a contiguous collection and (b) allows the output data to differ from the bytes on disk (byte swapping and other conversions).

    Interpretations must implement the following methods:

    **identifier**
        *(property)* a unique identifier for this interpretation, used as part of the cache key so that stale interpretations are not counted as cache hits.

    **empty(self)**
        return a zero-entry container (for special cases that can skip complex logic by returning an empty set).

    **compatible(self, other)**
        return ``True`` if and only if ``self`` and ``other`` interpretations would return equivalent results, such as different source interpretations that fill the same destination.

    **numitems(self, numbytes, numentries)**
        calculate the number of "items" (whatever that means for a given interpretation, but always greater than or equal to the number of entries), knowing only the number of bytes (``numbytes``) and the number of entries (``numentries``).

    **source_numitems(self, source)**
        calculate the number of "items" given a ``source`` instance.

    **fromroot(self, data, offsets, local_entrystart, local_entrystop, keylen)**
        produce a source from one basket ``data`` array (dtype ``numpy.uint8``) and its corresponding ``offsets`` array (dtype **numpy.int32** or ``None`` if not present) that has *n + 1* elements for *n* entries: ``offsets[0] == 0 and offsets[-1] == numentries``. The ``local_entrystart`` and ``local_entrystop`` are entry start (inclusive) and stop (exclusive), in which the first entry in the basket is number zero (hence "local"). The result of this operation may be a zero-copy cast of the basket data.

    **destination(self, numitems, numentries)**
        create or otherwise produce an unfilled destination object, knowing only the number of items (``numitems``) and number of entries (``numentries``).

    **fill(self, source, destination, itemstart, itemstop, entrystart, entrystop)**
        copy data from one basket``source`` (in its entirety) to part of the ``destination`` (usually a small slice). The items range from ``itemstart`` (inclusive) to ``itemstop`` (exclusive) and the entries range from ``entrystart`` (inclusive) to ``entrystop`` (exclusive). This function returns nothing; it is the only function in this interface called for its side-effects (the rest may be pure functions).

    **clip(self, destination, itemstart, itemstop, entrystart, entrystop)**
        return a slice of the ``destination`` from ``itemstart`` (inclusive) to ``itemstop`` (exclusive) and from ``entrystart`` (inclusive) to ``entrystop`` (exclusive). This is to trim memory allocated but not used, for instance if the entry range does not align with basket boundaries.

    **finalize(self, destination)**
        possibly post-process a ``destination`` to make it ready for consumption. This is needed if a different form must be used for filling than should be provided to the user--- for instance, offsets of a jagged array can't be computed when filling sections of it in parallel (sizes can), but the user should receive a jagged array based on offsets for random access.
""", width=TEXT_WIDTH)

################################################################ uproot3.interp.auto.interpret

uproot3.interp.auto.interpret.__doc__ = wrap(
u"""Generate a default interpretation of a branch.

    This function is called with default options on each branch in the following methods to generate a default interpretation. You can override the default either by calling this function explicitly with different parameters or by modifying its result.

    - :py:meth:`TTreeMethods.array <uproot3.tree.TTreeMethods.array>`
    - :py:meth:`TTreeMethods.arrays <uproot3.tree.TTreeMethods.arrays>`
    - :py:meth:`TTreeMethods.lazyarray <uproot3.tree.TTreeMethods.lazyarray>`
    - :py:meth:`TTreeMethods.lazyarrays <uproot3.tree.TTreeMethods.lazyarrays>`
    - :py:meth:`TTreeMethods.iterate <uproot3.tree.TTreeMethods.iterate>`
    - :py:meth:`TTreeMethods.iterate_clusters <uproot3.tree.TTreeMethods.iterate_clusters>`
    - :py:meth:`TBranchMethods.array <uproot3.tree.TBranchMethods.array>`
    - :py:meth:`TBranchMethods.lazyarray <uproot3.tree.TBranchMethods.lazyarray>`
    - :py:meth:`TBranchMethods.basket <uproot3.tree.TBranchMethods.basket>`
    - :py:meth:`TBranchMethods.baskets <uproot3.tree.TBranchMethods.baskets>`
    - :py:meth:`TBranchMethods.iterate_baskets <uproot3.tree.TBranchMethods.iterate_baskets>`

    Parameters
    ----------
    branch : :py:class:`TBranchMethods <uproot3.tree.TBranchMethods>`
        branch to interpret.

    awkwardlib : ``None``, str, or module
        if ``None`` *(default)*, use ``import awkward`` to get Awkward Array constructors. Otherwise, parse the module string name or use the provided module.

    classes : ``None`` or ``dict`` of str \u2192 :py:class:`ROOTStreamedObject <uproot3.rootio.ROOTStreamedObject>`
        class definitions associated with each class name, usually generated by ROOT file streamers. If ``None`` *(default)*, use the class definitions generated from the file from which this branch was read.

    swapbytes : bool
        if ``True``, generate an interpretation that converts ROOT's big-endian numbers into the machine-native endianness (usually little-endian).

    Returns
    -------
    :py:class:`Interpretation <uproot3.interp.interp.Interpretation>`
        the interpretation.
""", width=TEXT_WIDTH)

################################################################ uproot3.interp fragments

interp_fragments = {
    # see1
    "see1": u"""Part of the :py:class:`Interpretation <uproot3.interp.interp.Interpretation>` interface; type ``help(uproot3.interp.interp.Interpretation)`` for details.""",

    # see2
    "see2": u"""Methods implementing the :py:class:`Interpretation <uproot3.interp.interp.Interpretation>` interface are not documented here.""",
    }

################################################################ uproot3.interp.numerical fragments

interp_numerical_fragments = {
    # items
    "items": u"""In this interpretation, "items" (for ``numitems``, ``itemstart``, ``itemstop``, etc.) has the same meaning as in Numpy: an item is a single scalar value. For example, 100 entries of 2\u00d72 matrices (``todims == (2, 2)``) is 400 items.""",

    # fromdtype
    "fromdtype": u"""fromdtype : ``numpy.dtype``
        the source type; the meaning associated with bytes in the ROOT file. Should be big-endian (e.g. ``">i4"`` for 32-bit integers and ``">f8"`` for 64-bit floats).""",

    # fromdims
    "fromdims": u"""fromdims : tuple of ints
        Numpy shape of each source entry. The Numpy shape of the whole source array is ``(numentries,) + fromdims``. Default is ``()`` (scalar).""",
    }

################################################################ uproot3.interp.numerical.asdtype

uproot3.interp.numerical.asdtype.__doc__ = wrap(
u"""Interpret branch data as a new Numpy array with given dtypes and dimensions.

    This interpretation directs branch-reading functions to allocate new Numpy arrays and fill them with the branch contents. See :py:class:`asarray <uproot3.interp.numerical.asarray>` to fill an existing array, rather than filling a new array.

    {items}

    Parameters
    ----------
    {fromdtype}

    todtype : ``None`` or ``numpy.dtype``
        the destination type; the conversion performed if different from the source type. If ``None`` *(default)*, the destination type will be a native-endian variant of the source type, so that a byte-swap is performed.

    {fromdims}

    todims : ``None`` or tuple of ints
        Numpy shape of each destination entry. The Numpy shape of the whole destination array is ``(numentries,) + todims``. If ``None`` *(default)*, ``todims`` will be equal to ``fromdims``. Making them different allows you to reshape arrays while reading.

    Notes
    -----

    {see2}
""".format(**dict(list(interp_fragments.items()) + list(interp_numerical_fragments.items()))), width=TEXT_WIDTH)

_method(uproot3.interp.numerical.asdtype.to).__doc__ = wrap(
u"""Create a new :py:class:`asdtype <uproot3.interp.numerical.asdtype>` interpretation from this one.

    Parameters
    ----------
    todtype : ``None`` or ``numpy.dtype``
        if not ``None``, change the destination type.

    todims : ``None`` or tuple of ints
        if not ``None``, change the destination dimensions.

    Returns
    -------
    :py:class:`asdtype <uproot3.interp.numerical.asdtype>`
        new interpretation.
""", width=TEXT_WIDTH)

_method(uproot3.interp.numerical.asdtype.toarray).__doc__ = wrap(
u"""Create a :py:class:`asarray <uproot3.interp.numerical.asarray>` interpretation from this one.

    Parameters
    ----------
    array : ``numpy.ndarray``
        the array to fill, instead of allocating a new one.

    Returns
    -------
    :py:class:`asarray <uproot3.interp.numerical.asarray>`
        new interpretation.
""", width=TEXT_WIDTH)

_method(uproot3.interp.numerical.asdtype.empty).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.numerical.asdtype.compatible).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.numerical.asdtype.numitems).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.numerical.asdtype.source_numitems).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.numerical.asdtype.fromroot).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.numerical.asdtype.destination).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.numerical.asdtype.fill).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.numerical.asdtype.clip).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.numerical.asdtype.finalize).__doc__ = interp_fragments["see1"]

################################################################ uproot3.interp.numerical.asarray

uproot3.interp.numerical.asarray.__doc__ = wrap(
u"""Interpret branch as array data that should overwrite an existing array.

    This interpretation directs branch-reading functions to fill the given Numpy array with branch contents. See :py:class:`asdtype <uproot3.interp.numerical.asdtype>` to allocate a new array, rather than filling an existing array.

    {items}

    Parameters
    ----------
    {fromdtype}

    toarray : ``numpy.ndarray``
        array to be filled; must be at least as large as the branch data.

    {fromdims}

    Notes
    -----

    {see2}

    This class has *todtype* and *todims* parameters like :py:class:`asdtype <uproot3.interp.numerical.asdtype>`, but they are derived from the *toarray* attribute.
""".format(**dict(list(interp_fragments.items()) + list(interp_numerical_fragments.items()))), width=TEXT_WIDTH)

_method(uproot3.interp.numerical.asarray.destination).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.numerical.asarray.fill).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.numerical.asarray.clip).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.numerical.asarray.finalize).__doc__ = interp_fragments["see1"]

################################################################ uproot3.interp.jagged.asjagged

uproot3.interp.jagged.asjagged.__doc__ = wrap(
u"""Interpret branch as a jagged array (array of non-uniformly sized arrays).

    This interpretation directs branch-reading to fill contiguous arrays and present them to the user in a ``JaggedArray`` interface. Such an object behaves as though it were an array of non-uniformly sized arrays, but it is more memory and cache-line efficient because the underlying data are contiguous.

    In this interpretation, "items" (for ``numitems``, ``itemstart``, ``itemstop``, etc.) are the items of the inner array (however that is defined), and "entries" are elements of the outer array. The outer array is always one-dimensional.

    Parameters
    ----------
    asdtype : :py:class:`asdtype <uproot3.interp.numerical.asdtype>`
        interpretation for the inner arrays.

    Notes
    -----

    {see2}
""".format(**interp_fragments), width=TEXT_WIDTH)

_method(uproot3.interp.jagged.asjagged.to).__doc__ = wrap(
u"""Create a new :py:class:`asjagged <uproot3.interp.jagged.asjagged>` interpretation from this one.

    Parameters
    ----------
    todtype : ``None`` or ``numpy.dtype``
        if not ``None``, change the destination type of inner arrays.

    todims : ``None`` or tuple of ints
        if not ``None``, change the destination dimensions of inner arrays.

    Returns
    -------
    :py:class:`asjagged <uproot3.interp.jagged.asjagged>`
        new interpretation.
""", width=TEXT_WIDTH)

_method(uproot3.interp.jagged.asjagged.empty).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.jagged.asjagged.compatible).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.jagged.asjagged.numitems).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.jagged.asjagged.source_numitems).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.jagged.asjagged.fromroot).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.jagged.asjagged.destination).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.jagged.asjagged.fill).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.jagged.asjagged.clip).__doc__ = interp_fragments["see1"]
_method(uproot3.interp.jagged.asjagged.finalize).__doc__ = interp_fragments["see1"]

# TODO: add asdtype asarray asdouble32 asstlbitset asjagged astable asobj asgenobj asstring STLVector STLString

################################################################ uproot3.source.cursor.Cursor

uproot3.source.cursor.Cursor.__doc__ = wrap(
u"""Maintain a position in a :py:class:`Source <uproot3.source.source.Source>` that updates as data are read.

    **Attributes, properties, and methods:**

    - **index** (*int*) the position.
    - **origin** (*int*) "beginning of buffer" position, used in the **refs** key in :py:func:`uproot3.rootio._readobjany <uproot3.rootio._readobjany>`.
    - **refs** (``None`` or ``dict``-like) manages cross-references in :py:func:`uproot3.rootio._readobjany <uproot3.rootio._readobjany>`.
    - :py:meth:`copied <uproot3.source.cursor.Cursor.copied>` return a copy of this :py:class:`Cursor <uproot3.source.cursor.Cursor>` with modifications.
    - :py:meth:`skipped <uproot3.source.cursor.Cursor.skipped>` return a copy of this :py:class:`Cursor <uproot3.source.cursor.Cursor>` with the **index** moved forward.
    - :py:meth:`skip <uproot3.source.cursor.Cursor.skip>` move the **index** of this :py:class:`Cursor <uproot3.source.cursor.Cursor>` forward.
    - :py:meth:`fields <uproot3.source.cursor.Cursor.fields>` interpret bytes in the :py:class:`Source <uproot3.source.source.Source>` with given data types and skip the **index** past them.
    - :py:meth:`field <uproot3.source.cursor.Cursor.field>` interpret bytes in the :py:class:`Source <uproot3.source.source.Source>` with a given data type and skip the **index** past it.
    - :py:meth:`bytes <uproot3.source.cursor.Cursor.bytes>` return a range of bytes from the :py:class:`Source <uproot3.source.source.Source>` and skip the **index** past it.
    - :py:meth:`array <uproot3.source.cursor.Cursor.array>` return a range of bytes from the :py:class:`Source <uproot3.source.source.Source>` as a typed Numpy array and skip the **index** past it.
    - :py:meth:`string <uproot3.source.cursor.Cursor.string>` read a string from the :py:class:`Source <uproot3.source.source.Source>`, interpreting the first 1 or 5 bytes as a size and skip the **index** past it.
    - :py:meth:`cstring <uproot3.source.cursor.Cursor.cstring>` read a null-terminated string from the :py:class:`Source <uproot3.source.source.Source>` and skip the **index** past it.
    - :py:meth:`skipstring <uproot3.source.cursor.Cursor.skipstring>` interpret the first 1 or 5 bytes as a size and skip the **index** past the string (without creating a Python string).
    - :py:meth:`hexdump <uproot3.source.cursor.Cursor.hexdump>` view a section of the :py:class:`Source <uproot3.source.source.Source>` as formatted by the POSIX ``hexdump`` program and *do not* move the **index**.

    Parameters
    ----------
    index : int
       the initial **index**.

    origin : int
       the **origin**, *(default is 0)*.

    refs : ``None`` or ``dict``-like
       if ``None`` *(default)*, use a new dict as the **ref**; otherwise, use the value provided.
""", width=TEXT_WIDTH)

format_source_cursor = {
    # source
    "source": u"""source : :py:class:`Source <uproot3.source.source.Source>`
        data to be read."""
    }

_method(uproot3.source.cursor.Cursor.copied).__doc__ = wrap(
u"""Return a copy of this :py:class:`Cursor <uproot3.source.cursor.Cursor>` with modifications.

    Parameters
    ----------
    index : ``None`` or int
        if not ``None`` *(default)*, use this as the new index position.

    origin : ``None`` or int
        if not ``None`` *(default)*, use this as the new origin.

    refs : ``None`` or ``dict``-like
        if not ``None`` *(default)*, use this as the new refs.

    Returns
    -------
    :py:class:`Cursor <uproot3.source.cursor.Cursor>`
        the new cursor.

    Notes
    -----

    This is a shallow copy--- the **refs** are shared with the parent and all other copies.
""".format(**format_source_cursor), width=TEXT_WIDTH)

_method(uproot3.source.cursor.Cursor.skipped).__doc__ = wrap(
u"""Return a copy of this :py:class:`Cursor <uproot3.source.cursor.Cursor>` with the **index** moved forward.

    Parameters
    ----------
    numbytes : int
        number of bytes to be skipped in the copy, leaving the original unchanged.

    origin : ``None`` or int
        if not ``None`` *(default)*, use this as the new origin.

    refs : ``None`` or ``dict``-like
        if not ``None`` *(default)*, use this as the new refs.

    Returns
    -------
    :py:class:`Cursor <uproot3.source.cursor.Cursor>`
        the new cursor.

    Notes
    -----

    This is a shallow copy--- the **refs** are shared with the parent and all other copies.
""".format(**format_source_cursor), width=TEXT_WIDTH)

_method(uproot3.source.cursor.Cursor.skip).__doc__ = wrap(
u"""Move the **index** of this :py:class:`Cursor <uproot3.source.cursor.Cursor>` forward.

    Parameters
    ----------
    numbytes : int
        number of bytes to skip
""".format(**format_source_cursor), width=TEXT_WIDTH)

_method(uproot3.source.cursor.Cursor.fields).__doc__ = wrap(
u"""Interpret bytes in the :py:class:`Source <uproot3.source.source.Source>` with given data types and skip the **index** past them.

    Parameters
    ----------
    {source}

    format : ``struct.Struct``
        compiled parser from Python's ``struct`` library.

    Returns
    -------
    tuple
        field values (types determined by format)
""".format(**format_source_cursor), width=TEXT_WIDTH)

_method(uproot3.source.cursor.Cursor.field).__doc__ = wrap(
u"""Interpret bytes in the :py:class:`Source <uproot3.source.source.Source>` with a given data type and skip the **index** past it.

    Parameters
    ----------
    {source}

    format : ``struct.Struct``
        compiled parser from Python's ``struct`` library; must return only one field.

    Returns
    -------
    type determined by format
        field value
""".format(**format_source_cursor), width=TEXT_WIDTH)

_method(uproot3.source.cursor.Cursor.bytes).__doc__ = wrap(
u"""Return a range of bytes from the :py:class:`Source <uproot3.source.source.Source>` and skip the **index** past it.

    Parameters
    ----------
    {source}

    length : int
        number of bytes.

    Returns
    -------
    ``numpy.ndarray`` of ``numpy.uint8``
        raw view of data from source.
""".format(**format_source_cursor), width=TEXT_WIDTH)

_method(uproot3.source.cursor.Cursor.array).__doc__ = wrap(
u"""Return a range of bytes from the :py:class:`Source <uproot3.source.source.Source>` as a typed Numpy array and skip the **index** past it.

    Parameters
    ----------
    {source}

    length : int
        number of items.

    dtype : ``numpy.dtype``
        type of the array.

    Returns
    -------
    ``numpy.ndarray``
        interpreted view of data from source.
""".format(**format_source_cursor), width=TEXT_WIDTH)

_method(uproot3.source.cursor.Cursor.string).__doc__ = wrap(
u"""Read a string from the :py:class:`Source <uproot3.source.source.Source>`, interpreting the first 1 or 5 bytes as a size and skip the **index** past it.

    Parameters
    ----------
    {source}

    Returns
    -------
    bytes
        Python string (``bytes`` in Python 3).
""".format(**format_source_cursor), width=TEXT_WIDTH)

_method(uproot3.source.cursor.Cursor.cstring).__doc__ = wrap(
u"""Read a null-terminated string from the :py:class:`Source <uproot3.source.source.Source>` and skip the **index** past it.

    The index is also skipped past the null that terminates the string.

    Parameters
    ----------
    {source}

    Returns
    -------
    bytes
        Python string (``bytes`` in Python 3).
""".format(**format_source_cursor), width=TEXT_WIDTH)

_method(uproot3.source.cursor.Cursor.skipstring).__doc__ = wrap(
u"""Interpret the first 1 or 5 bytes as a size and skip the **index** past the string (without creating a Python string).

    Parameters
    ----------
    {source}
""".format(**format_source_cursor), width=TEXT_WIDTH)

_method(uproot3.source.cursor.Cursor.hexdump).__doc__ = wrap(
u"""View a section of the :py:class:`Source <uproot3.source.source.Source>` as formatted by the POSIX ``hexdump`` program and *do not* move the **index**.

    This is much more useful than simply hexdumping the whole file, since partial interpretation is necessary to find the right point in the file to dump.

    Parameters
    ----------
    {source}

    size : int
        number of bytes to view; default is 160 (10 lines).

    offset : int
        where to start the view, relative to index; default is 0 (at index).

    format : str
        Python's printf-style format string for individual bytes; default is "%02x" (zero-prefixed, two-character hexidecimal).

    Returns
    -------
    str
        hexdump-formatted view to be printed
""".format(**format_source_cursor), width=TEXT_WIDTH)

################################################################ uproot3.source.source.Source

uproot3.source.source.Source.__doc__ = wrap(
u"""Interface for data sources.

    Sources do not need to inherit from this class, but they do need to satisfy the interface described below.

    **parent(self)**
        return the :py:class:`Source <uproot3.source.source.Source>` from which this was copied; may be ``None``.

    **threadlocal(self)**
        either return ``self`` (if thread-safe) or return a thread-safe copy, such as a new file handle into the same file.

    **dismiss(self)**
        thread-local copies are no longer needed; they may be eliminated if redundant.

    **data(self, start, stop, dtype=None)**
        return a view of data from the starting byte (inclusive) to the stopping byte (exclusive), with a given Numpy type (numpy.uint8 if ``None``).
""", width=TEXT_WIDTH)

source_fragments = {
    # see1
    "see1": u"""Part of the :py:class:`Source <uproot3.source.source.Source>` interface; type ``help(uproot3.source.source.Source)`` for details.""",

    # see2
    "see2": u"""Methods implementing the :py:class:`Source <uproot3.source.source.Source>` interface are not documented here.""",
    }

################################################################ uproot3.source.file.FileSource

uproot3.source.file.FileSource.__doc__ = wrap(
u"""Emulate a memory-mapped interface with traditional file handles, opening many if necessary.

    :py:class:`FileSource <uproot3.source.file.FileSource>` objects avoid double-reading and many small reads by caching data in chunks. All thread-local copies of a :py:class:`FileSource <uproot3.source.file.FileSource>` share a :py:class:`ThreadSafeArrayCache <uproot3.cache.ThreadSafeArrayCache>` to avoid double-reads across threads.

    Parameters
    ----------
    path : str
        local file path of the input file (it must not be moved during reading!).

    chunkbytes : int or string matching number + /[kMGTPEZY]?B/i
        number of bytes per chunk.

    limitbytes : int or string matching number + /[kMGTPEZY]?B/i
        maximum number of bytes to keep in the cache.

    Notes
    -----

    {see2}
""".format(**source_fragments), width=TEXT_WIDTH)

_method(uproot3.source.file.FileSource.parent).__doc__ = source_fragments["see1"]
_method(uproot3.source.file.FileSource.threadlocal).__doc__ = source_fragments["see1"]
_method(uproot3.source.file.FileSource.dismiss).__doc__ = source_fragments["see1"]
_method(uproot3.source.file.FileSource.data).__doc__ = source_fragments["see1"]

################################################################ uproot3.source.memmap.MemmapSource

uproot3.source.memmap.MemmapSource.__doc__ = wrap(
u"""Thin wrapper around a memory-mapped file, which already behaves like a :py:class:`Source <uproot3.source.source.Source>`.

    Parameters
    ----------
    path : str
        local file path of the input file.

    Notes
    -----

    {see2}
""".format(**source_fragments), width=TEXT_WIDTH)

_method(uproot3.source.memmap.MemmapSource.parent).__doc__ = source_fragments["see1"]
_method(uproot3.source.memmap.MemmapSource.threadlocal).__doc__ = source_fragments["see1"]
_method(uproot3.source.memmap.MemmapSource.dismiss).__doc__ = source_fragments["see1"]
_method(uproot3.source.memmap.MemmapSource.data).__doc__ = source_fragments["see1"]

################################################################ uproot3.source.xrootd.XRootDSource

uproot3.source.xrootd.XRootDSource.__doc__ = wrap(
u"""Emulate a memory-mapped interface with XRootD.

    XRootD is already thread-safe, but provides no caching. :py:class:`XRootDSource <uproot3.source.xrootd.XRootDSource>` objects avoid double-reading and many small reads by caching data in chunks. They are not duplicated when splitting into threads.

    Parameters
    ----------
    path : str
        remote file URL.

    chunkbytes : int or string matching number + /[kMGTPEZY]?B/i
        number of bytes per chunk.

    limitbytes : int or string matching number + /[kMGTPEZY]?B/i
        maximum number of bytes to keep in the cache.

    Notes
    -----

    {see2}
""".format(**source_fragments), width=TEXT_WIDTH)

_method(uproot3.source.xrootd.XRootDSource.parent).__doc__ = source_fragments["see1"]
_method(uproot3.source.xrootd.XRootDSource.threadlocal).__doc__ = source_fragments["see1"]
_method(uproot3.source.xrootd.XRootDSource.dismiss).__doc__ = source_fragments["see1"]
_method(uproot3.source.xrootd.XRootDSource.data).__doc__ = source_fragments["see1"]

################################################################ uproot3.source.compressed.Compression

uproot3.source.compressed.Compression.__doc__ = wrap(
u"""Describe the compression of a compressed block.

    **Attributes, properties, and methods:**

    - **algo** (*int*) algorithm code.
    - **level** (*int*) 0 is no compression, 1 is least, 9 is most.
    - **algoname** (*str*) algorithm expressed as a string: ``"zlib"``, ``"lzma"``, ``"old"``, ``"lz4"`` or ``"zstd"``.
    - **copy(algo=None, level=None)** copy this :py:class:`Compression <uproot3.source.compressed.Compression>` object, possibly changing a field.
    - **decompress(source, cursor, compressedbytes, uncompressedbytes)** decompress data from **source** at **cursor**, knowing the compressed and uncompressed size.

    Parameters
    ----------
    fCompress : int
        ROOT fCompress field.
""", width=TEXT_WIDTH)

################################################################ uproot3.source.compressed.CompressedSource

uproot3.source.compressed.CompressedSource.__doc__ = wrap(
u"""A :py:class:`Source <uproot3.source.source.Source>` for compressed data.

    Decompresses on demand--- without caching the result--- so cache options in higher-level array functions are very important.

    Ordinary users would never create a :py:class:`CompressedSource <uproot3.source.compressed.CompressedSource>`. They are produced when a TKey encounters a compressed value.

    Parameters
    ----------
    compression : :py:class:`Compression <uproot3.source.compressed.Compression>`
        inherited description of the compression. Note that *this is overridden* by the first two bytes of the compressed block, which can disagree with the higher-level description and takes precedence.

    source : :py:class:`Source <uproot3.source.source.Source>`
        the source in which compressed data may be found.

    cursor : :py:class:`Cursor <uproot3.source.cursor.Cursor>`
        location in the source.

    compressedbytes : int
        number of bytes after compression.

    uncompressedbytes : int
        number of bytes before compression.
""", width=TEXT_WIDTH)

################################################################ uproot3.cache.ArrayCache

uproot3.cache.ArrayCache.__doc__ = wrap(
u"""A cache (wrapping cachetools) whose eviction threshold is determined by total array size.

    Uses the nbytes property of all values to determine total size. By default, cachetools only counts the number of objects, ignoring their sizes.

    Parameters
    ----------
    limitbytes : int or string matching number + /[kMGTPEZY]?B/i
        maximum number of bytes to keep in the cache.

    method : "LRU" *(default)* or "LFU"
        least recently used or least frequently used
""", width=TEXT_WIDTH)

################################################################ uproot3.cache.ThreadSafeArrayCache

uproot3.cache.ThreadSafeArrayCache.__doc__ = wrap(
u"""An :py:class:`ArrayCache <uproot3.cache.ArrayCache>` with locks for thread safety.

    Parameters
    ----------
    limitbytes : int or string matching number + /[kMGTPEZY]?B/i
        maximum number of bytes to keep in the cache.

    method : "LRU" *(default)* or "LFU"
        least recently used or least frequently used
""", width=TEXT_WIDTH)
