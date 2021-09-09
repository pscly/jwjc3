
from bs4 import BeautifulSoup
import re
from addict import Dict


def xuanke_jx(html:str):
    '''
    将选课网页解析成字典
    '''
    r_data = Dict()
    soup = BeautifulSoup(html, 'html5lib')
    xk_b = soup.find_all('table')[-2]
    xk_tr = xk_b.find_all('tr')[1:]
    for kc in xk_tr:
        # 如果是已满，那就获取不到课程 url
        if kc.find_all('td')[12].text.strip(' ') == '已满':
            continue
        xk_url = kc.find_all('td')[13].a['href']
        # 这里后期可能会使用strip功能实现，但是现在又不回拿到前面的域名
        # xk_url =  re.findall(r'http://.*?/(.*)', kc.find_all('td')[13].a['href'])[0]  
        r_data[kc.find_all('td')[3].text] = {
            '课程编号': kc.find_all('td')[0].text,
            '课程班级': kc.find_all('td')[2].text,
            '课程名称': kc.find_all('td')[3].text,
            '学分': kc.find_all('td')[4].text,
            '教师': kc.find_all('td')[5].text,
            '上课时间': kc.find_all('td')[6].text,
            '周次': kc.find_all('td')[7].text,
            '计划人数': kc.find_all('td')[9].text,
            '已选人数': kc.find_all('td')[12].text,
            '选课': xk_url,
        }
    return r_data


if __name__ == '__main__':
    filt_path = 'kaike.html'
    filt_path = 'pa_app/view_class_card/kaike.html'
    with open(filt_path, 'r', encoding='utf-8') as f:
        html = f.read()
    x = xuanke_jx(html)
    print(x)
