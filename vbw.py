import feedparser
import datetime

"""
now = datetime.datetime.now()
year = str(now.year)
month = str(now.month)
day = str(now.day)
print(year +" "+month + " " + day)
"""

def lastPodcastInfo():
   feed = feedparser.parse('https://verybadwizards.fireside.fm/rss')
   title = feed.entries[0].title
   published = feed.entries[0].published
   pubyear = published[0]
   pubday = published[1]
   description = feed.entries[0].description
  # return { 'title' : title }
      
   return {
           'title' : title,
           'published' : published,
           'description' : description
          }
   
#print(title)
#print(published)
#print(description)
