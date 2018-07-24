from google.appengine.ext import ndb

class Person(ndb.Model):
    username = ndb.StringProperty(required = True)
    name = ndb.StringProperty(required = True)
    college = ndb.StringProperty(required = True)
    long1 = ndb.FloatProperty(required = True)
    lat1 = ndb.FloatProperty(required = True)
    highschool = ndb.StringProperty(required = True)
    long2 = ndb.FloatProperty(required = True)
    lat2 = ndb.FloatProperty(required = True)
