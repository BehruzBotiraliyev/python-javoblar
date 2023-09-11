# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 11:55:38 2023

@author: Uzbb
"""

# uy_raqami = int(input())
# s = []
# for son in range(1,uy_raqami)  :
#     if(son + son%100 ==uy_raqami) :
#         s.append(son)

# N = int(input())
# s = 0
# for son in range(N+1):
#   s = s + son
# print(s)

# T =int(input())
# s = []
# for son in range(T):
#     s.append(int(input()))
# for son in s:
#     if son == 1:
#         print(1)
#     else :
#         print(son//2)
        
# N  = int(input())
# print((N*(N-3))//2)

# N = int(input())
# s1 = 1
# for son in range(1,N+1):
   
# N = int(input())
# s2=0
# for son in range(N+1):
#   for s in range(N+1):      
#      if son>=s and son+s ==N :
#       s2= s2+1
# print(s2)    
# N =int(input())
# S = 1
# for son in range(1,N+1) :
#   S = S *son
# print(S%(N+1))
# N = int(input())
# if N>=38 :
#    if N%5>=3:
#        print(5*(N//5+1))
#    else :
#        print(N)
# else :
#     print(N)
# T = int(input())
# s = []
# for son in range(T):
#     s.append(int(input()))
# for son in s :
#     if son%2==0:
#         print(1)
#     else :
#         print(0)
# T = int(input())
# s = []
# for son in range(T) :
#     s.append(int(input()))
# for son in s :
#   a=0
#   b=0
#   if son>0 :
#    for a in range(1,son+1):
#      if son%a == 0 :
#        if a%2 ==0 :
#           a = a+1
#        else :
#           b = b+1
#   if a==b :
#      print("Yes")
#   if a!=b :
#      print("No")
# n = int(input())
# a=0
# for son in range(1,n+1) :
#   if (son%3 == 0 or son%5 ==0 or son%7==0) :
#        a = a +son
# print(a)       
# R = float(input())
# PI = 3.141593
# print(PI*R**2)
# print(((2*R)**2)/2)

# s = []
# for son in range(9) :
#     s.append(int(input()))


# N = int(input())
# N = str(N)
# if len(N)== 6 :
#     if int(N[0:1])+int(N[1:2])+int(N[2:3]) == int(N[3:4])+int(N[4:5])+int(N[5:6]) :
#         print("Yes")
#     else :
#         print("No")
# N = int(input())
# a = 0
# for son in range(1,N+1):
#   a = a +son
#   if a == N or a+son>N:
#       print(son)
N  =int(input())
summa=0
if N>=0 :
    for son in range(N+1) :
        summa =summa+son
else :
    for son in range(N,2):
        summa=summa +son
print(summa)













