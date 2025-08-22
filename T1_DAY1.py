#Program to check whether it is a leap year or not
year=int(input("Enter a year:"))
if(year%100 and year%100!=0)or year%400==0:
    print("It is a leap year")
else:
    print("It is not a leap year")



#Check whether the number is even or odd
num=int(input("Enter the num:"))
if (num&1)==0:
    print("Even")
else:
    print("Odd")
    


#Write a program to swap two numbers
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
a,b=b,a
print(a)
print(b)



#Codeforces(4(a))
w=int(input("Enter the weight of the watermelon"))
if w%2==0:
    print("No")
else:
    x=w//2
    if x%2==0:
        print(x,x)
    else:
        print(x-1,x+1)


#codeforces(617(A))
#The Elephant Problem
x=int(input())
if x>5:
    print(1)
elif x%5==0:
    print(x//5)
else:
    print((x//5)+1)


#To get user input in single line
a, b, c = map(int, input("Enter the nums: ").split())
print(a, b, c)


# Codeforces - Ann problem
#n=total no.of.travels
#m=total no.of.travels using metrocard(30)
#a=cost of normal ticket
#b=cost of metrocard
n,m,a,b=map(int,input().split())
# Calculate minimum cost
cost = min(n * a, (n // m) * b + min(b, (n % m) * a))
print(cost)


#other basic 10 problems to practice were given

