from time import sleep
import pyautogui as pag
import func_data, func_geral, func_verifica_tela, func_wms

func_wms.abre_wms()

func_wms.abre_app_wms('GERENCIAMENTO')

sleep(3)

func_wms.abre_consulta_analise_curva()

sleep(3)

func_data.colar_data_1_ano_atras()

func_wms.baixar_analise_curva('curva_geral')
func_geral.salvar_planilha(r'C:\Users\samuel.lucas\OneDrive - MAXIFARMA DISTRIBUIDORA DE MEDICAMENTOS LTDA\Documentos\estoque.renan\projetos\Projeto_Curva_ABC\data\tratamento_curva_abc\datasets\curva_geral.xlsx')

func_wms.baixar_analise_curva('curva_cx')
func_geral.salvar_planilha(r'C:\Users\samuel.lucas\OneDrive - MAXIFARMA DISTRIBUIDORA DE MEDICAMENTOS LTDA\Documentos\estoque.renan\projetos\Projeto_Curva_ABC\data\tratamento_curva_abc\datasets\curva_cx.xlsx')

func_wms.baixar_analise_curva('curva_frac')
func_geral.salvar_planilha(r'C:\Users\samuel.lucas\OneDrive - MAXIFARMA DISTRIBUIDORA DE MEDICAMENTOS LTDA\Documentos\estoque.renan\projetos\Projeto_Curva_ABC\data\tratamento_curva_abc\datasets\curva_frac.xlsx')

pag.hotkey('alt', 'f4')
pag.hotkey('alt', 'f4')
pag.hotkey('alt', 'f4')