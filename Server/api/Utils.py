import hashlib
import time


def create_one_url(txt):
    text = f"{txt}'xby159357'{int(time.time())}"
    sign = hashlib.md5(bytes(text.encode("utf-8"))).hexdigest()
    return sign


if __name__ == '__main__':
    # print(int(time.time()))
    print(create_one_url("发生什么事了"))
