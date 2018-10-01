import pandas as pd
import MeCab
import re



SOT = '__SOT__'
EOT = '__EOT__'
matchList = ['@', '#', 'http://', 'https://']


def text_list():
    csv = pd.read_csv('1.csv')
    csv2  = pd.read_csv('2.csv')
    csv3 = pd.read_csv('3.csv')
    textList = []
    texts = [ csv['text'], csv2['text'], csv3['text'] ]

    for t in texts:

        for text in t:
            text += '\n'
            if text.find('RT ') != 0 and text.find('#NowPlaying') == -1 and text.find('bot:') != 0 :
                for i in matchList:
                    match = re.search(i+'.* ', text)
                    while match != None:
                        text = text[0:match.start()]+text[match.end():]
                        match = re.search(i+'.* ', text)
                    match = re.search(i+'.*\n', text)
                    while match != None:
                        text = text[0:match.start()]+text[match.end():]
                        match = re.search(i+'.* \n', text)

                textList.append(text)
                #print(text)



    return textList

def words(textList):
    wordsList = []

    for text in textList:
        wordList = MeCab.Tagger('-Owakati').parse(text).split(' ')
        wordList.insert(0, SOT)
        wordList.append(EOT)


        while True:
            try:
                wordList.remove('\n')
            except ValueError:
                break

        wordsList.append(wordList)

    return wordsList

def data(wordsList):
    dataList = []
    
    for tweet in wordsList:
        i = 0
        for i, word in enumerate(tweet):
            #print(tweet)
            try:
                dataList.append([tweet[i],tweet[i+1],tweet[i+2]])
            except IndexError:
                break
            if(tweet[i+2] == EOT):
                break

    #print(dataList)
    return dataList
            
            

def make_data():
    return data(words(text_list()))