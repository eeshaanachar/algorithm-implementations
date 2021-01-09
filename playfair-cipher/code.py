class PlayfairCipher:

    def __init__(self, key):
        key = key.lower().replace('j', 'i') + 'abcdefghiklmnopqrstuvwxyz'
        flat_grid = list()
        for letter in key:
            if letter not in flat_grid:
                flat_grid.append(letter)
        self.grid = [flat_grid[i:i+5] for i in range(0, len(flat_grid), 5)]

    def getPos(self, letter):
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] == letter:
                    return (i, j)

    def encrypt(self, plain_text):

        spaces = list()
        for i, letter in enumerate(plain_text):
            if letter == ' ':
                spaces.append(i)
            elif not letter.isalpha():
                raise Exception('Invalid character in plain text')

        plain_text = plain_text.lower().replace(' ', '').replace('j', 'i') + 'z'        
        cipher_text = ''
        
        for i in range(0, len(plain_text) - 1, 2):
            i1, j1 = self.getPos(plain_text[i])
            i2, j2 = self.getPos(plain_text[i + 1])
            if i1 == i2:
                cipher_text += self.grid[i1][(j1 + 1) % 5]
                cipher_text += self.grid[i2][(j2 + 1) % 5]
            elif j1 == j2:
                cipher_text += self.grid[(i1 + 1) % 5][j1]
                cipher_text += self.grid[(i2 + 1) % 5][j2]
            else:
                cipher_text += self.grid[i1][j2]
                cipher_text += self.grid[i2][j1]

        for i in spaces:
            cipher_text = cipher_text[:i] + ' ' + cipher_text[i:]

        return cipher_text


    def decrypt(self, cipher_text):
        
        spaces = list()
        for i, letter in enumerate(cipher_text):
            if letter == ' ':
                spaces.append(i)
            elif letter == 'j' or not letter.isalpha():
                raise Exception('Corrupted cipher text given')

        cipher_text = cipher_text.lower().replace(' ', '')
        if len(cipher_text) % 2 != 0:
            raise Exception('Corrupted cipher text given')

        plain_text = ''

        for i in range(0, len(cipher_text), 2):
            i1, j1 = self.getPos(cipher_text[i])
            i2, j2 = self.getPos(cipher_text[i + 1])
            if i1 == i2:
                plain_text += self.grid[i1][j1 - 1]
                plain_text += self.grid[i2][j2 - 1]
            elif j1 == j2:
                plain_text += self.grid[i1 - 1][j1]
                plain_text += self.grid[i2 - 1][j2]
            else:
                plain_text += self.grid[i1][j2]
                plain_text += self.grid[i2][j1]

        for i in spaces:
            plain_text = plain_text[:i] + ' ' + plain_text[i:]

        return plain_text

def menu():
    print('\n' + '-' * 30 + '\n' + '-' * 13 + 'MENU' + '-' * 13)
    return int(input('1. Encrypt\n2. Decrypt\n3. Quit\n: '))

cipher = PlayfairCipher('monarchy')

while True:
    choice = menu()
    if choice == 1:
        plain_text = input('Enter plain text\n: ')
        print('Cipher text: ', cipher.encrypt(plain_text))
    elif choice == 2:
        cipher_text = input('Enter cipher text\n: ')
        print('Plain text: ', cipher.decrypt(cipher_text))
    else:
        break