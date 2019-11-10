import hashlib



def main():
	with open('a.txt', 'r') as afile:
		fo = open("b.txt","w")
		c=0
		for i in afile:
			#print(i,j)
			result = hashlib.md5(str.encode(i)) 
			#print(result.hexdigest()) 
			fo.write(result.hexdigest())
			fo.write("\n")
			c = c+ 1
			print("count : " + str(c))
			
		fo.close()
main()

