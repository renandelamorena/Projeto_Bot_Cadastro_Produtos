import pyautogui as pag
import pyperclip as pcl
import os
import time

import func_verifica_tela
# from verifica_tela import verificar_imagem_encontrada, click

def pause(seg=1):
    pag.PAUSE = seg

def salvar_excel(nome_arquivo, onde_fixado):

    pause(1)
    
    # click no excel
    func_verifica_tela.verificar_imagem_encontrada(time.time(), 1800 , 'img/excel/exel_gerado.png', 5, 'salvar_planilha - exel_gerado')
    func_verifica_tela.click('img/excel/exel_gerado.png', 1)  

    # tela cheia
    pag.hotkey('ctrl', 'shift', 'f1')
    pag.hotkey('ctrl', 'shift', 'f1')

    # vai em salvar como

    pag.press('alt')
    pag.press('a')
    pag.press('a')
    pag.press('y')
    pag.press('1')
    pag.press('y')
    pag.press(onde_fixado)

    # coloca o nome do arquivo
    func_verifica_tela.verificar_imagem_encontrada(time.time(), 20 , 'img/excel/nome_arquivo.png', 0.1, 'salvar_planilha - nome_arquivo')
    func_verifica_tela.click('img/excel/nome_arquivo.png', 2)
    pcl.copy(nome_arquivo)
    pag.hotkey('ctrl', 'v')

    # salvar
    func_verifica_tela.verificar_imagem_encontrada(time.time(), 20 , 'img/excel/salvar_excel.png', 0.1, 'salvar_planilha - salvar_excel')
    func_verifica_tela.click('img/excel/salvar_excel.png', 1)

    # confirmar subistituição
    pag.press('tab')
    pag.press('enter')

    # fechar
    pag.hotkey('alt', 'f4')
    
    pause()

def salvar_planilha(local_com_arquivo):

    pause(0.5)

    # Click em icone da planilha
    func_verifica_tela.verificar_imagem_encontrada(time.time(), 1800 , 'img/excel/planilha_gerada.png', 5, 'salvar_planilha - planilha_gerada')
    func_verifica_tela.click('img/excel/planilha_gerada.png', 1)

    time.sleep(3)

    pag.hotkey('ctrl', 's')

    pcl.copy(local_com_arquivo)
    pag.hotkey('ctrl', 'v')

    func_verifica_tela.verificar_imagem_encontrada(time.time(), 1800 , 'img/excel/guardar.png', 5, 'salvar_planilha - guardar')
    func_verifica_tela.click('img/excel/guardar.png', 1)

    pag.press('enter')

    # fechar
    pag.hotkey('alt', 'f4')

    pause()

def salvar_dados():

    pause(0.2)
    # minimisa
    with pag.hold('win'):
        pag.press('m')

    pag.press('win')
    pcl.copy('chrome')
    pag.hotkey('ctrl', 'v')

    pause(1)

    pag.press('enter')

    func_verifica_tela.verificar_imagem_encontrada(time.time(), 10, 'img/projeto_curva/controle_estoque.png', 0.2, 'controle_estoque - perfil do chrome')
    func_verifica_tela.click('img/projeto_curva/controle_estoque.png', 1)

    pag.hotkey('ctrl', 't')

    pcl.copy('https://projeto-curva-abc.streamlit.app/Dados_brutos')
    pag.hotkey('ctrl', 'v')

    pag.press('enter')

    time.sleep(5)

    func_verifica_tela.verificar_imagem_encontrada(time.time(), 50, 'img/projeto_curva/campo_token.png', 0.2, 'campo_token - Token de acesso')
    time.sleep(1)
    func_verifica_tela.click('img/projeto_curva/campo_token.png', 1)

    func_verifica_tela.verificar_imagem_encontrada(time.time(), 10, 'img/projeto_curva/preenchimento_auto.png', 0.2, 'preenchimento_auto')
    time.sleep(1)
    func_verifica_tela.click('img/projeto_curva/preenchimento_auto.png', 1)

    func_verifica_tela.verificar_imagem_encontrada(time.time(), 10, 'img/projeto_curva/campo_upload.png', 0.2, 'campo_upload')
    func_verifica_tela.click('img/projeto_curva/campo_upload.png', 1)

    time.sleep(3)

    nome_arquivo =  '"curva_cx" "curva_frac" "curva_geral" "produtos"'
    pcl.copy(nome_arquivo)
    pag.hotkey('ctrl', 'v')

    func_verifica_tela.verificar_imagem_encontrada(time.time(), 10, 'img/projeto_curva/local_pasta.png', 0.2, 'local_pasta')
    func_verifica_tela.click('img/projeto_curva/local_pasta.png', 1)

    time.sleep(3)

    caminho_local = r'C:\Users\samuel.lucas\OneDrive - MAXIFARMA DISTRIBUIDORA DE MEDICAMENTOS LTDA\Documentos\estoque.renan\projetos\Projeto_Curva_ABC\data\tratamento_curva_abc\datasets'
    pcl.copy(caminho_local)
    pag.hotkey('ctrl', 'v')

    pag.press('tab')

    func_verifica_tela.verificar_imagem_encontrada(time.time(), 10, 'img/projeto_curva/abrir.png', 0.2, 'abrir')
    func_verifica_tela.click('img/projeto_curva/abrir.png', 1)

    pag.press('down', presses=10, interval=0.1)

    func_verifica_tela.verificar_imagem_encontrada(time.time(), 180, 'img/projeto_curva/enviar_dados.png', 3, 'enviar_dados')
    func_verifica_tela.click('img/projeto_curva/enviar_dados.png', 1)

# salvar_planilha(r'C:\Users\samuel.lucas\OneDrive - MAXIFARMA DISTRIBUIDORA DE MEDICAMENTOS LTDA\Documentos\estoque.renan\projetos\Projeto_Curva_ABC\data\tratamento_curva_abc\datasets\teste')
# salvar_dados()