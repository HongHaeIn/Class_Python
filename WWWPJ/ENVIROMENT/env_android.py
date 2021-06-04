class env_Android_package:
    def show_envfile(self):
        print("========ANDROIDMENV=========")
        print("1. Window+R키(실행 단축키)를 누르고 ", "sysdm.cpl", "을 입력한다.")
        print("2. 시스템 속성창--> 고급--> 환경변수 --> Path --> 편집 --> 새로만든다.")
        print("C:\Program Files\Android\Android Studio\jre\bin --> 복사해서 넣는다.")

        import WWWPJ.ENVIROMENT.env_base
        show_menu = WWWPJ.ENVIROMENT.env_base.Base()
        show_menu.envBase()
