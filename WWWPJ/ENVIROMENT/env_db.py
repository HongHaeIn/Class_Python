class env_Db_package:
    def show_envfile(self):
        print("========DBMENV=========")
        print("SQL Developer 환경설정")
        print("1. 인코딩 UTF-8로 변경한다. (환경설정-->환경-->인코딩)")
        print("2. 주석 (환경설정-->코드편집기-->PL/SQL구문색상-->기본주석-->글꼴,색상,배경색)")
        print("3. 행번호 (환경설정-->코드편집기-->PL/SQL구문색상-->행 여백-->행 번호 표시)")
        print("4. 나머지는 환경설정에 들어가면 어느정도 찾을 수 있다.")
        print("계정 새로 만들기")
        print("1. 왼속상단에 초록색 + 버튼을 눌러준다.")
        print("2. 사용자이름, 비밀번호를 적어준다.(※비밀번호를 잊어버리지 않도록 주의※)")
        print("3. 접속유형이 호스트이름 : localhost, 포트 : 1521, sid기본값 xe로 되어있는지 확인한다")
        print("4. 테스트 성공이라고 뜨면 저장한다. (저장하면 왼쪽에 접속이름과 접속 세부정보다 뜸)")

        import WWWPJ.ENVIROMENT.env_base
        show_menu = WWWPJ.ENVIROMENT.env_base.Base()
        show_menu.envBase()