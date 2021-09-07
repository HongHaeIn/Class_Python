# 1. 핸드폰 요금이 62421원 나왔다. 100원 미만은 절사한다고 한다. 62400원 청구. 59827원일 경우, 실제 청구 금액은?

sellphone = (62421 / 100)
round(sellphone)
print(sellphone)


# 2. 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다. 채점한 결과 93점이 나왔다. 90점 부여. 56점은 몇 점 부여?

test_score1 = 9.3
test_score2 = 5.6
round(test_score1)
round(test_score2)
print(test_score1)
print(test_score2)

print(round(9.3))
print(round((5.6)))
# 3. 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
import random
i = random.randint(1, 45)

# 4. 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)

# 5. 내가 태어난 날로부터 며칠이 지났는지?
print("얼만큼 살았는지 보자")
import datetime
now = datetime.datetime.now()
print(now)
birthday = datetime.datetime(2004, 4, 12, 11, 30)
print(birthday)
print(now - birthday)

# 6. 올해 크리스마스까지 며칠이 남았는지?
print("내 솔크가 얼마나 남았는지 굳이 계산해보고 상처 받아보자")
now = datetime.datetime.now()
print(now)
ch = datetime.datetime(2021, 12, 25, 00, 00)
print(ch)
print(ch - now)

# 7. 내 생일이 며칠 남았는지?
print("다음 생일엔 생일도 가야지")
now = datetime.datetime.now()
print(now)
birthday = datetime.datetime(2022, 4, 12, 11, 30)
print(birthday)
print(birthday-now)

# 8. 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?