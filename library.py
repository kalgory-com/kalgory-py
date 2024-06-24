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
        
    @abc.abstractmethod 
    def execute(self):
        pass #TODO:customize error message
    
    @property
    def name(self):
        return(self._name)
    @name.setter
    def name(self, name):
        self._name = name
        return

		