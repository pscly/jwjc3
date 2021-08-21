import os, base64, hashlib, hmac

# 登录加密算法
def login_str(s1:str) -> str:
    if not isinstance(s1, str):
        raise TypeError('s1 不是字符串')
    s2 = ''  # 返回的字符串
    for i in s1:
        s2 += str(100000+ord(i))
    return s2

if __name__ == '__main__':
    print(login_str('abc'))
