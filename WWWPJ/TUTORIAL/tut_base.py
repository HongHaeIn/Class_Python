class Base:
    def tutBase(self):
        print("========BACKFINISHMENU=========")
        print("1. MAINMENU")
        print("2. TUTORIAL")
        print("3. FINISH")

        menu = input('메뉴를 선택하세요: ')  # 사용자가 메뉴 선택
        menu = int(menu)  # 인덱스를 위해 문자를 순자로

        if (menu == 1):
            print("MAINMENU로 이동합니다.")
            import WWWPJ.menu
            show_file = WWWPJ.menu.Mainmenu()
            show_file.mainmenu()

        elif (menu == 2):
            print("TUTORIAL로 이동합니다.")
            import WWWPJ.tutorial
            show_file = WWWPJ.tutorial.Tutorial_Package()
            show_file.detailmenu()

        elif (menu == 3):
            print("프로그램을 종료합니다.")

        else:
            print("1-3을 선택하여 주십시오.")