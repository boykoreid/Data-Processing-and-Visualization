
class DLinkedListNode:
    """An instance of this class represents a doubly linked list node"""
    def __init__(self, InitData, InitNext, InitPrevious):
        self.data = InitData
        self.next = InitNext
        self.previous = InitPrevious

        if InitNext != None:
            self.next.previous = self
        if InitPrevious != None:
            self.previous.next = self

    def get_data(self):
        """
        Input: None
        Returns: Data stored in the node
        """
        return self.data
    
    def set_data(self,newData):
        """
        Sets the data in the node to the given data.
        Input: New data to be stored in the node`
        Returns: None
        """
        self.data = newData
        
    def get_next(self):
        """
        Input: None
        Returns: Next node in the list
        """
        return self.next
    
    def get_previous(self):
        """
        Input: None
        Returns: Previous node in the list
        """
        return self.previous
    
    def set_next(self,newNext):
        """
        Sets the next node in the list to the given node.
        Input: New next node in the list
        Returns: None
        """
        self.next = newNext
        
    def set_previous(self,newPrevious):
        """
        Sets the previous node in the list to the given node.
        Input: New previous node in the list
        Returns: None
        """
        self.previous = newPrevious


class Carousel:
    """An instance of this class represents a carousel"""
    def __init__(self):
        self.head = None
        self.current = None

    def add(self, data):
        """
        This function adds a new node after current
        Inputs: any - data: the data we want to add into the carousel
        Returns: None
        """
        
        if self.current == None and self.head == None:
            new = DLinkedListNode(data, None, None)

            self.current = new
            self.head = new 

            self.current.set_next(self.head)
            self.current.set_previous(self.head)

            self.head.set_next(self.current)
            self.head.set_previous(self.current)

        else:
            next_node = self.current.get_next()
            new = DLinkedListNode(data, next_node, self.current)
            self.current.set_next(new)
            next_node.set_previous(new)
            self.current = new

    def move_next(self):
        """
        Move current to the next node
        Inputs: None
        Returns: None
        """
        if self.head == None:
            raise Exception('Error: Carousel is Empty')
        self.current = self.current.get_next()

    def move_previous(self):
        """
        Move current to the previous node
        Inputs: None
        Returns: None
        """
        if self.head == None:
            raise Exception('Error: Carousel is Empty')
        self.current = self.current.get_previous()

    def get_current_data(self):
        """
        Inputs: None
        Returns: The data of the current node
        """
        if self.head == None:
            raise Exception('Error: Carousel is Empty')
        return self.current.get_data()

    def __str__(self):
        """
        Inputs: None
        Returns: The string representation of the carousel
        """
        #add self.head to the string representation before looping through the rest
        temp = self.head
        str_exp = "["
        string = str(temp.get_data())
        str_exp = str_exp + string + ','
        temp = temp.get_next()

        while temp != self.head:
            if temp.get_next() == self.head:
                string = str(temp.get_data())
                str_exp = str_exp + string + ']'
                temp = temp.get_next()
            else:
                string = str(temp.get_data())
                str_exp = str_exp + string + ','
                temp = temp.get_next()

        return str_exp
    
def main():
    # Create a carousel
    carousel = Carousel()

    # Add some employees as strings
    carousel.add("Alice, HR, ID:101")
    carousel.add("Bob, Sales, ID:102")
    carousel.add("Charlie, IT, ID:103")
    carousel.add("Diana, Marketing, ID:104")

    # Print the carousel
    print("Full Carousel:")
    print(carousel)

    # Show the current employee
    print("\nCurrent Employee:")
    print(carousel.get_current_data())

    # Move forward through the carousel
    carousel.move_next()
    print("\nAfter moving next:")
    print(carousel.get_current_data())

    # Move backward using movePrevious()
    carousel.move_previous()
    print("Previous:", carousel.get_current_data())

if __name__ == "__main__":
    main()




        