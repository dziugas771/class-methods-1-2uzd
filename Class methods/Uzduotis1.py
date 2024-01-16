
class Factorial:

    @classmethod
    def factorial(cls, number):
        fact = 1
        for num in range(2, number + 1):
            fact *= num
        return fact

factorial = Factorial()
print(Factorial.factorial(10))
