class Tutorial_Package:
    def detailmenu(self):
        print("[1. DB / 2. Php / 3. Jsp / 4. Java / 5. Python / 6. DS / 7. C / 8. Wsm / 9. Spring ]")

        menu = input('메뉴를 선택하세요: ')                                         #사용자가 메뉴 선택하게 하자
        menu = int(menu)                                                        #인덱스를 위해 문자를 순자로 바꿔주자

        if (menu == 1):
            print("1번 [DB] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_db                                        #TUTORIAL 폴더 속 tut_db 파일로 임폴트 하자
            show_file = WWWPJ.TUTORIAL.tut_db.tutorial_Db_package()             #tut_db 파일에 tutorial_Db_package 클래스에 들어가자
            show_file.show_tutfile()                                            #tutorial_Db_package 클래스에 show_tutfile 함수를 보여주자

        elif (menu == 2):
            print("2번 [Php] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_php                                       #TUTORIAL 폴더 속 tut_php 파일로 임폴트 하자
            show_file = WWWPJ.TUTORIAL.tut_php.tutorial_Php_package()           #tut_php 파일에 tutorial_Php_package 클래스에 들어가자
            show_file.show_tutfile()                                            #tutorial_Php_package 클래스에 show_tutfile 함수를 보여주자

        elif (menu == 3):
            print("3번 [Jsp] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_jsp                                       #TUTORIAL 폴더 속 tut_jsp 파일로 임폴트 하자
            show_file = WWWPJ.TUTORIAL.tut_jsp.tutorial_Jsp_package()           #tut_jsp 파일에 tutorial_Jsp_package 클래스에 들어가자
            show_file.show_tutfile()                                            #tutorial_Jsp_package 클래스에 show_tutfile 함수를 보여주자

        elif (menu == 4):
            print("4번 [Java] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_java                                      #TUTORIAL 폴더 속 tut_java 파일로 임폴트 하자
            show_file = WWWPJ.TUTORIAL.tut_java.tutorial_Java_package()         #tut_java 파일에 tutorial_Java_package 클래스에 들어가자
            show_file.show_tutfile()                                            #tutorial_Java_package 클래스에 show_tutfile 함수를 보여주자

        elif (menu == 5):
            print("5번 [Python] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_python                                    #TUTORIAL 폴더 속 tut_python 파일로 임폴트 하자
            show_file = WWWPJ.TUTORIAL.tut_python.tutorial_Python_package()     #tut_python 파일에 tutorial_Python_package 클래스에 들어가자
            show_file.show_tutfile()                                            #tutorial_Python_package 클래스에 show_tutfile 함수를 보여주자

        elif (menu == 6):
            print("6번 [DS] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_ds                                        #TUTORIAL 폴더 속 tut_ds 파일로 임폴트 하자
            show_file = WWWPJ.TUTORIAL.tut_ds.tutorial_Ds_package()             #tut_ds 파일에 tutorial_Ds_package 클래스에 들어가자
            show_file.show_tutfile()                                            #tutorial_Ds_package 클래스에 show_tutfile 함수를 보여주자

        elif (menu == 7):
            print("6번 [C] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_c                                         #TUTORIAL 폴더 속 tut_c 파일로 임폴트 하자
            show_file = WWWPJ.TUTORIAL.tut_c.tutorial_C_package()               #tut_c 파일에 tutorial_C_package 클래스에 들어가자
            show_file.show_tutfile()                                            #tutorial_C_package 클래스에 show_tutfile 함수를 보여주자

        elif (menu == 8):
            print("6번 [Wsm] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_wsm                                       #TUTORIAL 폴더 속 tut_wsm 파일로 임폴트 하자
            show_file = WWWPJ.TUTORIAL.tut_wsm.tutorial_Wsm_package()           #tut_wsm 파일에 tutorial_Wsm_package 클래스에 들어가자
            show_file.show_tutfile()                                            #tutorial_Wsm_package 클래스에 show_tutfile 함수를 보여주자

        elif (menu == 9):
            print("6번 [Spring] 로 이동합니다.")
            import WWWPJ.TUTORIAL.tut_spring                                    #TUTORIAL 폴더 속 tut_spring 파일로 임폴트 하자
            show_file = WWWPJ.TUTORIAL.tut_spring.tutorial_Spring_package()     #tut_spring 파일에 tutorial_Spring_package 클래스에 들어가자
            show_file.show_tutfile()                                            #tutorial_Spring_package 클래스에 show_tutfile 함수를 보여주자
            
        else:
            print("1-9번까지 선택하여 주십시오.")                                    #1번부터 9번까지 고르지 않았을 경우엔 에러메세지를 보내주자
