class Message:
  def __init__ (self,sender, recipient, content, date):
    self.sender = sender
    self.recipient = recipient
    self.content = content
    self.date = date


message_1 = Message("Asmaa", "Aisha", "birthday greetings", "Mon 11 Nov")
message_2 = Message("Aisha", "Khadija", "videos", "Sat 9 Nov")
message_3 = Message("Fawzy", "Mohammed", "Football", "Tue 12 Nov")
message_4 = Message("Ahmed", "Leen", "love message", "Fri 21 Jun")

print(f"The first message sender is {message_1.sender}")
print(f"The second message recipient is {message_2.recipient}")
print(f"The third message date is {message_3.date}")
print(f"The forth message content is {message_4.content}")