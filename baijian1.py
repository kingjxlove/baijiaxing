# -*- coding: utf-8 -*-
# @File  : baijian1.py
# @Author: KingJX
# @Date  : 2018/11/24 9:56
""""""
import requests
import json
from pymongo import MongoClient
from lxml import etree
import pymysql


def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        return text
    return None


def parse_first_name(html):
    etree_html = etree.HTML(html)
    all_first_name = etree_html.xpath('/html/body/div[3]/div/div/div[2]/a')
    surname_dict = {}
    for item in all_first_name:
        # surname_list = []
        first_name_url = item.xpath('.//@href')[0]
        first_name = item.xpath('.//text()')[0]
        first_name1 = str(first_name).split('姓')[0]
        # surname_list.append(first_name_url)
        # surname_list.append(first_name1)
        surname_dict[first_name1] = first_name_url
        # print(surname_dict)
    # print(surname_dict)
    with open('./surname.json', 'w', encoding='utf8')as f:
        f.write(json.dumps(surname_dict, ensure_ascii=False))
    # with open('./surname.txt', 'r', encoding='utf-8')as f:
    #     a = f.read()
    # print(a)
    return surname_dict


def parse_name(html):
    etree_html = etree.HTML(html)
    all_name = etree_html.xpath('/html/body/div[3]/div[2]/div[1]/div/a')
    name_dict = {}
    for item in all_name:
        name = item.xpath('.//text()')[0]
        name_url = item.xpath('.//@href')[0]
        name_dict[name] = name_url
    return name_dict


def insert_name(cursor, db, k, m, n):
    sql = 'insert into biajingxing(surname, name, name_url) value ("%s","%s","%s")' % (k, m, n)
    cursor.execute(sql)
    db.commit()


def main():
    db = pymysql.connect(host='localhost', user='root', password='root', database='baijiaxing', port=3306)
    cursor = db.cursor()
    url = 'http://www.resgain.net/xmdq.html'
    html = get_one_page(url)
    # print(html)
    surname_dict = parse_first_name(html)
    for k, v in surname_dict.items():
        i = 1
        for _ in range(10):
            list1 = str(v).split('/')
            list2 = list1[3].split('.')[0]
            url = 'http://' + list1[2] + '/' + list2 + '_' + str(i) + '.html'
            i += 1
            surname_html = get_one_page(url)
            name_dict = parse_name(surname_html)
            for n, m in name_dict.items():
                print(n)

                insert_name(cursor, db, k, m, n)


if __name__ == '__main__':
    main()
