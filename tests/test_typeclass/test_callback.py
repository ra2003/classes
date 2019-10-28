# -*- coding: utf-8 -*-

from typing import Callable

from classes import TypeClass, typeclass


@typeclass
def example(instance) -> int:
    """Example typeclass."""


@example.instance(str)
def _example_str(instance: str) -> int:
    return len(instance)


def _callback(
    instance: str,
    callback: TypeClass[str, int, Callable[[str], int]],
) -> int:
    return callback(instance)


def test_callback():
    """Tests that callback works."""
    assert _callback('a', example) == 1
    assert _callback('abcd', example) == 4