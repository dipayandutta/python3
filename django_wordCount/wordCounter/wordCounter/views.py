from django.http import HttpResponse
from django.shortcuts import render 
import operator

def homePage(request,*args,**kwargs):
	#return HttpResponse("<h1>Hello World!</h1>")
	return render(request,'home.html',{})

def countWord(request,*args,**kwargs):
	
	# Getting userinput
	userInput = request.GET['textbox']
	# creating the wordlist by spliting the userinput
	wordList = userInput.split()
	# calculating the length of the wordlist
	listLength = len(wordList)
	#print (userInput)
	# define a dictonary
	counts = dict()
	# counting each occurance of words
	for word in wordList:
		if word in counts:
			counts[word] += 1
		else:
			counts[word] = 1

	print (counts) # print for debuging
	# sorting the items 
	sortedWords = sorted(counts.items(),key=operator.itemgetter(1),reverse=True)
	# dictonary for passing as vairable 
	pageString = {
					"title":"Count",
					"result_string" : "Number of Words",
					"input" : userInput,
					"wordlist" : wordList,
					"listLength" : listLength,
					"count":	counts.items,
					"sortedWords" : sortedWords,
				}
	return render(request,'count.html',pageString)
	
	