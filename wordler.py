#!/usr/bin/env python
# coding: utf-8

# In[2]:


#ingest words

words = []

files = ['data.adj','data.adv','data.noun','data.verb']

for file in files:
    with open(file, 'r') as f:        
        for l in f.readlines():
            wrds = l.split(' ')
            for w in wrds:
                if len([a for a in w if a.isalpha()]) == 5:
                    words.append(''.join([a.lower() for a in w if a.isalpha()]))
            
                


# In[3]:


words = set(words)


# In[4]:


len(words)


# In[5]:


numberScores = {'a':1}
numberScores.keys()


# In[6]:


numberScores = {}
for w in  words:
    for c in w:
        if c in numberScores.keys():
            numberScores[c] += 1
        else:
            numberScores[c] = 1
        


# In[43]:





# In[40]:


numberScores


# In[7]:


def orderTheWords(words):
    wordScores = {}
    numberScores = {}
    for w in  words:
        for c in w:
            if c in numberScores.keys():
                numberScores[c] += 1
            else:
                numberScores[c] = 1

    for w in words:
        wordScores[w] = 0
        seenLetters = []
        for c in w:
            if c not in seenLetters:
                wordScores[w] += numberScores[c]
                seenLetters.append(c)

    wordScores = {k: v for k, v in sorted(wordScores.items(), key=lambda item: item[1], reverse=True)}       
    orderedWords = [k for k,v in wordScores.items()]
    return orderWords


# In[58]:


wordScores


# In[57]:


orderedWords


# In[79]:


answer = 'moldy'


# In[8]:


def orderTheWords(words):
    wordScores = {}
    numberScores = {}
    for w in  words:
        for c in w:
            if c in numberScores.keys():
                numberScores[c] += 1
            else:
                numberScores[c] = 1

    for w in words:
        wordScores[w] = 0
        seenLetters = []
        for c in w:
            if c not in seenLetters:
                wordScores[w] += numberScores[c]
                seenLetters.append(c)

    wordScores = {k: v for k, v in sorted(wordScores.items(), key=lambda item: item[1], reverse=True)}       
    orderedWords = [k for k,v in wordScores.items()]
    return orderedWords


def wordler(answer):
    orderedWords = orderTheWords(words)

    found = False
    ansList = [c for c in answer]

    correctChar = {}
    wrongChar = []
    missedChar = {}

    #print("let's get started")

    guesses = 0

    while found == False:

        guess = orderedWords[0]
        guesses += 1
        #print("my next guess is: {0}".format(guess))


        if guess == answer:
            found = True
            #print("I found it: {0} | and I found it in {1} guesses".format(guess,guesses))


        for i,c in enumerate(guess):
            if c == ansList[i]:
                if c in correctChar.keys():
                    if i not in correctChar[c]:
                        correctChar[c].append(i)
                else:
                    correctChar[c] = [i]

            elif c in ansList:
                if c in missedChar.keys():
                    missedChar[c].append(i)
                else:
                    missedChar[c] = [i]
            else:
                wrongChar.append(c)

        #remove bad guesses from words

        for wc in wrongChar:
            orderedWords = [w for w in orderedWords if wc not in w]

        for cc,l in correctChar.items():
            for i in l:
                orderedWords = [w for w in orderedWords if w[i] == cc]

        for mc,l in missedChar.items():
            for i in l:
                orderedWords = [w for w in orderedWords if w[i] != mc]
                orderedWords = [w for w in orderedWords if mc in w]

        #if found == False:
            #print('Correct Chars: ',correctChar)
            #print('Missed Chars: ',missedChar)
            #print('Wrong Chars: ',wrongChar)
        if guesses > 100:
            print("bugger {0}".format(answer))
            return [answer,-1]
        orderedWords = orderTheWords(orderedWords)
        #reorder the words
    return [answer, guesses]


    
    


# In[9]:


guessesNeeded = []
badGuesses = []
for w in words:
    answer = wordler(w)
    guessesNeeded.append(answer[1])
    if answer[1] > 9:
        badGuesses.append(answer)


# In[109]:


badGuesses


# In[95]:


sum(guessesNeeded) / len(guessesNeeded)
#reorder each time


# In[98]:


sum(guessesNeeded) / len(guessesNeeded)
#don't reorder each time


# In[16]:


def orderTheWords(words):
    wordScores = {}
    numberScores = {}
    #score the characters - each time we see a character in our word, we add 1
    for w in  words:
        for c in w:
            if c in numberScores.keys():
                numberScores[c] += 1
            else:
                numberScores[c] = 1
    #next we use that to score the words, we sum the character's number scores within the word
    #we ignore repeated letters score, so that we try more letters
    for w in words:
        wordScores[w] = 0
        seenLetters = []
        for c in w:
            if c not in seenLetters:
                wordScores[w] += numberScores[c]
                seenLetters.append(c)

    wordScores = {k: v for k, v in sorted(wordScores.items(), key=lambda item: item[1], reverse=True)}       
    orderedWords = [k for k,v in wordScores.items()]
    return orderedWords


def wordler(answer):
    orderedWords = orderTheWords(words)

    found = False
    ansList = [c for c in answer]

    correctChar = {}
    wrongChar = []
    missedChar = {}

    print("let's get started")

    guesses = 0

    while found == False:

        guess = orderedWords[0]
        guesses += 1
        print("my next guess is: {0} | I have {1} to choose from".format(guess, len(orderedWords)))




        if guess == answer:
            found = True
            print("I found it: {0} | and I found it in {1} guesses".format(guess,guesses))
        for i,c in enumerate(guess):
            if c == ansList[i]:
                if c in correctChar.keys():
                    if i not in correctChar[c]:
                        correctChar[c].append(i)
                else:
                    correctChar[c] = [i]

            elif c in ansList:
                if c in missedChar.keys():
                    missedChar[c].append(i)
                else:
                    missedChar[c] = [i]
            else:
                wrongChar.append(c)

        #remove bad guesses from words

        for wc in wrongChar:
            orderedWords = [w for w in orderedWords if wc not in w]

        for cc,l in correctChar.items():
            for i in l:
                orderedWords = [w for w in orderedWords if w[i] == cc]

        for mc,l in missedChar.items():
            for i in l:
                orderedWords = [w for w in orderedWords if w[i] != mc]
                orderedWords = [w for w in orderedWords if mc in w]

        if found == False:
            print('Correct Chars: ',correctChar)
            print('Missed Chars: ',missedChar)
            print('Wrong Chars: ',wrongChar)
        if guesses > 100:
            print("bugger {0}".format(answer))
            return [answer,-1]
        orderedWords = orderTheWords(orderedWords)
        
        if len(correctChar) == 4:
            found = True
            print("I have four characters and there are {0} valid answers | this took {1} guesses".format(len(orderedWords),guesses))
            print(orderedWords, "Answer was: ", answer)
        #reorder the words
    return [answer, guesses]


    
wordler('tears')

