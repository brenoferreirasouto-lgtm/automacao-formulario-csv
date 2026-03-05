import pandas as pd
import pyautogui
import time

# Configurações
FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSeKnRdULBMWGPiGwER67Ikz4inPG-kVF--Mkdy1XblYWXq-WQ/viewform'
CSV_PATH = 'dados.csv'
COORD_NOME_X, COORD_NOME_Y = 738, 349  # coordenadas do primeiro campo do formulário

# Carrega a base de dados
tabela = pd.read_csv(CSV_PATH)
pyautogui.PAUSE = 1  # intervalo entre cada ação do pyautogui

# Abre o navegador e acessa o formulário
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
time.sleep(2)

pyautogui.write(FORM_URL)
pyautogui.press('enter')
time.sleep(3)

# Inicia o preenchimento automático
pyautogui.click(x=COORD_NOME_X, y=COORD_NOME_Y)

for linha in tabela.index:
    nome = str(tabela.loc[linha, 'nome'])
    idade = str(tabela.loc[linha, 'idade'])
    email = str(tabela.loc[linha, 'email'])

    # Preenche os campos do formulário
    pyautogui.write(nome)
    pyautogui.press('tab')
    pyautogui.write(idade)
    pyautogui.press('tab')
    pyautogui.write(email)
    pyautogui.press('tab')

    # Envia o formulário
    pyautogui.press('enter')
    time.sleep(2)

    # Clica em "Enviar outra resposta"
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)

    # Retorna ao primeiro campo para o próximo cadastro
    pyautogui.click(x=COORD_NOME_X, y=COORD_NOME_Y)

    print(f'[{linha + 1}/{len(tabela)}] Cadastrado: {nome} | {idade} | {email}')

print('Fim do processo!')