# def grow(arr):
#     total=1
#     for i in arr:
#         total *=i
#     return total
# print(grow([5,7,10]))



# def find_multiples(n, limit):
#     total=0
#     while total!=limit-n:
#         total=n+n
#     return n,total,limit  
 
# print(find_multiples(5,25))




# def count_positives_sum_negatives(arr):
#     if arr==0:
#         return 0
#     else:
#         return sum(arr)>0
#         return sum(arr)<0

# arr=[5,10,7,5,-5,-7,-5,-10]
# print(count_positives_sum_negatives(arr))

# def powers_of_two(n):
#     if n==0:
#         return 1
#     elif n>0:
#         arr=[]
#         while len(arr)!=int(n):
#             arr+=n 
#     return arr
# print(powers_of_two(2))
# def say_hello(name):
#     a=["Hello",name]
#     w=", ".join(a)
#     return w
# print(say_hello("Mr.Beast"))





# def between(a,b):
#     if a<b:
#         while a!=b:
#             total=[]
#             total=a+1
#     return total
# print(between(1,5))


# def tower_builder(n_floors):
#     if n_floors>0:
#         return "*" * n_floors
# print(tower_builder(5))


# def min_max(lst):
#     if len(lst)>2:
#         return min(lst),max(lst)





# def solution(nums):
#     return nums.sort()
 

# print(solution([1,2,3,6,1,810,8]))

# def duty_free(price, discount, holiday_cost):
#     result  = price * discount
#     result1 = result//100
#     if type(result1)==int:
#         return holiday_cost//result1
#     elif type(result1)==float:
#         return holiday_cost//result1
# print(duty_free(17,10,500))

# def high_and_low(number):
#     number.split()
#     result = (int(x) for x in number)
#     m1= max (result)
#     m2= min (result)
#     mm1= str (m1)
#     mm2= str (m2)
#     return mm1,mm2

# print(high_and_low("1 2 3 4 5"))

# def sum_mix(arr):
#     for i in arr:
#         if type(i)==str:
#             i1=int(i)
#             s1=str(i)
#             s2=int(s1)
#             return s2+i1
 
        

# print(sum_mix(["5",5]))


# def greet(name):
#     n=name.capitalize()
#     total = ["Hello",n]
#     w=" ".join(total) 
#     return w+"!"
    
# print(greet("JACK"))

# def calculate_years(p, i, t, d):
#     f = p
#     r = f * (1+t)
#     return r

# print(calculate_years(1000, 0.05, 0.18, 1100))




# def splitSentence(s):
#     return(s.split())

# print(splitSentence("hello world"))
# bmi1=0
# bmi2=0
# def bmi(weight, height):
#     bmi1=height*height
#     bmi2=weight/bmi1
#     bmi3=bmi2
#     if bmi3<=18.5:
#          return "Underweight"
#     elif bmi3<=25.0:
#          return "Normal"
#     elif bmi3<= 30.0:
#         return "Overweight"
#     elif bmi3>30.0:
#          return "Obese"
    
# print(bmi(100,1.80))
    
# def likes(names):
#     n="".join(names)
#     r1=[n, "likes this"]
#     t=" ".join(r1)
#     names.append("and")
#     names.append("like this")
#     nn=names[0]+names[2]+names[1]+names[3]

#     if len(names)==0:                                 #"Jacob and Alex like this"
#         return "no one likes this"
#     elif len(names)==1:
#         return t.capitalize()
#     else:
#         return 2



# print(likes([["Jacob", "Alex"] ]))

# def count_by(x, n):
#     lst=[]
#     total=0
#     t1=x*n
#     while total!=t1:
#         total+=x
#         lst.append(total)
#         return lst




# print(count_by(1,10))


# def array_diff(a, b):
#     result = []
#     for i in a:
#         if i not in b:
#             result.append(i)
#     return result

# print(array_diff([1,2,3],[1]))


# def digital_root(n):
#     result=[]
#     t = str(n)
#     t.split()
#     w="".join(t)
#     for i in w:
    
#        result.append(int(i))
#        continue
#     s =  sum(result)
#     if s>=10:
#         result.append(int(i))
        
#     return sum(result)
 
# print(digital_root(942))


    


# print(digital_root(942))



# def digital_root(n):
#     result=[]
#     result1=[]
    
#     t = str(n)
#     t.split()
#     w="".join(t)
#     for i in w:
#         result.append(int(i))
#         continue
#     s=sum(result)
#     if s>=10:
#         r = str(result)
#         r.split()
#         w1="".join(r)
#         for x in w1:
#             result1.append(int(x))
#             continue
#         return sum(result1)

# def create_phone_number(n):
#     n1 = n[:3]
#     n2 = n[3:6]
#     n3 = n[6:]
#     r1 = ""
#     for i in n1:
#         r1 += str(i)
        
#     r2 = ""
#     for i in n2:
#         r2 += str(i)
        
#     r3 = ""
#     for i in n3:
#         r3 += str(i)
        
#     return "("+r1+") "  +r2+"-"+r3
        




# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))         # => returns "(123) 456-7890")


# def find_outlier(i):
#     even=[]
#     odd=[]
#     if sum(i) % 2 !=0:
#         for x in i:
#             if x % 2 !=0:
#                 even.append(x)
#                 w="".join(map(str,even))
#                 s= int(w)
#                 return s
#     else:
#         for x in i:
#             if x % 2 == 0:
#                 odd.append(x)
#                 w="".join(map(str,odd))
#                 s= int(w)
#                 return s
                
                
                
                
            



# print(find_outlier([2, 4, 6, 8, 10, 3]))

# def find_outlier(i):
#     even=[]
#     odd=[]
#     for x in i:
#         if x % 2 == 0:
#             even.append(x)
#         else:
#             odd.append(x)
#     if len(even)==1:
#         return even[0]
#     else:
#         return odd[0]
        




# print(find_outlier([2, 4, 6, 8, 10, 3]))

# def count_by(x, n):
#     result = []
#     result.append(x)
#     s = x*n
#     while x!=s:
#         x+=x
#         result.append(x)
#     return result

# print(count_by(1,10))




# def name_shuffler(s):
#     result =s.split()
#     result1 = result[::-1]
#     result2 = " ".join(result1)
#     return result2


# print(name_shuffler('john McClane'))


def find_short(s):
    result = s.split()
    return len(min(result,key=len))

print(find_short("lets talk about javascript the best language"))