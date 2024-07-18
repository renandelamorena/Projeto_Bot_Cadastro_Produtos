import time
import pyautogui as pag
import pyperclip as pcl

from func_verifica_tela import verificar_imagem_encontrada, click
from func_geral import pause

def abre_wms():
    
    pause(0.1)
    # minimisa
    with pag.hold('win'):
        pag.press('m')

    pag.press('win')
    pcl.copy('wms')
    pag.hotkey('ctrl', 'v')

    verificar_imagem_encontrada(time.time(), 10, 'img/aplicativos.png', 0.1, 'abre_wms - aplicativos')
    click('img/aplicativos.png', 1)
    
    # Seleciona WMS
    
    verificar_imagem_encontrada(time.time(), 10, 'img/wms.png', 0.1, 'abre_wms - wms')
    click('img/wms.png', 1)

    # Executa WMS
    
    time.sleep(1)
    verificar_imagem_encontrada(time.time(), 10, 'img/executar.png', 0.1, 'abre_wms - executar')
    click('img/executar.png', 1)

    # Loguin

    verificar_imagem_encontrada(time.time(), 10, 'img/usuario.png', 0.1, 'abre_wms - usuario')
    click('img/usuario.png', 1)

    login = 'renan'
    senha = 134679
    
    pause(0.1)
    pcl.copy(login)
    pag.hotkey('ctrl', 'v')
    pag.press('tab')
    pcl.copy(senha)
    pag.hotkey('ctrl', 'v')

    pag.press('tab')
    pag.press('enter')

def abre_app_wms(app):

    pause(0.1)
    
    verificar_imagem_encontrada(time.time(), 10, 'img/lupa_wms.png', 0.1, 'abre_app_wms - lupa_wms')
    click('img/lupa_wms.png', 1)

    pcl.copy(app)
    
    pag.hotkey('ctrl', 'v')

    pag.press('tab')
    pag.press('enter')
    

def abre_consulta_cadastro_produto():

    # verificar_imagem_encontrada(time.time(), 10, 'img/wms/wms.png'), 0.1, 'abre_consulta_cadastro_produto - wms')
    
    verificar_imagem_encontrada(time.time(), 10, 'img/wms/consultas.png', 0.1, 'abre_consulta_cadastro_produto - consultas')
    click('img/wms/consultas.png', 1)

    verificar_imagem_encontrada(time.time(), 10, 'img/wms/consulta_cadastro_endereco_apanha.png', 0.1, 'abre_consulta_cadastro_produto - consulta_cadastro_endereco_apanha')
    click('img/wms/consulta_cadastro_endereco_apanha.png', 1)
        
def baixar_cadastro_produto():

    pause(0.1)

    #seleciona 'todos' os flag

    verificar_imagem_encontrada(time.time(), 10, 'img/wms/filtro_cadastro_ender_apanha.png', 0.1, 'baixar_cadastro_produto - filtro_cadastro_ender_apanha')
    click('img/wms/filtro_cadastro_ender_apanha.png', 1)

    verificar_imagem_encontrada(time.time(), 10, 'img/wms/estoq_apan_frac.png', 0.1, 'baixar_cadastro_produto - estoq_apan_frac')
    click('img/wms/estoq_apan_frac.png', 1)

    verificar_imagem_encontrada(time.time(), 10, 'img/wms/estoq_apan_promo_frac.png', 0.1, 'baixar_cadastro_produto - estoq_apan_promo_frac')
    click('img/wms/estoq_apan_promo_frac.png', 1)

    verificar_imagem_encontrada(time.time(), 10, 'img/wms/estoq_armazenagem.png', 0.1, 'baixar_cadastro_produto - estoq_armazenagem')
    click('img/wms/estoq_armazenagem.png', 1)

    verificar_imagem_encontrada(time.time(), 10, 'img/wms/pedido_pendente.png', 0.1, 'baixar_cadastro_produto - pedido_pendente')
    click('img/wms/pedido_pendente.png', 1)

    verificar_imagem_encontrada(time.time(), 10, 'img/wms/estoq_apan_cx.png', 0.1, 'baixar_cadastro_produto - estoq_apan_cx')
    click('img/wms/estoq_apan_cx.png', 1)

    # verificar_imagem_encontrada(time.time(), 10, 'img/wms/estoque_apan_promo_cx.png', 0.1, 'baixar_cadastro_produto - estoque_apan_promo_cx')
    # click('img/wms/estoque_apan_promo_cx.png', 1)

    verificar_imagem_encontrada(time.time(), 10, 'img/wms/receb_pendente.png', 0.1, 'baixar_cadastro_produto - receb_pendente')
    click('img/wms/receb_pendente.png', 1)

    # ---

    verificar_imagem_encontrada(time.time(), 10, 'img/excel/botao_gerar_excel.png', 0.1, 'baixar_cadastro_produto - botao_gerar_excel')
    click('img/excel/botao_gerar_excel.png', 1)


def abre_consulta_analise_curva():

    verificar_imagem_encontrada(time.time(), 10, 'img/wms/consultas.png', 0.1, 'abre_consulta_analise_curva - consultas')
    click('img/wms/consultas.png', 1)

    verificar_imagem_encontrada(time.time(), 10, 'img/wms/analise_curva_abc.png', 0.1, 'abre_consulta_analise_curva - analise_curva_abc')
    click('img/wms/analise_curva_abc.png', 1)

def baixar_analise_curva(tipo_curva):
    
    if tipo_curva == 'curva_geral':

        pag.press('tab', presses=2)
        pag.press('enter')

        time.sleep(10)
        verificar_imagem_encontrada(time.time(), 1800, 'img/wms/gerando_dados.png', 5, 'baixar_analise_curva - gerando_dados')
        click('img/wms/gerando_dados.png', 1)

        # espera filtrar para precionar o botão
        verificar_imagem_encontrada(time.time(), 1800, 'img/excel/botao_gerar_excel.png', 5, 'baixar_analise_curva - botao_gerar_excel')
        click('img/excel/botao_gerar_excel.png', 1)

        pag.press('tab')
        pag.press('enter')

    if tipo_curva == 'curva_cx':

        verificar_imagem_encontrada(time.time(), 20, 'img/wms/limpar_filtro.png', 1, 'baixar_analise_curva - limpar_filtro')
        click('img/wms/limpar_filtro.png', 1)

        verificar_imagem_encontrada(time.time(), 20, 'img/wms/selec_curva_cx.png', 1, 'baixar_analise_curva - selec_curva_cx')
        click('img/wms/selec_curva_cx.png', 1)

        pag.press('tab', presses=3)
        pag.press('enter')

        time.sleep(10)
        verificar_imagem_encontrada(time.time(), 1800, 'img/wms/gerando_dados.png', 5, 'baixar_analise_curva - gerando_dados')
        click('img/wms/gerando_dados.png', 1)

        # espera filtrar para precionar o botão
        verificar_imagem_encontrada(time.time(), 1800, 'img/excel/botao_gerar_excel.png', 5, 'baixar_analise_curva - botao_gerar_excel')
        click('img/excel/botao_gerar_excel.png', 1)
        pag.press('tab')
        pag.press('enter')

    if tipo_curva == 'curva_frac':
        
        verificar_imagem_encontrada(time.time(), 20, 'img/wms/limpar_filtro.png', 1, 'baixar_analise_curva - limpar_filtro')
        click('img/wms/limpar_filtro.png', 1)

        verificar_imagem_encontrada(time.time(), 20, 'img/wms/selec_curva_frac.png', 1, 'baixar_analise_curva - selec_curva_frac')
        click('img/wms/selec_curva_frac.png', 1)

        pag.press('tab', presses=3)
        pag.press('enter')

        time.sleep(10)
        verificar_imagem_encontrada(time.time(), 1800, 'img/wms/gerando_dados.png', 5, 'baixar_analise_curva - gerando_dados')
        click('img/wms/gerando_dados.png', 1)

        # espera filtrar para precionar o botão
        verificar_imagem_encontrada(time.time(), 1800, 'img/excel/botao_gerar_excel.png', 5, 'baixar_analise_curva - botao_gerar_excel')
        click('img/excel/botao_gerar_excel.png', 1)
        pag.press('tab')
        pag.press('enter')