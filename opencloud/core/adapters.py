"""Public provider adapter interface. Concrete adapters are private."""
from abc import ABC, abstractmethod
from typing import Any
from .urc import UnifiedRequestContract

class ProviderAdapter(ABC):
    def __init__(self,provider_name:str,model:str):
        self.provider_name=provider_name; self.model=model
    @abstractmethod
    def build_request(self,urc:UnifiedRequestContract)->dict[str,Any]: ...
    @abstractmethod
    def execute(self,provider_request:dict[str,Any])->dict[str,Any]: ...
    @abstractmethod
    def parse_response(self,provider_response:dict[str,Any])->dict[str,Any]: ...
    @abstractmethod
    def count_tokens(self,text:str)->int: ...
    @abstractmethod
    def get_pricing(self)->dict[str,float]: ...
    @abstractmethod
    def health_check(self)->dict[str,Any]: ...
