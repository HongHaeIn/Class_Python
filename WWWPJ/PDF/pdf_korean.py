class pdf_Korean_package:
    def show_pdffile(self):
        print("========KOREANPDF=========")
        print("국어PDF:", "http://www.hnedu.co.kr/textbook/textbook/ebook/high_korean/index.html")

        import WWWPJ.PDF.pdf_base
        show_file = WWWPJ.PDF.pdf_base.Base()
        show_file.pdfBase()
