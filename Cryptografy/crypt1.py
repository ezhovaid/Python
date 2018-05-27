symbolsAlpha = [chr(x) for x in range(65,91)]
symbolsCrypt = ['!','@','#','$','%','^','&','*','(',')','-','=',
'+','?',':',';','<','>','/','[',']','{','}','|','.',',','~']

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
keys = dict(zip(symbolsAlpha,symbolsCrypt))

def encryptDecrypt(mode, message, final = ""):
	if mode == 'E':
		for symbol in message:
			if symbol in keys: final += keys[symbol]
	else:
		for symbol in message:
			for key in keys:
				if symbol == keys[key]: final += key
	return final
print("Final message:",encryptDecrypt(cryptMode, startMessage))

class write():
    try:
        namefile = input("File name: ")
        with open(namefile, 'ab') as file:
            text = (encryptDecrypt(cryptMode, startMessage))
            file.write(text.encode("utf-8"))
    except FileNotFoundError:
        print("[x] File: '" + str(namefile) + "' is not defined!")
        raise SystemExit
    else:
        print("[+] File: " + str(namefile) + " successfully overwritten!")