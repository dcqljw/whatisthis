import hashlib


def create_one_url(date):
    sign = hashlib.md5(bytes(date.encode("utf-8"))).hexdigest()
    return sign


if __name__ == '__main__':
    print(create_one_url("1241qq4124"))
