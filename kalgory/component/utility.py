import json
from typing import get_type_hints

from kalgory.bindings.block import Block


def zipjson(block_output: any) -> bytes:
    if isinstance(block_output, dict):
        # If block_output is a dict, use its items directly as a list of key-value pairs
        j_array = [{"key": key, "value": value} for key, value in block_output.items()]
    elif isinstance(block_output, (list, tuple)):
        # If block_output is a list or tuple, use its items directly
        j_array = list(block_output)
    elif isinstance(block_output, (int, str, bool, float)):
        # If block_output is a single value, create a single-item array
        j_array = [block_output]
    else:
        # Handle other types or raise an error if necessary
        raise TypeError("Unsupported type for block_output")
    return json.dumps(j_array).encode("utf-8")


def validate(ins: Block, jsondata: list):
    # check length
    if len(jsondata) != ins.handle.__code__.co_argcount - 1:  # -1 bcs of self
        raise RuntimeError(
            f'Block "{ins.__class__.__name__}" expects '
            f"{ins.handle.__code__.co_argcount} arguments, but received "
            f"{len(jsondata)} arguments from previous blocks"
        )
    # check if every parameter is annotated
    hints = get_type_hints(ins.handle)
    if ins.handle.__code__.co_argcount != len(hints):
        raise TypeError("Every input/argument must be assigned type")
    # check type
    # list and tuple types are confusing in python, for now only simple checks is implemented
    # TODO: add checks of elements of list and tuple
    hints.pop("return")
    for (arg_value, annotation) in zip(jsondata, hints.values()):
        if type(arg_value) != annotation:
            type_string = str(type(arg_value))
            if type_string == "<class 'list'>" and str(annotation)[:4] == "list" or str(annotation)[:5] == "tuple":
                continue
            raise TypeError(f"block expects input {annotation}, but receives {type(arg_value)}")
