class MealyMachine:
    def __init__(self):
        self.state = 'S0'
        self.output = ''
        
    def transition(self, input):
        if input == '0':
            self.output = '1' if self.state == 'S1' else '0'
            self.state = 'S0'
        elif input == '1':
            self.output = '0' if self.state == 'S1' else '1'
            self.state = 'S1'
            
        return self.output
        
machine = MealyMachine()

input_string = '1011101'

for i in input_string:
    output = machine.transition(i)
    print(f'Input: {i}, Output: {output}')