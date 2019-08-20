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

    # define number of keys and array to hold them
    num_keys = 100
    keys = []

    print("starting inserts to redis-server-1")

    # insert #s 1-100 into os db
    for i in range(1, num_keys+1):
        key = "key-" + str(i)
        keys.append(key)
        r1.set(key, i)

    print('inserts complete. starting reads from redis-server-2')

    # open connection to es db to read data
    r2 = redis.Redis(
        host=host2,
        port=port2
    )

    # read vaules 100-1 from es db
    for i in range(num_keys, 0, -1):
        print(str(r2.get(keys[i-1]), 'utf-8'))

    print('reads complete. exiting')

if __name__ == '__main__':
    main()