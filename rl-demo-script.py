import redis

def main():
    # redis os db 
    host1 = 'localhost'
    port1 = 6379

    # redis es db 
    host2 = '172.31.20.132'
    port2 = 16055

    # open connection to os db to read data
    r1 = redis.Redis(
        host=host1,
        port=port1
    )

    print("starting inserts to redis-server-1")

    # define number of keys and add them to sorted set on os db
    num_keys = 100
    for i in range(1, num_keys+1):
        r1.zadd("my-sset", {i: i})

    print('inserts complete. starting reads from redis-server-2')

    # open connection to es db to read data
    r2 = redis.Redis(
        host=host2,
        port=port2
    )

    # read vaules 100-1 from es db
    print(r2.zrevrange("my-sset", 0, -1))

    print('reads complete. deleting key and exiting')
    r1.delete("my-sset")

if __name__ == '__main__':
    main()