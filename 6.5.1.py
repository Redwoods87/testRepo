def partA(text):
	for i in range(len(text)):
		print(text[i])

def partB(text):
	newText = ''
	for i in range(len(text)):
		if text[i] != ' ':
			newText = newText + text[i]
	return newText

def partC(text):
	for i in range(2, 10):
		if text[i] >= 'a' and text[i] <= 'z':
			print(text[i])

def partD(text):
	for i in range(1, len(text)-1):
		print(text.count(text[i]))


if __name__=='__main__':
	#print(partB('goblins are going to Mordor'))
	#partC('watermelonsonastick')
	partD('snuffleupagus')
