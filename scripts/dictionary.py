#import libraries 
import json
from difflib import get_close_matches

#data import
data = json.load(open('../data/english_dictionary_data.json'))

# function searches the json libary based on user input 
def translate (w):
    #input is case agnostics
    w = w.lower()

    #user provided word is in the dictionary
    if w in data:
        return data[w]
    
    #not in the dictionary, looks for similarity 
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input( "Did you mean %s, instead?, Enter Y if yes, and N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())][0]
        
        elif yn == "N":
            return "The word doesn't exist in this dictionary."

        else:
            return "Sorry this dictionary didn't understand your response"

    else:
        return "This word isn't in the dictionary "
    

# ask the user to put in a word using the input method 
word = input('Enter Word: ')

#returns the output
print (translate(word))
