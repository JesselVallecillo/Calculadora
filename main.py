# main.py - Calculadora Geométrica en equipo 
import math 

def calcular_area_triangulo(base, altura): 
    return (base * altura) / 2

print("--- BIENVENIDO A LA CALCULADORA GEOMÉTRICA ---") 
print(f"Área de un triangulo de base 5 y altura 10: {calcular_area_triangulo(5, 10):.2f}")