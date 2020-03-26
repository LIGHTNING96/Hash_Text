
from hashing import Fucken_hash
text = str(input("Hello Mother fucker input your text plz ==> : "))
hashtype = str(input("input hash type mother fucker ==> : "))
while text=="":
    print("your text Mother Fucker")
    text = str(input("Hello Mother fucker input your text : "))
    if text !="":
        break
while hashtype=="":
    print("your hashtype Mother Fucker")
    hashtype = str(input("Hello Mother fucker input your hashtype : "))
    if hashtype !="":
        break


h =Fucken_hash()
print(h.fucken_hash(text,hashtype))
input("Enter to exit")
