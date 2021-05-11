class pdf_C_package:
    def show_pdffile(self):
        print("C언어PDF:", "https://drive.google.com/drive/folders/1RcUjxbwaHjnriK56DM7MyyMfkwfhYueA?usp=sharing")

        print("========BACKFINISHMENU=========")
        print("1. MAINMENU")
        print("2. PDFMENU")
        print("3. FINISH")

        menu = input('메뉴를 선택하세요: ')  # 사용자가 메뉴 선택
        menu = int(menu)  # 인덱스를 위해 문자를 순자로

        if (menu == 1):
            print("MAINMENU로 이동합니다.")
            import WWWPJ.menu
            show_file = WWWPJ.menu.Mainmenu()
            show_file.menu()

        elif (menu == 2):
            print("PDFMENU로 이동합니다.")
            import WWWPJ.pdf
            show_file = WWWPJ.pdf.Pdf_Package()
            show_file.detailmenu()

        elif (menu == 3):
            print("프로그램을 종료합니다.")

        else:
            print("1-3을 선택하여 주십시오.")