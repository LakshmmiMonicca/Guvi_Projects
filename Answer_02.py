class TelephoneBook:
    def __init__(self, contacts):
        self.contacts = contacts  # public visibility by default

    def addContacts(self):
        with open("contacts.txt", "w") as file:
            for name, number in self.contacts:
                file.write(f"{name}:{number}\n")

    def getContacts(self, startsWith):
        result = []
        try:
            with open("contacts.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    name, number = line.split(":")
                    if name.startswith(startsWith):
                        result.append([name, number])
        except FileNotFoundError:
            print("contacts.txt not found. Run addContacts() first.")
        return result
