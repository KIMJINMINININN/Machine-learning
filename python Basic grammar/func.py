def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a=1,b=1):
    return a*b

def tot(a):
    sum = 0
    for i in range(1,a+1):
        sum = sum + i
    return sum
    print("1부터 a까지의 합은",sum,"입니다")

def avg(a):
    sum = 0
    avg = 0
    for i in range(1,a+1):
        sum = sum + i
        avg = sum/a
    print("1부터 a까지의 평균은",avg,"입니다")
    return avg

#자신이 자신을 수행했을때 실행해되게 만들어주는 방법
#즉 main문이라고 생각할수있다
if __name__ == "__main__":
    print("AAA")