class Drink:
    _CUPS = ('레귤러', '점보')
    _ICES = ('0%', '50%', '100%', '150%')
    _SUGARS = ('0%', '50%', '100%', '150%')
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0 #Dring._CUPS[0] => 레귤러
        self.ice = 2 #Dring._ICES[2] => 100
        self.sugar = 2 #Dring._SUGARS[2] => 100

    def set_cup(self):
        for index, cup in enumerate(Drink._CUPS):
            print(f'{index+1}: {cup}')

        cup = input('컵사이즈를 선택하세요: ')
        if cup == '':
            self.cup = 0
        else:
            cup = int(cup) -1
            self.cup = cup

    def set_ice(self):
        for index, ice in enumerate(Drink._ICES):
            print(f'{index + 1}: {ice}')
        ice = input('얼음량을 선택하세요: ')
        self.ice = 2 if ice == '' else self.ice = int(ice) - 1

    def set_sugar(self):
        for index, sugar in enumerate(Drink._SUGARS):
            print(f'{index + 1}: {sugar}')
        sugar = input('당도를 선택하세요: ')
        self.sugar = 2 if sugar == '' else self.sugar = int(sugar) - 1

    def order(self):
        self.set_cup()






class Coffee(Drink):
    pass

해인이꺼 = Drink('초코버블티', 3300)
해인이꺼.order()
print(해인이꺼)

class Bubbletea:
    _PEARL = ('타피오카', '코코', '젤리', '알로에')
    def __init__(self, name, pearl):
        super().__init__(name, pearl)
        self.pearl = 0

    def set_pearl(self):
        for index, pearl in enumerate(Bubbletea._PEARL):
            print(f'{index + 1}: {pearl}')
        ice = input('펄을 선택하세요: ')
        self.pearl =3  if ice == '' else self.pearl = int(pearl) - 1

    def __str__(self):
        return super().__str__() + f'\t펄 : {Bubbletea._PEALRS[self.pearl]}'

    def order(self):
        super().order()
        self.set_pearl()


class Order:
    def __init__(self):
        self.menu = []
        self.init_menu()
        self.order_menu = []

    def init_menu(self):
        drink1 = Coffee('아메리카노', 1800)
        drink2 = Bubbletea('하동녹차오레오', 3300)
        drink3 = Bubbletea('딸기요거트', 3400)
        self.menu.append(drink1)
        self.menu.append(drink2)
        self.menu.append(drink3)

    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index + 1}: {drink}')

    def order_drink(self):
        self.show_menu()
        while True:
            drink = input('메뉴를 선택하세요: ')
            self.input(drink) -1
            new_drink = self.menu[drink]
            new_drink.order()
            self.order_menu.append(new_drink)
            is_add = input('더 주문하실까요?(N: 끝): ')
            if is_add == 'n':
                break
        print(self.order_menu)
        print(self)

    def sum_price(self):
        total_price = 0
        for drink in self.order_menu:
            total_price += drink.price
        return  total_price
        return 0

    def __str__(self):
        s = '-' * 20 + '주문 내역' + '-' * 20
        for drink in self.order_menu:
            s += drink + '\n'
        s += f'주문한 음료수 개수: {len(self.order_menu)}개\n'
        s += f'총 가격: {self.sum_price()}원'

        return  s

order = Order()
order.order_drink()