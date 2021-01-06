class WindowDoor:
    def __init__(self, wd_len, wd_hgt):
        self.square = wd_len * wd_hgt


class Room:
    def __init__(self, len_1, len_2, height):
        self.square = 2 * height * (len_1 + len_2)
        self.wd = []

    def add_windoor(self, wd_len, wd_hgt):
        self.wd.append(WindowDoor(wd_len, wd_hgt))

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
            return main_square


r = Room(7, 4, 3.2)
print(r.square)

r.add_windoor(1.5, 1.5)
r.add_windoor(0.7, 2)

print(r.common_square())
