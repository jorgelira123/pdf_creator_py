from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.image('template.png', x=0, y=0)

projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo_estimado = input("Digite o prazo estimado: ")
valor_total_estimado = int(horas_estimadas) * int(valor_hora)

formatted_valor_total_estimado = "R$ {:,.2f}".format(valor_total_estimado)

pdf.text(115, 198, projeto)
pdf.text(115, 212, horas_estimadas + " horas")
pdf.text(115, 226, "R$ " + valor_hora)
pdf.text(115, 240, prazo_estimado)
pdf.text(115, 254, formatted_valor_total_estimado)

pdf.output('orçamento.pdf')
print("Orçamento gerado com sucesso!")
