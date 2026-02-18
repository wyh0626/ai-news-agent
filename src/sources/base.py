"""数据源适配器基类 - 所有数据源实现统一接口"""

from abc import ABC, abstractmethod
from datetime import datetime

from src.models import RawItem


class BaseSource(ABC):
    """数据源基类，所有数据源适配器必须继承此类"""

    @abstractmethod
    async def fetch(self, since: datetime | None = None) -> list[RawItem]:
        """拉取 since 之后的新内容，若 since 为 None 则拉取最新内容"""
        ...

    @property
    @abstractmethod
    def source_id(self) -> str:
        """数据源唯一标识"""
        ...

    @property
    def default_interval(self) -> int:
        """默认采集间隔（秒）"""
        return 900  # 15 min

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} source_id={self.source_id}>"
