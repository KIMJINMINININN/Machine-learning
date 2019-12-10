import re
Pcount = 0
customer = []
while True:
    choie = input("메뉴를 입력하세요 I:저장,  P:이전고객정보, N:다음고객정보, U:정보수정, D:고객정보삭제, Q:프로그램 종료").upper()
    if choie == 'I':
        # customer1 = []
        # a1 = str(input("이름:"))
        # a2 = input("성별 남자M, 여자 F:")
        # a3 = str(input("이메일:"))
        # a4 = int(input("출생년도:"))
        # customer1.append(a1)
        # customer1.append(a2)
        # customer1.append(a3)
        # customer1.append(a4)
        # customer.append(customer1)
        # print("입력하신 정보는", customer1)
        '''
        regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-z]{2,6}{.}[a-zA-z]{2,3}$')
        while True:
            customer['email']=input("이메일을 입력하세요 :")
            globang = regex.search(customer['email'])
            if globang:
                break
            else:
                print('"@"를 포함한 정확한 이메일을 써주세요')
        '''
        customer1 = {}
        a1 = str(input("이름:"))
        a2 = input("성별 남자M, 여자 F:")
        a3 = str(input("이메일:"))
        a4 = int(input("출생년도:"))
        customer1 = {"name":a1, "sex":a2,"email":a3, "born":a4}
        customer.append(customer1)
    elif choie == 'P':
        if Pcount >= 0 :
            print(customer[Pcount])
        else:
            print("error : 고객정보가 없습니다")
    elif choie == 'N':
        if Pcount < len(customer):
            Pcount = Pcount+1 
            print("고객정보", customer[Pcount])
        else:
            Pcount = len(customer)
            print("error : 고객정보가 없습니다")
    elif choie == 'U':
        pass
    elif choie == 'D':
        pass
    if choie == 'Q':
        break