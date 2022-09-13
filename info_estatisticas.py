# Importar as bibliotecas
from math import ceil


def info_estatisticas(inicio, final, dados):
    """Função responsável por colocar os dados estatísticos do período selecionado."""
    # Declarar os dados
    bpm = dados[0]
    pressao = dados[1]
    glicemia = dados[2]

    # Dados estatísticos da glicemia
    max_glicemia = max(glicemia['media'])
    min_glicemia = min(glicemia['media'])
    max_massa = max(glicemia['massa_glicose'])
    min_massa = min(glicemia['massa_glicose'])
    max_desvio_padrao_glicemia = max(glicemia['desvio_padrao'])
    min_desvio_padrao_glicemia = min(glicemia['desvio_padrao'])
    max_variabilidade_glicemia = max(glicemia['variabilidade'])
    min_variabilidade_glicemia = min(glicemia['variabilidade'])
    tamanho_dados_media = len(glicemia['media'])
    entre_70_180 = [i for i in glicemia['media'] if 70 <= i <= 180]
    porcentagem_media_glicemia = ceil((len(entre_70_180) / tamanho_dados_media) * 100)
    tamanho_dados_desvio_padrao = len(glicemia['desvio_padrao'])
    abaixo_50 = [i for i in glicemia['desvio_padrao'] if i <= 50]
    porcentagem_desvio_padrao_glicemia = ceil((len(abaixo_50) / tamanho_dados_desvio_padrao) * 100)
    tamanho_dados_variabilidade = len(glicemia['variabilidade'])
    abaixo_36 = [i for i in glicemia['variabilidade'] if i <= 36]
    porcentagem_variabilidade_glicemia = ceil((len(abaixo_36) / tamanho_dados_variabilidade) * 100)

    # Dados estatísticos da pressão
    max_sistolica = max(pressao['media_sistolica'])
    min_sistolica = min(pressao['media_sistolica'])
    max_diastolica = max(pressao['media_diastolica'])
    min_diastolica = min(pressao['media_diastolica'])
    max_dp_sistolica = max(pressao['desvio_padrao_sistolica'])
    min_dp_sistolica = min(pressao['desvio_padrao_sistolica'])
    max_dp_diastolica = max(pressao['desvio_padrao_diastolica'])
    min_dp_diastolica = min(pressao['desvio_padrao_diastolica'])
    max_var_sistolica = max(pressao['variabilidade_sistolica'])
    min_var_sistolica = min(pressao['variabilidade_sistolica'])
    max_var_diastolica = max(pressao['variabilidade_diastolica'])
    min_var_diastolica = min(pressao['variabilidade_diastolica'])

    # Dados estatísticos do BPM
    max_bpm = max(bpm['media'])
    min_bpm = min(bpm['media'])
    max_dp_bpm = max(bpm['desvio_padrao'])
    min_dp_bpm = min(bpm['desvio_padrao'])
    max_var_bpm = max(bpm['variabilidade'])
    min_var_bpm = min(bpm['variabilidade'])

    # Escrever os dados estatísticos
    texto = [f'Intervalo: {inicio} - {final}\n',
             'Glicemia:\n',
             '\tMédia:\n',
             f'\t\t{porcentagem_media_glicemia}% dos dados estão entre 70 mg/dL e 180 mg/dL.',
             f'\t\tMáximo: {max_glicemia} mg/dL.',
             f'\t\tMínimo: {min_glicemia} mg/dL.\n',
             '\tDesvio padrão:\n',
             f'\t\t{porcentagem_desvio_padrao_glicemia}% dos dados estão abaixo de 50 mg/dL.',
             f'\t\tMáximo: {max_desvio_padrao_glicemia} mg/dL.',
             f'\t\tMínimo: {min_desvio_padrao_glicemia} mg/dL.\n',
             '\tVariabilidade:\n',
             f'\t\t{porcentagem_variabilidade_glicemia}% dos dados estão abaixo de 36%.',
             f'\t\tMáxima: {max_variabilidade_glicemia}%',
             f'\t\tMínima: {min_variabilidade_glicemia}%\n',
             '\tMassa de glicose:\n',
             f'\t\tMáxima: {max_massa} gramas.',
             f'\t\tMínima: {min_massa} gramas.\n\n',
             'Pressão arterial:\n',
             '\tMédia:\n',
             '\t\tSistólica:\n'
             f'\t\t\tMáxima: {max_sistolica} mmHg.',
             f'\t\t\tMínima: {min_sistolica} mmHg.\n',
             '\t\tDiastólica:\n',
             f'\t\t\tMáxima: {max_diastolica} mmHg.',
             f'\t\t\tMínima: {min_diastolica} mmHg.\n',
             '\tDesvio padrão:\n',
             '\t\tSistólica:\n',
             f'\t\t\tMáximo: {max_dp_sistolica} mmHg.',
             f'\t\t\tMínimo: {min_dp_sistolica} mmHg.\n',
             '\t\tDiastólica:\n'
             f'\t\t\tMáximo: {max_dp_diastolica} mmHg.',
             f'\t\t\tMínimo: {min_dp_diastolica} mmHg.\n',
             '\tVariabilidade:\n',
             '\t\tSistólica:\n'
             f'\t\t\tMáxima: {max_var_sistolica}%',
             f'\t\t\tMínima: {min_var_sistolica}%\n',
             '\t\tDiastólica:\n',
             f'\t\t\tMáxima: {max_var_diastolica}%',
             f'\t\t\tMínima: {min_var_diastolica}%\n\n',
             'BPM:\n',
             '\tMédia:\n',
             f'\t\tMáxima: {max_bpm} BPM.',
             f'\t\tMínima: {min_bpm} BPM.\n',
             '\tDesvio padrão:\n',
             f'\t\tMáximo: {max_dp_bpm} BPM.',
             f'\t\tMínimo: {min_dp_bpm} BPM.\n',
             '\tVariabilidade:\n',
             f'\t\tMáxima: {max_var_bpm}%',
             f'\t\tMínima: {min_var_bpm}%']

    return texto
