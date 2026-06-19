# main.py - Calculadora Geométrica en equipo
import math
def calcular_area_cuadrado(lado): 
    return lado * lado

def calcular_area_circulo(radio): 
    return math.pi * (radio ** 2) 

 def calcular_area_triangulo(base, altura): 
    return (base * altura) / 2
  
print("--- BIENVENIDO A LA CALCULADORA GEOMÉTRICA ---") 
print(f"Área de un círculo de radio 3: {calcular_area_circulo(3):.2f}")
print(f"Área de un cuadrado de lado 5: {calcular_area_cuadrado(5)}")
print(f"Área de un triangulo de base 5 y altura 10: {calcular_area_triangulo(5, 10):.2f}")