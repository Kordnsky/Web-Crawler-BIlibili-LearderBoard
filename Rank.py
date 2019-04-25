import requests
import re
import time
import os
location = "/Users/liuyiming/Desktop"
category= {
    "all": "GeneralRank",
    "origin": "OriginalRank",
    "rookie": "RookieRank",
}

timeClassification = {1: "DailyRank", 3: "3-DayRank", 7: "WeeklyRank", 30: "MonthlyRank"}
general = {
    0: "All",
    1: "Animation",
    168: "CN_Animation",
    3: "Music",
    129: "Dance",
    4: "Game",
    36: "Technology",
    188: "Digital&Electronic",
    160: "Life",
    119: "Clip",
    155: "Fashion",
    5: "Celebrity",
    181: "Movie",
}

rookie= {
    0: "All",
    1: "Animation",
    3: "Music",
    129: "Dance",
    4: "Games",
    36: "Technology",
    188: "Digital&Electronic",
    160: "Life",
    119: "Clip",
    155: "Fashion",
    5: "Celebrity",
    181: "Movie",
}

BaseDict = {
    "all": general,
    "origin": general,
    "rookie": rookie,
}

def get_url():
    dic = {
        "all": 1,
        "origin": 2,
        "rookie": 3,
    }
    for x in category.keys():
        if x in ["all", "origin", "rookie"]:
            for y in BaseDict.get(x).keys():
                for z in timeClassification.keys():
                    url = "https://api.bilibili.com/x/web-interface/ranking?jsonp=jsonp&rid={}&day={}&type={}&arc_type=0&callback=__jp1".format(
                        y, z, dic.get(x))
                    yield url, [x, y, z]


head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Referer": "https://www.bilibili.com/ranking/all/0/0/3"
}
url_list = get_url()
for url in url_list:
    print("RequestingTo :  {}".format(url[0]))
    response = requests.get(url=url[0], headers=head)
    data = response.text.replace('"', "")
    p = r'.*?author:(?P<author>.*?),.*?play:(?P<play>.*?),.*?pts:(?P<pts>.*?),.*?title:(?P<title>.*?),'
    result_list = re.findall(p, data)
    path = os.path.join(location, "{}-{}-{}".format(category.get(url[1][0]),
                                                     rookie.get(url[1][1]) or general.get(url[1][1]),
                                                     timeClassification.get(url[1][2])))

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
    time.sleep(1)

