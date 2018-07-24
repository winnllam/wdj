from google.appengine.ext import ndb

class Person(ndb.Model):
    name = ndb.StringProperty(required = True)
    college = ndb.StringProperty(required = True)
    highschool = ndb.StringProperty(required = True)
