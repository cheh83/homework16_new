import func as t1

print('Вас вiтає бiблiотека фiльмiв')
print(
    'Якщо ви бажаєте шукати фiльм по назвi, то введiть - (title) \nЯкщо ви бажаєте шукати фiльм по жанру, то введiть - (genre)')
zirka = "*" * 100 + "\n"
print(f'{zirka}')

fraza = True
while fraza:
    greetings = input('Введіть (title) чи (genre): ').lower()
    print(f'{zirka}')
    if greetings == "title" or greetings == "genre":
        fraza = False
        if greetings == "title":
            print('Можливо вас зацікавить список фільмів з рейтингом > 9: ')
            t1.func_title_rating()
            print(f'{zirka}')
            film_yes = input("Введіть назву фильму: ").title()
            t1.func_title_film(film_yes)
            if len(t1.title_info) != 0:
                t1.func_title_sort(film_yes)
                print(f'{zirka}')
                num = input('Введіть номер фільму: ')
                print(f'{zirka}')
                t1.func_title_num(int(num))
                break
            else:
                print('немає такого фільму')
        if greetings == "genre":
            print('Жанри: ')
            t1.func_genre_title()
            print(f'{zirka}')
            genre_yes = input("Введіть назву жанру: ").capitalize()
            print(f'{zirka}')
            print('Список фільмів з цим жанром: ')
            t1.func_genre_title_films(genre_yes)
            print(f'{zirka}')
            film_yes = input("Введіть назву фильму з цього жанру: ").title()
            t1.func_title_film(film_yes)
            if len(t1.title_info) != 0:
                t1.func_title_sort(film_yes)
                print(f'{zirka}')
                num = input('Введіть номер фільму: ')
                print(f'{zirka}')
                t1.func_title_num(int(num))
                break
            else:
                print('немає такого фільму')






