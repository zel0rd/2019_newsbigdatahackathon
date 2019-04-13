#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:59:15 2019

@author: zelord
"""
import requests
import json

global response
access_key = "7052fd92-ec53-4623-a426-212c95308f0b"

def api_call(url, data):
    global response
    response = requests.post(url=url, json=data)
    print(response.json())
    return response
    
def write_txt(response, case):  
    with open("test" + str(case)+".txt", 'w') as outfile:
        json.dump(response.json(), outfile, sort_keys = True, indent = 4, ensure_ascii = False)

def auto(url, data, response, case):
    api_call(url, data)
    write_txt(response, case)
    
#case 2
case = 2
url = "http://tools.kinds.or.kr:8888/search/news"
data = {
"access_key" : "7052fd92-ec53-4623-a426-212c95308f0b",
"argument": {
        "query": "검색 키워드", 
        "published_at": {
                "from": "2015-01-01",
                "until": "2016-01-31"
        },
        "provider": [ "경향신문",],
        "category": [
                "정치>정치일반",
                "스포츠일반", ],
        "category_incident": [ 
                "범죄",
                "교통사고", ],
        "byline": "",
        "provider_subject": [
                "경제", "부동산" ],
        "subject_info" : [""],
        "subject_info1": [""],
        "subject_info2": [""],
        "subject_info3": [""],
        "subject_info4": [""],
        "sort": {"date": "desc"},
        "hilight": 200,
        "returnFrom": 0,
        "returnSize": 5,
        "fields": [
                "content",
                "byline",
                "category",
                "hilight",
                "category_incident",
                "images",
                "provider_subject",
                "provider_news_id",
                ] 
        }
}
auto(url,data,response,case)


#case 3
case = 3
url = "http://tools.kinds.or.kr:8888/search/news"
data = {
"access_key" : "7052fd92-ec53-4623-a426-212c95308f0b",
"argument": {
"news_ids": [ "01500701.2015083110018412570", "01100701.20150826100000152"
        ],
        "fields": [
            "content",
            "byline",
            "category",
            "category_incident",
            "images",
            "provider_subject",
            "provider_news_id",
            "publisher_code"
] }
}
auto(url,data,response,case)


#case 4
case = 4
url = "http://tools.kinds.or.kr:8888/issue_ranking"
data = {
"access_key" : "7052fd92-ec53-4623-a426-212c95308f0b",
"argument": {
        "date": "2016-01-18",
        "provider": []
    }
}
auto(url,data,response,case)


#case 5
case = 5
url = "http://tools.kinds.or.kr:8888/word_cloud"
data = {
    "access_key" : "7052fd92-ec53-4623-a426-212c95308f0b",
    "argument": {
        "query": "국정 교과서", "published_at": {
                    "from": "2015-01-01",
                    "until": "2016-01-31"
                },
        "provider": [ "경향신문",
                ],
                "category": [
        "정치>정치일반",
        "스포츠일반", ],
        "category_incident": [ "범죄",
        "교통사고", ],
                "byline": "",
        "provider_subject": [ "사회" ] }
}
auto(url,data,response,case)

#case 6
case = 6
url = "http://tools.kinds.or.kr:8888/time_line"
data = {
    "access_key" : "7052fd92-ec53-4623-a426-212c95308f0b",
    "argument": {
        "query": "빅데이터", 
#        "published_at": {
#            "from": "2012-01-01",
#            "until": "2014-01-01" },
        "provider": ["경향신문"],
        "category": ["정치>정치일반","스포츠일반"],
        "category_incident": ["범죄","교통사고"],
        "byline": "",
        "provider_subject": ["사회"] 
        }
}
auto(url,data,response,case)


#case 7  X
case= 7
url = "http://openapi.kinds.or.kr:8888/query_rank"
data = {
    "argument": {
    "from": "2016-05-01",
    "until": "2016-05-25",
    "offset": 5,
    "access_key": ""
    }
}
auto(url,data,response,case)



#case 8 X
case = 8
url = "http://tools.kinds.or.kr:8888/search/quotation"
data = {
"access_key" : "7052fd92-ec53-4623-a426-212c95308f0b",
"argument": {
"query": "범죄", "published_at": {
            "from": "2015-01-01",
            "until": "2019-01-31"
        },
        "provider": ["경향신문", ],
"category": [ "정치>정치일반", "스포츠일반",
        ],
        "category_incident": [
"범죄",
"교통사고", ],
        "byline": "",
        "provider_subject": [
"경제", "부동산" ],
        "subject_info": [
            ""
        ],
        "subject_info1": [
"" ],
        "subject_info2": [
            ""
        ],
        "subject_info3": [
"" ],
        "subject_info4": [
            ""
        ],
        "sort": {"date": "desc"},
        "hilight": 200,
        "returnFrom": 0,
        "returnSize": 5,
        "fields": [
            "category",
            "category_incident",
            "provider_subject",
            "subject_info",
            "subject_info1",
            "subject_info2",
            "subject_info3",
            "subject_info4",
            "publisher_code"
           ] 
             }
}
auto(url,data,response,case)



#case 9
case= 9
url = "http://tools.kinds.or.kr:8888/today_category_keyword"
data = {
"access_key" : "7052fd92-ec53-4623-a426-212c95308f0b",
"argument": {}
}
auto(url,data,response,case)


#case 10
case = 10
url = "http://tools.kinds.or.kr:8888/feature"
data = {
"access_key": access_key, 
"argument": {
"title": "'태풍 솔릭'에 항공기 대규모 결항...오후 10시까지 총 532편 결항", 
"sub_title": "일자리 창출·사회안전망 확충...내년 사상 최대 ‘나랏돈’ 푼다", 
"content": "2018아시안게임 남자 축구에서 박항서 감독이 이끄는 베트남 국가대표팀의 돌풍이 심상치 않다." }
}
auto(url,data,response,case)


#case 11
case = 11
url = "http://tools.kinds.or.kr:8888/keyword"
data = {
"access_key": access_key,
"argument": {
"title": "'태풍 솔릭'에 항공기 대규모 결항...오후 10시까지 총 532편 결항", 
"sub_title": "일자리 창출·사회안전망 확충...내년 사상 최대 ‘나랏돈’ 푼다", 
"content": "2018아시안게임 남자 축구에서 박항서 감독이 이끄는 베트남 국가대표팀의 돌풍이 심상치 않다." }
}
auto(url,data,response,case)
