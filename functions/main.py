import populartimes
import json
def getWaitTime(place_id):
    popTimes = populartimes.get_id("AIzaSyD05_UZtGyhAhq-bhVxsAJ4gLRw1xCd8KY", place_id)
    print(json.dumps(popTimes))
    return json.dumps(popTimes)

getWaitTime("ChIJibqUCJME9YgR4ych3D5KKzU")