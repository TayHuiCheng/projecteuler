"""The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

sqm = 0 #sum of the squares
sum = 0 #sum of the numbers to be for finding the square of the sum later 
# these 2 variables can also be written as sum = sqm = 0

for a in range(1,101):  # for integer between 1 to 100, so it starts at 1 and end before the last number, which is 101.
    sqm += a*a #sqm is to increase by a*a, 
    sum += a #sum is to crease by a
    
print(sum*sum - sqm)
