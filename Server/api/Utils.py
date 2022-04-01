import hashlib
import time
import random


def create_one_url(txt):
    rand = "".join([str(random.randint(1, 9)) for _ in range(0, 9)])
    text = f"{txt}'xby159357'{int(time.time())}{rand}"
    sign = hashlib.md5(bytes(text.encode("utf-8"))).hexdigest()
    return sign


if __name__ == '__main__':
    # print(int(time.time()))
    for i in range(0,10):
        print(create_one_url("发生什么事了")[2:12])
    # rand = "".join([str(random.randint(1, 90)) for _ in range(0, 4)])
    # print(random.randint(1, 1000))
