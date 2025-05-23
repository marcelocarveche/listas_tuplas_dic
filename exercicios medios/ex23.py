"""
Dada uma lista com nomes duplicados, elimine os nomes repetidos mantendo a ordem

"""

nomes = [
    "marcelo",
    "leticia",
    "otavio",
    "lucas",
    "monica",
    "marcelo",
    "julia",
    "leticia",
]

filtrada = []

for name in nomes:
    if name not in filtrada:
        filtrada.append(name)

print(filtrada)
