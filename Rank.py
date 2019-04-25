import requests
import re
import time
import os
location = "/Users/liuyiming"
category_dic = {
    "all": "全站榜",
    "origin": "原创榜",
    "rookie": "新人榜",
}

day_dic = {1: "日排行榜", 3: "三日排行榜", 7: "周排行榜", 30: "月排行榜"}
all_or_origin_dic = {
    0: "全站",
    1: "动画",
    168: "国创相关",
    3: "音乐",
    129: "舞蹈",
    4: "游戏",
    36: "科技",
    188: "数码",
    160: "生活",
    119: "鬼畜",
    155: "时尚",
    5: "娱乐",
    181: "影视",
}

bangumi_dic = {
    "番剧": 1,
    "国产动画": 4,
}

cinema_dic = {
    "记录篇": 177,
    "电影": 23,
    "电视剧": 11,
}

rookie_dic = {
    0: "全站",
    1: "动画",
    3: "音乐",
    129: "舞蹈",
    4: "游戏",
    36: "科技",
    188: "数码",
    160: "生活",
    119: "鬼畜",
    155: "时尚",
    5: "娱乐",
    181: "影视",
}

BaseDict = {
    "all": all_or_origin_dic,
    "origin": all_or_origin_dic,
    # "bangumi": bangumi_dic,
    # "cinema": cinema_dic,
    "rookie": rookie_dic,
}

dic = {
    "all": 1,
    "origin": 2,
    "rookie": 3,
}


def get_url():
    for first in category_dic.keys():
        if first in ["all", "origin", "rookie"]:
            for second in BaseDict.get(first).keys():
                for third in day_dic.keys():
                    url = "https://api.bilibili.com/x/web-interface/ranking?jsonp=jsonp&rid={}&day={}&type={}&arc_type=0&callback=__jp1".format(
                        second, third, dic.get(first))
                    yield url, [first, second, third]


s = requests.Session()
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Referer": "https://www.bilibili.com/ranking/all/0/0/3"
}
url_list = get_url()
for url in url_list:
    print("向{}发请求".format(url[0]))
    response = s.get(url=url[0], headers=head)
    data = response.text.replace('"', "")
    p = r'.*?author:(?P<author>.*?),.*?play:(?P<play>.*?),.*?pts:(?P<pts>.*?),.*?title:(?P<title>.*?),'
    result_list = re.findall(p, data)
    path = os.path.join(location, "{}-{}-{}".format(category_dic.get(url[1][0]),
                                                     rookie_dic.get(url[1][1]) or all_or_origin_dic.get(url[1][1]),
                                                     day_dic.get(url[1][2])))

    f = open(path + ".txt", "a", encoding="utf-8")
    print('Writing....{}'.format(path + ".txt"))
    for index, res in enumerate(result_list):
        f.write("Rank：{}\n".format(index + 1))
        f.write("Tittle：{}\n".format(res[3]))
        f.write("Author：{}\n".format(res[0]))
        f.write("Plays：{}\n".format(res[1]))
        f.write("Score：{}\n".format(res[2]))
        f.write("-" * 90 + "\n")
    f.close()
    time.sleep(2)