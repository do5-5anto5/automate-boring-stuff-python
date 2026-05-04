import re

class Calculator:

    """
    A small in-run calculator class handling basic arithmetic and memory operations.

    Defined in e5.py as class Calculator.
    Maintains memory, result, and last_operation.
    Supports expressions like n1 + n2, C, and memory commands (M+, M-, MS, MR, MC).
    """
    
    def __init__(self):
        # Initialize calculator state
        self.memory = None  # Stores memory value for memory operations
        self.result = 0.0  # Current result display
        self.last_operation = ""  # Stores last operation for continuation

    def handle_memory(self, expression: str) -> bool:
        # Handle memory operations (M, M+, M-, MS, MR, MC)
        # Returns True if expression was a memory operation, False otherwise
        
        if expression.upper().startswith("M"):
            e = expression.upper().replace(" ", "")

            # M: Store current result in memory
            if e == "M":
                self.memory = self.result
            # M+<number>: Add number to memory
            elif re.match(r'^M\+\d+(\.\d+)?$', e):
                mem = float(e[2:])
                if self.memory is not None: self.memory += mem
                else: self.memory = mem
            # M-<number>: Subtract number from memory
            elif re.match(r'^M\-\d+(\.\d+)?$', e):
                mem = float(e[2:])
                if self.memory is not None: self.memory -= mem                
                else: self.memory = -mem
            # MS<number>: Set memory to specific number
            elif re.match(r'^MS\d+(\.\d+)?$', e):
                mem = float(e.replace("MS", ""))
                self.memory = mem
            # MR: Recall memory to result
            elif e == "MR":
                self.result = self.memory
            # MC: Clear memory
            elif e == "MC":
                self.memory = None
            else: print("""Invalid Memory Expression 
            Add number to memory: M+<number>
            Subtract number from memory: M-<number>
            Rewrite memory number: MS<number>
            Get memory number: MR
            Memory clear: MC
            """)

            return True
        else:
            return False

    def handle_expression(self, expression: str) -> float:

        if self.handle_memory(expression):
            return self.result

        if expression.upper() == "C":
            result = self.reset_result()
            return result
        elif expression == "" and self.result != 0 and self.last_operation != "":
            # Continue last operation with empty input (e.g., after "5 + 3", pressing Enter again does "8 + 3")
            result = self.handle_expression(f"{self.result}{self.last_operation}")
            return result

        # Use regex to extract numbers and operators correctly
        # Pattern: optional spaces, number (with optional decimal), operator, number, optional spaces
        match = re.match(r'^\s*(-?\d+(?:\.\d+)?)\s*([\+\-\*/])\s*(-?\d+(?:\.\d+)?)\s*$', expression)
        if not match:
            print('Invalid Expression')
            return self.reset_result()
            
        n1 = float(match.group(1))
        operator = match.group(2)
        n2 = float(match.group(3))
        
        if operator == "+":
            return self.sum(n1, n2)
        elif operator == "-":
            return self.sub(n1, n2)
        elif operator == "*":
            return self.mult(n1, n2)
        elif operator == "/":
            if n2 != 0:
                return self.div(n1, n2)
            else:
                print('Is not possible divide any number by 0')
                return self.reset_result()
        else:
            return self.result


    def sum(self, n1: float, n2: float) -> float:
        # Perform addition and store operation for continuation
        self.last_operation = f"+{n2}"
        self.result = n1 + n2
        return self.result

    def sub(self, n1: float, n2: float) -> float:
        # Perform subtraction and store operation for continuation
        self.last_operation = f"-{n2}"
        self.result = n1 - n2
        return self.result

    def mult(self, n1: float, n2: float) -> float:
        # Perform multiplication and store operation for continuation
        self.last_operation = f"*{n2}"
        self.result = n1 * n2
        return self.result

    def div(self, n1: float, n2: float) -> float:
        # Perform division and store operation for continuation
        self.last_operation = f"/{n2}"
        self.result = n1 / n2
        return self.result

    def reset_result(self) -> float:
        # Reset calculator result to zero
        self.result = 0.0
        return self.result    


# Create calculator instance
calc = Calculator()

# Main calculator loop
while True:
    expression = input("Type math operations ( + , - , *, / )")
    
    result = calc.handle_expression(expression)

    print(result)
