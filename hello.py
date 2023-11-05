import time

print("Hello!")
print("It is", time.strftime('%Y-%m-%d %H:%M:%S'))
print()
print("Type 'terminate' or 'exit' if you want to exit!")
print()

while True:
    print("Type your word :")
    question = input()
    if question in ("terminate", "exit"): break
    print()
    print("You typed:")
    print(question)
    print()
    print("=============")
    print()
    time.sleep(0.5)