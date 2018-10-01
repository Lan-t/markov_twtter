import text
from random import randint
import pickle

def search(dataList, word):

    result = []
    
    for data in dataList:
        if(data[0] == word):
            result.append(data)

    return result

def generate(dataList):

    result = ''
    word = ''

    tracks = search(dataList, text.SOT)
    rand = randint(0,len(tracks)-1)
    word = tracks[rand][1]

    while True:
        tracks = search(dataList, word)
        try:
            rand = randint(0,len(tracks)-1)
        except ValueError:
            rand = 0
        try:
            result += tracks[rand][0]
        except IndexError:
            break
        word = tracks[rand][1]
        
        if tracks[rand][2] == text.EOT:
            result += tracks[rand][1]
            break

    return result



def specificGenerate(dataList, startTrack):

    result = ''
    word = ''
    word = startTrack[1]

    while True:
        tracks = search(dataList, word)
        try:
            rand = randint(0,len(tracks)-1)
        except ValueError:
            rand = 0
        try:
            result += tracks[rand][0]
        except IndexError:
            break
        word = tracks[rand][1]
        
        if tracks[rand][2] == text.EOT:
            result += tracks[rand][1]
            break

    return result
    

