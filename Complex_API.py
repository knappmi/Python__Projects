# Import requests and json
import requests
import json

# postCustomer will handle the API call to create a user named test1
def postCustomer():
    url = "https://gorest.co.in/public/v1/users"
    
    # Notice the "Autorization" method in the headers with our Token.
    headers = {
        "Content-type" : "application/json",
        "Accept": "application/json",
        "Authorization" : "Bearer 948fb74acc9dff6d9ddb60c94b86d7bbb1b976a523695bbfd541e1fe78cb9596"
        }

    # data_new contains all the information that we want sent in the POST request.
    data_new = {
        "name" : "test1",
        "email" : "mail22@mail.com",
        "status" : "active",
        "gender" : "male"
        }

    # Here is the actual API call. We use the json.dumps(data_new) to format the data in a json string.
    output = requests.post(url, data= json.dumps(data_new), headers=headers).json()
    
    return output

def getCustomer(cusId):
    url = "https://gorest.co.in/public/v1/users/" + str(cusId)
    headers = {
        "Content-type" : "application/json",
        "Accept": "application/json"
        }
    output = requests.get(url, headers=headers).json()
    easy_read = json.dumps(output, indent = 4)
    print(easy_read)

# The patchCustomer function will hand the PATCH method. Notice the cusId is set as a parameter.
def patchCustomer(cusId):

    # In order to use the PATCH method correctly, we need to specify the cusId in the URL. We can do that with concatination.
    url = "https://gorest.co.in/public/v1/users/" + str(cusId)
    
    # Token is back in the header.
    headers = {
        "Content-type" : "application/json",
        "Accept": "application/json",
        "Authorization" : "Bearer 948fb74acc9dff6d9ddb60c94b86d7bbb1b976a523695bbfd541e1fe78cb9596"
        }
    
    # data_new now contains the information we want patched
    data_new = {
        "name": "Patch me"
        }
    
    # The api call reflects postCustomer except we use requests.patch
    output = requests.patch(url, data= json.dumps(data_new), headers=headers).json()
    return output

# The main function defines the cusId and passes it as a parameter to our functions.
def main():
    cusId = postCustomer()["data"]["id"]
    getCustomer(cusId)
    patchCustomer(cusId)
    getCustomer(cusId)

if __name__ == "__main__":
    main()

