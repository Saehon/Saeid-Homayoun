"""Public router pattern. Business rules and thresholds remain private."""
from typing import Any
from .urc import UnifiedRequestContract,ProviderStrategy
from .adapters import ProviderAdapter

class OpenCloudRouter:
    def __init__(self,providers:dict[str,ProviderAdapter]):
        self.providers=providers; self.audit_log=[]
    def select_provider(self,urc:UnifiedRequestContract)->str:
        if urc.provider_config.strategy==ProviderStrategy.PRIMARY_ONLY:
            return urc.provider_config.primary_provider
        return urc.provider_config.primary_provider
    def execute(self,urc:UnifiedRequestContract)->dict[str,Any]:
        raise NotImplementedError("Real implementation lives in private runtime")
    def get_cost_summary(self)->dict:
        raise NotImplementedError("Real implementation lives in private runtime")
