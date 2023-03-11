class MooreMachine:
    def __init__(self):
        self.current_state = 'q0'
        self.num_vowels = 0

    def process_input(self, input_string):
        for char in input_string:
            if self.current_state == 'q0':
                if char in 'AEIOUaeiou':
                    self.current_state = 'q1'
                    self.num_vowels += 1
            elif self.current_state == 'q1':
                if char in 'AEIOUaeiou':
                    self.current_state = 'q1'
                else:
                    self.current_state = 'q0'

    def get_num_vowels(self):
        return self.num_vowels

input_string = "a a e e i i o o u u"
machine = MooreMachine()
machine.process_input(input_string)
num_vowels = machine.get_num_vowels()
print(num_vowels) 






