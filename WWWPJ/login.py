#로그인창 만들기
#기능 : 1. 미림이메일로 고유번호 확인
#      2. 비밀번호 3회 오류시 잠금
#      3. ID : 본인이름 PW : 학교 이메일
#      4. 전공을 + 이름 환영합니다
def show(id,pw):
    print("-------로그인 정보-------")
    print("ID : " + id)
    print("PW(e-mail) : " + pw)
    major = pw[:1] #과추출
    def check_major(major):
        if major == 's':
            return "소프트웨어과"
        elif major =='w':
            return "웹솔루션과"
        elif major == 'd':
            return "디자인과"
    print("{0} {1}님 환영합니다.".format(check_major(major),id))

cnt = 0
id = input("ID입력 : ")
pw = input("PW(e-mail)입력 : ")
# id = '이선우'
# pw = 'w2010@e-mirim.hs.kr'
check_pw = 'e-mirim.hs.kr' in pw #pw값에서 'e-mirim'찾기
while True:
    if check_pw == True : #존재할경우 True / 존재 하지 않을 경우 False
        print(">>>로그인되셨습니다.")
        break
    else:
        print("로그인 실패하셨습니다.")
        cnt += 1
        print("로그인 {0}회 실패".format(cnt))
        if cnt >= 3:
            print("PW를 3회 틀리셨기때문에 시스템을 종료합니다.")
            break

show(id,pw)