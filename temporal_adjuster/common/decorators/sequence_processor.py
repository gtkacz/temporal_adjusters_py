import inspect
from functools import wraps
from typing import Sequence, TypeVar, Union

import numpy as np

T = TypeVar("T")


def sequenceable(target: str):
    """
    This decorator is used to process if a sequence of values passed as an argument to a function. The function is called for each value in the sequence, and the result is stored in the same position in the sequence.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Union[T, Sequence[T]]:
            # Get the function signature
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Determine if the target parameter is in args or kwargs
            target_value = bound_args.arguments.get(target)

            if (
                target_value is not None
                and hasattr(target_value, "__iter__")
                and not isinstance(target_value, str)
            ):
                convert_type = type(target_value)
                target_value = np.asarray(list(target_value))

                for index, item in np.ndenumerate(target_value):
                    bound_args.arguments[target] = item
                    result = func(*bound_args.args, **bound_args.kwargs)
                    target_value[index[0]] = result

                return convert_type(target_value.tolist())

            else:
                return func(*args, **kwargs)

        return wrapper

    return decorator
