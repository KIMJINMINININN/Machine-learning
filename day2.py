크롬에서 http://ihongss.com/csv/exam1.csv 다운로드 후 이동
c:/data/exam1.csv 폴더 생성 후



"""
a=1
b=2
c=3
d = [1,  2,  3,  4,  5,  6,  7,  8]
#    0   1   2   3   4   5   6   7
#   -8  -7  -6  -5  -4  -3  -2  -1

print( type(d) )
print( d )
print( d[2] ) #인덱스가 0부터 시작함.
print( d[0:4] ) #0부터 4까지
print( d[:-4] ) #처음부터 -4

for i in d:  # for i in range(1,10,1):
    print(i+1, end=" ")

print()
for i in d:
    if i%3==0:
        print(i, end=" ")
"""

"""
import csv
f = open('C:/Users/ihong/Documents/data/exam1.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
next(rdr, None) #첫번째 라인을 skip
#numlines = len(f.readlines())
s=0
c=0
for i in rdr:
    c = c + 1
    s = s + float(i[4]) + float(i[5]) + float(i[3])

print(s) #합
print(s/c) #평균
"""

"""
for i in range(1,3,1): #1부터 2까지 1씩증가 => 1 2
    print(i)
    for j in range(1,4,1): #1부터 3까지 1씩증가 => 1 2 3
        print("{} - {}".format(i,j))
"""


"""
1 *
2 **
3 ***

for i in range(1,4,1):
    for j in range(1, i+1, 1):
        print("*",end="")
    print(end="\n")
"""


"""
*****
****
***
**
*

for i in range(5,0,-1):
    for j in range(1, i+1, 1):
        print("*",end="")
    print(end="\n")

for i in range(1, 6, 1):
    for j in range(1, 6-i, 1):
        print("*",end="")
    print(end="\n")
"""



"""

print( numlines )
"""
"""
c=0
d=0
c_name = [] #빈 리스트 생성
d_name = [] #빈 리스트 생성

for i in rdr:
    if i[2] =="male":
        c=c+1
        c_name.append(i[0])
    elif i[2] == "female":
        d=d+1
        d_name.append(i[0])

print("{}:{}".format(c,d))
print(c_name)
print(d_name)
"""

"""
#리스트 값 합 구하기
d=["1","2","3","4.0","5"]
s=0
for i in d:
    s=s+float(i)
print(s)    

d = 1 2 3 4 5
s = 0
"""


"""
c=0
for i in range(1,11,1):
    if i%3==0:
        c=c+1
print(c)
"""


"""
c=0
d=0
for i in rdr:
    if i[2] =="male":
        c=c+1
    elif i[2] == "female":
        d=d+1
print("{}:{}".format(c,d))
"""


"""
a = [[1,2],[3,4],[4,5]]
print(a)

for i in a:
    for j in i:
        print(j, end=" ")
    print(end="\n")
print()
"""

"""
1 *
2 ***
3 *****
1 ***
2 *
"""

"""
for i in range(1, 6, 1): # 1 2 3
    if i <= 3:
        for j in range(1, 2*i, 1): # 1 123 12345
            print("*", end="")
    else : # 11-4*2=>3 5*2=>1
        for j in range(1,12-(i*2) , 1): # 123 1
            print("*", end="")
    
    print()    
"""

"""
a = 156780 #원  => 50000:3  10000:0 5000:1 .... 
b = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in b:
    n = a // i  # 156780/50000 = 3
    a = a - (n*i) # 6780
    print("{} - {}".format(i, n))
"""

"""
a = [3, 5, 289, 2, 34, 134]
max = a[0]
min = a[0]

for i in a:
    if max < i:
        max = i

    if min > i:
        min = i

print("최대값은={}".format(max))
print("최대값은={}".format(min))
"""

"""
import csv
f = open('C:/Users/ihong/Documents/data/exam1.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
next(rdr, None) #첫번째 라인을 skip
#numlines = len(f.readlines())
s=0
c=0
for i in rdr:
    print(i)

print()    
f.seek(0) #파일을 처음 읽은것 처럼됨.
next(rdr, None) #첫번째 라인을 skip

for i in rdr:
    print(i)

print()
"""

"""
a = {1, 2, 5, 8}
b = [2, 4, 5]
c = a

for i in b:
    if i not in c:
        c.append(i)

print ( c )

print ( set(a+b) )
print ( set(a) | set(b) )
"""

"""
print()

for tmp in c:
    print (tmp, end=" ")

# a + b = [1, 2, 5, 8, 2, 4, 5]
# a + b = [1, 2, 5, 4, 8]

s1 = set(a)
s2 = set(b)

print( s1 & s2)
print( s1 | s2)
"""

"""
c = {1,2,3,2}
print(c)

a = "aaaa bbbb ccc ccc"
b = a.split(" ")
print(b)
print (set(b))
"""


# 문제 문자열을 입력받아서 a의 개수를 구하시오.
# ex) aaabbbb  => 3
b = "aaabcde"
c = 0
for i in b:
    if i == 'a':
        c=c+1
print(c)



# 문제 문자열을 입력받아서 문자열을 압축하시오.
# ex) aaabbbbbbcccc => a3b6c4
data = "aaabbbbbbcccca"
result = ''  #결과를 보관할 변수
count = 1

for i in range(1,len(data)) :
    if(data[i-1] == data[i]) :
        count += 1
    else :
        result += data[i-1] + str(count)
        count = 1

    if i == len(data)-1 :
        result += data[i] + str(count)
print(result)

