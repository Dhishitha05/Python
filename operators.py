#arithmetic
a=5
b=9
print(a+b)
print(a-b)
print(a//b)
print(a/b)
print(a%b)
print(a*b)
print(a**b)

#assignment
a=3
b=4
a+=b
print(a)
a-=b #here it takes the a value as the latest value which is a+b = 7
print(a) #so this ans will be 3
a*=b
print(a)
a//=b
print(a)
a/=b
print(a)
a**=b
print(a)
a%=b
print(a)

#comparion
a=10
b=7
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)
print(a==b)
a=b=1
print(a==b)

#logical
a=13
b=10
print(a<b and b>a)
print(a<b or a>b)
not True #changes the bool ans

#identify
a=189
print(type(a))
type(a) is int #returns true
print(type(a) is int)
type(a) is not int #returns false
print(type(a) is not int)

b=3+4j
print(type(b))
type(b) is complex #returns true
print(type(b) is complex)
type(b) is int #returns false
print(type(b) is int)
type(b) is not complex #returns false
print(type(b) is not complex)

#membership
a=4, 6, 2, 7, 8, 10, 1, 5, 3
print(6 in a)
print(15 in a)
print(20 not in a)

#bitwise
#&
a=2
b=4
print(bin(2))
print(bin(4))
print(a&b)
a=5
b=7
print(a&b)
print(bin(78))

#|
a=3
b=5
print(bin(3))
print(bin(5))
print(a|b)

#~
a=2
#~a = -(a+1)
print(~a)
#if a is negative then +(a-1)
b=-5
print(~b)

#^
a=6
b=9
print(a^b)

#<<
a=3
print(a<<2)
b=5
print(b<<3)

#>>
a=5
print(a>>3)
