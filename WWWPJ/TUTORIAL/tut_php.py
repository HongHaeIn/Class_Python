class tutorial_Php_package:
    def show_tutfile(self):
        print("========PHP_TUTORIAL=========")
        print("1. H생활코딩! PHP+MySQL\n"
            +"2. PHP 프로그래밍 입문(PHP Web Programming)")

        import WWWPJ.TUTORIAL.tut_base                  #TUTORIAL 폴더 속 tut_base 파일로 임폴트 하자
        show_menu = WWWPJ.TUTORIAL.tut_base.Base()      #tut_base 파일에 Base 클래스에 들어가자
        show_menu.tutBase()                             #Base 클래스에 tutBase 함수를 보여주자

