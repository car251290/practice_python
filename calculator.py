class Calculator:
    
    def _init_(self):
        self.result = 0
        
    def sum(self, a, b):
        self.result = a + b
        return self.result
    
    def rest(self, a, b):
        self.result = a - b
        return self.result
    
    def multiplication(self, a, b):
        self.result = a * b
        return self.result
    
    def divide(self, a, b):
        self.result = a / b
        return self.result
    
    #switcher for the calculator
    def switch_calc(self, operation, a, b):
         switch_calculator = {
        "case1": 
            sum,
        "case2": 
            rest,
        "case3": 
            multiplication,
        "case4": 
            divide
    }
         return switch_calculator.get(operation)(a, b)
if __name__ == "__main__":
    calc = Calculator()
    operation = input("Enter the operation: ")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = calc.switch_calc(operation, a, b)
    print(f"The result: {result}")
    


