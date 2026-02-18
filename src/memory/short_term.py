"""短期记忆 - Checkpointer 配置

v0.1: 使用 MemorySaver (内存)
v0.2+: 迁移到 PostgresSaver 或 RedisSaver
"""

from langgraph.checkpoint.memory import MemorySaver


def get_checkpointer():
    """获取短期记忆存储后端

    当前使用 MemorySaver（纯内存），适合开发和单次运行。
    生产环境应切换为 PostgresSaver:

        from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
        return AsyncPostgresSaver.from_conn_string(settings.postgres_url)
    """
    return MemorySaver()
