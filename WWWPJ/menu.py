#메뉴창 만들기
#기능
# 메인 메뉴: pdf, 강의, 자습서, 환경설정
# 디테일 메뉴:
#     Pdf 메뉴:
#         국어 / 수학 / 영어 / 과학 / 자바 / C언어
#     강의 메뉴:
#         DB / Php / Jsp / Java / Python / DS / C / Wsm / Spring
#     자습서 메뉴:
#         DMB / Php / Jsp / Java / Python / DS / C / Wsm/ Spring
#     환경설정메뉴:
#         DB / Php / Jsp / Java / Python / C /

from builtins import print

class Mainmenu:
    def __init__(self, Mainmenuname):
            self.Mainmenuname = Mainmenuname

    def __str__(self):
        return f'MAINMENU: {self.Mainmenuname}'

class Mainmenu_window:
    _Mainmenu_CATEGRIES = ['선택']
    _Choice_onlyone = [1]
    
    def __init__(self, Mainmenuname):
        self.Mainmenuname = Mainmenuname
        self.choice_menu = self.choice_menu
        self.count_menu = Mainmenu_window[self.choice_menu - 1]
        self.menu = []
        self.add_menu()
        self.choice_menu = []

    def add_menu(self):
        pdf = Mainmenu('PDF 메뉴')
        majorlecture = Mainmenu('강의 메뉴')
        majorbook = Mainmenu('자습서 메뉴')
        majorsetting = Mainmenu('환경설정')

        self.menu.append(pdf)
        self.menu.append(majorlecture)
        self.menu.append(majorbook)
        self.menu.append(majorsetting)
        

    def show_menu(self):
        for index, Mainmenu in enumerate(self.menu):
            print(index+1, Mainmenu)

    def choice(self):
        for n in range(self.choice_menu):
            self.show_menu()
            Mainmenu= input('메뉴를 고르세요: ')
            Mainmenu = int(Mainmenu)
            Mainmenu = self.menu[Mainmenu - 1]
            self.choice_menu.append(Mainmenu)
        print('고르신 메뉴 입니다.')
        for Mainmenu in self.choice_menu:
            print(Mainmenu)

    def __str__(self):
        return f'MAINMENU: {self.Mainmenuname}\t가격: {self.count_menu}원\t종류: {Mainmenu_window._Mainmenu_CATEGRIESS[self.choice_menu -1]}'

해인학생 = Mainmenu_window('선택', 1)
print(해인학생)
해인학생.choice



