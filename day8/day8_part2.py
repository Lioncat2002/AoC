f=open("inputs.txt","r")
L=f.read().split("\n")

slice=lambda s, t:sum([1 for l in s if l in t])
m=0
for r in L:
	k=r.split('|')
	a=k[0].split()
	b=k[1].split()
	for i in a+b:
		if len(i)==2:one=i
		if len(i)==4:four=i
	s=""
	for i in b:
		if   len(i)==2:s+="1"
		elif len(i)==3:s+="7"
		elif len(i)==4:s+="4"
		elif len(i)==7:s+="8"
		elif len(i)==5:
			if slice(i,one)==2:s+="3"
			elif slice(i,four)==2:s+="2"
			else:s+="5"
		else:
			if slice(i,four)==4:s+="9"
			elif slice(i,one)==2:s+="0"
			else:s+="6"
	m+=int(s)
print(m)


f.close()




