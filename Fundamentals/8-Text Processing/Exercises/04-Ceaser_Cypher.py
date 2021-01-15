class Text:
    def __init__(self, data):
        self.text_data = data
        self.text_encrypted = None
        self.encryption()

    def encryption(self):
        encrypted_text = ''
        for letter in self.text_data:
            new_letter = ord(letter) + 3
            encrypted_text += chr(new_letter)
        self.text_encrypted = encrypted_text


text_1 = Text(input())
print(text_1.text_encrypted)
