import re

def extrair_numero_antes_primeira_unidade(texto):
    # procura por um número (com vírgula ou ponto) seguido de letras (tipo mg, ml, etc)
    match = re.search(r'(\d+(?:[.,]\d+)?)(?=\D)', texto)
    if not match:
        return None
    valor = match.group(1).replace(',', '.')
    try:
        return float(valor)
    except ValueError:
        return None

def parse_dosagem(dosagem_str):
    """
    Extrai valor numérico da dosagem e converte para mg como unidade base.
    Exemplo de entrada: "100 mg", "1 g", "0,5 mg"
    Retorna valor em mg (float).
    """
    # Substitui vírgula por ponto para float funcionar
    dosagem_str = dosagem_str.replace(',', '.').lower()

    # Regex para capturar número e unidade
    match = re.match(r'([\d\.]+)\s*(mg|g|mcg)?', dosagem_str)
    if not match:
        return None  # não conseguiu parsear

    valor = float(match.group(1))
    unidade = match.group(2) or 'mg'  # padrão mg se nada especificado

    # Converte para mg
    if unidade == 'g':
        valor_mg = valor * 1000
    elif unidade == 'mcg':
        valor_mg = valor / 1000
    else:  # mg
        valor_mg = valor

    return valor_mg