from abc import ABC, abstractmethod
class LibraryResource(ABC):
    def __init__(self, resource_id, title, author_publisher, publication_year):
        self._resource_id = resource_id
        self._title = title
        self._author_publisher = author_publisher
        self._publication_year = publication_year
        self._is_available = True
    def get_resource_id(self):
        return self._resource_id
    def get_title(self):
        return self._title
    def set_availability(self, available):
        self._is_available = available
    def is_available(self):
        return self._is_available
    @abstractmethod
    def display_details(self):
        pass
    def __del__(self):
        print(f"LibraryResource '{self._title}' (ID: {self._resource_id}) is being deallocated.")
class Book(LibraryResource):
    def __init__(self, resource_id, title, author, publication_year, isbn, genre):
        super().__init__(resource_id, title, author, publication_year)
        self._isbn = isbn
        self._genre = genre
    def get_isbn(self):
        return self._isbn
    def get_genre(self):
        return self._genre
    def display_details(self):
        super().display_details()
        print(f"ISBN: {self._isbn}, Genre: {self._genre}")
class Journal(LibraryResource):
    def __init__(self, resource_id, title, publisher, publication_year, issn, volume, issue):
        super().__init__(resource_id, title, publisher, publication_year)
        self._issn = issn
        self._volume = volume
        self._issue = issue
    def get_issn(self):
        return self._issn
    def get_volume(self):
        return self._volume
    def get_issue(self):
        return self._issue
    def display_details(self):
        super().display_details()
        print(f"ISSN: {self._issn}, Volume: {self._volume}, Issue: {self._issue}")
class EBook(LibraryResource):
    def __init__(self, resource_id, title, author, publication_year, format, 
download_url):
        super().__init__(resource_id, title, author, publication_year)
        self._format = format
        self._download_url = download_url
    def get_format(self):
        return self._format
    def get_download_url(self):
        return self._download_url
    def display_details(self):
        super().display_details()
        print(f"Format: {self._format}, Download URL: {self._download_url}")
class Member:
    def __init__(self, member_id, name, contact_info):
        self._member_id = member_id
        self._name = name
        self._contact_info = contact_info
        self._borrowed_items = []
    def get_member_id(self):
        return self._member_id
    def get_name(self):
        return self._name
    def borrow_item(self, resource):
        if resource.is_available():
            self._borrowed_items.append(resource)
            resource.set_availability(False)
            print(f"{self._name} borrowed '{resource.get_title()}'.")
            return True
        else:
            print(f"'{resource.get_title()}' is currently unavailable.")
            return False
    def return_resource(self, resource):
        if resource in self._borrowed_items:
            self._borrowed_items.remove(resource)
            resource.set_availability(True)
            print(f"{self._name} returned '{resource.get_title()}'.")
            return True
        else:
            print(f"{self._name} did not borrow '{resource.get_title()}'.")
            return False
    def display_borrowed_items(self):
        if self._borrowed_items:
            print(f"{self._name} has borrowed:")
            for item in self._borrowed_items:
                print(f"- {item.get_title()} (ID: {item.get_resource_id()})")
        else:
            print(f"{self._name} has not borrowed any items.")
class Librarian:
    def __init__(self, librarian_id, name):
        self._librarian_id = librarian_id
        self._name = name
    def get_librarian_id(self):
        return self._librarian_id
    def get_name(self):
        return self._name
    def add_resource(self, resource):
        print(f"{self._name} added resource: '{resource.get_title()}' (ID: {resource.get_resource_id()})")
    def remove_resource(self, resource):
        print(f"{self._name} removed resource: '{resource.get_title()}' (ID: {resource.get_resource_id()})")
    def process_loan(self, member, resource):
        if member.borrow_item(resource):
            print(f"{self._name} processed loan of '{resource.get_title()}' to {member.get_name()}.")
            return True
        else:
            print(f"{self._name} could not process loan of '{resource.get_title()}' to {member.get_name()}.")
            return False
    def process_return(self, member, resource):
        if member.return_resource(resource):
            print(f"{self._name} processed return of '{resource.get_title()}' from {member.get_name()}.")
            return True
        else:
            print(f"{self._name} could not process return of '{resource.get_title()}' from {member.get_name()}.")
            return False
if __name__ == "__main__":
    book1 = Book("B001", "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, "978-0345391803", "Science Fiction")
    journal1 = Journal("J001", "Nature", "Nature Publishing Group", 2023, "00280836", 620, 7974)
    ebook1 = EBook("E001", "Python Crash Course", "Eric Matthes", 2019, "PDF", "https://nostarch.com/pythoncrashcourse2e")
    member1 = Member("M001", "Alice Smith", "alice.smith@example.com")
    member2 = Member("M002", "Bob Johnson", "bob.johnson@example.com")
    librarian1 = Librarian("L001", "Sarah Lee")
    print("\n--- Resource Details ---")
    book1.display_details()
    journal1.display_details()
    ebook1.display_details()
    print("\n--- Initial Borrowing ---")
    librarian1.process_loan(member1, book1)
    librarian1.process_loan(member1, journal1)
    librarian1.process_loan(member2, book1)
    print("\n--- Member Borrowed Items ---")
    member1.display_borrowed_items()
    member2.display_borrowed_items()
    print("\n--- Returning a Resource ---")
    librarian1.process_return(member1, book1)
    librarian1.process_return(member1, ebook1)
    print("\n--- Member Borrowed Items After Return---")
    member1.display_borrowed_items()
    print("\n--- Adding and Removing ---")
    librarian1.add_resource(ebook1)
    librarian1.remove_resource(journal1)
    del book1
    del journal1
    del member1
    del member2
    del librarian1
    del ebook1
