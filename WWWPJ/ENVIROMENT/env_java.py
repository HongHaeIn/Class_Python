class env_Java_package:
    def show_envfile(self):
        print("========JAVAMENV=========")
        print("JDK 설치")
        print("1. Oracle 사이트", "https://www.oracle.com/index.html", "에 들어가 회원가입 한다")
        print("2. JAVA SE(Standard Edition) Oracle JDK 1.8을 사용하고 있는 컴퓨터 운영체제에 맞는 파일로 다운받는다.")
        print("3. 파일을 받은 후, 변다른 조작 없이 설치과정을 진행한다.(초기에 지정된 위치에 설치되는 것이 안전함)")
        print("4. CMD를 열어, java -version 을 입력해 설치가 잘 이루어 졌는지 확인해 본다.(다운로드 받은 jdk 버전이 나오면 성공)")
        print("Java 환경변수 설정")
        print("1. 제어판 > 시스템 > 시스템 환경 변수 편집 환경변수(Window10 의 경우 하단검색기능을 사용하면 편리)")
        print("2. 시스템 변수(상단과 하단 중 하단부)"
              "-> 새로 만들기"
              "변수명 : JAVA_HOME / 변수값 : C:\Program Files\Java\jdk1.8.0_271 (변수값은 자바 JDK 설치 경로 의미)")
        print("3. 시스템 변수(상단과 하단 중 하단부)"
              "-> Path 변수를 찾아 더블클릭(혹은 클릭 후 편집 버튼 클릭)"
              "-> 새로만들기 %JAVA_HOME%Wbin ")
        print("4. 시스템 변수(상단과 하단 중 하단부) -> 새로 만들기"
              "변수명 : CLASSPATH"
              "변수값 : %JAVA_HOME% lib (변수값은 자바 JDK 설치경로 의미)")
        print("5. 위의 과정 후, CMD 창을 열어 javac -version 을 입력한다.(JDK와 동일한 버전이 나오면 성공)")

        import WWWPJ.ENVIROMENT.env_base
        show_menu = WWWPJ.ENVIROMENT.env_base.Base()
        show_menu.envBase()