class pdf_English_package:
    def show_pdffile(self):
        print("========ENGLISH_PDF=========")
        print('\033[94m'+"[ 영어 PDF ]:", "https://drive.google.com/drive/folders/1EMt1U4S3-3ydWsu23QSqkMhZ3JWS1K7u?usp=sharing"+'\033[0m')

        import WWWPJ.PDF.pdf_base               #PDF 폴더 속 pdf_base 파일로 임폴트 하자
        show_file = WWWPJ.PDF.pdf_base.Base()   #pdf_base 파일에 Base 클래스에 들어가자
        show_file.pdfBase()                     #Base 클래스에 pdfBase 함수를 보여주자