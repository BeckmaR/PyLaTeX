# -*- coding: utf-8 -*-
"""
    pylatex.arguments
    ~~~~~~~

    This module implements the classes that deal with parameters, in particular with options and arguments.

    :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""
from .base_classes import BaseLaTeXClass


class Parameters(BaseLaTeXClass):
    """
    A class implementing LaTex parameters. It supports normal positional parameters, as well as key-value pairs.
    Parameters can be rendered optional within square brackets ``[]`` or required within braces ``{}``.
    ::
        >>> args = Parameters('a', 'b', 'c')
        >>> args.dumps()
        '{a}{b}{c}'
        >>> args.optional = True
        >>> args.dumps()
        '[a,b,c]'
        >>> args = Parameters('clip', width=50, height='25em', trim='1 2 3 4')
        >>> args.optional = True
        >>> args.dumps()
        '[clip,trim=1 2 3 4,width=50,height=25em]'

    :param optional: Specifies whether this parameters are optional or not
    :type optional: bool
    """

    optional = False

    def __init__(self, *args, **kwargs):
        self._positional_args = list(args)
        self._key_value_args = dict(kwargs)
        super().__init__(packages=None)

    def __key(self):
        return self.optional, tuple(self.list())

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())

    def dumps(self):
        """
        Represents the parameters as a string in LaTeX syntax to be appended to a command.

        :return: The rendered parameters
        :rtype: str
        """
        params = self.list()
        if len(params) <= 0:
            return ''
        if self.optional:
            string = '[{args}]'.format(args=','.join(list(map(str, params))))
        else:
            string = '{{{args}}}'.format(args='}{'.join(list(map(str, params))))
        return string

    def list(self):
        params = []
        params.extend(self._positional_args)
        params.extend(['{k}={v}'.format(k=k, v=v) for k, v in self._key_value_args.items()])
        return params


class Options(Parameters):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.optional = True


class Arguments(Parameters):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.optional = False