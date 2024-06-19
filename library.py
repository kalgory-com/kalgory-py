# DUKE Version

import abc
from typing import get_type_hints

# Library 
class Block(abc.ABC):
    
    def __init__(self, name):
        super().__init__()
        self._name = name
        self._check_execute_signature()

    def _check_execute_signature(self):
        # check if every parameter is assigned type
        execute_method = getattr(self.__class__, 'execute', None)
        
        if execute_method is None:
            raise TypeError("must implement an 'execute' method.")
        
        # get_argument_type
        hints = get_type_hints(execute_method)
        params = execute_method.__code__.co_argcount
        if params != len(hints):
            raise TypeError("Every input/argument must be assigned type") #TODO make this more detailed
    
    @property
    def _get_argument_type(self):
        # return arguments' type
        execute_method = getattr(self.__class__, 'execute', None)
        hints = get_type_hints(execute_method)
        return hints
    
    @abc.abstractmethod 
    def execute(self):
        pass #找不到如何customize error message
    
    @property
    def name(self):
        return(self._name)
    @name.setter
    def name(self, name):
        self._name = name
        return

		
"""
# Usercode
class CustomBlock(Block):
		
	def execute(self, x:int, y:float) -> str:
		print("hello world")
"""

"""
#UI
a = CustomBlock("blockl")
print(a.name)
"""