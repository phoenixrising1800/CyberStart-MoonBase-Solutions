# ""Unlocking the Mothership""
# Connect to the  server at 'localhost', 10000 send any data,
# the server will respond with the required word codes
# You will find a passage of text in the file backdoor.txt. Write a script
# which will use that text to build a message using the received word codes.
# Each word code is sent on a new line and contains
# paragraph_number, line_number, word_number from backdoor.txt
# Send the expected words back to the server to retrieve the flag.
# The server expects all the words in a single transmission.
# The words should have punctuation stripped from them.
# And the words should be separated by newline characters (\n)
#
import socket as s
import string

# Set up socket client
client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(('localhost', 10000))
client.send(b'Hello World')
word_codes = client.recv(4096) ## Changes every time!!!
strWordCodes = str(word_codes, 'utf-8') 

# Open and read file by paragraph lines
f = open('backdoor.txt', 'r')
content = f.read().split("\n\n")

wordList = []
data = strWordCodes.split("\n")[:-1] #[:-1] also removes last empty item
for item in data: # Printing each paragraph, line, and word as it goes
	row = item.split(",")
	paragraph_number, line_number, word_number = [x for x in row]
	print(paragraph_number, line_number, word_number)
  
  # Get paragraph
	PARAGRAPH_TEXT = content[int(paragraph_number)-1]
	paragraphLines = PARAGRAPH_TEXT.split('\n')
	for ind, line in enumerate(paragraphLines):
		print(ind+1, line)
   
 	# Get line
	LINE_TEXT = paragraphLines[int(line_number)-1]
	lineWords = LINE_TEXT.split(" ")
	print("LINE: " + LINE_TEXT)
  
  # Get word, removing punctuation
	WORD = lineWords[int(word_number)-1]
	puncList = [x for x in string.punctuation]
	for c in WORD:
		if c in puncList:
			WORD = WORD.replace(c, "")
	wordList.append(WORD)
	print("WORD: " + WORD)
	print()
  
replyStr = ''
for word in wordList:
	replyStr = replyStr + word + '\n'
  
print(replyStr)
client.send(replyStr.encode())
print(str(client.recv(4096), 'utf-8'))
