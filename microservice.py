import json
import time

while True:
    time.sleep(1)
    fp = open("workout_plan.json")#open the .json file

    planData = json.load(fp)

    if planData['status'] == "true": #if json is not empty
        fp2 = open("workout_plan.txt", "r+") #open text file to be written to

        fp2.truncate(0) #clear the file
        fp2.seek(0) #puts file pointer at start of file

        #print in a nice looking way (requires fixing if JSON format changes)
        # fp2.write("Workout Name: " + planData['workout_name'] +"\n")
        # fp2.write("Name: " + planData['user_name'] +"\n")
        # fp2.write("Total Duration: " + str(planData['total_duration']) + " minutes\n\n")
        # fp2.write("------------------------------------------------\n\n")
        # for i in planData['workouts']:
        #     fp2.write("Workout Type: " + i['workout_type'] +"\n")
        #     fp2.write("Workout Duration: " + str(i['workout_time']) +"\n\n")

        #print the json directly (does not require fixing if format changes)
        jsonString = json.dumps(planData, indent=4)
        fp2.write(jsonString)

        fp2.close()

    fp.close()
    
    #change status to false so microservice won't continue running
    fp = open("workout_plan.json", "w")
    sample = {
        "status": "false"
    }
    jsonObject = json.dumps(sample) #convert sample object to json
    fp.write(jsonObject) #write json to file
    fp.close()