# # # 1-1.주민등록번호 앞 6자리를 변수 id_number에 넣고,
# # # 출생년도 끝 두자리\n출생 월일\n그 두개의 곱 출력
# # from numpy.core import number
# #
# # in_number ="040412"
# # print("출생년도 끝 두자리: "+int(in_number[:2]))
# # print("n출생 월일: "+int(in_number[2:]))
# # print("n두개의 곱 출력하기: "+int(in_number[:2])*int(in_number[2:]))
# #
# #
# # # 1-2. 집 전화번호를 phone_number에 넣고,
# # # 지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
# # phone_number = "010-8997-5892"
# # x = phone_number.index('-')
# # print(phone_number[0:x])
# # print(phone_number[-4:])
# #
# # phone_number2 = "02-1234-5678"
# # print(phone_number2[0:x])
# # print(phone_number2[-4:])
# #
# # #전화번호 입력시, -가 있든 없든  찰떡같이 알아듣기
# # phone_number1 = '010-1234-5678'
# # phone_number2 = '01098765432'
# # phone_number3 = '010 1111 2222'
# #
# # result = phone_number1.replace('-', '')
# # print(result)
# #
# # result = phone_number3.replace(' ', '')
# # print(result)
# #
# #
# # #2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# # # student_number = 2100
# # # cls = int(student_number[1])
# # # print(cls)
# # #
# # # if cls <=0 or cls >= 7:
# # #     print("잘못입력했습니다.")
# # # elif cls > 0 or cls < 3 :
# # #     print("{0}반 뉴미디어소프트웨어과".format(cls))
# # # elif cls > 2 or cls < 5:
# # #     print("{0}반 뉴미디어웹솔루션과".format(cls))
# # # elif cls > 4 or cls < 7 :
# # #     print("{0}반 뉴미디어디자인과".format(cls))
# # #
# # # student_number = "2319"
# # # number = student_number[1]
# # # if number == "1":
# # #     print("1반 뉴미디어소프트웨어과")
# # # elif number == "2":
# # #     print("2반 뉴미디어소프트웨어과")
# # # elif number == "3":
# # #     print("3반 뉴미디어웹솔루션과")
# # # elif number == "4":
# # #     print("4반 뉴미디어웹솔루션과")
# # # elif number == "5":
# # #     print("5반 뉴미디어디자인과")
# # # elif number == "6":
# # #     print("6반 뉴미디어디자인과")
# # #
# # # student_number = "2319"
# # # number = student_number[1]
# # # number = int(number)
# # # if number == 1:
# # #     print(f"{number}반 뉴미디어소프트웨어과")
# # # elif number == 2:
# # #     print(f"{number}반 뉴미디어소프트웨어과")
# # # elif number == 3:
# # #     print(f"{number}반 뉴미디어웹솔루션과")
# # # elif number == 4:
# # #     print(f"{number}반 뉴미디어웹솔루션과")
# # # elif number == 5:
# # #     print(f"{number}반 뉴미디어디자인과")
# # # elif number == 6:
# # #     print(f"{number}반 뉴미디어디자인과")
# #
# #
# #
# # #2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
# # # def get_major(argument):
# # #     if argument[1] == "1" or argument[1] == "2":
# # #         major = "뉴미디어소프트웨어과"
# # #         return argument[0], major
# # #     elif argument[1] == "3" or argument[1] == "4":
# # #         major = "뉴미디어웹솔루션과"
# # #         return argument[0], major
# # #     elif argument[1] == "5" or argument[1] == "6":
# # #         major = "뉴미디어디자인과"
# # #         return argument[0], major
# #
# # majors = ['0' '뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어디자인과']
# # print(f'{number}반 {majors[(number-1) //2]}')
# #
# #
# #
# # grade, major = get_major('2100')
# # print(f'{number}반 {majors[number-1]}')
# #
# #
# # #2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# # def average(*number):
# #     sum=0;
# #     for num in number:
# #         sum+=num
# #     return sum / len(number)
# #
# # print(average(10,20,30))
# #
# # def average2(*numbers):
# #     return sum(numbers) / len(numbers)
# #
# # print(average2(10, 20, 30))
# # print(average2(4, 23))
# #
# # def average3(*numbers):
# #     sum_value = 0
# #     count = 0
# #     for number in numbers:
# #         sum_value += number
# #         count += 1
# #         return sum_value / count
# #
# # print(average3(10, 20, 30))
# # print(average3(4, 23))
# #
#
# #
# # #2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# # def get_bmi(cm, kg) :
# #     return round(kg/((cm/100)*(cm/100)),1)
# # bmi = get_bmi(176, 69)
# # print(bmi)
# #
# # def get_bmi(height, weight):
# #     height /= 100
# #     return round(weight/height ** 2, 1)
#
# # bmi = get_bmi(160, 60)
# # if bmi < 18.5:
# #     print('저체중')
# # elif bmi < 23:
# #     print('정상')
# # elif bmi < 25:
# #     print('과제충')
# # elif bmi <= bmi:
# #     print('비만')
#
# #구구단 7단 출력하기
# # print(f'7 x 1 = {7 * 1}')
# # print(f'7 x 2 = {7 * 2}')
# # print(f'7 x 3 = {7 * 3}')
#
# # for dan in range(2, 10):
# #     for i in range(1, 9 + 1):
# #         print(f'{dan} x {i} = {dan * i}
# #     print('-' * 10)
# #
# # for dna in range(2, 7):
# #     if dna == 7
# #         break
# #     for i in range(1, 9+1):
# #         print(f'{dan} X {i} = {dan * i}')
# #     print('-' * 10)
# #     if dan == 7:
# #         break
#
# # Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
# def n_sum(argument):
#     result = 0
#     num = str(argument)
#     if len(num) >= 10:
#         return -1
#     for i in range(len(num)):
#         result += int(num[i])
#     return result
# result = n_sum(10)
# print(result)
# result = n_sum(331)
# print(result)
# result = n_sum(408)
# print(result)
# result = n_sum(1000000000)
# print(result)
# result = n_sum(10)
# print(result)        #1
# result = n_sum(331)
# print(result)
# result= n_sum(1000000000)
# # print(result)lt)         #7
# result = n_sum(408)
# print(result)         #12
# result = n_sum(1000000000)
# print(result)         #-1
#
# # # Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
# # # * 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
# def get_subway_fare(km):
#     money_S = 720
#     if(km<=10):
#         return money_S
#     elif(10<=km<50):
#         C_money1 = round(km/5,0)*100 #추가금액
#         return money_S + C_money1
#     elif(km>50):
#         C_money1= round((km-50),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -1)/5*100
#         C_money2 = round(km/8,0)*100 #추가금액
#         return money_S + C_money1 + C_money2
# fare = get_subway_fare(5)
# print(fare)        #720
# fare = get_subway_fare(26)
# print(fare)        #11120
# fare = get_subway_fare(61)
# print(fare)        #1720
#
#
# # # Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
# # # * 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
# def get_three_six_nine(num):
#     number = str(num)
#     result = ""
#
#     count = (number.count('3') + number.count('6') + number.count('9'))
#     if count != 0:
#         for i in range(count):
#             result += '짝'
#     else:
#         result= number
#     return result
# result = get_three_six_nine(1)
# print(result)        #1
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝
# result = get_three_six_nine(36)
# print(result)        #짝짝
#
# # Quiz3-4. 나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
# # 1. 함수의 이름을 정해준다.
# # 2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
# # 3. 리턴하는 것을 말해준다.
# # 4. 출력 예시를 보여준다.
# # 5. 내가 낸 문제의 답안을 제출한다.
#
# #248 게임 하기
#
#
# def get_two_four_eight(num):
#     number = str(num)
#     result = ""
#
#     count = (number.count('2') + number.count('4') + number.count('8'))
#     if count != 0:
#         for i in range(count):
#             result += '짝'
#     else:
#         result = number
#     return result
#
# result = get_two_four_eight(2)
# print(result)        #1
# result = get_two_four_eight(4)
# print(result)        #짝
# result = get_two_four_eight(18)
# print(result)        #짝
# result = get_two_four_eight(26)
# print(result)        #짝
#
# # Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
# # is_prime() 함수를 만든다.
# # 인수로 1개의 숫자를 받는다.
# # 인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
def is_prime(num):
    number = str(num)
    result = ""

    num = ...
    if num != pirme_number:
        result ="소수아님"
    else:
        result= "소수"
    return result

result = is_prime(2)
print(result)     #소수
result = is_prime(13)
print(result)     #소수
result = is_prime(36)
print(result)     #소수 아님

# # Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
# # '고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
# # '놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다.

#모르겠습니다 죄송해용 ..