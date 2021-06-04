class Tutorial_Package:
    def detailmenu(self):
        print("[1. DB / 2. Php / 3. Jsp / 4. Java / 5. Python / 6. DS / 7. C / 8. Wsm / 9. Spring ]")

        menu = input('메뉴를 선택하세요: ')  # 사용자가 메뉴 선택
        menu = int(menu)  # 인덱스를 위해 문자를 순자로

        if (menu == 1):
            print("1번 [DB] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_db
            show_file = WWWPJ.TUTORIAL.tut_db.tutorial_Db_package()
            show_file.show_tutfile()

        elif (menu == 2):
            print("2번 [Php] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_php
            show_file = WWWPJ.TUTORIAL.tut_php.tutorial_Php_package()
            show_file.show_tutfile()

        elif (menu == 3):
            print("3번 [Jsp] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_jsp
            show_file = WWWPJ.TUTORIAL.tut_jsp.tutorial_Jsp_package()
            show_file.show_tutfile()

        elif (menu == 4):
            print("4번 [Java] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_java
            show_file = WWWPJ.TUTORIAL.tut_java.tutorial_Java_package()
            show_file.show_tutfile()

        elif (menu == 5):
            print("5번 [Python] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_python
            show_file = WWWPJ.TUTORIAL.tut_python.tutorial_Python_package()
            show_file.show_tutfile()

        elif (menu == 6):
            print("6번 [DS] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_ds
            show_file = WWWPJ.TUTORIAL.tut_ds.tutorial_Ds_package()
            show_file.show_tutfile()

        elif (menu == 7):
            print("6번 [C] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_c
            show_file = WWWPJ.TUTORIAL.tut_c.tutorial_C_package()
            show_file.show_tutfile()

        elif (menu == 8):
            print("6번 [Wsm] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_wsm
            show_file = WWWPJ.TUTORIAL.tut_wsm.tutorial_Wsm_package()
            show_file.show_tutfile()

        elif (menu == 9):
            print("6번 [Spring] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_spring
            show_file = WWWPJ.TUTORIAL.tut_spring.tutorial_Spring_package()
            show_file.show_tutfile()
            
        else:
            print("1-9번까지 선택하여 주십시오.")
