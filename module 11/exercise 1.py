class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Name: {self.name} \nAuthor: {self.author} \nPages: {self.page_count}")

class Magazine(Publication):
    def __init__(self,name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_information(self):
        print(f"Name: {self.name} \nChief editor: {self.chief_editor}")

# main program
magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment No. 6", "Rosa Liksom", 192)
magazine.print_information()
print()
book.print_information