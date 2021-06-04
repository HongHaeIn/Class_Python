class Recipe:
    def __init__(self, name):
        self.name = name #이름
        self.whatin = {} #딕셔너리 - 사전 - key-value #재료
        self.time = ' ' #시간
        self.link = ' ' #영상주소
        self.info = ' ' #설명
        self.quantity = 1 #인분
        pass

    def set_link(self):
        link = input('>> 레시피 영상 주소를 입력하세요: ')
        self.link = link
        self.link='입력된 주소가 없습니다.' if link == ' ' else link

    def set_info(self):
        info = input('>> 레시피 정보를 입력하세요: ')
        self.info = info
        self.info = '입력된 정보가 없습니다.' if info == ' ' else info

    def set_quantity(self):
        quantity = input('>> 레시피가 몇 인분 기준인가요?: ')
        self.quantity = quantity
        self.quantity = '1' if quantity == ' ' else quantity

    def set_time(self):
        time = input('>> 레시피 소요시간을 입력하세요: ')
        self.time = time
        self.time = '0' if time == ' ' else time

    def set_whatin(self):
        while True:
            whatin = input('>> 재료를 입력하세요: (예시: 감자 100g)(입력이 끝나면 enter 치세요)')
            if whatin == '':
                break
            name, gram = whatin.split()
            self.whatin[name] = gram+'g'

    def set_recipe(self):
        self.set_link()
        self.set_whatin()
        self.set_time()
        self.set_info()
        self.set_quantity()

    def __str__(self):
        return f'레시피: {self.name}\n 양:{self.quantity}인분\n정보: {self.info}\n링크: {self.link}\n재료: {self.whatin}\n시간: {self.time}'


# 김치찌개 = Recipe('김치찌개')
# 김치찌개.set_whatin()
# 김치찌개.set_info()
# 김치찌개.set_time()
# print(김치찌개)
