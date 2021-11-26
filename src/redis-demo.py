from datetime import date
import redis

print("Hello Redis")

print("Connecting to REDIS")

r = redis.Redis(host='localhost', port=6379, db=5)

print("Connected.")

# Strings
r.set('foo', 'bar')

print(r.get('foo'))

r.mset({"Croatia":"Zagreb", "Poland":"Warsaw", "France":"Paris"})

print(r.get("Poland"))

r.set('points', 0)

r.incr('points')
r.incr('points')
r.incr('points')

points = r.get('points')

print(f'Points: {points}')

# Sets

today = date.today().isoformat()

print(today)

visitors = {"dan", "jon", "alex"}

r.sadd(today, *visitors)

print(r.smembers(today))


# Hash


# r.hset('my_key', {'field0': 'value0', 'field1':'value1', 'field2':'value2'})

#r.hset("test", {"Croatia":"Zagreb", "Poland":"Warsaw", "France":"Paris"})

print(r.hgetall("vehicle"))

print(r.hkeys("vehicle"))

print(r.hvals("vehicle"))

r.hincrby("vehicle", "quantity", 1)

r.hget("vehicle", "quantity")

# Transacions
stationid = "station:1"
accountid = "account:1"

with r.pipeline() as pipe:
        pipe.watch(stationid)
        pipe.multi()
        pipe.hincrby(stationid, "quantity", -1)
        pipe.hincrby(accountid, "rents", 1)
        pipe.execute()
        
