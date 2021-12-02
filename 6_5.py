class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        return('Синяя мажущая паста')
class Pencil(Stationery):
    def draw(self):
        return('Тведрый бледный карандаш')
class Handle(Stationery):
    def draw(self):
        return('Жирный черный маркер')
stat = Stationery('Something')
corvina = Pen('corvina')
stabilo = Pencil('stabilo')
gamma = Handle('gamma')
stat_dict = [stat, corvina, stabilo, gamma]
for i in stat_dict:
    print(i.draw())