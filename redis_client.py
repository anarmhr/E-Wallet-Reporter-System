import json
import redis


class RedisClient:
    def __init__(self):
        self.host = 'localhost'
        self.port = 6380

        self.redis_client = redis.StrictRedis(host='localhost', port=6380, decode_responses=True)

    def push_object(self, key, obj):
        self.redis_client.lpush(key, json.dumps(obj))

    def get(self, key):
        self.redis_client.get(key)

    def blpop(self, keys, timeout):
        return self.redis_client.blpop(keys, timeout=timeout)
