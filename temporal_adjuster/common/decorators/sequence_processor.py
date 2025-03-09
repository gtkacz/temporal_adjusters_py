import inspect
from functools import wraps
from typing import Any, Callable, TypeVar, Union

try:
	from typing import ParamSpec  # Python 3.10+
except ImportError:
	from typing_extensions import ParamSpec  # type: ignore

import numpy as np

P = ParamSpec('P')
R = TypeVar('R')


def sequenceable(target: str) -> Callable[[Callable[P, R]], Callable[P, Union[R, Any]]]:
	"""
	This decorator processes a sequence of values passed as an argument to a function.
	If the target parameter (specified by `target`) is an iterable (but not a string),
	the function is called for each value in the sequence, and the result is stored in the
	corresponding position in the sequence. Otherwise, the function is called with the
	provided arguments as usual.
	"""

	def decorator(func: Callable[P, R]) -> Callable[P, Union[R, Any]]:
		@wraps(func)
		def wrapper(*args: P.args, **kwargs: P.kwargs) -> Union[R, Any]:
			# Get the function signature and bind the provided arguments.
			sig = inspect.signature(func)
			bound_args = sig.bind(*args, **kwargs)
			bound_args.apply_defaults()

			# Get the value of the target parameter.
			target_value = bound_args.arguments.get(target)

			# If target_value is iterable (and not a string), apply the function elementwise.
			if (
				target_value is not None
				and hasattr(target_value, '__iter__')
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
