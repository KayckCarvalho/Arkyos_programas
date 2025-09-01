class atributos:
    tem_mana = True
    def __init__(self):
        self.forca = 0
        self.destreza = 0
        self.agilidade = 0
        self.constituicao = 0
        self.inteligencia = 0
        ###################################
        ############# FORÇA ###############
        self.pdg_tank = 0
        self.pdg_max = 0
        self.pdg_med = 0
        self.pdg_dps = 0
        self.pdg_flanco = 0
        self.pdg_magic = 0
        self.pdg_suporte = 0

        self.kg_tank = 45
        self.kg_max = 85
        self.kg_med = 42
        self.kg_dps = 30
        self.kg_flanco = 27
        self.kg_magic = 22
        self.kg_suporte = 20

        self.impacto_tank = 0
        self.impacto_max = 0
        self.impacto_lutador = 0
        ########### NM #############
        self.nm_pdg_tank = 0
        self.nm_pdg_max = 0
        self.nm_pdg_med = 0
        self.nm_pdg_dps = 0
        self.nm_pdg_flanco = 0
        self.nm_pdg_suporte = 0

        self.nm_kg_tank = 52
        self.nm_kg_max = 92
        self.nm_kg_med = 49
        self.nm_kg_dps = 37
        self.nm_kg_flanco = 27
        self.nm_kg_suporte = 20

        self.nm_impacto_tank = 0
        self.nm_impacto_max = 0
        self.nm_impacto_lutador = 0

        ###################################
        ############ DESTREZA #############
        self.qd_classes = 0
        self.qd_dps = 0
        self.qd_combatente = 0

        self.cm_dps = 0

        self.ms_tank = 0.8
        self.ms_max = 1
        self.ms_med = 1.8
        self.ms_dps = 2.8
        self.ms_flanco = 3.3
        self.ms_suporte = 2
        ########### NM #############
        self.nm_qd_classes = 0
        self.nm_qd_dps = 0
        self.nm_qd_combatente = 0

        self.nm_cm_dps = 0

        self.nm_ms_tank = 8.5
        self.nm_ms_max = 8.5
        self.nm_ms_med = 8.5
        self.nm_ms_dps = 8.5
        self.nm_ms_flanco = 8.5
        self.nm_ms_suporte = 8.5

        ###################################
        ########### AGILIDADE #############

        self.km_tank = 1.8
        self.km_max = 1.2
        self.km_med = 3.5
        self.km_dps = 5.5
        self.km_flanco = 5.8
        self.km_magic = 3.8
        self.km_suporte = 3.3

        self.aspd_tank = 2.5
        self.aspd_max = 1.8
        self.aspd_med = 3.5
        self.aspd_dps = 6.4
        self.aspd_flanco = 5.9
        self.aspd_magic = 4
        self.aspd_suporte = 3
        ########### NM #############
        self.nm_km_tank = 1.8
        self.nm_km_max = 1.9
        self.nm_km_med = 4.2
        self.nm_km_dps = 6.5
        self.nm_km_flanco = 6.5
        self.nm_km_suporte = 4

        self.nm_aspd_tank =3.2
        self.nm_aspd_max = 3.2
        self.nm_aspd_med = 4.2
        self.nm_aspd_dps = 7.1
        self.nm_aspd_flanco = 6.6
        self.nm_aspd_suporte = 3.7

        ###################################
        ########## CONSTITUIÇÃO ###########

        self.pdr_tank = 0
        self.vida_tank = 0
        self.pdr_max = 0
        self.vida_max = 0
        self.pdr_med = 0
        self.vida_med = 0
        self.pdr_dps = 0
        self.vida_dps = 0
        self.pdr_flanco = 0
        self.vida_flanco = 0
        self.pdr_magic = 0
        self.vida_magic = 0
        self.pdr_suporte = 0
        self.vida_suporte = 0
        
        self.mm_fisico = 0
        self.mm_militar = 0
        ########### NM #############
        self.nm_pdr_tank = 0
        self.nm_vida_tank = 0
        self.nm_pdr_max = 0
        self.nm_vida_max = 0
        self.nm_pdr_med = 0
        self.nm_vida_med = 0
        self.nm_pdr_dps = 0
        self.nm_vida_dps = 0
        self.nm_pdr_flanco = 0
        self.nm_vida_flanco = 0
        self.nm_pdr_magic = 0
        self.nm_vida_magic = 0
        self.nm_pdr_suporte = 0
        self.nm_vida_suporte = 0
        
        self.nm_mm_fisico = 0
        self.nm_mm_militar = 0

        ###################################
        ############# MAGICO ##############

        self.mdr_tank = 0
        self.mdr_max = 0
        self.mdr_med = 0
        self.mdr_dps = 0
        self.mdr_flanco = 0
        self.mdr_magic = 0
        self.mdr_suporte = 0

        self.mana_tank = 0
        self.mana_max = 0
        self.mana_med = 0
        self.mana_dps = 0
        self.mana_flanco = 0
        self.mana_magic = 0
        self.mana_suporte = 0

        self.ms_magic = 4.8

        self.mdg_jumper = 0
        self.rit_jumper = 0

        self.mdg_mago = 0
        self.rit_mago = 0

        self.mdg_necromante = 0
        self.rit_necromante = 0

        self.mdg_sacerdote = 0
        self.rit_sacerdote = 0

        self.mdg_invocador = 0
        self.rit_invocador = 0

        self.mdg_demonista = 0
        self.rit_demonista = 0

        self.mdg_bardo = 0
        self.rit_bardo = 0

        self.mdg_ilusionista = 0
        self.rit_ilusionista = 0
        ########### NM #############
        self.nm_foco = 0
        self.nm_reacao = 8.5

atributo = atributos()

def perguntas():
    def ler_numero(msg):
        contador = 0
        while True:
            valor = input(msg)
            try:
                return float(valor)
            except ValueError:
                contador += 1
                if contador >= 7:
                    print("\nMaluco, para de digitar errado! Vou considerar 0 pra você.\n")
                    return 0
                else:
                    print("\nErro: digite apenas números amigão!\n")

    input('\nBem-vindo ao sistema de cálculo de atributos do Arkyos RPG!\nPressione Enter para continuar...\n')
    while True:
        pergunta = input('Sua raça é primitiva?\n >>')
        if pergunta.lower() in ['sim', 's', 'yes', 'y']:
            atributo.tem_mana = False
            break
        elif pergunta.lower() in ['não', 'nao', 'n', 'no']:
            atributo.tem_mana = True
            break
        else:
            print('\nDigitou errado ai amigo, faz de novo.')
    f = ler_numero('Digite o valor da força:\n >>')
    d = ler_numero('\nDigite o valor da destreza:\n >>')
    a = ler_numero('\nDigite o valor da agilidade:\n >>')
    c = ler_numero('\nDigite o valor da constituição:\n >>')
    i = ler_numero('\nDigite o valor da inteligência:\n >>')

    atributo.forca += f
    atributo.destreza += d
    atributo.agilidade += a
    atributo.constituicao += c
    atributo.inteligencia += i

def atributo_forca():
    if atributo.tem_mana == True:
        pdg_tank = atributo.forca * 0.054
        kg_tank = atributo.forca * 0.21
        impact_tank = atributo.forca * 0.018
        atributo.impacto_tank += impact_tank
        atributo.kg_tank += kg_tank
        atributo.pdg_tank += pdg_tank

        pdg_max = atributo.forca * 0.095
        kg_max = atributo.forca * 0.25
        impact_tank = atributo.forca * 0.026
        atributo.impacto_max += impact_tank
        atributo.kg_max += kg_max
        atributo.pdg_max += pdg_max

        pdg_med = atributo.forca * 0.061
        kg_med = atributo.forca * 0.23
        atributo.kg_med += kg_med
        atributo.pdg_med += pdg_med

        pdg_dps = atributo.forca * 0.043
        kg_pds = atributo.forca * 0.15
        atributo.kg_dps += kg_pds
        atributo.pdg_dps += pdg_dps

        pdg_flanco = atributo.forca * 0.041
        kg_flanco = atributo.forca * 0.12
        atributo.kg_flanco += kg_flanco
        atributo.pdg_flanco += pdg_flanco

        pdg_magic = atributo.forca * 0.034
        kg_magic = atributo.forca * 0.1
        atributo.kg_magic += kg_magic
        atributo.pdg_magic += pdg_magic
        
        pdg_suporte = atributo.forca * 0.023
        kg_suporte = atributo.forca * 0.09
        atributo.kg_suporte += kg_suporte
        atributo.pdg_suporte += pdg_suporte

        impact_lutador = atributo.forca * 0.026
        atributo.impacto_lutador += impact_lutador

        if atributo.impacto_lutador > 35:
            atributo.impacto_lutador = 35
        elif atributo.impacto_tank > 22:
            atributo.impacto_tank = 22
        elif atributo.impacto_max > 28:
            atributo.impacto_max = 28

    elif atributo.tem_mana == False:

        nm_pdg_tank = atributo.forca * 0.061
        nm_kg_tank = atributo.forca * 0.28
        nm_impact_tank = atributo.forca * 0.025
        atributo.nm_impacto_tank += nm_impact_tank
        atributo.nm_kg_tank += nm_kg_tank
        atributo.nm_pdg_tank += nm_pdg_tank

        nm_pdg_max = atributo.forca * 0.102
        nm_kg_max = atributo.forca * 0.32
        nm_impact_tank = atributo.forca * 0.033
        atributo.nm_impacto_max += nm_impact_tank
        atributo.nm_kg_max += nm_kg_max
        atributo.nm_pdg_max += nm_pdg_max

        nm_pdg_med = atributo.forca * 0.068
        nm_kg_med = atributo.forca * 0.30
        atributo.nm_kg_med += nm_kg_med
        atributo.nm_pdg_med += nm_pdg_med

        nm_pdg_dps = atributo.forca * 0.050
        nm_kg_pds = atributo.forca * 0.22
        atributo.nm_kg_dps += nm_kg_pds
        atributo.nm_pdg_dps += nm_pdg_dps

        nm_pdg_flanco = atributo.forca * 0.048
        nm_kg_flanco = atributo.forca * 0.19
        atributo.nm_kg_flanco += nm_kg_flanco
        atributo.nm_pdg_flanco += nm_pdg_flanco
        
        nm_pdg_suporte = atributo.forca * 0.030
        nm_kg_suporte = atributo.forca * 0.16
        atributo.nm_kg_suporte += nm_kg_suporte
        atributo.nm_pdg_suporte += nm_pdg_suporte

        nm_impact_lutador = atributo.forca * 0.032
        atributo.nm_impacto_lutador += nm_impact_lutador

        if atributo.nm_impacto_lutador > 42:
            atributo.nm_impacto_lutador = 42
        elif atributo.nm_impacto_tank > 29:
            atributo.nm_impacto_tank = 29
        elif atributo.nm_impacto_max > 35:
            atributo.nm_impacto_max = 35

        
def atributo_destreza():
    if atributo.tem_mana == True:
        qd_classes = atributo.destreza * 0.0008
        atributo.qd_classes += qd_classes
        qd_combatente = atributo.destreza * 0.0013
        atributo.qd_combatente += qd_combatente

        qd_dps = atributo.destreza * 0.0008
        atributo.qd_dps += qd_dps

        cm_dps = atributo.destreza * 0.02
        atributo.cm_dps += cm_dps

        if atributo.qd_classes > 35:
            atributo.qd_classes = 35
        elif atributo.qd_combatente > 60:
            atributo.qd_combatente = 60
        elif atributo.qd_dps > 35:
            atributo.qd_dps = 35
        elif atributo.cm_dps > 45:
            atributo.cm_dps = 45

        ms_tank = atributo.destreza * 0.0015
        atributo.ms_tank += ms_tank
        ms_max = atributo.destreza * 0.018
        atributo.ms_max += ms_max
        ms_med = atributo.destreza * 0.026
        atributo.ms_med += ms_med
        ms_dps = atributo.destreza * 0.030
        atributo.ms_dps += ms_dps
        ms_flanco = atributo.destreza * 0.036
        atributo.ms_flanco += ms_flanco
        ms_suporte = atributo.destreza * 0.023
        atributo.ms_suporte += ms_suporte

    if atributo.tem_mana == False:

        nm_qd_classes = atributo.destreza * 0.0015
        atributo.nm_qd_classes += nm_qd_classes
        nm_qd_combatente = atributo.destreza * 0.0020
        atributo.nm_qd_combatente += nm_qd_combatente

        nm_qd_dps = atributo.destreza * 0.0015
        atributo.nm_qd_dps += nm_qd_dps

        nm_cm_dps = atributo.destreza * 0.09
        atributo.nm_cm_dps += nm_cm_dps

        if atributo.qd_classes > 40:
            atributo.qd_classes = 40
        elif atributo.qd_combatente > 65:
            atributo.qd_combatente = 65
        elif atributo.qd_dps > 40:
            atributo.qd_dps = 40
        elif atributo.cm_dps > 50:
            atributo.cm_dps = 50

        nm_ms_tank = atributo.destreza * 0.0102
        atributo.nm_ms_tank += nm_ms_tank
        nm_ms_max = atributo.destreza * 0.0102
        atributo.nm_ms_max += nm_ms_max
        nm_ms_med = atributo.destreza * 0.0102
        atributo.nm_ms_med += nm_ms_med
        nm_ms_dps = atributo.destreza * 0.0102
        atributo.nm_ms_dps += nm_ms_dps
        nm_ms_flanco = atributo.destreza * 0.0102
        atributo.nm_ms_flanco += nm_ms_flanco
        nm_ms_suporte = atributo.destreza * 0.0102
        atributo.nm_ms_suporte += nm_ms_suporte

def atributo_agilidade():
    if atributo.tem_mana == True:
        km_tank = atributo.agilidade * 0.008
        atributo.km_tank += km_tank
        km_max = atributo.agilidade * 0.013
        atributo.km_max += km_max
        km_med = atributo.agilidade * 0.055
        atributo.km_med += km_med
        km_dps = atributo.agilidade * 0.065
        atributo.km_dps += km_dps
        km_flanco = atributo.agilidade * 0.071
        atributo.km_flanco += km_flanco
        km_magic = atributo.agilidade * 0.044
        atributo.km_magic += km_magic
        km_suporte = atributo.agilidade * 0.033
        atributo.km_suporte += km_suporte

        aspd_tank = atributo.agilidade * 0.032
        aspd_max = atributo.agilidade * 0.028
        aspd_med = atributo.agilidade * 0.053
        aspd_dps = atributo.agilidade * 0.076
        aspd_flanco = atributo.agilidade * 0.083
        aspd_suporte = atributo.agilidade * 0.027
        atributo.aspd_tank += aspd_tank
        atributo.aspd_max += aspd_max
        atributo.aspd_med += aspd_med
        atributo.aspd_dps += aspd_dps
        atributo.aspd_flanco += aspd_flanco
        atributo.aspd_suporte += aspd_suporte
    
    if atributo.tem_mana == False:
        nm_km_tank = atributo.agilidade * 0.015
        atributo.nm_km_tank += nm_km_tank
        nm_km_max = atributo.agilidade * 0.020
        atributo.nm_km_max += nm_km_max
        nm_km_med = atributo.agilidade * 0.062
        atributo.nm_km_med += nm_km_med
        nm_km_dps = atributo.agilidade * 0.072
        atributo.nm_km_dps += nm_km_dps
        nm_km_flanco = atributo.agilidade * 0.078
        atributo.nm_km_flanco += nm_km_flanco
        nm_km_suporte = atributo.agilidade * 0.049
        atributo.nm_km_suporte += nm_km_suporte

        nm_aspd_tank = atributo.agilidade * 0.039
        nm_aspd_max = atributo.agilidade * 0.035
        nm_aspd_med = atributo.agilidade * 0.060
        nm_aspd_dps = atributo.agilidade * 0.083
        nm_aspd_flanco = atributo.agilidade * 0.090
        nm_aspd_suporte = atributo.agilidade * 0.034
        atributo.nm_aspd_tank += nm_aspd_tank
        atributo.nm_aspd_max += nm_aspd_max
        atributo.nm_aspd_med += nm_aspd_med
        atributo.nm_aspd_dps += nm_aspd_dps
        atributo.nm_aspd_flanco += nm_aspd_flanco
        atributo.nm_aspd_suporte += nm_aspd_suporte

def atributo_constituicao():
    if atributo.tem_mana == True:
        pdr_tank = atributo.constituicao * 0.005
        vida_tank = atributo.constituicao * 1.2
        atributo.pdr_tank += pdr_tank
        atributo.vida_tank += vida_tank
        pdr_max = atributo.constituicao * 0.004
        vida_max = atributo.constituicao * 0.8
        atributo.pdr_max += pdr_max
        atributo.vida_max += vida_max
        pdr_med = atributo.constituicao * 0.002
        vida_med = atributo.constituicao * 0.5
        atributo.pdr_med += pdr_med
        atributo.vida_med += vida_med
        pdr_dps = atributo.constituicao * 0.002
        vida_dps = atributo.constituicao * 0.5
        atributo.pdr_dps += pdr_dps
        atributo.vida_dps += vida_dps
        pdr_flanco = atributo.constituicao * 0.002
        vida_flanco = atributo.constituicao * 0.5
        atributo.pdr_flanco += pdr_flanco
        atributo.vida_flanco += vida_flanco
        pdr_magic = atributo.constituicao * 0.002
        vida_magic = atributo.constituicao * 0.5
        atributo.pdr_magic += pdr_magic
        atributo.vida_magic += vida_magic
        pdr_suporte = atributo.constituicao * 0.002
        vida_suporte = atributo.constituicao * 0.5
        atributo.pdr_suporte += pdr_suporte
        atributo.vida_suporte += vida_suporte

        mm_fisico = atributo.constituicao * 0.0012
        mm_militar = atributo.constituicao * 0.0023
        atributo.mm_fisico += mm_fisico
        atributo.mm_militar += mm_militar

        if atributo.pdr_tank > 45:
            atributo.pdr_tank = 45
        elif atributo.pdr_max > 40:
            atributo.pdr_max = 40
        elif atributo.pdr_med > 30:
            atributo.pdr_med = 30
        elif atributo.pdr_dps > 30:
            atributo.pdr_dps = 30
        elif atributo.pdr_flanco > 25:
            atributo.pdr_flanco = 25
        elif atributo.pdr_magic > 20:
            atributo.pdr_magic = 20
        elif atributo.pdr_suporte > 20:
            atributo.pdr_suporte = 20
        elif atributo.mm_fisico > 15:
            atributo.mm_fisico = 15
        elif atributo.mm_militar > 35:
            atributo.mm_militar = 35

    if atributo.tem_mana == False:

        nm_pdr_tank = atributo.constituicao * 0.012
        nm_vida_tank = atributo.constituicao * 1.9
        atributo.nm_pdr_tank += nm_pdr_tank
        atributo.nm_vida_tank += nm_vida_tank
        nm_pdr_max = atributo.constituicao * 0.011
        nm_vida_max = atributo.constituicao * 1.5
        atributo.nm_pdr_max += nm_pdr_max
        atributo.nm_vida_max += nm_vida_max
        nm_pdr_med = atributo.constituicao * 0.009
        nm_vida_med = atributo.constituicao * 1.2
        atributo.nm_pdr_med += nm_pdr_med
        atributo.nm_vida_med += nm_vida_med
        nm_pdr_dps = atributo.constituicao * 0.009
        nm_vida_dps = atributo.constituicao * 1.2
        atributo.nm_pdr_dps += nm_pdr_dps
        atributo.nm_vida_dps += nm_vida_dps
        nm_pdr_flanco = atributo.constituicao * 0.009
        nm_vida_flanco = atributo.constituicao * 1.2
        atributo.nm_pdr_flanco += nm_pdr_flanco
        atributo.nm_vida_flanco += nm_vida_flanco
        nm_pdr_suporte = atributo.constituicao * 0.009
        nm_vida_suporte = atributo.constituicao * 1.2
        atributo.nm_pdr_suporte += nm_pdr_suporte
        atributo.nm_vida_suporte += nm_vida_suporte

        nm_mm_fisico = atributo.constituicao * 0.0019
        nm_mm_militar = atributo.constituicao * 0.0030
        atributo.nm_mm_fisico += nm_mm_fisico
        atributo.nm_mm_militar += nm_mm_militar

        if atributo.nm_pdr_tank > 50:
            atributo.nm_pdr_tank = 50
        elif atributo.nm_pdr_max > 45:
            atributo.nm_pdr_max = 45
        elif atributo.nm_pdr_med > 35:
            atributo.nm_pdr_med = 35
        elif atributo.nm_pdr_dps > 35:
            atributo.nm_pdr_dps = 35
        elif atributo.nm_pdr_flanco > 30:
            atributo.nm_pdr_flanco = 30
        elif atributo.nm_pdr_suporte > 30:
            atributo.nm_pdr_suporte = 30
        elif atributo.nm_mm_fisico > 20:
            atributo.nm_mm_fisico = 20
        elif atributo.nm_mm_militar > 40:
            atributo.nm_mm_militar = 40

def atributo_inteligencia():
    if atributo.tem_mana == True:
        mdr_tank = atributo.inteligencia * 0.0025
        atributo.mdr_tank += mdr_tank
        mdr_max = atributo.inteligencia * 0.002
        atributo.mdr_max += mdr_max
        mdr_med = atributo.inteligencia * 0.002
        atributo.mdr_med += mdr_med
        mdr_dps = atributo.inteligencia * 0.002
        atributo.mdr_dps += mdr_dps
        mdr_flanco = atributo.inteligencia * 0.002
        atributo.mdr_flanco += mdr_flanco
        mdr_magic = atributo.inteligencia * 0.004
        atributo.mdr_magic += mdr_magic
        mdr_suporte = atributo.inteligencia * 0.004
        atributo.mdr_suporte += mdr_suporte

        mana_tank = atributo.inteligencia * 0.5
        atributo.mana_tank += mana_tank
        mana_max = atributo.inteligencia * 0.5
        atributo.mana_max += mana_max
        mana_med = atributo.inteligencia * 0.5
        atributo.mana_med += mana_med
        mana_dps = atributo.inteligencia * 0.5
        atributo.mana_dps += mana_dps
        mana_flanco = atributo.inteligencia * 0.8
        atributo.mana_flanco += mana_flanco
        mana_magic = atributo.inteligencia * 1.5
        atributo.mana_magic += mana_magic
        mana_suporte = atributo.inteligencia * 1
        atributo.mana_suporte += mana_suporte
        ms_magic = atributo.inteligencia * 0.095
        atributo.ms_magic += ms_magic

        mdg_jumper = atributo.inteligencia * 0.060
        atributo.mdg_jumper += mdg_jumper
        rit_jumper = atributo.inteligencia * 0.0015
        atributo.rit_jumper += rit_jumper
        mdg_mago = atributo.inteligencia * 0.068
        atributo.mdg_mago += mdg_mago
        rit_mago = atributo.inteligencia * 0.0011
        atributo.rit_mago += rit_mago
        mdg_necromante = atributo.inteligencia * 0.064
        atributo.mdg_necromante += mdg_necromante
        rit_necromante = atributo.inteligencia * 0.0010
        atributo.rit_necromante += rit_necromante
        mdg_sacerdote = atributo.inteligencia * 0.065
        atributo.mdg_sacerdote += mdg_sacerdote
        rit_sacerdote = atributo.inteligencia * 0.0012
        atributo.rit_sacerdote += rit_sacerdote
        mdg_invocador = atributo.inteligencia * 0.063
        atributo.mdg_invocador += mdg_invocador
        rit_invocador = atributo.inteligencia * 0.0011
        atributo.rit_invocador += rit_invocador
        mdg_demonista = atributo.inteligencia * 0.065
        atributo.mdg_demonista += mdg_demonista
        rit_demonista = atributo.inteligencia * 0.0012
        atributo.rit_demonista += rit_demonista
        mdg_bardo = atributo.inteligencia * 0.061
        atributo.mdg_bardo += mdg_bardo
        rit_bardo = atributo.inteligencia * 0.0011
        atributo.rit_bardo += rit_bardo
        mdg_ilusionista = atributo.inteligencia * 0.060
        atributo.mdg_ilusionista += mdg_ilusionista
        rit_ilusionista = atributo.inteligencia * 0.0010
        atributo.rit_ilusionista += rit_ilusionista
    
    if atributo.tem_mana == False:
        atributo.nm_foco = atributo.inteligencia * 0.0037
        atributo.nm_reacao = atributo.inteligencia * 0.0102
        if atributo.nm_foco > 30:
            atributo.nm_foco = 30

def mostrar_atributos():
    separador = "=" * 50
    if atributo.tem_mana:
        print(f"\n{separador}")
        print("         RESUMO DOS ATRIBUTOS DO PERSONAGEM")
        print(f"{separador}\n")
        print(f"Atributos Base:")
        print(f"  Força:         {atributo.forca:.2f}")
        print(f"  Destreza:      {atributo.destreza:.2f}")
        print(f"  Agilidade:     {atributo.agilidade:.2f}")
        print(f"  Constituição:  {atributo.constituicao:.2f}")
        print(f"  Inteligência:  {atributo.inteligencia:.2f}")
        print(f"\n{separador}")

        print("Força:")
        print(f"  PDG Tank:      {atributo.pdg_tank:.2f}    | KG Tank:      {atributo.kg_tank:.2f}    | Impacto Tank:      {atributo.impacto_tank:.2f}")
        print(f"  PDG Max:       {atributo.pdg_max:.2f}     | KG Max:       {atributo.kg_max:.2f}     | Impacto Max:       {atributo.impacto_max:.2f}")
        print(f"  PDG Med:       {atributo.pdg_med:.2f}     | KG Med:       {atributo.kg_med:.2f}")
        print(f"  PDG DPS:       {atributo.pdg_dps:.2f}     | KG DPS:       {atributo.kg_dps:.2f}")
        print(f"  PDG Flanco:    {atributo.pdg_flanco:.2f}  | KG Flanco:    {atributo.kg_flanco:.2f}")
        print(f"  PDG Magic:     {atributo.pdg_magic:.2f}   | KG Magic:     {atributo.kg_magic:.2f}")
        print(f"  PDG Suporte:   {atributo.pdg_suporte:.2f} | KG Suporte:   {atributo.kg_suporte:.2f}")
        print(f"  Impacto Lutador: {atributo.impacto_lutador:.2f}")
        print(f"{separador}")

        print("Destreza:")
        print(f"  QD Classes:    {atributo.qd_classes:.2f}  | QD Combatente: {atributo.qd_combatente:.2f} | QD DPS: {atributo.qd_dps:.2f}")
        print(f"  CM DPS:        {atributo.cm_dps:.2f}")
        print(f"  MS Tank:       {atributo.ms_tank:.2f}     | MS Max:       {atributo.ms_max:.2f}     | MS Med: {atributo.ms_med:.2f}")
        print(f"  MS DPS:        {atributo.ms_dps:.2f}      | MS Flanco:    {atributo.ms_flanco:.2f}  | MS Suporte: {atributo.ms_suporte:.2f}")
        print(f"{separador}")

        print("Agilidade:")
        print(f"  KM Tank:       {atributo.km_tank:.2f}     | KM Max:       {atributo.km_max:.2f}     | KM Med: {atributo.km_med:.2f}")
        print(f"  KM DPS:        {atributo.km_dps:.2f}      | KM Flanco:    {atributo.km_flanco:.2f}  | KM Magic: {atributo.km_magic:.2f} | KM Suporte: {atributo.km_suporte:.2f}")
        print(f"  ASPD Tank:     {atributo.aspd_tank:.2f}   | ASPD Max:     {atributo.aspd_max:.2f}   | ASPD Med: {atributo.aspd_med:.2f}")
        print(f"  ASPD DPS:      {atributo.aspd_dps:.2f}    | ASPD Flanco:  {atributo.aspd_flanco:.2f} | ASPD Magic: {atributo.aspd_magic:.2f} | ASPD Suporte: {atributo.aspd_suporte:.2f}")
        print(f"{separador}")

        print("Constituição:")
        print(f"  PDR Tank:      {atributo.pdr_tank:.2f}    | Vida Tank:    {atributo.vida_tank:.2f}")
        print(f"  PDR Max:       {atributo.pdr_max:.2f}     | Vida Max:     {atributo.vida_max:.2f}")
        print(f"  PDR Med:       {atributo.pdr_med:.2f}     | Vida Med:     {atributo.vida_med:.2f}")
        print(f"  PDR DPS:       {atributo.pdr_dps:.2f}     | Vida DPS:     {atributo.vida_dps:.2f}")
        print(f"  PDR Flanco:    {atributo.pdr_flanco:.2f}  | Vida Flanco:  {atributo.vida_flanco:.2f}")
        print(f"  PDR Magic:     {atributo.pdr_magic:.2f}   | Vida Magic:   {atributo.vida_magic:.2f}")
        print(f"  PDR Suporte:   {atributo.pdr_suporte:.2f} | Vida Suporte: {atributo.vida_suporte:.2f}")
        print(f"  MM Físico:     {atributo.mm_fisico:.2f}   | MM Militar:   {atributo.mm_militar:.2f}")
        print(f"{separador}")

        print("Inteligência:")
        print(f"  MDR Tank:      {atributo.mdr_tank:.2f}    | MDR Max:      {atributo.mdr_max:.2f}    | MDR Med: {atributo.mdr_med:.2f}")
        print(f"  MDR DPS:       {atributo.mdr_dps:.2f}     | MDR Flanco:   {atributo.mdr_flanco:.2f} | MDR Magic: {atributo.mdr_magic:.2f} | MDR Suporte: {atributo.mdr_suporte:.2f}")
        print(f"  Mana Tank:     {atributo.mana_tank:.2f}   | Mana Max:     {atributo.mana_max:.2f}   | Mana Med: {atributo.mana_med:.2f}")
        print(f"  Mana DPS:      {atributo.mana_dps:.2f}    | Mana Flanco:  {atributo.mana_flanco:.2f} | Mana Magic: {atributo.mana_magic:.2f} | Mana Suporte: {atributo.mana_suporte:.2f}")
        print(f"  MS Magic:      {atributo.ms_magic:.2f}")
        print(f"\n  Magias Específicas:")
        print(f"    Jumper:      MDG {atributo.mdg_jumper:.2f} | Rit {atributo.rit_jumper:.2f}\n")
        print(f"    Mago:        MDG {atributo.mdg_mago:.2f}   | Rit {atributo.rit_mago:.2f}\n")
        print(f"    Necromante:  MDG {atributo.mdg_necromante:.2f} | Rit {atributo.rit_necromante:.2f}\n")
        print(f"    Sacerdote:   MDG {atributo.mdg_sacerdote:.2f} | Rit {atributo.rit_sacerdote:.2f}\n")
        print(f"    Invocador:   MDG {atributo.mdg_invocador:.2f} | Rit {atributo.rit_invocador:.2f}\n")
        print(f"    Demonista:   MDG {atributo.mdg_demonista:.2f} | Rit {atributo.rit_demonista:.2f}\n")
        print(f"    Bardo:       MDG {atributo.mdg_bardo:.2f}   | Rit {atributo.rit_bardo:.2f}\n")
        print(f"    Ilusionista: MDG {atributo.mdg_ilusionista:.2f} | Rit {atributo.rit_ilusionista:.2f}\n")
        print(f"{separador}\n")
    else:
        print(f"\n{separador}")
        print("         RESUMO DOS ATRIBUTOS DO PERSONAGEM (Primitivo)")
        print(f"{separador}\n")
        print(f"Atributos Base:")
        print(f"  Força:         {atributo.forca:.2f}")
        print(f"  Destreza:      {atributo.destreza:.2f}")
        print(f"  Agilidade:     {atributo.agilidade:.2f}")
        print(f"  Constituição:  {atributo.constituicao:.2f}")
        print(f"  Inteligência:  {atributo.inteligencia:.2f}")
        print(f"\n{separador}")

        print("Força:")
        print(f"  PDG Tank:      {atributo.nm_pdg_tank:.2f}    | KG Tank:      {atributo.nm_kg_tank:.2f}    | Impacto Tank:      {atributo.nm_impacto_tank:.2f}")
        print(f"  PDG Max:       {atributo.nm_pdg_max:.2f}     | KG Max:       {atributo.nm_kg_max:.2f}     | Impacto Max:       {atributo.nm_impacto_max:.2f}")
        print(f"  PDG Med:       {atributo.nm_pdg_med:.2f}     | KG Med:       {atributo.nm_kg_med:.2f}")
        print(f"  PDG DPS:       {atributo.nm_pdg_dps:.2f}     | KG DPS:       {atributo.nm_kg_dps:.2f}")
        print(f"  PDG Flanco:    {atributo.nm_pdg_flanco:.2f}  | KG Flanco:    {atributo.nm_kg_flanco:.2f}")
        print(f"  PDG Suporte:   {atributo.nm_pdg_suporte:.2f} | KG Suporte:   {atributo.nm_kg_suporte:.2f}")
        print(f"  Impacto Lutador: {atributo.nm_impacto_lutador:.2f}")
        print(f"{separador}")

        print("Destreza:")
        print(f"  QD Classes:    {atributo.nm_qd_classes:.2f}  | QD Combatente: {atributo.nm_qd_combatente:.2f} | QD DPS: {atributo.nm_qd_dps:.2f}")
        print(f"  CM DPS:        {atributo.nm_cm_dps:.2f}")
        print(f"  MS Tank:       {atributo.nm_ms_tank:.2f}     | MS Max:       {atributo.nm_ms_max:.2f}     | MS Med: {atributo.nm_ms_med:.2f}")
        print(f"  MS DPS:        {atributo.nm_ms_dps:.2f}      | MS Flanco:    {atributo.nm_ms_flanco:.2f}  | MS Suporte: {atributo.nm_ms_suporte:.2f}")
        print(f"{separador}")

        print("Agilidade:")
        print(f"  KM Tank:       {atributo.nm_km_tank:.2f}     | KM Max:       {atributo.nm_km_max:.2f}     | KM Med: {atributo.nm_km_med:.2f}")
        print(f"  KM DPS:        {atributo.nm_km_dps:.2f}      | KM Flanco:    {atributo.nm_km_flanco:.2f}  | KM Suporte: {atributo.nm_km_suporte:.2f}")
        print(f"  ASPD Tank:     {atributo.nm_aspd_tank:.2f}   | ASPD Max:     {atributo.nm_aspd_max:.2f}   | ASPD Med: {atributo.nm_aspd_med:.2f}")
        print(f"  ASPD DPS:      {atributo.nm_aspd_dps:.2f}    | ASPD Flanco:  {atributo.nm_aspd_flanco:.2f} | ASPD Suporte: {atributo.nm_aspd_suporte:.2f}")
        print(f"{separador}")

        print("Constituição:")
        print(f"  PDR Tank:      {atributo.nm_pdr_tank:.2f}    | Vida Tank:    {atributo.nm_vida_tank:.2f}")
        print(f"  PDR Max:       {atributo.nm_pdr_max:.2f}     | Vida Max:     {atributo.nm_vida_max:.2f}")
        print(f"  PDR Med:       {atributo.nm_pdr_med:.2f}     | Vida Med:     {atributo.nm_vida_med:.2f}")
        print(f"  PDR DPS:       {atributo.nm_pdr_dps:.2f}     | Vida DPS:     {atributo.nm_vida_dps:.2f}")
        print(f"  PDR Flanco:    {atributo.nm_pdr_flanco:.2f}  | Vida Flanco:  {atributo.nm_vida_flanco:.2f}")
        print(f"  PDR Suporte:   {atributo.nm_pdr_suporte:.2f} | Vida Suporte: {atributo.nm_vida_suporte:.2f}")
        print(f"  MM Físico:     {atributo.nm_mm_fisico:.2f}   | MM Militar:   {atributo.nm_mm_militar:.2f}")
        print(f"{separador}")

        print("Inteligência:")
        print(f"  Foco:          {atributo.nm_foco:.2f}")
        print(f"  Reação:        {atributo.nm_reacao:.2f}")

def main():
    while True:
        global atributo
        atributo = atributos()

        perguntas()
        atributo_forca()
        atributo_destreza()
        atributo_agilidade()
        atributo_constituicao()
        atributo_inteligencia()
        mostrar_atributos()

        while True:
            escolha = input("\nDeseja voltar ao início ou encerrar?\n[1] Voltar\n[2] Fechar\n >> ")
            if escolha == "2":
                print("\nValeu por jogar! Até mais 👋\n")
                return
            elif escolha == "1":
                print("\nReiniciando...\n")
                break
            else:
                print("\nOpção inválida, tente novamente.\n")


if __name__ == "__main__":
    main()

