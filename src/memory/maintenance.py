"""记忆维护模块 - 清理过期记忆、压缩旧数据

v0.3+: 定时任务，清理过期 embedding、合并旧话题
v0.1: 提供接口定义，暂不实现
"""

import logging

logger = logging.getLogger(__name__)


async def cleanup_expired_memories(store=None, days: int = 30):
    """清理超过 N 天的去重指纹和旧文章索引

    v0.1: 暂不实现
    """
    logger.debug(f"记忆清理暂未实现 (v0.3), 保留天数={days}")


async def compress_topic_trends(store=None):
    """压缩话题热度数据：将每日计数合并为周/月汇总

    v0.1: 暂不实现
    """
    logger.debug("话题趋势压缩暂未实现 (v0.3)")
