import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

while True:
    
        nome = str(input("Qual o seu nome: "))
        idade = int(input("qual a sua idade: "))
        email = input("qual o seu email? ")

        cursor = banco.cursor()
        cursor.execute(f"INSERT INTO pessoas  (nome, idade, email) VALUES (?, ?, ?)", (nome, idade, email))
        banco.commit()
    
        r = str(input("deseja cadastrar mais uma pessoa? [S/N] ")).upper().strip()
        if r in 'N':
            break
banco.close()
print("Programa encerrado!\n Volte Sempre!")
            