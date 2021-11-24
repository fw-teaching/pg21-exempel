import datetime

current_time = datetime.datetime.now()

print("Hello VSCode!")

with open('fil.txt') as file_handle:
    file_contents = file_handle.read()

print(file_contents)

"""
new_contents = f"Python was here"
with open('fil.txt', 'w') as file_handle:  # w = write
    file_handle.write(new_contents)
"""
with open('fil.txt', 'a') as file_handle: # a = append
    file_handle.write(f"Updated: {current_time}\n")

print(file_contents)
