# Importar as bibliotecas
from math import ceil
from statistics import mean
from math import sqrt as raiz
from statistics import variance as var


def estatistica_glicose(valor_peso, valores_glicemia):
    """Função responsável por retornar os dados estatísticos da glicemia."""
    # Estatística quando "valores_glicemia" tiver somente um dado
    if len(valores_glicemia) == 1:
        media = valores_glicemia[0]
        desvio_padrao = 0
        variabilidade = 0

        peso = valor_peso[0]
        media_convertida = media / 100
        litros_sangue = 0.075 * peso
        massa_glicose = media_convertida * litros_sangue

    # Estatística quando "valores_glicemia" tiver mais de um dado
    else:
        media = mean(valores_glicemia)
        variancia = var(valores_glicemia)
        desvio_padrao = raiz(variancia)
        variabilidade = (desvio_padrao / media) * 100

        peso = valor_peso[0]
        media_convertida = media / 100
        litros_sangue = 0.075 * peso
        massa_glicose = media_convertida * litros_sangue

    return ceil(media), ceil(desvio_padrao), ceil(variabilidade), ceil(massa_glicose), ceil(peso)


def estatistica_pressao(valores_sistolica, valores_diastolica):
    """Função responsável por retornar os dados estatísticos da pressão arterial."""
    # Estatística quando "valores_pressao" tiver somente um dado
    if len(valores_sistolica) == 1:
        media_sistolica = valores_sistolica[0]
        desvio_padrao_sistolica = 0
        variabilidade_sistolica = 0

        media_diastolica = valores_diastolica[0]
        desvio_padrao_diastolica = 0
        variabilidade_diastolica = 0

    # Estatística quando "valores_pressao" tiver mais de um dado
    else:
        media_sistolica = mean(valores_sistolica)
        variancia_sistolica = var(valores_sistolica)
        desvio_padrao_sistolica = raiz(variancia_sistolica)
        variabilidade_sistolica = (desvio_padrao_sistolica / media_sistolica) * 100

        media_diastolica = mean(valores_diastolica)
        variancia_diastolica = var(valores_diastolica)
        desvio_padrao_diastolica = raiz(variancia_diastolica)
        variabilidade_diastolica = (desvio_padrao_diastolica / media_diastolica) * 100

    return (f'{media_sistolica:.1f}', f'{desvio_padrao_sistolica:.1f}', ceil(variabilidade_sistolica),
            f'{media_diastolica:.1f}', f'{desvio_padrao_diastolica:.1f}', ceil(variabilidade_diastolica))


def estatistica_bpm(valores_bpm):
    """Função responsável por retornar os dados estatísticos do BPM."""
    # Estatística quando "valores_bpm" tiver somente um dado
    if len(valores_bpm) == 1:
        media = valores_bpm[0]
        desvio_padrao = 0
        variabilidade = 0

    # Estatística quando "valores_pressao" tiver mais de um dado
    else:
        media = mean(valores_bpm)
        variancia = var(valores_bpm)
        desvio_padrao = raiz(variancia)
        variabilidade = (desvio_padrao / media) * 100

    return ceil(media), ceil(desvio_padrao), ceil(variabilidade)
