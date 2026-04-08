from datetime import datetime
import re


def agora_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def normalizar_preco(valor):
    if valor is None:
        return None

    if isinstance(valor, (int, float)):
        return float(valor)

    texto = str(valor).strip()
    if not texto:
        return None

    texto = texto.replace("R$", "").replace("\xa0", " ")
    texto = re.sub(r"[^\d,\.]", "", texto)

    if "," in texto:
        texto = texto.replace(".", "").replace(",", ".")

    try:
        return float(texto)
    except ValueError:
        return None


def limpar_texto(texto):
    if texto is None:
        return ""
    return re.sub(r"\s+", " ", str(texto)).strip()