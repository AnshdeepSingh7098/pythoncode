count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1

count = 0
while count < 10:
    print(count)
    if count == 5:
        break  # Exit the loop when count is 5
    count += 1

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the rest of the code when count is 3
    print(count)

# infinite loop
# while True:
#     user_input = input("Type 'exit' to stop: ")
#     if user_input.lower() == 'exit':
#         break

tasks = []

while True:
    task = input("Enter a task (or type 'done' to finish): ")
    if task.lower() == 'done':
        break
    tasks.append(task)

print("Your tasks:")
for t in tasks:
    print(f"- {t}")

n = 100
while n > 1:
    print(f"Current value: {n}")
    if n % 2 == 0:
        n //= 2  # Halve the value if even
    else:
        n = 3 * n + 1  # Apply Collatz Conjecture rule for odd

i = 1
while i <= 3:  # Outer loop
    j = 1
    while j <= 3:  # Inner loop
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1

# A loop that runs until one of the conditions is false
x, y = 0, 10
while x <= 5 and y >= 5:
    print(f"x = {x}, y = {y}")
    x += 1
    y -= 1
