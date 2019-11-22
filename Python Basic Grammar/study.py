#별 찍기- 1
'''
N = int(input("몇번째줄까지 별을 출력할까요(1~100)"))
a = "*"
for i in range(0, N+1, 1):
    print(a)
    a = a + "*"
'''
#별 찍기- 2
'''
N = int(input("몇번째줄까지 별을 출력할까요(1~100)->오른쪽정렬"))
a = "*"
for i in range(0, N+1, 1):
    print("{0:>100}".format(a))
    a = a + "*"
'''
#별 찍기- 3
N = int(input("몇번째줄까지 별을 출력할까요(1~100)->왼쪽으로 거꾸로"))
a = "*"
for i in range(0, N-1, 1):
    a = a + "*"
print(a)
a = a - "*"

    