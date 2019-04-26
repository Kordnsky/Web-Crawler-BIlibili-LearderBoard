"# WebCrawler-Bilibili TopRanked Videos"  
Indivadual Project of Yiming Liu for EE551-Python.
===

Intro:  
---
  A web crawler to go over video leaderboard of Bilibili, a Chinese video-sharing website, and crawl video information（Rank, Video Name, Author, Plays and Score).  
  Restore them in local txt files and draw the Score/Rank Chart of Monthly GeneralRank, Monthly OriginalRank and Monthly RookieRank.

Project Overview:  
---
```
1: Pre-thinking & analyze source code
2: Web Crawler	
3: Restore
4: Chart Graphics
```
Project Objective:  
---
```
·Get the informations of all the top ranking videos in Bilibili.
·Classify them into DayRank, MonthRank and MonthRank
·Draw the Score/Rank Chart of Monthly GeneralRank, Monthly OriginalRank and Monthly RookieRank

```
Conclusion:  
---
  First analyze the HTML code of Bilibili LeaderBoard Page, I picked out the useful classification tag(e.g: 0 to "ALL") and crate several dictionaries, each key corresponds to a LeaderBoard of Bilibili.  
  Then crate the headers for the crawler to camouflage the User-Agent(See "RequestHeader.png").  
  Then start the crawler and a total of 152 LeaderBoards were crawled down (See "textfiles.zip").  
  After all that use "matplotlib" to draw the Score/Rank Chart of Monthly GeneralRank, Monthly OriginalRank and Monthly RookieRank. (See "ScoreAndRankPlot.png").  
  We now know from the figure that:
```
1.Higher Rank in LeaderBoard dose not guarantee more Views 
2.Rookie Uploaders' videos usually cannot compete with other's in Views
```
