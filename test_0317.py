# import redis
# class RedisUtil:
#     def __init__(self, host, password, port='6379', decode_responses=True):
#         # redis的连接池
#         self.Poorl = redis.ConnectionPool(host=host, port=port, password=password, encoding_errors='ignore',
#                                           decode_responses=True)
#         self.r = redis.Redis(connection_pool=self.Poorl)  # 表示从上面的连接池拿到一个连接对象r
#
#     def get(self, key):
#         type = self.r.type(key)
#         if type == 'string':
#             return type.get(key)
#         elif type == 'hash':
#             return type.hgetall(key)
#         elif type == 'zset':
#             return type.zrange(key)
#         elif type == 'set':
#             return type.smembers(key)
#         elif type == 'list':
#             return type.lrange(key)
#         else:
#             raise Exception(f'不支持的数据类型是{type}或者{key}不存在')
#
#
# if __name__ == '__main__':
#     redis_util = RedisUtil('121.42.15.146', password='testfan')
#     res = redis_util.get('{stock}{SKU_STOCK}_enable_988')
#     print(res)
#     # newname=RedisUtil('localhost')
#     # res = newname.get(f'list1')
#     # print(res)
