class Lecture_Package:
    def detailmenu(self):
        print("[ 1. DB / 2. Jsp / 3. Java / 4. Python / 5. C / 6. Wsm / 7. Spring ]")

        menu = input('메뉴를 선택하세요: ')  # 사용자가 메뉴 선택
        menu = int(menu)  # 인덱스를 위해 문자를 순자로

        if (menu == 1):
            print("1번 [DB 강의] 로 이동합니다.")
            import WWWPJ.LECTURE.lec_db
            show_file = WWWPJ.LECTURE.lec_db.lecture_db_package()
            show_file.show_lecfile()

        elif (menu == 2):
            print("2번 [JSP 강의] 로 이동합니다.")
            import WWWPJ.LECTURE.lec_jsp
            show_file = WWWPJ.LECTURE.lec_jsp.lecture_jsp_package()
            show_file.show_lecfile()

        elif (menu == 3):
            print("3번 [JAVA 강의] 로 이동합니다.")
            import WWWPJ.LECTURE.lec_java
            show_file = WWWPJ.LECTURE.lec_java.lecture_java_package()
            show_file.show_lecfile()

        elif (menu == 4):
            print("4번 [Python 강의] 로 이동합니다.")
            import WWWPJ.LECTURE.lec_python
            show_file = WWWPJ.LECTURE.lec_python.lecture_python_package()
            show_file.show_lecfile()

        elif (menu == 5):
            print("5번 [C 강의] 로 이동합니다.")
            import WWWPJ.LECTURE.lec_c
            show_file = WWWPJ.LECTURE.lec_c.lecture_c_package()
            show_file.show_lecfile()

        elif (menu == 6):
            print("6번 [WSM 강의] 로 이동합니다.")
            import WWWPJ.LECTURE.lec_wsm
            show_file = WWWPJ.LECTURE.lec_wsm.lecture_wsm_package()
            show_file.show_lecfile()

        elif (menu == 7):
            print("7번 [Spring 강의] 로 이동합니다.")
            import WWWPJ.LECTURE.lec_spring
            show_file = WWWPJ.LECTURE.lec_spring.lecture_spring_package()
            show_file.show_lecfile()

        else:
            print("1-7번을 선택하여 주십시오.")
