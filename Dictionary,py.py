import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    if w in data:
        #if w.isupper(w==0):
           # if w.isupper():
        return data[w]     # return data[w]
    elif len(get_close_matches("w",data.keys())[0])>0:
        a=input( f"Did You Mean {get_close_matches(w,data.keys())[0]} Enter your choice 'yes' or 'no' : ").lower()

        if a=="yes":
            return data[get_close_matches(w,data.keys())[0]]
        if a=="no":
            return "Word doesn't exist "
        else:
            return "We didn't understand! Please check your query! "
    else:
        print("The word doesn't exist")
    


word=input("Enter your word : ").lower()
output=translate(word)
if type(output)==list:
    
    for item in output:
        print(item)
else:
    print(output)    