class env_Php_package:
    def show_envfile(self):
        print("========PHP_ENVIROMENT=========")
        print("1. PHP개발환경 구축하기(Git설치-> XAMPP설치(or APMsetup, AutoSet))\n"
              +"1-1. 개발에디터설치 하기(Editplus, Visual Studio, Eclipse, Vim)\n"
              +"1-2. iPuTTY다운로드 하기(자신의 포트번호와 비밀번호 설정)\n"
              +"1-3. AWS Educate 신청&사용하기")
        print("2. iPuTTY환경설정하기(웹서버 설정)\n"
                +"serverAdmin #자신의 이메일 주소\n"
                +"DocumentRoot /home/계정/ www\n"
                +"<Directory /home/계정 /www>\n"
                    +"Options FllowSymLinks MultiViews\n"
                    +"AllowOverride All\n"
                    +"allow from all\n"
                    +"require all granted\n"
                    +"<LimitExcpt GET POST>\n"
                            +"Order allow, deny\n"
                            +"Deny from all\n"
                +"</LimitExcept>\n"
                +"</Directory>")
        print("3. ⇒iPuTTY에서 HelloWorld출력(PHP시작)\n"
              +"<?php\n"
              +"echo Hello World!;\n"
              +"phpinfo();\n"
              +"?>")

        import WWWPJ.ENVIROMENT.env_base                #LECTURE 폴더 속 lec_base 파일로 임폴트 하자
        show_menu = WWWPJ.ENVIROMENT.env_base.Base()    #lec_base 파일에 Base 클래스에 들어가자
        show_menu.envBase()                             #Base 클래스에 lecBase 함수를 보여주자