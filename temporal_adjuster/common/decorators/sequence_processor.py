# Copyright (c) 2024 Gabriel Mitelman Tkacz
"""Decorators for applying temporal adjustments to sequences."""

import inspect
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, Protocol, TypeVar, cast, overload

import numpy as np

P = ParamSpec("P")
R_co = TypeVar("R_co", covariant=True)


class _SequenceableCallable(Protocol[P, R_co]):
    """A scalar callable with a permissive fallback for container arguments."""

    @overload
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R_co: ...

    @overload
    def __call__(self, *args: object, **kwargs: object) -> object: ...


def sequenceable(target: str) -> Callable[[Callable[P, R_co]], _SequenceableCallable[P, R_co]]:
    """Process sequence arguments elementwise.

    If the target parameter (specified by `target`) is an iterable (but not a string),
    the function is called for each value in the sequence, and the result is stored in the
    corresponding position in the sequence. Otherwise, the function is called with the
    provided arguments as usual.

    Returns:
        Callable: A decorator that applies the wrapped function elementwise when needed.
    """

    def decorator(func: Callable[P, R_co]) -> _SequenceableCallable[P, R_co]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> object:
            # Get the function signature and bind the provided arguments.
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Get the value of the target parameter.
            target_value = bound_args.arguments.get(target)

            # If target_value is iterable (and not a string), apply the function elementwise.
            if target_value is not None and hasattr(target_value, "__iter__") and not isinstance(target_value, str):
                convert_type = type(target_value)
                results = []

                for item in target_value:
                    bound_args.arguments[target] = item
                    results.append(func(*bound_args.args, **bound_args.kwargs))

                if isinstance(target_value, np.ndarray):
                    return np.asarray(results)
                return convert_type(results)
            return func(*args, **kwargs)

        return cast("_SequenceableCallable[P, R_co]", wrapper)

    return decorator
