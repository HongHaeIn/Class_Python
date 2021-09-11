#숫자 야구 게임
#퀴즈 내자(숫자 3자리 중복 없이)
def make_quiz():
    #숫자 3자리 중복 업이
    return "238"

answer = make_quiz()
print(answer)


def check(answer, player):
    strike = 0
    ball = 0
    #번호가 있고 자리가 같으면 strike += 1
    #번호가 있고 자리가 다르면 ball += 1
    return strike, ball


#무한반복
while True:
    #숫자 3자리 중복없이 묻자
    player = input("숫자 세자리를 입력하세요 >>> ")
    #strike, ball 확인하자
    strike, ball = (check(answer, player)
    #출력하자
    print(f'{player}\tstrike: {strike}\tball : {ball}')
    #strike가 3일 때 나가자
    if strike == 3:
        break
#축하해주자

answer = make_quiz()
print(answer)
check("238", "241")
print(strike, ball)