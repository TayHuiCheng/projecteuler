
"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

tt = 0 # variable for holding the sum of the total, with initial value of 0
for a in range(1,1000): # a is a variable which is a number from 1 to 999  
    if not(a%3 and a%5): # if a/3 and a/5 both have remainders means they are not divisible by 3 or 5 then the a is not added since it is not a multiple
#the if not function does the reverse of if function
#so it means if a%3 or a%5 has a remainder of 0, then it will add up
        tt += a # tt = tt+a
print (tt)

tt = 0
for a in range (0, 1000, 3): #: starts a function. The range (X, Y, Z), x = initial value, final value and step = how much to increae every time (multiple of 3)
#a goes through 0,3,6,9,12...999 before 1000
    tt +=a
for a in range (0, 1000, 5):
    tt +=a
for a in range (0, 1000, 15):
    tt -=a #subtract multiples of 15 since it will be multi-counting the multiples of 3 and 5
print(tt)

    
