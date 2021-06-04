class env_Jsp_package:
    def show_envfile(self):
        print("========JSPMENV=========")
        print("JDK(Java SE Development Kit) 설치"
              "- 자바 기반의 프로그램을 작성하기 위해 필수적인 컴파일러 및 실행환경"
              "- Jsp를 사용하기 위해 필수적으로 설치되어야 함")
        print("1. JDK를 설치하기 위해선", "https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html",
              "링크에 접속하여 자신이 사용하는 운영체제에 맞는 버전을 다운 받는다.")
        print("2. 다운 받은 파일을 실행하여 설치를 진행한다.(별다른 설정을 하지 않고 Next 만 눌러도 설치 완료)")
        print("3. 내 컴퓨터 - 속성 - 시스템에서 고급시스템 설정 - 시스템 속성의 고급 - 환경변수"
              "JDK를 사용하기 위한 환경 변수를 설정을 해주어야 한다.")
        print("4. 변수 Path 에서 편집을 눌러 변수 값 C:/Program Files/Java/jsk1.8.0_101/bin 내용을 추가해줍니다. (자바 버전에 따라 설치된 경로명은 바뀔 수 있습니다.)")
        print("5. 확인을 눌러 저장을 하고 정상적으로 설치가 되었는지 확인해보려면 명령 프롬프트를 실행해서",
                 "java와 javas 를 입력해봅니다.")
        print("7. cmd 창에 이런식으로 뜬다면 정상적으로 설치된것입니다 ( 정식앱 사진 첨부)")

        import WWWPJ.ENVIROMENT.env_base
        show_menu = WWWPJ.ENVIROMENT.env_base.Base()
        show_menu.envBase()