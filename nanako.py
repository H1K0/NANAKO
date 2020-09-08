def encode(plain):
	cipher=[]
	for num in plain:
		neg=num<0
		num=bin(abs(num))[2:]
		while len(num)>7:
			cipher.append('1'+num[:7])
			num=num[7:]
		cipher.append(num.rjust(8,'0'))
		cipher.append(str(int(neg))+bin(len(num))[2:].rjust(7,'0'))
	return bytes(list(map(lambda byte: int(byte,2),cipher)))

def decode(cipher):
	cipher=list(map(lambda byte: bin(byte)[2:].rjust(8,'0'),cipher))
	stack=''
	plain=[]
	i=0
	while i<len(cipher):
		byte=cipher[i]
		if byte[0]=='1':
			stack+=byte[1:]
		else:
			tail=int(cipher[i+1],2)
			neg=1-int(tail>127)*2
			tail%=128
			plain.append(neg*int(stack+byte[-tail:],2))
			stack=''
			i+=1
		i+=1
	return plain