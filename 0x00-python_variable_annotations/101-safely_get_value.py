#!/usr/bin/env python3
"""More involved type annotations"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')
ret_t = Union[Any, T]
def_t = Optional[T]


def safely_get_value(dct: Mapping, key: Any, default: def_t = None) -> ret_t:
    if key in dct:
        return dct[key]
    else:
        return default
