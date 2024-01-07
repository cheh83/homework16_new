import csv

file = "filmsDZ16.csv"

with open(file, newline='') as csvfile:
    reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))

    title_info = []

    def func_title_rating():
        for film in reader:
            if film['rating'] > '9':
                print(film["title"])

    def func_title_film(film_yes):
        for i, film in enumerate(reader):
            if film["title"].startswith(film_yes):
                title_info.append(film["title"])
        return True


    def func_title_sort(film_yes):
        for i, film in enumerate(reader):
            if film["title"].startswith(film_yes):
                print(f'Назва фільму: ({film["title"]})\tв базі є такий фільм під номером:-({i + 1})')
        return True


    def func_title_num(num):
        for i, film in enumerate(reader):
            if num == i+1:
                print('назва фільму: ', film['title'], ', рік: ', film['year'], ', опис: ', film['description'])
        return True


    def func_genre_title():
        genres = []
        for i in reader:
            i['gen'] = eval(i['gen'])
            for j in i['gen']:
                genres.append(j['genre'])
        genres = set(genres)
        for gen in genres:
            print(gen)
        return True


    def func_genre_title_films(genre_yes):
        for d in reader:
            for j in d['gen']:
                if j['genre'] == genre_yes:
                    print(d['title'])

        return True