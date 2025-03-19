import json
from dtos import SqlRequest

from rabbit_mq import RabbitMQ
from redis_client import RedisClient
from sql_response_generator import generate_sql_response

from loguru import logger

rabbit_mq = RabbitMQ()
redis_template = RedisClient()

SQL_REQUEST_QUEUE = 'sql-requests'
KEY_PATTERN = 'sql-result:%s'


def process_sql_request(channel, method, properties, sql_request):
    logger.info('Received message from sql-requests queue: {}', sql_request)
    sql_request = SqlRequest.model_validate_json(sql_request.decode('utf-8'))

    user_query = sql_request.user_query

    sql_result = generate_sql_response(user_query)
    sql_result = sql_request['request_id']

    rabbit_mq.declare_queue('sql-results')
    rabbit_mq.publish('sql-results', sql_result)


def main():
    rabbit_mq.declare_queue('sql-requests')
    logger.info('Consumer active')
    rabbit_mq.consume('sql-requests', process_sql_request)


if __name__ == '__main__':
    main()
