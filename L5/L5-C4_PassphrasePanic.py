# ""Passphrase Panic""
# Write a script to generate a passphrase by taking words from
# /tmp/words.txt
# The wordNumbers array holds three random numbers. Each number
# corresponds to a word in words.txt. So for example
# wordNumbers[1] is the second word in /tmp/words.txt.
# Put a space between each word and print it out
#
with open("/tmp/randomwordsnumbers.txt", "r") as file:
    data = file.read()

wordNumbers = data.rstrip().split("\n")

f = open('/tmp/words.txt', 'r')
wordData = f.readlines()

word1 = wordData[int(wordNumbers[0])].rstrip()
word2 = wordData[int(wordNumbers[1])].rstrip()
word3 = wordData[int(wordNumbers[2])].rstrip()
print(word1 + " " + word2 + " " + word3)
