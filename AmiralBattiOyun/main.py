import random
board = []#Matris oluşturma
counter = 0
score = 160
for i in range(4):
    board.append(["0"]*4) #Her satırda 4 tane 0 olacak. toplam 4 satırlı 4 sütunlu matris

def show_board(board):
    for row in board:
        print (" ".join(row)) #Her bir eleman arasında boşluk bırakmak için
def rand(board):
    return random.randint(1, len(board)-1) #Geminin yerlerini belirtmek için rastgele sayı üretiyor.

print("-"*40)
print("Welcome to Amiral Batti Game")
print("-"*40)
print("Your score is",score)
print("-"*40)
show_board(board)

ship1_row=rand(board) #1. geminin satır yerini belirtmek için
ship1_column=rand(board)
ship2_row=rand(board)
ship2_column=rand(board) #2. geminin sütun yerini belirtmek için
while True:
    if((ship1_row == ship2_row) and (ship1_column == ship2_column)): #Eğer 2 gemide aynı yere atandıysa diğerini değiştirmek için
        ship2_row=rand(board)
        ship2_column=rand(board)
        continue
    else:
        print("-"*40)
        guess_row = int(input("Please enter the row: ")) #Kullanıcıdan satır ve sütun değeri almak için
        guess_column = int(input("Please enter the column: "))
        if((guess_row==ship1_row and guess_column==ship1_column) or (guess_row==ship2_row and guess_column==ship2_column)): #Tahmin edilen sayılarla geminin yeri tespit edilirse
            if board[guess_row-1][guess_column-1] == "/":
                print("-"*40)
                print("You already guessed")
                print("-" * 40)
                show_board(board)
            else:
                print("-"*40)
                print("Congratulations you sunk the ship")
                board[guess_row-1][guess_column-1] = "/" #Sürekli bir eksiğini alırız çünkü diziler 0 dan başlıyor.
                print("Your score is", score)
                print("-" * 40)
                show_board(board)
                counter += 1 #Gemi bulundu. Sayaç 1 artırılır.
        else:
            if ((guess_row < 0 or guess_row > 4) or (guess_column < 0 or guess_column > 4)): #Kullanıcıdan değer alırken eğer yanlış değer girerse...
                print("-" * 40)
                print("You entered the wrong value...")
                print("Try again...")
            elif board[guess_row - 1][guess_column - 1] == "X":
                print("-" * 40)
                print("You already guessed")
                print("-"*40) #Kod çalıştırılırken kullanıcı daha rahat görebilmesi için...
                show_board(board)
            else:
                print("-" * 40)
                board[guess_row - 1][guess_column - 1] = "X"
                print("You could not hit ")
                score -= 10
                print("Your score is", score)
                print("-" * 40)
                show_board(board)

        if counter == 2: #Sayaç 2 ye eşitse oyun biter...
            print("-" * 40)
            print("Congratulations, you won the game")
            print("Your score is", score)
            print("-" * 40)
            break
        if score == 0:
            print("-" * 40)
            print("Game over")
            print("-" * 40)
            break










