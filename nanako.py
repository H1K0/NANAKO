def encrypt(plain):
	plain=list(map(lambda num: bin(num)[2:],plain))
	cipher=[]
	for num in plain:
		while len(num)>7:
			cipher.append('1'+num[:7])
			num=num[7:]
		cipher.append(num.rjust(8,'0'))
		cipher.append(bin(len(num))[2:])
	return bytes(list(map(lambda byte: int(byte,2),cipher)))

def decrypt(cipher):
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
			plain.append(stack+byte[-tail:])
			stack=''
			i+=1
		i+=1
	return list(map(lambda num: int(num,2),plain))