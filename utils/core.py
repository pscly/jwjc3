import requests, re
import yaml

def load_config_yaml(path='/config/config.yaml', mode='WAI'):
    """
    加载配置文件
    """
    return yaml.safe_load(open(path, 'r'))[mode]
    


def get_1(url, cookies, re_text=None, headers=load_config_yaml()['HEADERS'], coding='gb2312'):
    '''
    封装requests.get方法

    args:
        url: 访问地址
        cookies: cookies
        re_text: 可选，提供正则，自动匹配
        headers: 可选，自己提供一个headers
    return: res1, re后的东西
    返回res1，想要什么就拿什么
    '''
    res1 = requests.get(url, headers=headers, cookies=cookies)
    res1.encoding = coding
    if re_text:
        re_hou = re.findall(re_text,res1.text)
        return res1, re_hou
    return res1, None


