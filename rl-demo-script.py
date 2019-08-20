import redis

def main():
    # redis os server 
    host1 = 'localhost'
    port1 = 6379

    # redis enterprise server 
    host2 = '172.31.20.132'
    port2 = 16055

    print("starting redis reads!")

    # open connection to enterprise server to read data
    r1 = redis.Redis(
        host=host1,
        port=port1
    )

    # get two keys from enterprise server 
    print('fetching test key 1: ', r1.get('memtier-474195'))
    print('fetching test key 2: ', r1.get('memtier-2703924'))

    # open connection to enterprise server to read data
    r2 = redis.Redis(
        host=host2,
        port=port2
    )

    # get two keys from enterprise server 
    print('fetching test key 1: ', r2.get('memtier-474195'))
    print('fetching test key 2: ', r2.get('memtier-2703924'))



if __name__ == '__main__':
    main()