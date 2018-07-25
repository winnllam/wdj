from google.appengine.ext import ndb
import json
class Person(ndb.Model):
    email = ndb.StringProperty(required = True)
    name = ndb.StringProperty(required = True)
    college = ndb.StringProperty(required = True)
    collegecity = ndb.FloatProperty(required = True)
    collegestate = ndb.FloatProperty(required = True)
    highschool = ndb.StringProperty(required = True)
    highschoolcity = ndb.FloatProperty(required = True)
    highschoolstate = ndb.FloatProperty(required = True)
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
