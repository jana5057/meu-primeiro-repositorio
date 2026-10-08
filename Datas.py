from datetime import datetime, date

nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

hoje = date.today()
nascimento = nascimento.date()

dias_vividos = (hoje - nascimento).days
idade = dias_vividos // 365

print(f"Você tem aproximadamente {idade} anos.")
print(f"Você nasceu em uma {nascimento.strftime('%A')}.")

natal = date(hoje.year, 12, 25)

if hoje > natal:
    natal = date(hoje.year + 1, 12, 25)

dias_para_natal = (natal - hoje).days

print(f"Faltam {dias_para_natal} dias para o Natal.")

                              






    