from fpdf import FPDF


arquivo = []
pos = []
vazio = '*'

nome = input('Digite o nome:  ')
RG = input('Digite o RG: ')
CPF = input('Digite o CPF:  ')

texto_info = [nome, RG, CPF]


 





pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size =15)


pdf.cell(200, 10, txt = 'Hello World', ln = 3, align='C')
    

pdf.output(f"preenchido.pdf")
