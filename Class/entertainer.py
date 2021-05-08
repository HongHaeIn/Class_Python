class Entertainer:
    def __init__(self, name):
        self.name = name

    def set_height(self, height):
        self.height = height

    def set_face(self, face):
        self.face = face

    def set_kind(self, kind): #인성
        self.kind = kind

    def set_name(self, name):
        self.name = name

    # def info(self):
    #     print(f'이름: {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}')

    def __str__(self):
        return f'이름: {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}'
백현 = Entertainer('변백현')
백현.set_name('백현')
백현.set_height('174cm')
백현.set_face('강아지상')
백현.set_kind('착하고 귀엽고 리더역할일땐 리더역할을 잘 해냄')
print(백현)

아빠 = Entertainer('홍석강')
아빠.set_name('석강띠')
아빠.set_height('175cm')
아빠.set_face('홍해인 남자 ver')
아빠.set_kind('ESFJ')
print(아빠)

class Singer(Entertainer):
    def __init__(self, name, song):
        super().__init__(name)     # self.name = name
        self.song = song

    def __str__(self):
        return super().__str__()+f'\t대표곡: {self.song}'

김세정 = Singer('김세정', 'Warning')
김세정.set_height('164cm')
김세정.set_face('사슴같은 얼굴에 눈이 맑음')
김세정.set_kind('인성돌로 유명')
print(김세정)

십센치 = Singer('권정렬', 'pet, 폰서트')
십센치.set_height('172cm')
십센치.set_face('사슴같은데 섹시함')
십센치.set_kind('날 설레게 해놓고 유부남임 화난다')
print(십센치)

인디음악 = []
인디음악.append(김세정)
인디음악.append(십센치)
print(인디음악)

class Talent(Entertainer):
    def __init__(self, name, drama):
        super().__init__(name)
        self.drama =drama

    def __str__(self):
        return super().__str__() +f'\t드라마: {self.drama}'


정해인 = Talent('정해인', '당신이 잠든 사이에')
정해인.set_height('175cm')
정해인.set_face('완전 귀여움 ㅠㅠㅠㅠㅠ 제복 입어줘 평생')
정해인.set_kind('착함 진짜')
print(정해인)