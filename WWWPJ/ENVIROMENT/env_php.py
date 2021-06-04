class env_Php_package:
    def show_envfile(self):
        print("========PHPMENV=========")
        print("1. PHP개발환경 구축"
              "⇒Git설치"
              "⇒XAMPP설치(or APMsetup, AutoSet)"
              "⇒개발에디터설치(Editplus, Visual Studio, Eclipse, Vim) ※ Vim추천"
              "⇒iPuTTY다운로드(자신의 포트번호와 비밀번호 설정)"
              "⇒AWS Educate 신청&사용")
        print("2. iPuTTY환경설정"
                "⇒웹서버 설정"
                "serverAdmin #자신의 이메일 주소"
                "DocumentRoot /home/계정/ www"
                "<Directory /home/계정 /www>"
                    "Options FllowSymLinks MultiViews"
                    "AllowOverride All"
                    "allow from all"
                    "require all granted"
                    "<LimitExcpt GET POST>"
                            "Order allow, deny"
                            "Deny from all"
                "</LimitExcept>"
                "</Directory>")
        print("3. ⇒iPuTTY에서 HelloWorld출력(PHP시작)"
              "<?php"
              "echo Hello World!;" \
              "phpinfo();"
              "?>")

        import WWWPJ.ENVIROMENT.env_base
        show_menu = WWWPJ.ENVIROMENT.env_base.Base()
        show_menu.envBase()