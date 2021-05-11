# # 메뉴창 만들기
# # 기능
# # 메인 메뉴: pdf, 강의, 자습서, 환경설정
# # 디테일 메뉴:
# #     Pdf 메뉴:
# #         국어 / 수학 / 영어 / 과학 / 자바 / C언어
# #     강의 메뉴:
# #         DB / Php / Jsp / Java / Python / DS / C / Wsm / Spring
# #     자습서 메뉴:
# #         DMB / Php / Jsp / Java / Python / DS / C / Wsm/ Spring
# #     환경설정메뉴:
# #         DB / Php / Jsp / Java / Python / C /
#

class Mainmenu:
    print("========MAINMENU=========")
    print("1. PDF모음")
    print("2. 강의추천")
    print("3. 자습서추천")
    print("4. 환경설정")

    menu = input('메뉴를 선택하세요: ')  #사용자가 메뉴 선택
    menu = int(menu)                  #인덱스를 위해 문자를 순자로

    if (menu ==1):
        print("1번 [PDF모음] 메뉴로 이동합니다.")
        import WWWPJ.pdf
        show_menu = WWWPJ.pdf.Pdf_Package()
        show_menu.detailmenu()

    elif (menu ==2):
        print("2번 [강의추천] 메뉴로 이동합니다.")
        import WWWPJ.lecture
        show_menu = WWWPJ.lecture.Lecture_Package()
        show_menu.detailmenu()

    elif (menu ==3):
        print("3번 [자습서추천] 메뉴로 이동합니다.")
        import WWWPJ.tutorial
        show_menu = WWWPJ.tutorial.Tutorial_Package()
        show_menu.detailmenu()

    elif (menu ==4):
        print("4번 [환경설정] 메뉴로 이동합니다.")
        import WWWPJ.enviroment
        show_menu = WWWPJ.enviroment.Enviroment_Package()
        show_menu.detailmenu()

    else:
        print("1-4번을 선택하여 주십시오.")



# from builtins import print
#
#
# class Mainmenu:
#     def __init__(self, Mainmenuname):
#         self.Mainmenuname = Mainmenuname
#
#     def __str__(self):
#         return f'MAINMENU: {self.Mainmenuname}'
#
#
# class Mainmenu_window:
#     _Mainmenu_CATEGRIES = ['선택']
#     _Choice_onlyone = [1]
#
#     def __init__(self, Mainmenuname):
#         self.Mainmenuname = Mainmenuname
#         self.choice_menu = self.choice_menu
#         self.count_menu = Mainmenu_window[self.choice_menu - 1]
#         self.menu = []
#         self.add_menu()
#         self.choice_menu = []
#
#     def add_menu(self):
#         pdf = Mainmenu('PDF 메뉴')
#         majorlecture = Mainmenu('강의 메뉴')
#         majorbook = Mainmenu('자습서 메뉴')
#         majorsetting = Mainmenu('환경설정')
#
#         self.menu.append(pdf)
#         self.menu.append(majorlecture)
#         self.menu.append(majorbook)
#         self.menu.append(majorsetting)
#
#     def show_menu(self):
#         for index, Mainmenu in enumerate(self.menu):
#             print(index + 1, Mainmenu)
#
#     def choice(self):
#         for n in range(self.choice_menu):
#             self.show_menu()
#             Mainmenu = input('메뉴를 고르세요: ')
#             Mainmenu = int(Mainmenu)
#             Mainmenu = self.menu[Mainmenu - 1]
#             self.choice_menu.append(Mainmenu)
#         print('고르신 메뉴 입니다.')
#         for Mainmenu in self.choice_menu:
#             print(Mainmenu)
#
#     def __str__(self):
#         return f'MAINMENU: {self.Mainmenuname}'

