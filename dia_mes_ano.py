# Importar as bibliotecas
from datetime import date


def dia_mes_ano():
    """Função responsável por retornar os valores dos dias, meses e anos para os ComboBox."""
    # Criar uma lista com todos os dias do mês
    dias_1_digito = list(range(1, 10))
    dias_2_digitos = list(range(10, 32))
    dias_str = [f'0{i}' for i in dias_1_digito]
    for j in dias_2_digitos:
        dias_str.append(str(j))

    # Criar uma lista com todos os meses do ano
    meses_1_digito = list(range(1, 10))
    meses_2_digitos = list(range(10, 13))
    meses_str = [f'0{i}' for i in meses_1_digito]
    for j in meses_2_digitos:
        meses_str.append(str(j))

    # Criar uma lista com os anos atualizando de modo automático
    ano_atual = date.today().year
    anos = list(range(2020, ano_atual+1))
    anos_str = [str(i) for i in anos]

    return dias_str, meses_str, anos_str
