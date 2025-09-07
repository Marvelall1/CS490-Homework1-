# (Import Requests) This facilitates the impoting of the requests library 
import requests
'''
With it, you can:

Do GET requests (fetch data from an API).
Do POST requests (send data to an API).
Add headers (Content-Type: application/json).
Send data in JSON, form-data, or query parameters.
Handle responses (status codes, JSON results, errors, etc.).
'''

#REQUIREMENTS 
# UCID (Your university ID, initials and sequence number)
# First Name
# Last Name
# GitHub Username
# Discord Username (that can be used to send direct messages)
# Favorite Cartoon
# Favorite Programming Language
# Your favorite Movie, Game, or Book
# Section (use "101")

myurl = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

# Dictionary used to store my data 
MarveData = {"UCID": "mab286", 
             "first_name": "Marvellous", 
             "last_name": "Bassey", 
             "github_username": "Marvelall1", 
             "discord_username": "Marvelall", 
             "favorite_cartoon": "Justice league unlimited", 
             "favorite_language": "Java", "movie_or_game_or_book": 
             "The Conjuring Sequal", 
             "section": "101"
            }

# POST REQUEST
# (A POST request is how we send new data to an API (like submitting a form online).)
# sends a post request to the url and the response is saved under API_response

API_response = requests.post(myurl, json = MarveData) 

# Tells us if the request was a success 200=OK and 400/500 = error

print("\n")
print("POST OUTPUT") 
print ("Status Code Output: ", API_response.status_code) 

# Server Response
print ("Actual Response Text from Server: ", API_response.text)







