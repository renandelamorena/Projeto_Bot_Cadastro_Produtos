from time import sleep
import pyautogui as pag
import func_geral, func_wms

func_wms.abre_wms()

func_wms.abre_app_wms('GERENCIAMENTO')

sleep(3)

func_wms.abre_consulta_cadastro_produto()

func_wms.baixar_cadastro_produto()

func_geral.salvar_planilha(r'C:\Users\samuel.lucas\OneDrive - MAXIFARMA DISTRIBUIDORA DE MEDICAMENTOS LTDA\Documentos\estoque.renan\projetos\Projeto_Curva_ABC\data\tratamento_curva_abc\datasets\produtos.xlsx')
# func_geral.salvar_excel('produtos', '2')

sleep(5)

pag.hotkey('alt', 'f4')

pag.hotkey('alt', 'f4')
pag.hotkey('alt', 'f4')
pag.hotkey('alt', 'f4')

func_geral.salvar_dados()