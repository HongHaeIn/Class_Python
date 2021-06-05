class Base:
    def tutBase(self):
        # BACKMENU: 1.MAINMENU, 2.PDFMENU, 3.FINISH
        print("========BACKMENU=========")
        print("1. MAINMENU")
        print("2. TUTORIAL")
        print("3. FINISH")

        menu = input('메뉴를 선택하세요: ')                     #사용자가 메뉴 선택하게 하자
        menu = int(menu)                                    #인덱스를 위해 문자를 순자로 바꿔주자

        if (menu == 1):
            print("MAINMENU로 이동합니다.")
            import WWWPJ.menu                               #menu 파일로 임폴트 하자
            show_file = WWWPJ.menu.Mainmenu()               #menu 파일에 Mainmenu 클래스에 들어가자
            show_file.mainmenu()                            #Mainmenu 클래스에 mainmenu 함수를 보여주자

        elif (menu == 2):
            print("TUTORIAL로 이동합니다.")
            import WWWPJ.tutorial                           #tutorial 파일로 임폴트 하자
            show_file = WWWPJ.tutorial.Tutorial_Package()   #tutorial 파일에 Tutorial_Package 클래스에 들어가자
            show_file.detailmenu()                          #Tutorial_Package 클래스에 detailmenu 함수를 보여주자

        elif (menu == 3):
            print("프로그램을 종료합니다.")                     #프로그램을 종료하는 메세지를 보내주자

        else:
            print("1-3을 선택하여 주십시오.")                   #1번부터 3번까지 고르지 않았을 경우엔 에러메세지를 보내주자