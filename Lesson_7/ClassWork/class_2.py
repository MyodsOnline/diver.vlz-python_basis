class Test:
    def __init__(self, p_1):
        self.p_1 = p_1

    def __call__(self, new_p_1):
        self.p_1 = new_p_1

    def __str__(self):
        return f'Result - {self.p_1}'

var_1 = Test(23)
var_2 = Test(77)
print(var_1, var_2)

print()
var_1('one')
var_2('two')
print(var_1, var_2)