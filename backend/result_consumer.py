import json

from rabbit_mq import RabbitMQ
from redis_client import RedisClient
from service import extract_data

from loguru import logger

rabbit_mq = RabbitMQ()
redis_template = RedisClient()


def process_sql_result(channel, method, properties, sql_result):
    sql_result = json.loads(sql_result.decode('utf-8'))
    data = extract_data(sql_result['sql'])
    rabbit_mq.declare_queue('responses', data)


def consume_sql_result():
    rabbit_mq.consume('sql-results', process_sql_result())
