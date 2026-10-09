def e_bissexto(ano):
    """O ano é Bissexto?"""
    return (ano % 4 ==0 and ano % 100 !=0) or (ano % 400 ==0)
def calcular_imc(peso, altura):
    ###Qual o imc tendo como base o meu peso?###
    return peso / (altura ** 2)
