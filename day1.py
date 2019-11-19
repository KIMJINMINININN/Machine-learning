파이썬 설치 : http://ihongss.com/home/post?id=p_1573360254079

a = 3
b = 3.5
c = "hello"

print(a)
print(b)
print(c)

print( type(a) )
print( type(b) )
print( type(c) )

#################################################
a = int(input('첫 번째 숫자를 입력하세요'))
b = int(input('두 번째 숫자를 입력하시요'))

print( type(a) )
print( type(b) )
print(a + b)  #합
print(a - b)  #차
print(a * b)  #곱
print(a // b) #몫
print(a % b)  #나머지

#####################################################

#문제 3개의 숫자를 입력받아서 합과 평균을 구하시오.
a,b,c = map(int, input("숫자를 3개 입력하세요.").split(","))
print( a+b+c )
print( (a+b+c)//3 )

#문제 3개의 숫자를 입력받아서 첫번째, 세번째 숫자의 차를 구하시오.
print( a-c )



a = int(input("숫자를 입력하세요"))
b = int(input("숫자를 입력하세요"))
c = int(input("숫자를 입력하세요"))

if a > b and a > c :
    print("a가 가장 큽")
elif b > a and b > c :
    print('b가 가장 큼')
else :
    print('c가 가장 큼')
    
print("if문과 상관없이 항상 실행")

#############################################################33

#문제 국어,영어, 수학 점수를 입력받아서 평균이 
# 90이상이면 A
# 80이상이면 B
# 70이상이면 C
# 나머지는 D


"""
a,b,c = map(int, input("숫자를 3개 입력하세요.").split(",")) # 45,67,89
sum = (a + b + c)//3

if sum>=90 :
    print("A")
elif sum >= 80 :
    print("B")
elif sum >= 70 :
    print("C")
else :
    print("D")            
"""

"""
a = int(input("숫자를 입력하세요"))
if a%5 == 0:  # == 같냐?  != 다르냐?
    print("5의 배수입니다.")
else :
    print("5의 배수가 아닙니다.")    
"""


"""
x = int(input("숫자입력"))

if 11 <= x <= 20:
    print("11~20")
elif 21 <= x <= 30:
    print("21~30")        
"""

"""
# 반복문
for i in range(0, 10, 2) : #range(0, 10, 1)  시작숫자, 조건(9까지), 증가값
    print("hello world : " + str(i))
"""
"""
for i in range(10, 0, -2): #10부터 1까지 2씩 감소
    print(i)

# 문제 숫자 2개를 입력받아서 그 사이의 숫자를 출력하시오.
# ex) 1 5 => 
1 
2 
3 
4 
5

# ex) 5 1 => 1 2 3 4 5

a=1
b=5

if a < b:
    for i in range(a, b+1, 1):
        print(i, end=" ")
else :
    for i in range(b, a+1, 1):
        print(i, end=" ")
"""

"""
a=3
b=4
print("{0}+{1}={2}".format(a,b,(a+b))) #3+4=7
"""

"""
숫자 1개를 입력받아서 3의 배수 5의 배수 3, 5배수를 출력하시오
16을 입력했을 경우
ex) 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ... 
    X X 3 X 5 3 X X 3  5  X  3  X  X 35 X ...
a = int(input("숫자입력?"))  #16

for i in range(1, a+1, 1):
    if i%3 == 0 and i%5 == 0 :
        print("{}-{}".format(i, "35"))
    elif i%3 == 0 :
        print("{}-{}".format(i, "3"))
    elif i%5 == 0 :
        print("{}-{}".format(i, "5"))
    else :
        print("{}-{}".format(i, "X"))            
"""

"""
#1부터 10까지 짝수 구하기
a=0
for i in range(1,11,1):
    if i%2==0:
        a=a+1
print(a)
"""


"""
숫자1개를 입력받아서 끝자리가 3 과 7인 숫자의 개수를 구하시오.
ex ) 1 2 3 4 5 6 7 8 9 10 11 12 13 => 3
"""

a = int(input("숫자입력?"))
b = 0

for i in range(1, a+1, 1) :
    if i%10 == 3 or i%10 == 7 :
        b=b+1
        
print("개수는{}".format(b))
