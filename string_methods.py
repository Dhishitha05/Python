#string methods
#len()
a="python"
print(len(a))
b=""
print(len(b))
c=" "
print(len(c))
d="dhishitha kancherla"
print(len(d))

#count()
a="twinkle twinkle little star"
print(a.count("twinkle"))
a="twinkletwinkle"
print(a.count("twinkle"))
print(a.count("k"))
print(a.count(" "))

#find a string
a = "dhishitha"
print(a.find("h"))
print(a.find("m"))
b="dhishitha kancherla"
print(b.find("k"))

#escape sequences
#\n
a = "name\nmobileno\nbranch"
print(a)
#\t
b = "name:dhishitha\tmobileno:9014676478\tbranch:cse"
print(b)
c = "name:dhishitha\nmobile:123\tbranch:cse\ncollege:klh"
print(c)

#replace()
a="wait until you succeed"
print(a.replace("wait", "work"))
b = "dhishitha"
print(b.replace('h', 'n'))

#upper
a="hello"
print(a.upper())
print(a[0].upper())
print(a[2].upper())
print(a.capitalize())
b = 'i am in class'
print(b.title())

#lower
a="HELLO"
print(a.lower())
print(a[3].lower())

#true/false cases
a="python"
print(a.isupper())
print(a.islower())
b='python course'
print(b.isalpha())
b='pythoncourse'
print(b.isalpha())
c='1234'
print(c.isdigit())
d='dhishitha'
print(d.isalnum())
e='dhishitha1234'
print(e.isalnum())
f='dhishitha@1234'
print(f.isalnum())
g='java'
print(g.startswith('j'))
print(g.endswith('a'))

#strip()
a="            class            "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

#split()
a='i love python'
print(a.split())

#join()
a = 'i', 'am', 'interested'
print("".join(a))
print(" ".join(a))
print("b".join(a))
b="python"
print("c".join(b))

