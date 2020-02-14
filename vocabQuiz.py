import glob
import random

def makeWordFile(filename, wordDict):
   fd = open(filename, "w")
   for spaWord in wordDict.keys():
      fd.write(spaWord+":")
      fd.write(str(wordDict[spaWord]).replace('[','').replace(']', '').replace("\', \'",",").replace("\'",""))
      fd.write('\n')    
   fd.close()

def quizQuestion(spaWord, engWords):
   incorrect = False
   i = 1
   print
   print("spanish word: "+spaWord)
   print("Enter "+str(len(engWords))+" equivalent English word(s).")   
   while (len(engWords) > 0 and incorrect == False):
      engWord = input("Word [" + str(i) + "]: ")
      if (engWord in engWords):
         engWords.remove(engWord)
         i += 1
      else:
         print("Incorrect.")
         incorrect = True
   if not incorrect:
      print("Correct!")
   print
   print("---")
   return not incorrect

def createDict(filename):
   wordDict = {}   
   fd = open(filename, "r") 
   for line in fd:
      line = line.strip()
      tokens = line.split(":")      
      spaWord = tokens[0]
      engWords = tokens[1]    
      engWordList = tokens[1].split(",")  
      wordDict[spaWord] = engWordList
   fd.close()
   return wordDict

def main():  
   fileList = glob.glob("*.txt")
   if len(fileList) == 0:
      print("There are no vocab lists available!")
      return
   print("Welcome to the vocabulary quiz program.  Select one of the following word lists:")
   for file in fileList:
      print("\t"+file)
   filename = input("Please make your selection: ")
   while filename not in fileList:
      filename = input("Please make a valid selection: ") 
   wordDict = createDict(filename)
   noQs = int(input(str(len(wordDict)) + " entries found.  How many words would you like to be quizzed on? "))
   while(noQs < 1 or noQs > len(wordDict)):
      noQs = int(input("Invalid input.  Please try again: "))
   quizList = random.sample(wordDict.keys(), noQs)
   numCorrect = 0
   incorrectDict = {}
   for word in quizList:
      if quizQuestion(word, wordDict[word][:]) == True:
         numCorrect += 1
      else:
         incorrectDict[word] = wordDict[word]
   print
   print(numCorrect," out of ",noQs," correct.")
   if numCorrect != noQs:
      filename = input("Enter an output file (or press enter to quit): ")
      if filename != "":
         makeWordFile(filename, incorrectDict)

main()
