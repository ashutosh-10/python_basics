# letter = '''
# Hey <|name|>
# \n
# You are selected
# '''
# name= input("Enter name")
# letter =letter.replace("<|name|>",name)
# print(letter)




#find
# letter = "This has double spaces here  okay"
# ds = letter.find("  ")
# letter = letter.replace("  ", " ")
# print(ds,letter)
# # if ds == -1:
# #     print("Not found")



# #lists
# # a  = [1,2,4,6,8]
# # print(a)
# # a = [4,"Ashutosh",9.6]
# # print(a[1])
# a = ["ashutosh", "soumya", "minakshi", "susanta", "rinku", "romy", "jhuni", "tukan"]
# # print(len(a))
# # print(a[-4:-1])
# # print(a)

# # a.sort() 
# # a.reverse()

# a.append("Append")
# a.pop(1)
# a.remove("ashutosh")
# print(a)
















# #tuples

# a = (1,2,4,8,10,1)

# print("acou",a.count(1))
# print("aind",a.index(2))









#listInput

# f1 = input("enter fruit 1 ")
# f2 = input("enter fruit 2 ")
# f3 = input("enter fruit 3 ")
# f4 = input("enter fruit 4 ")
# f5 = input("enter fruit 5 ")
# f6 = input("enter fruit 6 ")
# f7 = input("enter fruit 7 ")
# f8 = input("enter fruit 8 ")
# frls = [f1,f2,f3,f4,f5,f6,f7,f8]
# print(frls)





# #marks list
# s1 = input("enter marks of 1 student")
# s2 = input("enter marks of 2 student")
# s3 = input("enter marks of 3 student")
# s4 = input("enter marks of 4 student")
# s5 = input("enter marks of 5 student")
# s6 = input("enter marks of 6 student")
# s = [s1,s2,s3,s4,s5,s6]
# s.sort()
# print(s)




# #sum of list
# a = [1,2,3,4]
# print(sum(a))






# #count in tuple
# a = (7,0,8,0,0,9)
# print(a.count(0))








# #Dictionary and Sets
# a  = {"python": "Data Science" , "java":"Web App" , "marks":[1,2,3,4], "anotherdic":{"ashutosh":"panda"}}
# print(a['python'])
# print(a['java'])
# print(a['marks'])
# print(a['anotherdic']['ashutosh'])
# print(type(a.keys()))
# print("VALUES OF DIC ARE:- ",a.values(),"\n")
# print("KEYS AND VALUES OF DIC ARE:- ",a.items(),"\n")
# a.update({"upd":"datee"})
# print(a)
# print(a['python'])
# print(a.get('pythonn'))


# a={'alphabet':'a','number':7}
# a['alphabet'] = "hey"
# print(a)














#sets
#cannot add list or dict
# a={1,2,3,4,5,1}
# print(type(a))  
# b=set()
# print(type(b))
# b.add(4)
# b.add(4)
# b.add(4)
# b.add(4)
# b.add(5)
# b.add(5)
# b.add(5)
# b.add(5)
# b.add((9,6,7))
# print(b)
# print(len(b))
# #b.remove(4)
# print(b)

# b.pop()
# print(b)    
# b.clear()
# print(b)














#dict practise set
# a = {
#     "pankha":"fan",
#     "dabba":"box",
#     "ladka":"boy"
# }
# print(a.keys())
# b = input("Enter the word you want the meaning of:- ")
# print("The meaning of the word is:- ", a.get(b)) #because a[b] throws an error if, user gives a wrong input

#practice set 2 dict
# a = input("Enter a")
# b= input("Enter a number")
# c= input("Enter a number")
# d= input("Enter a number")
# e= input("Enter a number")
# f= input("Enter a number")
# g= input("Enter a number")
# h= input("Enter a number")
# st = {a,b,c,d,e,f,g,h}
# print(st)

#practice set 3 dict
# s  = set()
# s.add(4)
# s.add(4.0)
# s.add("4")
# print(len(s))



#names ps dict
# a = {}
# f1 = input("enter fav lang 1")
# f2 = input("enter fav lang 2")
# f3 = input("enter fav lang 3")
# f4 = input("enter fav lang 4")
# a['one'] = f1
# a['two'] = f2
# a['three'] = f3
# a['four'] = f4
# print(a)
                

# a= int(input("age "))
# if(a>=18):
#     print("yes")



# a= [1,2,4,5]
# print(4 in a)




# a = int(input("enter a:- "))
# b = int(input("enter b:- "))
# c = int(input("enter c:- "))
# d = int(input("enter d:- "))
# if (a>d):
#     f1=a
# else:
#     f1=d

# if (b>c):
#     f2=b
# else:
#     f2=c
# if(f1>f2):
#     print(str(f1) + "is greatest")
# else:
#     print(str(f2) + "is greatest")

# sub1 = int(input("enter sub 1 marks"))
# sub2 = int(input("enter sub 2 marks"))
# sub3 = int(input("enter sub 3 marks"))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("fail")
# elif((sub1 + sub2 + sub3) < (300*40)/100):
#     print("Fail because of perce")
# else:
#     print("Pass")
#     # g = (sub1 + sub2 + sub3) < (300*40)/100
#     # print(g)



# txt = input("enter text")
# spam = False
# if ("make a lot of money" in txt):
#     spam = True
# elif ("Subscribe" in txt):
#     spam = True
# elif ("Buy now" in txt):
#     spam = True
# else:
#     spam= False

# if(spam):
#     print("This txt is spam")
# else:
#     print("not spam")



# user = input("enter something")
# if(len(user)<10):
#     print("less than 10")
# else:
#     print("more")


# name = ["ashu", "panda" , "ashutosh"]
# ip  = input("enter name")
# if (ip in name):
#     print("found")
# else:
#     print("not found")



# marks = int(input("Enter marks"))

# if (marks>90):
#     print("Excellent")
# elif (marks>=80):
#     print("B")
# elif (marks>=70):
#     print("C")
# elif (marks>=60):
#     print("D")
# else:
#     print("fail")




#LOOOOPPPPPSSS
# i  = 1
# while i <= 50:
#     print(i)
#     i += 1

# i=1
# while i<=5:
#     print("ashutosh") 
#     i += 1    


# a = ['a','b','c','d']
# i=0
# print(len(a))
# while i<len(a):
#     print (a[i])
# #     i = i+1
# for i in a:
#     print(i)
# for i in range(1,8 ):
    
#     if i==5:
#         continue
#     print(i)
# else:
#     print("for loop executed")



#pass
# i=9
# if i>4:
#     pass

# # while i>3:
# #     pass


# print('hey')
# i=4

# if i>0:
#     pass
    

# while i>6:
#     pass

# def f1(a,b):
#     pass

# print("hEy")



# a= int(input("enter a no  "))
# for i in range(1,11):
#     # c= a*i
#     # print(c)
#     # print(str(a) + "x" + str(i) + "="  + str(i*a) )
#     print(f"{a} x {i} = {a*i}")




# a = ['ashtosh', 'sachin', 'ramu']
# for i in range(0,len(a)):
#     print("Good morning " + a[i])


# b = ['ashutosh', 'aditya', 'sachin']
# for i in b:
#     if i.startswith('a'):
#         print("hello" + i)

# a= int(input("enter a no  "))

# i=1
# while i<=10:
#     print(str(a) + "x" + str(i) + "=" + str(a*i))
#     i = i+1



# a = int(input("enter a no "))
# for i in range(2,a):
#     if(a%i==0):
#         print("Not Prime")
#         break

# else:
#     print("Prime")



# a = int(input('enter a number ')) #5
# # for i in range(1,a):
# #     print()

# # for i in range(a,1,-1):
# #     print(a*(a-1))
# fact = 1
# for i in range(1, a+1): #1....2....3..4..5
#     fact = fact *i                                 #
# print(f"The factorial of {a} is {fact}")









# a =  int(input("enter  a no"))
# for i in range(1,a+1):
  
#     print("*"*i)



# for i in range(4): #rows
#     for j in range(4-i): #columns
#         print("#", end="")
#     print()
 











# for i in range(4):
#     for j in range(4):
#         print("#", end="")
#     print()

####
####
####
####


# for i in range(4):                        
#     for j in range(i+1):
#         print("#",end="")
#     print()

#
##
###
####












# a = int(input("Enter a no:- "))
# for i in range(10,0,-1):
#     print(f"{a} * {i} = {a*i}")




# marks= [12,23,4,5]
# per = (sum(marks)/400)*100
# print(per)

# a= int(input("mrk"))
# b= int(input("mrk"))
# c= int(input("mrk"))
# d= int(input("mrk"))


# def perc(marks):
#     return (((marks[0]+marks[1]+marks[2]+marks[3])/400)*100)

# mks = [12,12,13,12]
# p1 = perc(mks)
# print(p1)


# def greet(name):
#     print("good day" + name)
# greet("Ashutosh")


# def sumn(n):
# #     return 
#  def fact(x):
#      return x * fact(x-1)


# n=4
# pro=1#1....2....6.....24
# for i in range(n): #0 to 3.....0....1.....2....3
#     pro = pro *(i+1) #1.....2....6.....24
# print(pro)



# def fact(n):
#     pro = 1
#     for i in range(n):
#         pro = pro * (i+1)
#     print(pro)

# def factori(x):
#     if x==0 or x==1:
#         return 1
#     return x*factori(x-1)

# hey = factori(4)
# print(hey)
# def recur_factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)

# num = 4

# a = recur_factorial(num)
# print(a)


# n!  = 1*2*3*4*5*.....n
# n=4
# product = 1
# #4! = 1*2*3*4
# #
# for i in range(n):           #i=0,i=1,i=2,i =3
#     product = product * (i+1)#product = 1 * 1,product =1-----product = 1*2,product=2-----product = 2*3,product = 6----product = 6*4,product = 24


# print(product)


# n!  = 1*2*3*4*5*.....(n-1)*n
#n! = (n-1)! * n!
# def factorial_recursive(n):
#     if n==1 or n==0:
#         return 1
#     return n * factorial_recursive(n-1)

# print(factorial_recursive(4))

# def greatest (num1,num2,num3):
#     if num1 > num2 and num1 >num3:
#         print(num1)
#     elif num2>num1 and num2 >num3:
#         print(num2) 
#     elif num3>num1 and num3 >num2:
#         print(num3)

# greatest(44,7,49)

# def farh(cel):
#     return (cel * 9/5) + 32

# print(farh(45))


# def sum(n):
#     if n==1:
#         return 1
#     return n + sum(n-1)

# print(sum(4))
# print("*", end="")
# print("*", end="")
# print("*", end="")
# print("*", end="")
# print()
# print("*", end="")
# print("*", end="")
# print("*", end="")
# print("*", end="")
# print()
# print("*", end="")
# print("*", end="")
# print("*", end="")
# print("*", end="")
# print()

# for i in range(4):
#     for j in range(4-i):
#         print("*", end="")
        
#     print()
    
# n = 6
# for i in range(n):
#     print("*" * (n-i))


# for i in range(n):
#     print("*" * i)


# a = "         Ashutosh Panda        "
# print(a)
# print(a.strip)
# def remove_and_spit(string,word):
#     newStr = string.replace(word,"")
#     return newStr.strip()

# a = "         Ashutosh Panda        "
# print(remove_and_spit(a,"Panda"))


#SNAKE WATER GUN




# import random




# def game(comp,you):
#     if comp == you:
#         return None
#     elif comp == "s":
#         if you == "w":
#             return False
#         if you == "g":
#             return True
#     elif comp == "w":
#         if you == "g":
#             return False
#         if you == "s":
#             return True
#     elif comp == "g":
#         if you == "s":
#             return False
#         if you == "w":
#             return True        


# comp = random.randint(1,3)

# print("Comps turn")

# if comp == 1:
#     comp = "s"
#     # print (comp)
# elif comp == 2:
#     comp = "w"
#     # print (comp)
# elif comp == 3:
#     comp = "g"
#     #  print (comp)

# you = input("Snake(s) Water(w) or Gun(g)")

   
# print(you)


# res = game(comp,you)
# if res == None:
#     print(f"Computer chose {comp}")
#     print(f"You  chose {you}")
    
#     print("Tie")
# elif res== True:
#     print(f"Computer chose {comp}")
#     print(f"You  chose {you}")
#     print(" ----YOU WIN---- ")
# elif res== False:
#     print(f"Computer chose {comp}")
#     print(f"You  chose {you}")
#     print(" ----YOU LOSE---- ")










# f = open('sample.txt','r')
# f = open('sample.txt')
# data = f.read()
# print(data)
# f.close()



# f = open('sample.txt')
# data = f.read(5)
# print(data)
# f.close()

# f = open('sample.txt', 'w')
# f.write("Wrote this now")
# f.close()



# f = open('sample.txt', 'a')
# f.write("\nAppending this")
# f.close()



# with open('sample.txt','r') as f:
#     a= f.read()

# print(a)


# with open('sample.txt') as f:
#     a = f.read()
#     if 'twinkle' in a:
#         print('found')
#     else:
#         print('not found')


# def game():
#     return 89
# score = game()
# with open ("hiscore.txt") as f:
#     hi = int(f.read())


# if hi<score:
#     with open ("hiscore.txt","w") as f:
#         f.write(str(score))

# a=2
# for j in range(2,21):
#     with open(f"tables_mult_table_of{j}", "w") as f:
#         for i in range(1,11):
#             f.write(f"{j} * {i} = {j*i} \n")
    

# words = ["kadda", "kaddu", "dog"]

# with open("sample.txt") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word,"@#$")
    
#     with open("sample.txt","w") as f:
#         f.write(content)





# with open("log.txt") as f:
#     content = f.read()

# if "python" in content:
#     print("Found")






# content =True
# i=1
# with open("log.txt") as f:
#     while content:
#         content = f.readline()
#         if "python" in content:
#             print(f"found at {i}")
#         i+=1
        
# with open("this.txt") as f:z
#     content = f.read()
        
# with open("copy.txt","w") as f:
#     f.write(content)
# file1 = "this.txt"
# file2 = "copy.txt"
# with open(file1) as f:
#     a= f.read()
        
# with open(file2) as f:
#     b = f.read()


# if a==b:
#     print("identical")
# else:
#     print("not identical")

# import os
# with open ("sample1.txt") as f:
#     content = f.read()

# with open ("nww.txt","w") as f:
#     content = f.write(content)
# os.remove("sample1.txt")






class Employee:
    def details():
        