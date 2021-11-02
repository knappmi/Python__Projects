''' This exercise will take the jokeAPI function from the last exercise 
and format the output in a way that is human-readable and easy to understand.'''

# Import our JokeAPI function
from easy import jokeAPI

# This is our parseJson function. It takes ugly Json and pulls what we need from it. In this case: A funny programming Joke!
def parseJson():
    
    # Here I am assigning a variable to our jokeAPI function so I can call it easier.
    joke_Main = jokeAPI()
   
    # We then want to know what type of joke it will be. 
    # We noticed that it can either be a "single" or "twopart" type of joke. 
    # The JSON response will greatly differ based on what type of joke we recieve.
    joke_Type = joke_Main["type"]

    # If joke_type is a "twopart": we will want two key values from the dictionary keys ["setup"] and ["delivery"].
    if joke_Type == "twopart":
        joke_key1 = joke_Main["setup"]
        joke_key2 = joke_Main["delivery"]
        return print(f'\n{joke_key1} {joke_key2}\n')
    
    # Else: we want the ["joke"] key value from a "single" joke_type.
    else:
        joke_Parse = joke_Main["joke"]
        return print(f'\n{joke_Parse}\n')

# Our main function is simple and acts a kickstart or more literally a script. It is the brain of your code.
def main():
    parseJson()

# Code actually begins here! If the code is being called locally (not imported) it will run main().
if __name__ == "__main__":
    main()
