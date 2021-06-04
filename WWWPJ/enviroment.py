class Env_Package:
    def detailmenu(self):
        print("========ENVIROMENTMENU=========")
        print("[ 1. DB / 2. Php / 3.Jsp / 4. Java / 5. C / 6. Android ]")

        menu = input('메뉴를 선택하세요: ')  # 사용자가 메뉴 선택
        menu = int(menu)  # 인덱스를 위해 문자를 순자로

        if (menu == 1):
            print("1번 [DB] 로 이동합니다.")
            import WWWPJ.ENVIROMENT.env_db
            show_file = WWWPJ.ENVIROMENT.env_db.env_Db_package()
            show_file.show_envfile()

        elif (menu == 2):
            print("2번 [Php] 로 이동합니다.")
            import WWWPJ.ENVIROMENT.env_php
            show_file = WWWPJ.ENVIROMENT.env_php.env_Php_package()
            show_file.show_envfile()

        elif (menu == 3):
            print("3번 [Jsp] 로 이동합니다.")
            import WWWPJ.ENVIROMENT.env_jsp
            show_file = WWWPJ.ENVIROMENT.env_jsp.env_Jsp_package()
            show_file.show_envfile()

        elif (menu == 4):
            print("4번 [Java] 로 이동합니다.")
            import WWWPJ.ENVIROMENT.env_java
            show_file = WWWPJ.ENVIROMENT.env_java.env_Java_package()
            show_file.show_envfile()

        elif (menu == 5):
            print("5번 [C] 로 이동합니다.")
            import WWWPJ.ENVIROMENT.env_c
            show_file = WWWPJ.ENVIROMENT.env_c.env_C_package()
            show_file.show_envfile()

        elif (menu == 6):
            print("6번 [Android] 로 이동합니다.")
            import WWWPJ.ENVIROMENT.env_android
            show_file = WWWPJ.ENVIROMENT.env_android.env_Android_package()
            show_file.show_envfile()

        else:
            print("1-6번을 선택하여 주십시오.")
