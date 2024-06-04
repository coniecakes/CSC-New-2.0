# tuples are immutable - similar to lists, but data within the tuple CANNOT be changed
# lists are defined with [] brackets and tuples are defined by ()
bry = ("Reverb","BCG",34)
gav = ("Cielo","IDK",25)
ryan = ("901W","Navy",24)
mathew = ("Banner Lane","Army",33)
friends_list = [bry, gav, ryan, mathew]
print(friends_list)
print(friends_list[0])
print(0)
print(ryan[0])
print(ryan[1])
print(ryan[2])
print()
# unpacking a tuple - create variables within a tuple and equate it to a previously created tuple
(complex, employer, age) = bry
print("bry")
print("complex = ", complex)
print("employer = ", employer)
print("age = ", age)
print()
# use tuples to swap variables
a = 15
b = 25
(b,a) = (a,b)
print(a)
print(b)
print()
# swapping variables without a tuple
c = 10
d = 15
print (c,d)
temp = c
c = d
d = temp
print(c,d)
