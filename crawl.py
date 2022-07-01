import pandas as pd
import requests
from requests import RequestException
import re


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None


if __name__ == '__main__':
    city_code = {'上海': '3', '北京': '1', '深圳': '49', '广州': '48', '重庆': '6', '苏州': '81', '成都': '300', '杭州': '37',
                 '武汉': '168', '南京': '78', '天津': '4', '宁波': '38', '青岛': '247', '无锡': '89', '长沙': '181', '郑州': '128',
                 '佛山': '53', '泉州': '72', '济南': '246', '合肥': '91', '西安': '274'}
    df = pd.DataFrame(columns=['城市', '年', '月', '新手房(元/㎡)', '二手房(元/㎡)', '总的平均价(元/㎡)'])
    for k, v in city_code.items():
        print(k)
        # 获取2022年
        url_all = 'https://fangjia.gotohui.com/fjdata-{}'.format(v)
        pattern = re.compile('<td>2022-(.*?)</td>\n<td>(.*?)</td>\n<td>(.*?)</td>', re.S)
        html = get_one_page(url_all)
        results = re.findall(pattern, html)
        for result in results:
            temp = ''
            if result[2] != '':
                temp = re.findall(r'\d+', result[2])[0]
            df = df.append({'城市': k, '年': '2022', '月': int(result[0]), '新手房(元/㎡)': temp, '二手房(元/㎡)': re.findall(r'\d+', result[1])[0], '总的平均价(元/㎡)': ''}, ignore_index=True)
        # 获取2019~2021年
        years = [2021, 2020, 2019]
        for year in years:
            url = 'https://fangjia.gotohui.com/years/{}/{}/'.format(v, year)
            html = get_one_page(url)
            pattern = re.compile('<tr><td>(.*?)月</td><td>(.*?)</td><td.*?>(.*?)</td>.*?</tr>', re.S)
            results = re.findall(pattern, html)
            results.reverse()
            print(year)
            print(results)
            for result in results:
                temp = ''
                if result[2] != '':
                    temp = re.findall(r'\d+', result[2])[0]
                df = df.append(
                    {'城市': k, '年': year, '月': int(result[0]), '新手房(元/㎡)': temp, '二手房(元/㎡)': re.findall(r'\d+', result[1])[0], '总的平均价(元/㎡)': ''}, ignore_index=True)
        # 获取2018年
        for i in range(12, 0, -1):
            df = df.append(
                {'城市': k, '年': 2018, '月': i, '新手房(元/㎡)': '', '二手房(元/㎡)': '', '总的平均价(元/㎡)': ''}, ignore_index=True)
        # 获取2016~2017年
        years = [2017, 2016]
        for year in years:
            url = 'https://fangjia.gotohui.com/years/{}/{}/'.format(v, year)
            html = get_one_page(url)
            pattern = re.compile('<tr><td>(.*?)月</td><td>(.*?)</td>.*?</tr>', re.S)
            results = re.findall(pattern, html)
            results.reverse()
            for result in results:
                df = df.append(
                    {'城市': k, '年': year, '月': int(result[0]), '新手房(元/㎡)': '', '二手房(元/㎡)': '',
                     '总的平均价(元/㎡)': re.findall(r'\d+', result[1])[0]}, ignore_index=True)
            print(year)
            print(results)
    df.to_csv('房价(副本).csv', index=False)
