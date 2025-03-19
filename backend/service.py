import sql_executor
import uuid

from dtos import SqlRequest
from redis_client import RedisClient

from rabbit_mq import RabbitMQ

SQL_REQUEST_QUEUE = 'sql-requests'
KEY_PATTERN = 'sql-result:%s'

rabbit_mq = RabbitMQ()
redis_template = RedisClient()


def extract_data(sql):
    return sql_executor.execute_query(query=sql)


def publish_sql_request(user_query):
    request_id = str(uuid.uuid4())

    sql_request = SqlRequest(
        request_id=request_id,
        user_query=user_query
    )

    rabbit_mq.publish(SQL_REQUEST_QUEUE, sql_request.model_dump_json())
    return request_id


publish_sql_request('list users')
