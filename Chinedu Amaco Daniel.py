# Fibonacci Sequence Management System

class FibonacciSequence:

    def __init__(self, terms):
        self.terms = terms
        self.sequence = []

    def generate_sequence(self):
        first = 0
        second = 1

        if self.terms <= 0:
            print("Please enter a positive number.")
            return

        elif self.terms == 1:
            self.sequence.append(first)

        else:
            self.sequence.append(first)
            self.sequence.append(second)

            for i in range(2, self.terms):
                next_term = first + second
                self.sequence.append(next_term)

                first = second
                second = next_term

    def display_sequence(self):
        print("\nFIBONACCI SEQUENCE")
        print("------------------")

        for num in self.sequence:
            print(num, end=" ")

        print()

    def display_statistics(self):
        if len(self.sequence) > 0:
            print("\nSEQUENCE STATISTICS")
            print("-------------------")
            print("Number of Terms:", len(self.sequence))
            print("First Term:", self.sequence[0])
            print("Last Term:", self.sequence[-1])
            print("Largest Number:", max(self.sequence))
            print("Sum of Terms:", sum(self.sequence))

    def search_number(self, number):
        if number in self.sequence:
            print(f"{number} exists in the Fibonacci sequence.")
        else:
            print(f"{number} does not exist in the Fibonacci sequence.")


# Main Program
print("===================================")
print(" FIBONACCI SEQUENCE MANAGEMENT SYSTEM")
print("===================================")

terms = int(input("Enter number of terms: "))

fib = FibonacciSequence(terms)

fib.generate_sequence()

fib.display_sequence()

fib.display_statistics()

search = int(input("\nEnter a number to search: "))
fib.search_number(search)
