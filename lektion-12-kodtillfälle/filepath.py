import os

# Sökvägen (path) som denna python-fil finns i
current_dir = os.path.dirname(os.path.abspath(__file__))

# Kombinera python-filens sökväg med namnet på en fil i samma katalog
my_file = os.path.join(current_dir, "dudes.json")

print(current_dir)
print(my_file)

# Nu kan vi öppna filen oberoende av varifrån vi kör vårt program,
with open(my_file) as f:
    contents = f.read()

print(contents)


