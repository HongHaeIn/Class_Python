from recipe import Recipe

class Recipebook:
    #각각의 레시피를 넣어두고 찾아보는 것
    def __init__(self):
        self.recipe_list = []
        self.food_court()
    def add_recipe(self):
        #추가할 레시피 이름을 입력받자
        recipe_name = input('>>레시피 이름을 입력하세요')
        #레시피 이름 중복을 체크하자
        for recipe in self.recipe_list:
            #중복 있으면
            if recipe_name == recipe.name:
                #이미 있다고 알려주자
                print('이미 존재하는 레시피입니다!')

                return
        #새 레시피를 생성하자
        new_recipe = Recipe(recipe_name)
        new_recipe.set_recipe()
            #레시피 리스트에 새 레시피를 추가하자
        self.recipe_list.append(new_recipe)

    def show_all_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'{index+1}번')
            print(recipe)

    def search_recipe(self):
        #찾을 레시피이름을 입력받자
        recipe_name = input('>> 원하는 레시피를 검색하세요: ')
        #(반복문)입력받은 레시피가 레시피모음에 있는지 확인한다
        searched_recipe = []
        for recipe in self.recipe_list:
            #중복이 있으면
            if recipe_name in recipe_name:  # if '부대' in '부대찌개' -> 찾을 수 있음
                #그 레시피를 보여주자
                print(recipe)
                searched_recipe.appand(recipe)
        #(반복문 종료)
        #찾는 레시피가 없다면
        if len(searched_recipe) == 0: #못찾았다는 뜻
            #레시피를 추가할지 물어보자
            choice = input('>> 원하는 레시피가 없습니다 ㅠ 추가하시겠습니까?(1 = 예 / 2 = 아니요)')
            #추가하겠다고 하면
            if choice == '1':
                #레시피 추가하자
                self.add_recipe()
                #추가 안한다고 하면
            else:
                return
    def search_whatin(self):
        pass

        #(재료세트)빈세트생성
        whatin_set=set()
        for recipe in self.recipe_list:
            for whatin in recipe.whatin:
                whatin_set.add(whatin)  #예를 들어 {김치, 두부, 감자} add.두부 -> {두부, 김치, 감자}
        # 모든 재료를 다 보여주자
        for index, whatin in enumerate(whatin_set):
            print(f'{index+1}번. {whatin}')
        #보여준 재료중에 사용할 재료를 고륻자
        num = int(input(">> 사용할 재료 번호를 입력하세요: "))
        use_Whatin = list(whatin_set)[num-1]
        #고른 재료가 포함되는 레시피를 다 보여주자
        for recipe in self.recipe_list:
            if use_Whatin in recipe.whatin:
                print(recipe)

    def food_court(self):
        해인이 = Recipe('케이크')
        해인이.quantity = 1
        해인이.link = 'youtube.com'
        해인이.whatin= {'밀가루':'500', '계란':'100', '생크림':'200', '딸기':300}
        해인이.info = "맛있게 드세용"
        해인이.time = 60
        self.recipe_list.append(해인이)
        서연이 = Recipe('삼겹살 볶음밥')
        서연이.quantity = 1
        서연이.whatin= {'삼겹살':'100', '김치':'100', '밥':'100'}
        서연이.link = 'youtube.com'
        서연이.info = "맛있게 드세용"
        서연이.time = 60
        self.recipe_list.append(서연이)
    def __str__(self):
        pass
