class Email:
    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}')

number_of_mails = 0
data = []
while True:
    emails = input().split()
    if 'Stop' in emails:
        indexes_of_delivered = [int(item) for item in input().split(', ')]
        break
    data.append(emails)
for substring in range(0, len(data)):
    sender = data[substring][0]
    receiver = data[substring][1]
    content = data[substring][2]
    object_email = Email(sender, receiver, content)
    if substring in indexes_of_delivered:
        object_email.send()
    object_email.get_info()





