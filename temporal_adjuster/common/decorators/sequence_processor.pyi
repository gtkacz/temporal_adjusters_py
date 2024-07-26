from typing import TypeVar

T = TypeVar('T')

def sequenceable(target: str):
	"""
	This decorator is used to process if a sequence of values passed as an argument to a function. The function is called for each value in the sequence, and the result is stored in the same position in the sequence.
	"""
