import redis

try:
    r = redis.StrictRedis(host='localhost', port=6379)
    r.ping()
    print("Connected to Redis")
except Exception as e:
    print(f"Error: {e}")
