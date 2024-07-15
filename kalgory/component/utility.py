import json
from typing import get_type_hints

from kalgory.bindings.block import Block


def zipjson(block_output: any) -> dict:
    j_dict = {}
    if isinstance(block_output, dict):
        # If block_output is a dict, use its items directly
        j_dict.update(block_output)
    elif isinstance(block_output, (list, tuple)):
        # If block_output is a list or tuple, enumerate its items
        for index, data in enumerate(block_output):
            key = f"o{index+1}"
            j_dict[key] = data
    elif isinstance(block_output, (int, str, bool, float)):
        j_dict["o"] = block_output
    else:
        # Handle other types or raise an error if necessary
        raise TypeError("Unsupported type for block_output")
    return json.dumps(j_dict).encode("utf-8")

def validate(ins: Block, jsondata:dict):
    #check length
    if len(jsondata) != ins.handle.__code__.co_argcount - 1: #-1 bcs of self
        raise RuntimeError(f'Block "{ins.__class__.__name__}" expects '
                   f'{ins.handle.__code__.co_argcount} arguments, but received '
                   f'{len(jsondata)} arguments from previous blocks')
    #check if every parameter is annotated
    hints = get_type_hints(ins.handle)
    if ins.handle.__code__.co_argcount != len(hints):
        raise TypeError("Every input/argument must be assigned type")
    #check type
    #list and tuple types are confusing in python, for now only simple checks is implemented
    #TODO: add checks of elements of list and tuple  
    hints.pop('return')
    for (_, arg_value), (_, annotation) in zip(jsondata.items(), hints.items()):
        if type(arg_value) != annotation:
            type_string = str(type(arg_value))
            if type_string == "<class 'list'>" and str(annotation)[:4] == 'list' or str(annotation)[:5] == 'tuple':
                continue
            raise TypeError(f"block expects input {annotation}, but receives {type(arg_value)}")
