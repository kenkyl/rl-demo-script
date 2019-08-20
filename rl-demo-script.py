import redis

def main():
    # redis os server 
    host1 = 'localhost'
    port1 = 6379

    # redis enterprise server 
    host2 = '172.31.20.132'
    port2 = 16055

    print("starting inserts to redis-server-1")
    # open connection to os server to read data
    r1 = redis.Redis(
        host=host1,
        port=port1
    )

    num_keys = 100
    keys = []

    # insert #s 1-100 into os db
    for i in range(1, num_keys+1):
        key = "key-" + str(i)
        keys.append(key)
        r1.set(key, i)

    print('inserts complete. starting reads from redis-server-2')

    # open connection to enterprise server to read data
    # r2 = redis.Redis(
    #     host=host2,
    #     port=port2
    # )

    # for i in range()

    # # get two keys from enterprise server 
    # print('fetching test key 1: ', r2.get('memtier-474195'))
    # print('fetching test key 2: ', r2.get('memtier-2703924'))

    # r1.set('test-script-in1', 'found me!')
    # print('fetching test insert key: ', r2.get('test-script-in1'))



if __name__ == '__main__':
    main()