import time

print("Hello!")
print("It is", time.strftime('%Y-%m-%d %H:%M:%S'))
print()

while True:
    print("Type your word:")
    question = input()
    if question == "terminate": break
    print()
    print("You typed:")
    print(question)
    time.sleep(1)