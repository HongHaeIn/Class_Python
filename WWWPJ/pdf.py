class Pdf_Package:
    def detailmenu(self):
        print("========PDFMENU=========")
        print("[ 1. 국어 / 2. 수학 / 3.영어 / 4. 과학 / 5. 자바 / 6. C언어 ]")

        menu = input('메뉴를 선택하세요: ')  # 사용자가 메뉴 선택
        menu = int(menu)  # 인덱스를 위해 문자를 순자로

        if (menu == 1):
            print("1번 [국어] 로 이동합니다.")
            import WWWPJ.pdf_korean
            show_file = WWWPJ.pdf_korean.pdf_Korean_package()
            show_file.show_pdffile()

        elif (menu == 2):
            print("2번 [수학] 로 이동합니다.")
            import WWWPJ.pdf_math
            show_file = WWWPJ.pdf_math.pdf_Math_package()
            show_file.show_pdffile()

        elif (menu == 3):
            print("3번 [영어] 로 이동합니다.")
            import WWWPJ.pdf_english
            show_file = WWWPJ.pdf_english.pdf_English_package()
            show_file.show_pdffile()

        elif (menu == 4):
            print("4번 [과학] 로 이동합니다.")
            import WWWPJ.pdf_science
            show_file = WWWPJ.pdf_science.pdf_Science_package()
            show_file.show_pdffile()

        elif (menu == 5):
            print("4번 [자바] 로 이동합니다.")
            import WWWPJ.pdf_java
            show_file = WWWPJ.pdf_java.pdf_Java_package()
            show_file.show_pdffile()

        elif (menu == 6):
            print("4번 [C언어] 로 이동합니다.")
            import WWWPJ.pdf_C
            show_file = WWWPJ.pdf_C.pdf_C_package()
            show_file.show_pdffile()

        else:
            print("1-6번을 선택하여 주십시오.")
