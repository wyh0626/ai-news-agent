"""长期记忆 - Store 配置 + 命名空间管理

v0.1: 使用 InMemoryStore (内存)
v0.3+: 迁移到 PostgresStore + pgvector 语义检索
"""

from langgraph.store.memory import InMemoryStore


# 命名空间设计
NAMESPACES = {
    "articles": ("published", "{date}"),        # 已发布文章索引
    "topics": ("topics", "{topic_name}"),        # 话题热度追踪
    "entities": ("entities", "{entity_type}"),   # 实体知识图谱
    "sources": ("sources", "{source_id}"),       # 数据源元数据
    "preferences": ("config", "writing_style"),  # 写作偏好
    "dedup_index": ("dedup", "{date}"),          # 去重指纹库
}


def get_store():
    """获取长期记忆存储后端

    当前使用 InMemoryStore（纯内存），适合开发。
    生产环境应切换为 PostgresStore + pgvector:

        from langgraph.store.postgres import PostgresStore
        return PostgresStore.from_conn_string(settings.postgres_url)
    """
    return InMemoryStore()
