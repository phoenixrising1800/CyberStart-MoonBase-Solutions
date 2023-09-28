# ""New Line of Communication""
# Connect over TCP to the following server: 'localhost', 10000
# Initiate communication with 'GET' to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline
#
import socket as s
from collections import Counter
        
def crackW(input):
	possibleOutput = ''
	maxPoints = 0 
	tempPoints = 0
	inputArr = input.split(" ")
  
	# Try an offset of every possibility from 0 to 25
	for i in range(0, 26):
		output = ""
		list_len = len(inputArr)-1
		for index, word in enumerate(inputArr):
			# For every character in the provided input-word
			for j in range(len(word)):
				char = word[j]
				newChar = chr((ord(char) + i - 65) % 26 + 65)
				output += newChar
			if index != list_len:
				output = output + " "

		# Find most frequent character
		MOST_FREQ_CHARS = ['E', 'T', 'A', 'O', 'S', 'H', 'I']
		freqChar, freqList = findMaxFreq(output)
    
		# check if freq. chars occur in this output instance (change this)
		if [c in str(freqList) for c in MOST_FREQ_CHARS]:
			for ch, val in freqList:
				if ch in MOST_FREQ_CHARS: 
					tempPoints = tempPoints + val
		if tempPoints >= maxPoints:
			maxPoints = tempPoints
			possibleOutput = output
		tempPoints = 0
	output = possibleOutput
	return output
    
# Return most frequent character, and list of 4 top frequent + counts
def findMaxFreq(input):
	counter = Counter(input)
	keys = sorted(counter, key=counter.get, reverse=True)
	res = keys[1] if keys[0] == ' ' else keys[0]
	most_common = counter.most_common(6)[1:] # 4 most common chars exc. spaces
	return (res, most_common)
    
client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(('localhost', 10000))
client.send(b'GET')
data = client.recv(1024)
dataMsgs = data.split(b'\n')

### Random shift each time!!!! 
# decode msg 1 
msg1 = dataMsgs[1].decode()
# decode msg 2 
msg2 = dataMsgs[2].decode()
# decode msg 3 
msg3 = dataMsgs[3].decode()

print(data)
print()

decoded1 = crackW(msg1)
decoded2 = crackW(msg2)
decoded3 = crackW(msg3)

decodedMsg = decoded1 + "\n" + decoded2 + "\n" + decoded3 + "\n"
decodedMsgStr = decodedMsg.encode()
print(decodedMsgStr)
client.send(decodedMsgStr)
print(client.recv(4096).decode())

client.close()
