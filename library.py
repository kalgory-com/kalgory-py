import abc
from typing import get_type_hints

# Library 
class Block(abc.ABC):
    
    def __init__(self, name = "name"):
        super().__init__()
        self._name = name
        self._check_execute_signature()
        self._check_class_name()
    def _check_execute_signature(self):
        # check if every parameter is assigned type
        execute_method = getattr(self.__class__, 'execute', None)
        
        if execute_method is None:
            raise TypeError("must implement an 'execute' method.")
        
        # get argument type
        hints = get_type_hints(execute_method)
        params = execute_method.__code__.co_argcount
        if params != len(hints):
            raise TypeError("Every input/argument must be assigned type") #TODO make this more detailed
    def _check_class_name(self):
        class_name = self.__class__.__name__
        if not (class_name[0].isupper() and class_name[1:].islower()):
            raise TypeError(f"""Invalid custom block name. Name must satisfy: 
                            1. only consists english letters
                            2. first letter is uppercase
                            3. the rest letters are lowercase
                            suggestion name for your block:{class_name[0].upper()}{class_name[1:].lower()} 
                            """)
    
    @abc.abstractmethod 
    def execute(self):
        pass #TODO customize error message
    
    @property
    def name(self):
        return(self._name)
    @name.setter
    def name(self, name):
        self._name = name
        return