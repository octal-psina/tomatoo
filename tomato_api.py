import base64
from os import walk
import requests
from bs4 import BeautifulSoup
#import lxml
import random
import json


class Napi_tomatto:
    def __init__(self):
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
        user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0', 'Mozilla/5.0 (X11; Linux x86_64; rv:112.0) Gecko/20100101 Firefox/112.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.69 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.10) Gecko/20100101 Firefox/102.10']
        self.headers = {
            'Accept': 'image/avif,image/webp,*/*',
            'User-Agent': random.choice(user_agents)
        }

    def link_creator(self, user_choose_category, user_choose_sort_type, user_choose_genre):
        '''create link add filters from user request'''
        # use characters just to format string
        print(user_choose_category, user_choose_sort_type, user_choose_genre)
        # Category
        if user_choose_category == 'tv series':
            a, b, c = self.tv_series, self.audience_rait, self.criic_rait
        elif user_choose_category == 'movie at home':
            a, b, c = self.movie_home, self.audience_rait, self.criic_rait
        elif user_choose_category == 'movie in theater':
            a, b, c = self.movi_theater, self.audience_rait, self.criic_rait
        # Genere
        if user_choose_genre.lower() in self.genres:
            f = f'~genres:{self.genres[self.genres.index(user_choose_genre)]}'
        # Sort type
        if user_choose_sort_type.lower() == 'popular':
            d = self.pop_shows
        elif user_choose_sort_type.lower() == 'new':
            d = self.new_shows
        # elif user_choose_sort_type.lower() == 'no filter':
            #d = ""
        link = 'https://www.rottentomatoes.com/napi/browse/{0}/{1}{2}{3}{4}?'.format(
            a, b, c, f, d)
        # print(link)

        return link

    def napi_appeal(self, source):  # source
        '''method pars json from source'''
        # This code to get API acsess
        # use url
        response = requests.request("GET", source, headers=self.headers)
        data = response.json()
        # use json
        # with open('hey.json', 'w') as file:
        #    json.dump(data,file, indent=4)
        #file = open("save.json")

        # with open('hey.json','r') as file:
        #  data = json.load(file)

        # print(data['grid']['list'][30])
        # print(len(data['grid']['list']))
        movies_list = data['grid']['list']

        list_of_output = []
        counter = 0
        for movie in movies_list:
            list_movie_info = []
            counter += 1
            try:
                movie_name = {data['grid']['list']
                              [movies_list.index(movie)]['title']}
                mov_nam_4_trailer = (str(movie_name).replace(
                    ' ', '+')).replace("'", "").replace("{", "").replace("}", "")
                complite_movie_name = f"Title: {data['grid']['list'][movies_list.index(movie)]['title']}"
                #trailer = 'Trailer may be here: https://www.youtube.com/results?search_query={0}'.format(mov_nam_4_trailer)
                # print(movie_name)
                list_movie_info.append("\n" + complite_movie_name)
                # list_movie_info.append("\n"+trailer)
            except(KeyError):
                pass
            try:
                audiece_r = f"Audience score: {data['grid']['list'][movies_list.index(movie)]['audienceScore']['score']}"
                # print(audiece_r)
                list_movie_info.append("\n" + audiece_r)
            except(KeyError):
                pass
            try:
                critics_r = f"Critic score: {data['grid']['list'][movies_list.index(movie)]['criticsScore']['score']}"
                # print(critics_r)
                list_movie_info.append("\n" + critics_r)
            except(KeyError):
                pass
            # try:
            #   tomato_url = f"Url: {data['grid']['list'][movies_list.index(movie)]['mediaUrl']}"
            #   print(tomato_url)
            #   list_movie_info.append("\n"+tomato_url)
            # except(KeyError):
            #    pass
            try:
                relese_data = data['grid']['list'][movies_list.index(
                    movie)]['releaseDateText']
                # print(relese_data)
                list_movie_info.append("\n" + relese_data)
            except(KeyError):
                pass
            try:
                poster_url = f"Poster: {data['grid']['list'][movies_list.index(movie)]['posterUri']}"
                list_movie_info.append("\n" + poster_url)
            except(KeyError):
                pass
            list_movie_info.append("\n" + f"{10*'='}{counter}{10*'='}\n")
            list_of_output.append(list_movie_info)
        try:
            has_next_page = data['pageInfo']['hasNextPage']
            list_of_output.append(has_next_page)
        except(KeyError):
            has_next_page = False
            list_of_output.append(has_next_page)
        return list_of_output

    def get_next_page(self, source):
        '''Create next page link'''
        url = source
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
        return link

#n = Napi_tomatto()
# appeal=n.napi_appeal()
# for film in appeal:
#    for f in film:
#        print(f)
# print(appeal)
