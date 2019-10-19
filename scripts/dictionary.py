## Loading the Data 

#import libraries 
import json

#data import
data = json.load(open('../data/english_dictionary_data.json'))

# function searches the json libary based on user input 
def translate (w):
    #input is case agnostics
    w = w.lower()

    #checking to see if the word is in the dictionary
    if w in data:
        return data[w]
    else:
        return "This word isn't in the dictionary "
    

# ask the user to put in a word using the input method 
word = input('Enter Word: ')

#returns the output
print (translate(word))
