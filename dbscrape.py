import vbw
from pymongo import MongoClient

client = MongoClient()
db = client['testDB']
posts = db.posts

post_data = vbw.lastPodcastInfo()
episodetitle = post_data.get('title')
dupepost = posts.find({'title' : episodetitle}).count()
if(dupepost == 0):
   result = posts.insert_one(post_data)
   print("post inserted: " + episodetitle)







"""
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
"""

