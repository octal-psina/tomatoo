import base64
from os import walk
import requests
from bs4 import BeautifulSoup
import lxml
import json


class Napi_tomatto:
    def __init__(self):
        # source
        self.url = 'https://www.rottentomatoes.com/'
        self.next_page = True
        # show category
        self.tv_series = 'tv_series_browse'
        self.movie_home = 'movies_at_home'
        self.movi_theater = 'movies_in_theaters'
        # raiting
        self.audience_rait = 'audience:upright'
        self.criic_rait = '~critics:fresh'
        self.genres = ['action', 'adventure', 'animation', 'anime', 'biography', 'comedy', 'crime', 'documentary', 'drama', 'entertainment', 'faith_and_spirituality', 'fantasy', 'game_show', 'lgbtq', 'health_and_wellness', 'history', 'holiday', 'horror',
                       'house_and_garden', 'kids_and_family', 'music', 'musical', 'mystery_and_thriller', 'nature', 'news', 'reality', 'romance', 'sci_fi', 'short', 'soap', 'special_interest', 'sports', 'stand_up', 'talk_show', 'travel', 'variety', 'war', 'western']
        # sort type
        self.pop_shows = '~sort:popular'
        self.new_shows = '~sort:newest'
        self.headers = {
            'Accept': 'image/avif,image/webp,*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0'
        }

    def link_creator(self, user_choose_category, user_choose_sort_type, user_choose_genre):
        '''create link add filters from user request'''
        # use characters just to format string
        for genre in self.genres:
            print(genre)
        # Category
        if user_choose_category.lower() == 'series':
            a, b, c = self.tv_series, self.audience_rait, self.criic_rait
        elif user_choose_category.lower() == 'at home':
            a, b, c = self.movie_home, self.audience_rait, self.criic_rait
        elif user_choose_category.lower() == 'in theaters':
            a, b, c = self.movi_theater, self.audience_rait, self.criic_rait
        # Genere
        if user_choose_genre in self.genres:
            f = f'~genres:{self.genres[self.genres.index(user_choose_genre)]}'
        # Sort type
        if user_choose_sort_type.lower() == 'popular':
            d = self.pop_shows
        elif user_choose_sort_type.lower() == 'new':
            d = self.new_shows
        elif user_choose_sort_type.lower() == 'no filter':
            d = ""
        link = 'https://www.rottentomatoes.com/napi/browse/{0}/{1}{2}{3}{4}?'.format(
            a, b, c, f, d)
        print(link)
        # return link
        self.url = link

    def napi_appeal(self):
        '''method pars json from request'''
        # This code to get API acsess
        url = self.url
        #url = Napi_tomatto.link_creator(self)
        response = requests.request("GET", url, headers=self.headers)
        data = response.json()

        # with open('hey.json', 'w') as file:
        #    json.dump(a,file, indent=4)
        #file = open("save.json")

        # with open('hey.json','r') as file:
        #    data = json.load(file)

        # print(data['grid']['list'][30])
        print(len(data['grid']['list']))
        movies_list = data['grid']['list']

        counter = 0
        for movie in movies_list:
            counter += 1
            try:
                audiece_r = f"Audience score: {data['grid']['list'][movies_list.index(movie)]['audienceScore']['score']}"
                print(audiece_r)
            except(KeyError):
                pass
            try:
                critics_r = f"Critic score: {data['grid']['list'][movies_list.index(movie)]['criticsScore']['score']}"
                print(critics_r)
            except(KeyError):
                pass
            try:
                tomato_url = f"Url: {data['grid']['list'][movies_list.index(movie)]['mediaUrl']}"
                print(tomato_url)
            except(KeyError):
                pass
            try:
                poster_url = f"Poster: {data['grid']['list'][movies_list.index(movie)]['posterUri']}"
                print(poster_url)
            except(KeyError):
                pass
            try:
                relese_data = data['grid']['list'][movies_list.index(
                    movie)]['releaseDateText']
                print(relese_data)
            except(KeyError):
                pass
            try:
                movie_name = f"Title: {data['grid']['list'][movies_list.index(movie)]['title']}"
                print(movie_name)
            except(KeyError):
                pass
            print(f"{10*'='}{counter}{10*'='}\n")
        try:
            has_next_page = data['pageInfo']['hasNextPage']
            print(has_next_page)
        except(KeyError):
            print("There is no page to open")
        Napi_tomatto.link_povider(self, url, has_next_page)

    def link_povider(self, url, next_page):
        '''Get url and information about existing next page'''
        # It's double method link_creator() not sure if it's realy need
        if url:
            self.url = url
            print(self.url)
        # Chenge class veriable
        if next_page == True:
            self.next_page = True
            # print(self.next_page)
        else:
            self.next_page = False
            #print("There is no page to open")

    def get_next_page(self):
        '''Create next page link'''
        if self.next_page == True:
            #url = Napi_tomatto.link_creator(self)
            url = self.url
            if 'after=' in url:
                part = url[url.find("=") + 1:]
                cut_url = url.partition("=")[0] + "="
                part_bytes = part.encode('ascii')
                part_base64 = base64.b64decode(part_bytes)
                part_number = part_base64.decode("ascii")
                new_number = str(int(part_number) + 30)
                new_number_bytes = new_number.encode('ascii')
                new_number_base64 = base64.b64encode(new_number_bytes)
                link = cut_url + new_number_base64.decode('ascii')
            elif 'after=' not in url:
                link = url + 'after='
                number = '29'
                number_bytes = number.encode('ascii')
                number_base64 = base64.b64encode(number_bytes)
                link += number_base64.decode("ascii")
            print(link)
            self.url = link
        elif self.next_page == False:
            print('There is no page to open.')

'''
n = Napi_tomatto()
user_choose_category = input('tv series/at home/in theaters: ')
user_choose_sort_type = input('popular/new/no filter: ')
user_choose_genre = input('plese choose genre: ')

n.link_creator(user_choose_category, user_choose_sort_type, user_choose_genre)
# n.link_creator()
n.napi_appeal()

next = input('Do you want next page y/n: ')
if next == 'y':
    n.get_next_page()
else:
    print('bye')
'''

# Добавить ссылку на трейлер в ютуб
# Привести весь текст скрипта в норёмальный вид
# Разобраться с передачей ссылки из функции в функцию (Возможно сохранять инфу в json с id чата)
# Сделать функцию которая меняет заголовки для BeautifulSoup
# Сокртить список жанров для филмов
#turn_page = input('Next page y/n: ')
# блок if/else для проверки первая ли это страница
# использовать обрезание строки до определенного знака
# if turn_page == 'y':
#s[s.find(":") + 1:]
# после обрезания декодировать цифру в int (если присутствует)
# закодировать обратно добавить к ссылке


# https://www.rottentomatoes.com/napi/browse/tv_series_browse/audience:upright~critics:fresh~sort:newest?page=1

'''


            try:
                audiece_r = f"Audience score: {data['grid']['list'][movies_list.index(movie)]['audienceScore']['score']}"
                print(audiece_r)
            except(KeyError):
                pass
            try:
                critics_r = f"Critic score: {data['grid']['list'][movies_list.index(movie)]['criticsScore']['score']}"
                print(critics_r)
            except(KeyError):
                pass
            try:    
                tomato_url = f"Url: {data['grid']['list'][movies_list.index(movie)]['mediaUrl']}"
                print(tomato_url)
            except(KeyError):
                pass
            try:
                poster_url = f"Poster: {data['grid']['list'][movies_list.index(movie)]['posterUri']}"
                print(poster_url)
            except(KeyError):
                pass   
            try: 
                relese_data = data['grid']['list'][movies_list.index(movie)]['releaseDateText']
                print(relese_data)
            except(KeyError):
                pass
            try:
                movie_name = f"Title: {data['grid']['list'][movies_list.index(movie)]['title']}"
                print(movie_name)
            except(KeyError):
                pass
            print(f"{10*'='}{counter}{10*'='}\n")

# Add genre to link_creator
'https://www.rottentomatoes.com/napi/browse/tv_series_browse/audience:upright~critics:fresh~genres:mystery_and_thriller~sort:popular?after=Mjk%3D'

genre=[
'action',
'adventure',
'animation',
'anime',
'biography',
'comedy',
'crime',
'documentary',
'drama',
'entertainment',
'faith_and_spirituality',
'fantasy',
'game_show',
'lgbtq',
'health_and_wellness',
'history',
'holiday',
'horror',
'house_and_garden',
'kids_and_family',
'music',
'musical',
'mystery_and_thriller',
'nature',
'news',
'reality',
'romance',
'sci_fi',
'short',
'soap',
'special_interest',
'sports',
'stand_up',
'talk_show',
'travel',
'variety',
'war',
'western',
]
print(genre)




rotten_link = 'https://www.rottentomatoes.com'
the_best = 'audience:upright~critics:certified_fresh~'
genre = 'genres:adventure'
movies_at_home = 'https://www.rottentomatoes.com/browse/movies_at_home/'
tv_series_browse = 'https://www.rottentomatoes.com/browse/tv_series_browse/?page=6'
movies_in_theaters = 'https://www.rottentomatoes.com/browse/movies_in_theaters/'

https://www.rottentomatoes.com/napi/browse/tv_series_browse/audience:upright~critics:fresh?'

https://www.rottentomatoes.com/napi/browse/tv_series_browse/audience:upright~critics:fresh~sort:newest?page=1

https://www.rottentomatoes.com/napi/browse/tv_series_browse/audience:upright~critics:fresh~sort:popular?after=Mjc=

https://www.rottentomatoes.com/napi/browse/movies_in_theaters/?after=Mjc%3D
https://www.rottentomatoes.com/napi/browse/movies/?
'''
