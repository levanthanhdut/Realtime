import time

start_time = time.time()

file = open('C:/Users/lvtha/Realtime/Mapredure/pg100.txt', "r+")

wordCount = {}

for word in file.read().split():
	if word not in wordCount:
		wordCount[word]=1
	else:
		wordCount[word]+=1
for key in wordCount.keys():
	print(key,' ',wordCount[key])

file.close()

end_time=time.time()

print ('total run-time: %f s' % (end_time - start_time))
