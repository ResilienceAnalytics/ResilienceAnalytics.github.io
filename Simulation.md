---
layout: default
title: Simulation of Agents
nav_exclude: false
nav_order: 2
has_children: false
parent: LLM and ML application
---

## Fixed

~~~python 

import numpy as np
import simpy
import math

# Basic Physical and Economic Functions
def speed(de, dt):
    return de / dt

def acceleration(de, dt):
    return (2 * de) / (dt ** 2)

def speed(de, dt):
    return de / dt

def acceleration(de, dt):
    return (2 * de) / (dt ** 2)

def force(m, gamma):
    return m * gamma

def work(F, de):
    return F * de

def amount_of_movement(m, v):
    return m * v

def kinetic_energy(m, v):
    return (1 / 2) * m * v ** 2

def principle_of_equivalence(W, J, Q):
    return W * J - Q

def first_principle(dQ_cause, dW_effect):
    return dQ_cause + dW_effect

def second_principle(Q1, T1, Q2, T2):
    return (Q1 / T1) + (Q2 / T2)

def core_law(P, V, r, T):
    return P * V - r * T

def heat(T, dS):
    return T * dS

def work_isobaric(W, P, Vf, Vi):
    return W - P * (Vf - Vi)

def internal_energy(dU, T, dS, P, dV):
    return dU - T * dS + P * dV

def isothermal_work(W, r, T, Vi, Vf):
    return W - r * T * math.log(Vf / Vi)

def adiabatic_work(W, r, gamma, Tf, Ti):
    return W - (r / (gamma - 1)) * (Tf - Ti)

def isochore_work(W):
    return W

def isothermal_heat(Q, T, Sf, Si):
    return Q - T * (Sf - Si)

def adiabatic_heat(Q):
    return Q


# Thermo-elastic coefficients
def thermo_elastic_alpha(V, dV, T):
    return 1 / V * (dV / T)

def thermo_elastic_beta(P, dP, T):
    return 1 / P * (dP / T)

def thermo_elastic_x_T(V, dV, P):
    return -1 / V * (dV / P)

# Eco-elastic coefficients for Work -> Money
def eco_elastic_alpha_TM(V, dV, U_P):
    return -1 / V * (dV / U_P)

def eco_elastic_beta_TM(F_A, dF_A, U_P):
    return -1 / F_A * (dF_A / U_P)

def eco_elastic_x_TM(V, dV, F_A):
    return 1 / V * (dV / F_A)

# Eco-elastic coefficients for Money -> Work
def eco_elastic_alpha_MT(B, dB, U_A):
    return 1 / B * (dB / U_A)

def eco_elastic_beta_MT(F_P, dF_P, U_A):
    return 1 / F_P * (dF_P / U_A)

def eco_elastic_x_MT(B, dB, F_P):
    return -1 / B * (dB / F_P)

# Calorimetric coefficients
def calorimetric_C_V(T, dS):
    return T * (dS / T)

def calorimetric_C_P(T, dS):
    return T * (dS / T)

def calorimetric_l(T, dS, V):
    return T * (dS / V)

def calorimetric_h(T, dS, P):
    return T * (dS / P)

def calorimetric_lambda(T, dS, V):
    return T * (dS / V)

def calorimetric_mu(T, dS, P):
    return T * (dS / P)

# Ecometric coefficients for Work -> Money
def ecometric_Phi_V(U_P, dP):
    return U_P * (dP / U_P)

def ecometric_Phi_F_A(U_P, dP):
    return U_P * (dP / U_P)

def ecometric_l_TM(U_P, dP, V):
    return U_P * (dP / V)

def ecometric_h_TM(U_P, dP, F_A):
    return U_P * (dP / F_A)

def ecometric_lambda_TM(U_P, dP, V):
    return U_P * (dP / V)

def ecometric_mu_TM(U_P, dP, F_A):
    return U_P * (dP / F_A)

# Ecometric coefficients for Money -> Work
def ecometric_Phi_B(U_A, dA):
    return U_A * (dA / U_A)

def ecometric_Phi_F_P(U_A, dA):
    return U_A * (dA / U_A)

def ecometric_l_MT(U_A, dA, B):
    return U_A * (dA / B)

def ecometric_h_MT(U_A, dA, F_P):
    return U_A * (dA / F_P)

def ecometric_lambda_MT(U_A, dA, B):
    return U_A * (dA / B)

def ecometric_mu_MT(U_A, dA, F_P):
    return U_A * (dA / F_P)

# Relations between coefficients
def relation_l(C_P, C_V, T, V):
    return (C_P - C_V) * (T / V)

def relation_h(C_P, C_V, T, P):
    return -(C_P - C_V) * (T / P)

def relation_lambda(C_V, T, P):
    return C_V * (T / P)

def relation_mu(C_P, T, V):
    return C_P * (T / V)



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

# ECONOMY TRANSFORMATION Work -> Money
def tachyaxy(dp, dt):
    return dp / dt

def inflation(gamma_omega, dt):
    return gamma_omega / dt

def gain_of_productivity(gamma_omega, dt):
    return -(gamma_omega / dt)

def force_a(c, gamma_omega, omega):
    return -c * gamma_omega * omega

def money(dM, F_a, dp):
    return dM - F_a * dp

def purchasing_power(c, omega):
    return -c * omega

def employment(c, omega):
    return c * omega

def kinetic_energy_cin(c, omega):
    return -(1 / 2) * c * omega ** 2

def principle_of_equivalence_economy(M, g_tm, T):
    return M - g_tm * T

def first_principle_economy(dT_cause, dM_effect):
    return dT_cause + dM_effect

def second_principle_economy(T1, U_P1, T2, U_P2):
    return (T1 / U_P1) + (T2 / U_P2)

def core_law_economy(F_A, V, r_p, U_P):
    return F_A * V - r_p * U_P

def work_economy(U_P, dP):
    return -U_P * dP

def money_isobaric(M, F_A, Vf, Vi):
    return M - F_A * (Vf - Vi)

def internal_work_economy(dE, U_P, dP, F_A, dV):
    return dE - U_P * dP + F_A * dV

def isopheles_money(M, r_p, U_P, Vf, Vi):
    return M - r_p * U_P * math.log(Vf / Vi)

def adiabatic_money(M, r, gamma_P, U_Pf, U_Pi):
    return M - (r / (gamma_P - 1)) * (U_Pf - U_Pi)

def isochore_money(M):
    return M

def isopheles_work(T, U_P, Pf, Pi):
    return T - U_P * (Pf - Pi)

def adiabatic_work_economy(T):
    return T


# ECONOMY TRANSFORMATION Money -> Work

def productivity(dl, dt):
    return -(dl / dt)

def gain_of_productivity(d2l, dt):
    return -(d2l / (dt ** 2))

def force_economy_MW(c, gamma_omega, omega):
    return c * gamma_omega * omega

def work_economy_MW(dT, F_p, dl):
    return dT - F_p * dl

def employment(c, omega):
    return c * omega

def kinetic_energy_economy_MW(c, omega):
    return (1 / 2) * c * omega ** 2

def principle_of_equivalence_economy_MW(T, g_MT, M):
    return T - g_MT * M

def first_principle_economy_MW(dM_cause, dT_effect):
    return dM_cause + dT_effect

def second_principle_economy_MW(M1, U_A1, M2, U_A2):
    return (M1 / U_A1) + (M2 / U_A2)

def core_law_economy_MW(F_P, B, r_A, U_A):
    return F_P * B - r_A * U_A

def money_economy_MW(U_A, dA):
    return U_A * dA

def work_isobaric_economy_MW(T, F_P, Bf, Bi):
    return T - F_P * (Bf - Bi)

def internal_work_economy_MW(dE, U_A, dA, F_P, dB):
    return dE + U_A * dA - F_P * dB

def isopheles_work_economy_MW(T, r_A, U_A, Bf, Bi):
    return T - r_A * U_A * math.log(Bf / Bi)

def adiabatic_work_economy_MW(T, r, gamma_A, U_Af, U_Ai):
    return T - (r / (gamma_A - 1)) * (U_Af - U_Ai)

def isochore_work_economy_MW(T):
    return T

def isophles_money_economy_MW(M, U_A, Af, Ai):
    return M - U_A * (Af - Ai)

def adiabatic_money_economy_MW(M):
    return M

# Agent Classes
class AgentEconomique:
    def __init__(self, env, role, paresse, avarice, egoisme):
        self.env = env
        self.paresse = paresse  # Laziness
        self.avarice = avarice  # Avarice
        self.egoisme = egoisme  # Selfishness
        self.richesse_monetaire = 0  # Monetary Wealth
        self.travail = 0  # Labor
        self.money = 0 
        self.cash = 0  # Cash
        self.product = 0  # Product
        self.env.process(self.cycle_vie())
        self.role = role # Seller, Transformer, or Buyer

    def ajuster_avarice(self, facteurs_externes):
        """ Ajuste l'avarice en fonction des facteurs externes """
        if facteurs_externes['recession']:
            self.avarice *= 1.1  # Augmente l'avarice en période de récession
        if facteurs_externes['inflation']:
            self.avarice *= 1.05  # Augmente légèrement l'avarice en période d'inflation

    def manufacture(self, cost):
        # Manufacturing process
        self.money -= cost
        self.product += 1

    def negotiate_and_sell(self, price):
        # Selling process
        self.money += price
        self.product -= 1

    def buy(self, price):
        # Buying process
        self.money -= price
        self.product += 1

    def cycle_vie(self):
       while True:
           if self.role in ['Seller', 'Transformer', 'Buyer']:
               # Role-specific actions
               if self.role == 'Seller':
                   self.manufacture(50)
                   yield self.env.timeout(1)
                   self.negotiate_and_sell(100)
               elif self.role == 'Transformer':
                   self.buy(100)
                   self.manufacture(30)
                   yield self.env.timeout(2)
                   self.negotiate_and_sell(150)
               elif self.role == 'Buyer':
                   self.buy(150)
                   yield self.env.timeout(3)
           else:
               # General economic activities
               self.realiser_travail()
               self.echanger()
               yield self.env.timeout(1)

    def realiser_travail(self):
        travail_effectue = 1 - self.paresse
        self.travail += travail_effectue

    def echanger(self):
        # Exchange logic based on avarice and selfishness
        pass

# Economic System Simulation
class Economie:
    def __init__(self, nombre_agents, facteurs_externes):
        self.env = simpy.Environment()
        self.facteurs_externes = facteurs_externes
        self.agents = []
        for _ in range(nombre_agents):
            role = np.random.choice(['Seller', 'Transformer', 'Buyer'])
            attributes = np.random.rand(), np.random.rand(), np.random.rand()
            agent = AgentEconomique(self.env, role, *attributes)
            self.agents.append(agent)

    def simuler(self, duree):
        for agent in self.agents:
            agent.ajuster_avarice(self.facteurs_externes)
            self.env.process(agent.cycle_vie())
        self.env.run(until=duree)

    def echanger(self):
        for agent in self.agents:
            autre_agent = np.random.choice(self.agents)
            # Exchange logic to be developed

def main():
    facteurs_externes = {'recession': True, 'inflation': False}
    economie = Economie(100, facteurs_externes)  # Pass both parameters
    economie.simuler(365)  # Simulate for a year

if __name__ == "__main__":
    main()
