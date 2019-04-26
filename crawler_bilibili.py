import requests
import re
import time
import os
# Output saving location
location = "/Users/liuyiming/Desktop"
# Using Developer tools of Chrome to Build the head
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Referer": "https://www.bilibili.com/ranking/all/5/0/3"}
# Crate the classification dictionarys
category={"all": "GeneralRank",
         "origin": "OriginalRank",
         "rookie": "RookieRank"
          }
timeClassification ={1: "DailyRank",
                     3: "3_DayRank",
                     7: "WeeklyRank",
                     30: "MonthlyRank"
                     }
general ={0: "All",
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
          181: "Movie"
          }
rookie={0: "All",
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
        181: "Movie"
        }

def get_url():
    for i in range()
    for url in url_list:
        print("RequestingTo :  %s" % url[0])
        response = requests.get(url=url[0], headers=head)
        data = response.text.replace('"', "")