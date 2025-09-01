import streamlit as st
import pandas as pd

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

def atributo_forca(atributo):
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

def atributo_destreza(atributo):
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

def atributo_agilidade(atributo):
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

def atributo_constituicao(atributo):
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

def atributo_inteligencia(atributo):
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

def formatar_valor(valor):
    if valor == int(valor):
        return f"{int(valor)}"
    else:
        return f"{valor:.2f}".replace('.', ',')

def tabela_filtrada(indices, valores):
    dados = [(nome, valor) for nome, valor in zip(indices, valores) if valor != 0]
    if not dados:
        return pd.DataFrame({"Atributo": ["Nenhum valor"], "Valor": ["-"]})
    nomes, vals = zip(*dados)
    return pd.DataFrame({
        "Atributo": nomes,
        "Valor": [formatar_valor(v) for v in vals]
    })

def mostrar_atributos_streamlit(atributo):
    st.subheader("Atributos Base")
    base = {
        "Força": [formatar_valor(atributo.forca)],
        "Destreza": [formatar_valor(atributo.destreza)],
        "Agilidade": [formatar_valor(atributo.agilidade)],
        "Constituição": [formatar_valor(atributo.constituicao)],
        "Inteligência": [formatar_valor(atributo.inteligencia)]
    }
    st.table(pd.DataFrame(base))

    if atributo.tem_mana:
        with st.expander("Força"):
            indices = [
                "PDG Tank", "PDG Max", "PDG Med", "PDG DPS", "PDG Flanco", "PDG Magic", "PDG Suporte",
                "Impacto Tank", "Impacto Max", "Impacto Lutador",
                "KG Tank", "KG Max", "KG Med", "KG DPS", "KG Flanco", "KG Magic", "KG Suporte"
            ]
            valores = [
                atributo.pdg_tank, atributo.pdg_max, atributo.pdg_med, atributo.pdg_dps, atributo.pdg_flanco, atributo.pdg_magic, atributo.pdg_suporte,
                atributo.impacto_tank, atributo.impacto_max, atributo.impacto_lutador,
                atributo.kg_tank, atributo.kg_max, atributo.kg_med, atributo.kg_dps, atributo.kg_flanco, atributo.kg_magic, atributo.kg_suporte
            ]
            st.table(tabela_filtrada(indices, valores))

        with st.expander("Destreza"):
            indices = [
                "QD Classes", "QD Combatente", "QD DPS", "CM DPS",
                "MS Tank", "MS Max", "MS Med", "MS DPS", "MS Flanco", "MS Suporte"
            ]
            valores = [
                atributo.qd_classes, atributo.qd_combatente, atributo.qd_dps, atributo.cm_dps,
                atributo.ms_tank, atributo.ms_max, atributo.ms_med, atributo.ms_dps, atributo.ms_flanco, atributo.ms_suporte
            ]
            st.table(tabela_filtrada(indices, valores))

        with st.expander("Agilidade"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**KM**")
                indices = ["Tank", "Max", "Med", "DPS", "Flanco", "Magic", "Suporte"]
                valores = [atributo.km_tank, atributo.km_max, atributo.km_med, atributo.km_dps, atributo.km_flanco, atributo.km_magic, atributo.km_suporte]
                st.table(tabela_filtrada(indices, valores))
            with col2:
                st.markdown("**ASPD**")
                indices = ["Tank", "Max", "Med", "DPS", "Flanco", "Magic", "Suporte"]
                valores = [atributo.aspd_tank, atributo.aspd_max, atributo.aspd_med, atributo.aspd_dps, atributo.aspd_flanco, atributo.aspd_magic, atributo.aspd_suporte]
                st.table(tabela_filtrada(indices, valores))

        with st.expander("Constituição"):
            indices = [
                "PDR Tank", "Vida Tank", "PDR Max", "Vida Max", "PDR Med", "Vida Med",
                "PDR DPS", "Vida DPS", "PDR Flanco", "Vida Flanco", "PDR Magic", "Vida Magic",
                "PDR Suporte", "Vida Suporte", "MM Físico", "MM Militar"
            ]
            valores = [
                atributo.pdr_tank, atributo.vida_tank, atributo.pdr_max, atributo.vida_max, atributo.pdr_med, atributo.vida_med,
                atributo.pdr_dps, atributo.vida_dps, atributo.pdr_flanco, atributo.vida_flanco, atributo.pdr_magic, atributo.vida_magic,
                atributo.pdr_suporte, atributo.vida_suporte, atributo.mm_fisico, atributo.mm_militar
            ]
            st.table(tabela_filtrada(indices, valores))

        with st.expander("Inteligência"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**MDR**")
                indices = ["Tank", "Max", "Med", "DPS", "Flanco", "Magic", "Suporte"]
                valores = [atributo.mdr_tank, atributo.mdr_max, atributo.mdr_med, atributo.mdr_dps, atributo.mdr_flanco, atributo.mdr_magic, atributo.mdr_suporte]
                st.table(tabela_filtrada(indices, valores))
            with col2:
                st.markdown("**Mana**")
                indices = ["Tank", "Max", "Med", "DPS", "Flanco", "Magic", "Suporte"]
                valores = [atributo.mana_tank, atributo.mana_max, atributo.mana_med, atributo.mana_dps, atributo.mana_flanco, atributo.mana_magic, atributo.mana_suporte]
                st.table(tabela_filtrada(indices, valores))
            st.markdown(f"**MS Magic:** {formatar_valor(atributo.ms_magic)}")

            st.markdown("**Classes Específicas**")
            indices = ["Jumper", "Mago", "Necromante", "Sacerdote", "Invocador", "Demonista", "Bardo", "Ilusionista"]
            mdg = [atributo.mdg_jumper, atributo.mdg_mago, atributo.mdg_necromante, atributo.mdg_sacerdote,
                   atributo.mdg_invocador, atributo.mdg_demonista, atributo.mdg_bardo, atributo.mdg_ilusionista]
            rit = [atributo.rit_jumper, atributo.rit_mago, atributo.rit_necromante, atributo.rit_sacerdote,
                     atributo.rit_invocador, atributo.rit_demonista, atributo.rit_bardo, atributo.rit_ilusionista]
            magias = [(nome, m, r) for nome, m, r in zip(indices, mdg, rit) if m != 0 or r != 0]
            if magias:
                st.table(pd.DataFrame({
                    "Classe": [m[0] for m in magias],
                    "MDG": [formatar_valor(m[1]) for m in magias],
                    "RIT": [formatar_valor(m[2]) for m in magias]
                }))
            else:
                st.write("Nenhuma magia específica.")

    else:
        st.info("Personagem Primitivo")
        with st.expander("Força"):
            indices = [
                "PDG Tank", "PDG Max", "PDG Med", "PDG DPS", "PDG Flanco", "PDG Suporte",
                "Impacto Tank", "Impacto Max", "Impacto Lutador",
                "KG Tank", "KG Max", "KG Med", "KG DPS", "KG Flanco", "KG Suporte"
            ]
            valores = [
                atributo.nm_pdg_tank, atributo.nm_pdg_max, atributo.nm_pdg_med, atributo.nm_pdg_dps, atributo.nm_pdg_flanco, atributo.nm_pdg_suporte,
                atributo.nm_impacto_tank, atributo.nm_impacto_max, atributo.nm_impacto_lutador,
                atributo.nm_kg_tank, atributo.nm_kg_max, atributo.nm_kg_med, atributo.nm_kg_dps, atributo.nm_kg_flanco, atributo.nm_kg_suporte
            ]
            st.table(tabela_filtrada(indices, valores))

        with st.expander("Destreza"):
            indices = [
                "QD Classes", "QD Combatente", "QD DPS", "CM DPS",
                "MS Tank", "MS Max", "MS Med", "MS DPS", "MS Flanco", "MS Suporte"
            ]
            valores = [
                atributo.nm_qd_classes, atributo.nm_qd_combatente, atributo.nm_qd_dps, atributo.nm_cm_dps,
                atributo.nm_ms_tank, atributo.nm_ms_max, atributo.nm_ms_med, atributo.nm_ms_dps, atributo.nm_ms_flanco, atributo.nm_ms_suporte
            ]
            st.table(tabela_filtrada(indices, valores))

        with st.expander("Agilidade"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**KM**")
                indices = ["Tank", "Max", "Med", "DPS", "Flanco", "Suporte"]
                valores = [atributo.nm_km_tank, atributo.nm_km_max, atributo.nm_km_med, atributo.nm_km_dps, atributo.nm_km_flanco, atributo.nm_km_suporte]
                st.table(tabela_filtrada(indices, valores))
            with col2:
                st.markdown("**ASPD**")
                indices = ["Tank", "Max", "Med", "DPS", "Flanco", "Suporte"]
                valores = [atributo.nm_aspd_tank, atributo.nm_aspd_max, atributo.nm_aspd_med, atributo.nm_aspd_dps, atributo.nm_aspd_flanco, atributo.nm_aspd_suporte]
                st.table(tabela_filtrada(indices, valores))

        with st.expander("Constituição"):
            indices = [
                "PDR Tank", "Vida Tank", "PDR Max", "Vida Max", "PDR Med", "Vida Med",
                "PDR DPS", "Vida DPS", "PDR Flanco", "Vida Flanco",
                "PDR Suporte", "Vida Suporte", "MM Físico", "MM Militar"
            ]
            valores = [
                atributo.nm_pdr_tank, atributo.nm_vida_tank, atributo.nm_pdr_max, atributo.nm_vida_max, atributo.nm_pdr_med, atributo.nm_vida_med,
                atributo.nm_pdr_dps, atributo.nm_vida_dps, atributo.nm_pdr_flanco, atributo.nm_vida_flanco,
                atributo.nm_pdr_suporte, atributo.nm_vida_suporte, atributo.nm_mm_fisico, atributo.nm_mm_militar
            ]
            st.table(tabela_filtrada(indices, valores))

        with st.expander("Inteligência"):
            st.markdown(f"**Foco:** {formatar_valor(atributo.nm_foco)} &nbsp;&nbsp; **Reação:** {formatar_valor(atributo.nm_reacao)}")
# --- Streamlit Interface ---
st.title("Sistema de Cálculo de Atributos - Arkyos RPG")
st.markdown("Preencha os campos abaixo para calcular os atributos do seu personagem.")

raca = st.selectbox("Sua raça é primitiva?", ["Não", "Sim"])
forca = st.number_input("Força", min_value=0.0, step=1.0)
destreza = st.number_input("Destreza", min_value=0.0, step=1.0)
agilidade = st.number_input("Agilidade", min_value=0.0, step=1.0)
constituicao = st.number_input("Constituição", min_value=0.0, step=1.0)
inteligencia = st.number_input("Inteligência", min_value=0.0, step=1.0)


if st.button("Calcular"):
    atributo = atributos()
    atributo.tem_mana = False if raca == "Sim" else True
    atributo.forca = forca
    atributo.destreza = destreza
    atributo.agilidade = agilidade
    atributo.constituicao = constituicao
    atributo.inteligencia = inteligencia

    atributo_forca(atributo)
    atributo_destreza(atributo)
    atributo_agilidade(atributo)
    atributo_constituicao(atributo)
    atributo_inteligencia(atributo)

    mostrar_atributos_streamlit(atributo)
