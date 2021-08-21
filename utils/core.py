import requests, re
import yaml

def load_config_yaml(path='config/config.yaml', mode='WAI'):
    """
    加载配置文件
    """
    return yaml.safe_load(open(path, 'r'))[mode]
    

class MyRes():
    '''
    封装一个获取结果的类
    仔细想想， 可以把cookies保存到一个对象中，到时候获取和调用都很方便了
    '''
    def __init__(self, config:dict, headers={}, cookies={}, coding='gb2312') -> None:
        self.config = config
        self.headers = headers
        self.cookies = cookies
        self.coding = coding
    
    def get_res(self, url, re_text=None):
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
        url = self.config['JWJC_URL'] + url
        res1 = requests.get(url, headers=self.headers, cookies=self.cookies)
        res1.encoding = self.coding
        self.cookies = res1.cookies.get_dict()
        self.headers = res1.headers
        self.headers['Referer'] = url
        if re_text:
            re_hou = re.findall(re_text,res1.text)
            return res1, re_hou
        return res1, None

    def post_res(self, url, data, re_text=None):
        '''
        封装requests.post方法
        '''
        url = self.config['JWJC_URL'] + url
        res1 = requests.post(url, data=data, cookies=self.cookies)  # 这里加上header就有问题
        res1.encoding = self.coding
        self.cookies = res1.cookies.get_dict()
        # self.headers = res1.headers
        self.headers['Referer'] = url
        if re_text:
            re_hou = re.findall(re_text, res1.text)
            return res1, re_hou
        return res1, None

