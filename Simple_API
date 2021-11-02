''' This exercise will familiarize you with APIs or Application Programming Interfaces.
This exercise is done for you already so we can go over key concepts of an API.

The python module "requests" is the heart of our interaction with an API. 
It allows us to use the GET and POST methods you'll see throughout the code. 

More about python requests library can be found here: https://pypi.org/project/requests/
'''
# This sample API call reaches out to a website and retrieves a joke for us.
# WARNING! There isnt a filter on the jokes (although you can configure one).

# First we import the python requests module. We also import the urllib3 module for use later.
import requests
import urllib3

# Now to define the jokeAPI function.
def jokeAPI():

    # The following disables annoying certificate warnings. Note: urllib3 will need to be imported to use it.
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Here we define the URL that our API uses to retrieve data.
    url = 'https://sv443.net/jokeapi/v2/joke/Programming'
    
    # Also we define the content-type in the header to tell the API what type of content is being sent.
    # Since we are using the "GET" method here, I only included it to help paint a picture.
    headers = {"Content-type" : "application/json"}

    # Now, the actual API call. Here we use a GET request with the URL variable we defined earlier. This is called an API "Call" to an API Endpoint.
    output = requests.get(url, headers=headers)
    
    # A Conditional!
    # If the server response code is anything other than 200 (Success): print an error with the code and exit the function.
    if output.status_code != 200:
        print(f'Error! Server response code was: {output.status_code}')
        quit()
    
    # Another one!
    # This conditional is so that if this function is imported, it wont display annoying unparsed data.
    if __name__ == "__main__":
        print(output.text)
    
    # This will return the output in JSON format if imported by another function.
    else:
        return output.json()
    
jokeAPI()
