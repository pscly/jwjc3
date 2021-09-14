import hashlib

# 将字符串进行哈希
def hash1(str_list: list) -> str:
    """
    传入列表，而不是单字符串
    """
    str2 = ''
    for str1 in str_list:
        str2 += str1
    hash_sha1 = hashlib.sha1()
    hash_sha1.update(str2.encode('utf-8'))
    return hash_sha1.hexdigest()

if __name__ == '__main__':
    print(hash1(['陈力源', '2', 'dsf']))
