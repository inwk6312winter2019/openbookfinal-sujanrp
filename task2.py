def create_log(fi,f1,f2,f3,f4):
	for line in fi:
		if("GET" in line):
			f1.write(line)

		elif("POST" in line):
			f2.write(line)

		elif("PUT" in line):
			f3.write(line)
		
		elif("DELETE" in line):
			f4.write(line)

		


fi = open("access.log")
f1 = open("get.log",'w')
f2 = open("post.log",'w')
f3 = open("put.log",'w')
f4 = open("delete.log",'w')

create_log(fi,f1,f2,f3,f4)

f1.close()
f2.close()
f3.close()
f4.close()

li = []
li2 = []
fget = open("get.log")
fpost = open("post.log")
for l in fget:
	l = l.strip()
	l = l.split()
	li.append(l[0])
	
for l1 in fpost:
	l1 = l1.strip()
	l1 = l1.split()
	li2.append(l1[0])

print("Top 20 IP addresses are of GET: ")
for i in range(0,21):
	print(li[i])

print("Top 20 IP addresses are of POST: ")
for j in range(0,21):
	print(li2[i])



