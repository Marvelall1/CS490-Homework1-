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
             "First Name": "Marvellous",
             "Last Name": "Bassey",
             "Github Username": "Marvelall1",
             "Discord Username": "Marvelall",
             "Favorite Cartoon": "Justice league unlimited",
             "favorite Programming Language": "Java",
             "Your favorite Movie, Game, or book": "The Conjuring Sequal",
             "section": "101"
            }

# POST REQUEST
# (A POST request is how we send new data to an API (like submitting a form online).)
# sends a post request to the url and the response is saved under API_response

API_response = requests.post(myurl, json = MarveData) 

# Tells us if the request was a success 200=OK and 400/500 = error

print("POST OUTPUT") 
print ("Status Code Output: ", API_response.status_code) 

# Server Response
print ("Actual Response Text from Server: ", API_response.text)
print("\n\n")

#GET 
getInfo = {"UCID": "mab286",
           "section": "101"
          }

print ("GET OUTPUT")
API_response = requests.get(myurl, params = getInfo) 
print ("Status Code Output: ", API_response.status_code) 

# Server Response
print ("Actual Response Text from Server: ", API_response.text)






