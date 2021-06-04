class env_C_package:
    def show_envfile(self):
        print("========CMENV=========")
        print("1. 비주얼 스튜디오 내려받아 설치한다.")
        print("2. 인터넷 브라우저에", "http://visualstudio.microsoft.com/ko/downloads/",
              "주소를 입력하고 커뮤니티 항목에 있는 [무료다운로드]를 클릭한다. 단축주소는 ", "bit.ly/VSdown", "이다.")
        print("3. 화면 아래에서 메시지 박스가 올라오면 [실행] 버튼을 클릭한다.")
        print("4. [계속] 버튼을 클릭해서 설치를 진행 한다.")
        print("5. 바로 다운로드 받아서 설치하는 터라 네트워크 속도에 따라 설치 시간이 걸릴 수 있다. \
                [설치 후 시작]박스는 체크한 상태로 진행한다")
        print("6. 설치가 모두 끝나면 온라인으로 지원되는 개발자 서비스를 위해 마이크로소프트 계정으로 로그인하는 창이 열린다. \
                [나중에 로그인] 링크를 누르면 새로운 창이 열린다. \
                이 창에서 [개발 설정]을 Viusal C++ 선택하고 원하는 색 테마 선택을 한 다음에 \
                [Visual Studio 시작] 버튼을 누른다.")

        import WWWPJ.ENVIROMENT.env_base
        show_menu = WWWPJ.ENVIROMENT.env_base.Base()
        show_menu.envBase()