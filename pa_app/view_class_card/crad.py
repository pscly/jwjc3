# coding: utf-8
# 作者:Pscly
# START-DATE: 2021-09-01 23:30
# END-DATE:
# 课程表分析

import re
from addict import Dict
from bs4 import BeautifulSoup
from rich import print


def main(s1: str):
    """
    args:
        path: 课程表的网页内容

    return: {userinfo}
    """
    r_data = Dict()

    # 人名
    r_data.userinfo['name'] = _[0] if (
        _ := re.findall(r'align=right ?>(.*?)</td>', s1)) else ''

    # 班级
    r_data.userinfo['class'] = _[0] if (
        _ := re.findall(r'align=left ?>(.*?)</td>', s1)) else ''

    # 学年
    r_data.userinfo['stu_year'] = _[0] if (_ := re.findall(
        r'size=3>四川科技职业学院(.*?)课程表</font>', s1)) else ''


    class_data = Dict()

    # 课程
    soup = BeautifulSoup(s1, 'html5lib')
    kb_tb = soup.find_all('table')
    kb = kb_tb[1]       # 0 是信息， 1 是课程表， 2 是课程信息(考察考试的细节)
    kb2 = kb.find_all('tr')[1::]

    # class_info_re = r"""<td align="center" height="50" valign="top" width="13.5%">(.*?)<br/>(.*?)<br/>(.*?)<br/>(.*?)<br/>(.*?)<br/>"""
    class_info_re = r""">(.*?)<br/?>(.*?)<br/?>(.*?)<br/?>(.*?)<br/?>(.*?)<br/?"""
    for kb2_2 in kb2:
        zhou = 1
        for i in kb2_2.find_all('td'):
            if not re.findall('valign=', str(i)) or zhou > 5:
                continue
            kc_data = Dict()
            kc_data1 = re.findall(class_info_re, str(i))    # 单节课程的信息
            if kc_data1:
                for kc_data2 in kc_data1:
                    # kc_data.date = kc_data1[0][1] # 现在是直接把他当作键, 其实可以考虑121 代表12节单周
                    # 122 代表12节双周
                    kc_data[kc_data2[1]][kc_data2[4]].name = kc_data2[0]
                    kc_data[kc_data2[1]][kc_data2[4]].date = kc_data2[1]
                    kc_data[kc_data2[1]][kc_data2[4]].teacher = kc_data2[2]
                    kc_data[kc_data2[1]][kc_data2[4]].addr = kc_data2[3]
                    kc_data[kc_data2[1]][kc_data2[4]].mondate = kc_data2[4]
            class_data[zhou] |= kc_data
            zhou += 1
    
    r_data.class_data = class_data
    return r_data


if __name__ == '__main__':
    file_path = r'F:\now2\jwjc3\template\test1.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        s1 = f.read()
    x = main(s1)
    print(x)