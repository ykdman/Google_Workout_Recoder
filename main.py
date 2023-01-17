# This Is the Python BootCamp Lecture Homework of Udemy
# I'm ykdman, Start!
# First , You must get your own api key of nutritionix, sheety
# So i'll Attach Link of API
# Sheety : https://sheety.co/
# Nutritionix :  https://www.nutritionix.com/business/api

# In Sheety, If You got your api key, Make New Project -> New Template ( Paste Google Sheet URL) And
# Check the 'GET', 'POST' Toggle Button


from datetime import datetime
import requests

TODAY = datetime.now().strftime("%Y%m%d")
now_time = datetime.now().strftime("%X")


# Endpoint Of Exercise API
Nutritionix_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
Sheety_ENDPOINT = "https://api.sheety.co/bc776dbd5c90eb75928c96b5970ad75e/workoutTracking/workouts"

# Header
APP_ID = "Your Nutritionix APP ID"
API_KEY = "Yout Nutritionix Api Key = Application key"

# Json Parameter
GENDER = "Your Gender"
WEIGHT_KG = 85  # Your Weight About Kg
HEIGHT_CM = 178  # Your Height About cm
AGE = 25

# exercise_text = input("Your Workout of Today :")
test_exercise_text = "squat 20minutes"


workout_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

workout_post_json = {
    "query": test_exercise_text,
    "gender": "male",
    "weight_kg": 100,
    "height_cm": 178,
    "age": 1999
}

response = requests.post(url=Nutritionix_ENDPOINT, json=workout_post_json, headers=workout_header)
response.raise_for_status()
result = response.json()
print(result)
print("------------------------------------------")


# TODAY, Time, Exercise, Duration, Calories

sheety_headers = {
    "Authorization": "Basic eWtkbWFuOkBydWRlanIzMDA="
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": TODAY,
            "time": now_time,
            "duration": exercise["duration_min"],
            "exercise": exercise["name"].title(),
            "calories": exercise["nf_calories"]
        }
    }
    print(sheet_inputs)
    sheety_response = requests.post(Sheety_ENDPOINT, json=sheet_inputs, headers=sheety_headers)

    print(sheety_response.text)

