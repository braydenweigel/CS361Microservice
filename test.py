import json
import time

#creates sample data
sample = {
    "workout_name": "My Workout",
    "user_name": "User Name",
    "total_duration": 110,
    "status": "true",
    "workouts": [
        {
            "workout_type": "Cardio",
            "workout_time": 60
        },
        {
            "workout_type": "Weights",
            "workout_time": 35
        },
        {
            "workout_type": "Calisthenics",
            "workout_time": 15
        }
    ]
}

fp = open("workout_plan.json", "w") #create file
jsonObject = json.dumps(sample, indent=4) #convert sample object to json
fp.write(jsonObject) #write json to file
fp.close()
time.sleep(1)

fp2 = open("workout_plan.txt", "r")
print(fp2.read())