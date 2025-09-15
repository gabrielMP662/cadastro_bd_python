import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()
cursor.execute('''
            CREATE TABLE IF NOT EXISTS pessoas (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL,
                 idade INTEGER NOT NULL,
                 email TEXT NOT NULL
                  )  ''')
while True:
    
    nome = str(input("Qual o seu nome: "))
    while True:
        try:    
            idade = int(input("qual a sua idade: "))
            break
        except ValueError:
            print('Por favor, digite um numero valido!')
    email = input("qual o seu email? ")

    cursor.execute(f"INSERT INTO pessoas  (nome, idade, email) VALUES (?, ?, ?)", (nome, idade, email))
    banco.commit()
    while True:
        r = str(input("deseja cadastrar mais uma pessoa? [S/N] ")).upper().strip()
        if r in ['N', 'S']:
            break
    if r == 'N':
        break
cursor.close()
banco.close()
print("Programa encerrado!\n Volte Sempre!")