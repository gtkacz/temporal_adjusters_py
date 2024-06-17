import inspect
from functools import wraps
from typing import Callable, Sequence, TypeVar, Union

T = TypeVar('T')


def sequenceable(target: str):
    """
    This decorator is used to process if a sequence of values passed as an argument to a function. The function is called for each value in the sequence, and the result is stored in the same position in the sequence.
    """
    def decorator(func: Callable[..., T]) -> Callable[..., Union[T, Sequence[T]]]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Union[T, Sequence[T]]:
            # Get the function signature
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Determine if the target parameter is in args or kwargs
            target_value = bound_args.arguments.get(target)

            if target_value is not None and hasattr(target_value, '__iter__') and not isinstance(target_value, str):
                convert_back = None

                if type(target_value) in [set, tuple]:
                    convert_back = type(target_value)
                    target_value = list(target_value)

                for index, item in enumerate(target_value):
                    bound_args.arguments[target] = item
                    result = func(*bound_args.args, **bound_args.kwargs)
                    target_value[index] = result

                return target_value if convert_back is None else convert_back(target_value)

            else:
                return func(*args, **kwargs)

        return wrapper

    return decorator
