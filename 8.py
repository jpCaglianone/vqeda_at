def selection_sort(jogadores):
    n = len(jogadores)
    for i in range(n - 1):
        indice_minimo = i
        for j in range(i + 1, n):
            if jogadores[j]["pontuacao"] < jogadores[indice_minimo]["pontuacao"]:
                indice_minimo = j
        jogadores[i], jogadores[indice_minimo] = jogadores[indice_minimo], jogadores[i]

jogadores = [
    {"nome": "João", "pontuacao": 85},
    {"nome": "Maria", "pontuacao": 70},
    {"nome": "Ana", "pontuacao": 95},
    {"nome": "Pedro", "pontuacao": 60},
    {"nome": "Lucas", "pontuacao": 75},
    {"nome": "Carlos", "pontuacao": 50},
    {"nome": "Fernanda", "pontuacao": 90},
    {"nome": "Paulo", "pontuacao": 55},
    {"nome": "Juliana", "pontuacao": 65},
    {"nome": "Rafael", "pontuacao": 80},
    {"nome": "Gabriel", "pontuacao": 40},
    {"nome": "Bianca", "pontuacao": 45},
    {"nome": "Eduardo", "pontuacao": 100},
    {"nome": "Clara", "pontuacao": 85},
    {"nome": "Renata", "pontuacao": 30},
    {"nome": "Sofia", "pontuacao": 20},
    {"nome": "Arthur", "pontuacao": 95},
    {"nome": "Ricardo", "pontuacao": 88},
    {"nome": "Vanessa", "pontuacao": 72},
    {"nome": "Aline", "pontuacao": 67},
    {"nome": "Thiago", "pontuacao": 90},
    {"nome": "Larissa", "pontuacao": 76},
    {"nome": "Fábio", "pontuacao": 62},
    {"nome": "Débora", "pontuacao": 81},
    {"nome": "Marcos", "pontuacao": 33},
    {"nome": "Helena", "pontuacao": 48},
    {"nome": "Felipe", "pontuacao": 91},
    {"nome": "Isabela", "pontuacao": 56},
    {"nome": "Leonardo", "pontuacao": 78},
    {"nome": "Camila", "pontuacao": 53},
    {"nome": "Matheus", "pontuacao": 84},
    {"nome": "Patrícia", "pontuacao": 43},
    {"nome": "Rodrigo", "pontuacao": 69},
    {"nome": "Bárbara", "pontuacao": 66},
    {"nome": "Otávio", "pontuacao": 73},
    {"nome": "Tatiana", "pontuacao": 92},
    {"nome": "Flávia", "pontuacao": 87},
    {"nome": "Gustavo", "pontuacao": 79},
    {"nome": "Rogério", "pontuacao": 49},
    {"nome": "Irene", "pontuacao": 35},
    {"nome": "Vinícius", "pontuacao": 77},
    {"nome": "André", "pontuacao": 68},
    {"nome": "Catarina", "pontuacao": 46},
    {"nome": "Hugo", "pontuacao": 52},
    {"nome": "Mônica", "pontuacao": 58},
    {"nome": "Samuel", "pontuacao": 82},
    {"nome": "Lorena", "pontuacao": 94},
    {"nome": "Vitor", "pontuacao": 71},
    {"nome": "Mariana", "pontuacao": 64},
    {"nome": "Pietra", "pontuacao": 74}
]


selection_sort(jogadores)

for jogador in jogadores:
    print(f"Nome: {jogador['nome']}, Pontuação: {jogador['pontuacao']}")
