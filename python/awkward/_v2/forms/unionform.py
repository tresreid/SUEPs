# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE

from collections.abc import Iterable

import awkward as ak
from awkward._v2.forms.form import Form, _parameters_equal


class UnionForm(Form):
    is_UnionType = True

    def __init__(
        self,
        tags,
        index,
        contents,
        has_identifier=False,
        parameters=None,
        form_key=None,
    ):
        if not ak._util.isstr(tags):
            raise TypeError(
                "{} 'tags' must be of type str, not {}".format(
                    type(self).__name__, repr(tags)
                )
            )
        if not ak._util.isstr(index):
            raise TypeError(
                "{} 'index' must be of type str, not {}".format(
                    type(self).__name__, repr(index)
                )
            )
        if not isinstance(contents, Iterable):
            raise TypeError(
                "{} 'contents' must be iterable, not {}".format(
                    type(self).__name__, repr(contents)
                )
            )
        for content in contents:
            if not isinstance(content, Form):
                raise TypeError(
                    "{} all 'contents' must be Form subclasses, not {}".format(
                        type(self).__name__, repr(content)
                    )
                )

        self._tags = tags
        self._index = index
        self._contents = list(contents)
        self._init(has_identifier, parameters, form_key)

    @property
    def tags(self):
        return self._tags

    @property
    def index(self):
        return self._index

    @property
    def contents(self):
        return self._contents

    def content(self, index):
        return self._contents[index]

    def __repr__(self):
        args = [
            repr(self._tags),
            repr(self._index),
            repr(self._contents),
        ] + self._repr_args()
        return "{}({})".format(type(self).__name__, ", ".join(args))

    def _tolist_part(self, verbose, toplevel):
        return self._tolist_extra(
            {
                "class": "UnionArray",
                "tags": self._tags,
                "index": self._index,
                "contents": [
                    content._tolist_part(verbose, toplevel=False)
                    for content in self._contents
                ],
            },
            verbose,
        )

    def _type(self, typestrs):
        return ak._v2.types.uniontype.UnionType(
            [x._type(typestrs) for x in self._contents],
            self._parameters,
            ak._v2._util.gettypestr(self._parameters, typestrs),
        )

    def __eq__(self, other):
        if (
            isinstance(other, UnionForm)
            and self._has_identifier == other._has_identifier
            and self._form_key == other._form_key
            and self._tags == other._tags
            and self._index == other._index
            and len(self._contents) == len(other._contents)
            and _parameters_equal(self._parameters, other._parameters)
        ):
            return self._contents == other._contents

        return False

    def generated_compatibility(self, other):
        if other is None:
            return True

        elif isinstance(other, UnionForm):
            if len(self._contents) == len(other._contents):
                return _parameters_equal(self._parameters, other._parameters) and all(
                    x.generated_compatibility(y)
                    for x, y in zip(self._contents, other._contents)
                )
            else:
                return False

        else:
            return False

    def _getitem_range(self):
        return UnionForm(
            self._tags,
            self._index,
            self._contents,
            has_identifier=self._has_identifier,
            parameters=self._parameters,
            form_key=None,
        )

    def _getitem_field(self, where, only_fields=()):
        return UnionForm(
            self._tags,
            self._index,
            self._content._getitem_field(where, only_fields),
            has_identifier=self._has_identifier,
            parameters=None,
            form_key=None,
        )

    def _getitem_fields(self, where, only_fields=()):
        return UnionForm(
            self._tags,
            self._index,
            self._content._getitem_fields(where, only_fields),
            has_identifier=self._has_identifier,
            parameters=None,
            form_key=None,
        )

    def _carry(self, allow_lazy):
        return UnionForm(
            self._tags,
            self._index,
            self._contents,
            has_identifier=self._has_identifier,
            parameters=self._parameters,
            form_key=None,
        )

    def simplify_uniontype(self, merge=True, mergebool=False):
        raise NotImplementedError

    def purelist_parameter(self, key):
        if self._parameters is None or key not in self._parameters:
            out = self._contents[0].purelist_parameter(key)
            for content in self._contents[1:]:
                tmp = content.purelist_parameter(key)
                if out != tmp:
                    return None
            return out
        else:
            return self._parameters[key]

    @property
    def purelist_isregular(self):
        for content in self._contents:
            if not content.purelist_isregular:
                return False
        return True

    @property
    def purelist_depth(self):
        out = None
        for content in self._contents:
            if out is None:
                out = content.purelist_depth
            elif out != content.purelist_depth:
                return -1
        return out

    @property
    def minmax_depth(self):
        if len(self._contents) == 0:
            return (0, 0)
        mins, maxs = [], []
        for content in self._contents:
            mindepth, maxdepth = content.minmax_depth
            mins.append(mindepth)
            maxs.append(maxdepth)
        return (min(mins), max(maxs))

    @property
    def branch_depth(self):
        if len(self._contents) == 0:
            return (False, 1)
        anybranch = False
        mindepth = None
        for content in self._contents:
            branch, depth = content.branch_depth
            if mindepth is None:
                mindepth = depth
            if branch or mindepth != depth:
                anybranch = True
            if mindepth > depth:
                mindepth = depth
        return (anybranch, mindepth)

    @property
    def fields(self):
        fieldslists = [cont.fields for cont in self._contents]
        return list(set.intersection(*[set(x) for x in fieldslists]))

    @property
    def dimension_optiontype(self):
        for content in self._contents:
            if content.dimension_optiontype:
                return True
        return False
