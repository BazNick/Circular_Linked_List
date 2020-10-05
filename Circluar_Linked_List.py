class Node:
    __slots__ = 'user_name', 'user_mail', '_next'

    def __init__(self, user_name, user_mail, _next):
        self.user_name = user_name
        self.user_mail = user_mail
        self._next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def create_user(self, name, mail):
        new_user = Node(name, mail, None)
        if self.is_empty():
            self.head = new_user
            self.tail = new_user
            new_user._next = new_user
        else:
            self.tail._next = new_user
            new_user._next = self.head
        self.tail = new_user
        self.size += 1

    def display(self):
        if self.is_empty():
            print('The list is empty\n')
            return False
        p = self.head
        i = 0
        while i < len(self):
            print('User:', p.user_name)
            print('Mail:', p.user_mail, '\n')
            p = p._next
            i += 1

    def search(self, search_user_by_mail):
        if self.is_empty():
            print('The list is empty\n')
            return False
        else:
            p = self.head
            j = 0
            while j < len(self):
                if p.user_mail == search_user_by_mail:
                    print('User with the mail', '"' + search_user_by_mail + '"', 'is found!')
                    print('User:', p.user_name)
                    print('Mail:', p.user_mail, '\n')
                    return True
                p = p._next
                j += 1
            print('User with mail', search_user_by_mail, 'is not found\n')
            return False

    def add_to_beginning(self, name, mail):
        first_user = Node(name, mail, None)
        if self.is_empty():
            self.head = first_user
            self.tail = first_user
            first_user._next = first_user
        else:
            self.tail._next = first_user
            first_user._next = self.head
        self.head = first_user
        self.size += 1

    def add_user_to_random_place(self, add_name, add_mail, position):
        if position < 1 or position > len(self):
            print('The list contains', self.size, 'elements')
            print("You can't insert in non existing position!\n")
            return False
        inserting_user = Node(add_name, add_mail, position)
        p = self.head
        k = 1
        while k < position - 1:
            p = p._next
            k += 1
        inserting_user._next = p._next
        p._next = inserting_user
        self.size += 1

    def remove_user(self, mail):
        if self.is_empty():
            print('The list is empty\n')
            return False
        p = self.head
        i = 0
        while i <= len(self):
            if p.user_mail == mail:
                break
            temp = p
            p = p._next
            i += 1
        if i > len(self):
            print('User with mail', mail, 'is not found\n')
            return False
        if p == self.head:
            self.tail._next = self.head._next
            self.head = self.head._next
            p._next = None
            self.size -= 1
            return p
        elif p == self.tail:
            i = 0
            position = len(self) - 1
            while i < position:
                p = p._next
                i += 1
            p._next._next = None
            p._next = self.head
            self.size -= 1
            return p
        else:
            temp._next = p._next
            self.size -= 1
            return p


user = CircularLinkedList()
