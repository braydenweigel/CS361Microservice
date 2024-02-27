# CS361Microservice
1: Start main program as well as the microservice in the same directory
  - Include a .json file (for testing I used workout_plan.json) with the field "status": "false"
  - Include an empty text file (workout_plan.txt)
  - To start microservice: python microservice.py

2: When user wants to export a text file from the main program, write the workout information to workout_plan.json, and set "status": "true" (this will cause the microservice to read in the data and write to the text file workout_plan.txt)
  - The microservice program includes the option to print with better looking formatting (this requires some edits if the structure of the JSON changes)
  - The default method of printing simply prints the JSON data into the text file

3: When the main program sees that workout_plan.txt is not empty, it can export the text file

![image](https://github.com/braydenweigel/CS361Microservice/assets/157440596/1271d6fa-7e94-42ee-bbc1-7118cd7cd8aa)

  
