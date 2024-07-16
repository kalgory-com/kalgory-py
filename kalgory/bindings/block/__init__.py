from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from .types import Result, Ok, Err, Some



class Block(Protocol):

    @abstractmethod
    def execute(self, payload: bytes) -> bytes:
        """
        Raises: `block.types.Err(None)`
        """
        raise NotImplementedError

