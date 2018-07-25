from google.appengine.ext import ndb
import json 
class Person(ndb.Model):
    username = ndb.StringProperty(required = True)
    name = ndb.StringProperty(required = True)
    college = ndb.StringProperty(required = True)
    long1 = ndb.FloatProperty(required = True)
    lat1 = ndb.FloatProperty(required = True)
    highschool = ndb.StringProperty(required = True)
    long2 = ndb.FloatProperty(required = True)
    lat2 = ndb.FloatProperty(required = True)
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
