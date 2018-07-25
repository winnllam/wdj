from google.appengine.ext import ndb
import json
class Person(ndb.Model):
    email = ndb.StringProperty(required = True)
    name = ndb.StringProperty(required = True)
    highschool = ndb.StringProperty(required = True)
    city1 = ndb.StringProperty(required = True)
    state1 = ndb.StringProperty(required = True)
    hslat = ndb.FloatProperty(required = True)
    hslong = ndb.FloatProperty(required = True)
    college = ndb.StringProperty(required = True)
    city2 = ndb.StringProperty(required = True)
    state2 = ndb.StringProperty(required = True)
    collat = ndb.FloatProperty(required = True)
    collong = ndb.FloatProperty(required = True)
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
