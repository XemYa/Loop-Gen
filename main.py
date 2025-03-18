print("-------Loop Number-------")
number = input("Pick a number for the loop:")
if not number.isdigit():
    print("Needs to be a number");
    exit()
number=int(number)
print("-------Loop Text-------")
text = input("Text:")
print("-------Loop Result-------")
for i in range(number):
    print(f"{i +1}.{text}")
