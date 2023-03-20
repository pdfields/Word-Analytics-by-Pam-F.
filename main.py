# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

# Create variable string
draculaText = readBook()

# create a dictionary
wordStats = {}

# create 4-letter word list

fourLtrWordList = []

# Initialize variables and string
numOfWords = 0
fourLtrWords = 0
highest = 0
highestOccurence = ""

# Create collection of words
words = draculaText.split()

# Step through word collection
for word in words:

# case insensitivity check
  word = word.lower()

# check to see if word has already been placed in Stat dictionary
  if (word not in wordStats):
    wordStats[word] = 1

# check to see if it is a 4-letter word, if so increment counter
    if (len(word) == 4):
      fourLtrWords += 1
      
# increment word counter if it is a unique word   
    numOfWords += 1

  else:
# Increment occurence value
    print()
    wordStats[word] = wordStats[word] + 1

# Step through Stat dictionary
for key, value in wordStats.items():

# check to see if current word has highest frequency, if so replace current one
  if (value > highest):
    highest = value
    highestOccurence = key

# Display Statistics
print("=== Results ===")

print()

print(f"'{highestOccurence}' is the word that appears the most throughout the text, a total of {wordStats[highestOccurence]} times")

print()

print(f"There are {fourLtrWords} words that are four letters long")

print()

# display words appearing 500 or more times
print("The following words occur at least 500 times:")

# Step through Stats dictionary
for  key, value in wordStats.items():
  if (value >= 500):
    print(f"{key} - {value}")

