from loklak import Loklak
import json

myTweets = Loklak()

movieName = raw_input("What movie would you like to search recent tweets for? ") #asks for what user would like to search for

index = 1
for tweet in myTweets.search(movieName)["statuses"]: #searches movie and finds "statuses" where "text" is under
    print '%d%s' %(index, '.') #prints the tweet number
    print tweet["text"] + "\n" #prints the text of the tweet and makes a new line
    index+=1 #increments index
        
