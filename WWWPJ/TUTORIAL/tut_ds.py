class tutorial_Ds_package:
    def show_tutfile(self):
        print("1. 인프런 - C로 배우는 자료구조 및 여러가지 예제 실습\n"
            +"2. 프로그래머스(유료) - 어서와! 자료구조와 알고리즘은 처음이지?")

        import WWWPJ.TUTORIAL.tut_base
        show_menu = WWWPJ.TUTORIAL.tut_base.Base()
        show_menu.tutBase()