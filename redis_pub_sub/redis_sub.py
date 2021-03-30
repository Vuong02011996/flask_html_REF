import redis


def listen():
    client = redis.StrictRedis(host='192.168.111.133', port=11032, db=5)
    pubsub = client.pubsub()

    pubsub.subscribe('group_video')
    # pubsub.subscribe('tf_stop_video')
    # pubsub.subscribe('tf_start_video')
    while True:
        for message in pubsub.listen():
            print(message)


if __name__ == '__main__':
    listen()
