---
layout: default
title: Dynamic Potentials and Magical Relationships
nav_exclude: false
nav_order: 2
has_children: false
parent: LLM and ML application
---

# Dynamic Potentials and Magical Relationships - Analogy and Symmetry

## Thermomechanics Transformation: Heat -> Work

```python

# Thermomechanics Transformation Heat -> Work
def internal_energy_thermo(dU, T, dS, P, dV):
    return dU - T * dS + P * dV

def free_energy_thermo(dF, S, dT, P, dV):
    return dF - S * dT - P * dV

def enthalpy_thermo(dH, T, dS, V, dP):
    return dH - T * dS + V * dP

def free_enthalpy_thermo(dG, S, dT, V, dP):
    return dG - S * dT + V * dP

# Economy Transformation Work -> Money
def internal_energy_economy_TM(dE_TM, U_P, dP, F_A, dV):
    return dE_TM - U_P * dP + F_A * dV

def free_energy_economy_TM(dE_TM_L, P, dU_P, F_A, dV):
    return dE_TM_L + P * dU_P + F_A * dV

def empraxia_economy_TM(dX, U_P, dP, V, dF_A):
    return dX - U_P * dP - V * dF_A

def free_empraxia_economy_TM(dX_L, P, dU_P, V, dF_A):
    return dX_L + P * dU_P - V * dF_A

# Economy Transformation Money -> Work
def internal_energy_economy_MT(dE_MT, U_A, dA, F_P, dB):
    return dE_MT + U_A * dA - F_P * dB

def free_energy_economy_MT(dE_MT_L, A, dU_A, F_P, dB):
    return dE_MT_L - A * dU_A - F_P * dB

def enomaillie_economy_MT(dL, U_A, dA, B, dF_P):
    return dL + U_A * dA + B * dF_P

def free_enomaillie_economy_MT(dL_L, A, dU_A, B, dF_P):
    return dL_L - A * dU_A + B * dF_P

# Maxwell Relations
def maxwell_relations_thermo(dT_dV_S, dP_dS_V):
    return (dT_dV_S, -dP_dS_V)

def maxwell_relations_economy_TM(dU_P_dV_P, dF_A_dP_V):
    return (dU_P_dV_P, -dF_A_dP_V)

def maxwell_relations_economy_MT(dU_A_dB_A, dF_P_dA_B):
    return (dU_A_dB_A, -dF_P_dA_B)
```
