class Auto:
    auto_count = 0

    def __init__(self, auto_name, auto_model, auto_year):
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        Auto.auto_count += 1
        print(f'Name - {self.auto_name}, model - {self.auto_model}, year - {self.auto_year}')

    def on_start(self, speed):
        print(f'Go - go, {self.auto_name} {self.auto_model}. Speed - {speed}')

    def on_stop(self, speed):
        print(f'Stop, speed - {speed}')


auto_1 = Auto('Lada', 'X-Ray', '2019')
# print(auto_1.auto_name)
# auto_1.on_start(80)
# auto_1.on_stop(100)

auto_new = Auto('Peugeot', '408', '2013')


# print(auto_new.auto_name)
# auto_new.on_start(40)

# ------
class Transport:
    def __init__(self, auto_name, auto_model, auto_year):
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year

    def on_start(self, speed):
        print(f'Go - go, {self.auto_name} {self.auto_model}. Speed - {speed}')

    def on_stop(self, speed):
        print(f'Stop, {self.auto_name}. Speed - {speed}')


class Auto(Transport):
    def __init__(self, auto_name, auto_model, auto_year, pass_):
        super().__init__(auto_name, auto_model, auto_year)
        self.pass_ = pass_

    def check(self):
        print('Some')


auto_my = Auto('Lada', 'X-Ray', '2019', '7')
auto_my.on_start(100)
print(
    f'Name - {auto_my.auto_name}, model - {auto_my.auto_model}, '
    f'year - {auto_my.auto_year}, passaagers - {auto_my.pass_}')
auto_my.check()


# ------ Наследование
class Transport:
    def trasport_method(self):
        print('Parent_method')


class Auto(Transport):
    def auto_method(self):
        print('cl_auto')


class Bus(Transport):
    def bus_method(self):
        print('cl_bus')


a = Auto()
a.auto_method()
a.trasport_method()


# ------
class Shape:
    def __init__(self, par_1, par_2):
        self.par_1 = par_1
        self.par_2 = par_2

    def get_par(self):
        return f'Shape is: {self.par_1}, {self.par_2}'


class Material:
    def __init__(self, par_1, par_2):
        self.par_1 = par_1
        self.par_2 = par_2

    def get_par(self):
        return f'Material is: {self.par_1}, {self.par_2}'


class Triangle(Shape, Material):
    pass


t = Material(10, 20)
print(t.get_par())
tg = Triangle(10, 20)
print(tg.get_par())


# ------
class Auto:
    def auto_start(self, par_1, par_2=None):
        if par_2 is not None:
            print(par_1 + par_2)
        else:
            print(par_1)


a = Auto()
a.auto_start(50)
b = Auto()
b.auto_start(50, 50)


# ------
class Transport:
    def show_method(self):
        print('Parent_method')


class Auto(Transport):
    def show_method(self):
        print('cl_auto')


class Bus(Transport):
    def show_method(self):
        print('cl_bus')
        super().show_method()
        Transport.show_method(self)


a = Transport()
a.show_method()
c = Auto()
c.show_method()
e = Bus()
e.show_method()
