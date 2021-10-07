
from builtins import print


class Icecream:
    def __init__(self, name, flavor):
            self.name = name
            self.flavor = flavor

    def set_description(self, description):
        self.description = description

    def __str__(self):
        return f'이름: {self.name}\t맛: {self.flavor}'

class Cup:
    _CUP_CATEGRIES = ['싱글컵', '더블컵', '파인트']
    _PRICES = [4000, 6200, 8200]

    def __init__(self, name, count_flavor):
        self.name = name
        self.count_flavor = count_flavor
        self.price = Cup._PRICES[self.count_flavor - 1]
        self.menu = []
        self.add_menu()
        self.order_menu = []

    def add_menu(self):
        오레오쿠키앤크림 = Icecream('아이스쿠키앤크림', '#크림치즈아이스크림#오레오쿠키#크림치즈크런치')
        오레오쿠키앤크림.set_description('부드러운 바닐라향 아이스크림에, 달콤하고 진한 오레오 쿠키가 듬뿍!')

        초콜릿무스 = Icecream('초콜릿무스', '#초콜릿#무스#초콜릿칩')
        초콜릿무스.set_description('초콜릿 칩이 들어있는 진한 초콜릿 아이스크림')

        엄마는외계인 = Icecream('엄마는외계인', '#밀크초콜릿#다크초콜릿#화이트무스')
        엄마는외계인.set_description('밀크 초콜릿, 다크 초콜릿, 화이트 무스 세 가지 아이스크림에 달콤 바삭한 초코볼이 더해진 아이스크림')

        self.menu.append(오레오쿠키앤크림)
        self.menu.append(초콜릿무스)
        self.menu.append(엄마는외계인)

    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(index+1, icecream)

    def order(self):
        for n in range(self.count_flavor):
            self.show_menu()                #메뉴 보여주기
            flavor = input('맛을 고르세요: ') #사용자 선택
            flavor = int(flavor)            #인데그를 위해 문자-> 숫자
            icecream = self.menu[flavor - 1]#메뉴에서 인덱스로 가져오자
            self.order_menu.append(icecream)#주문한 메뉴에 추가하자
        print('주문한 아이스크림입니다.')
        for icecream in self.order_menu:    #주문내역 보여주자
            print(icecream)

    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}원\t종류: {Cup._CUP_CATEGRIES[self.count_flavor -1]}'


해인이꼬 = Cup('더블컵', 2)
print(해인이꼬)
해인이꼬.order()

