class MyClass:
    def __init__(self, p_1, p_2):
        self.p_1 = p_1
        self.p_2 = p_2

    @property
    def my_method(self):
        return f"Параметры, переданный в класс:" \
               f" {self.p_1}, {self.p_2}"


mc = MyClass('par_1', 'par_2')

print(mc.p_1)
print(mc.p_2)
print(mc.my_method)


#
class Auto:
    def __init__(self, year):
        self.year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2020:
            self.__year = 2020
        else:
            self.__year = year

    def get_year(self):
        return f'Auto made in {str(self.year)}'


a = Auto(2018)
print(a.get_year())
