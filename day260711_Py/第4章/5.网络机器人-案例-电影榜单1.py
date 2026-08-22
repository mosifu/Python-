import requests
import csv
from lxml import html

# 定义网站常量
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"

# 根据电影详情链接获取电影详情数据
def get_movie_info(movie_info_url):
    pass

# 保存电影详情信息到csv文件
def save_all_movies(all_movies_info):
    pass

# 主函数,定义核心逻辑
def main():
    # 1.发送请求,获取高分电影榜单数据
    response = requests.get(TMDB_TOP_URL, timeout=60)

    # 2.解析响应的数据,获取电影列表信息
    doc = html.fromstring(response.text)
    movie_list =doc.xpath("//*[@class='media-list-results contents']//div[@class='relative w-full']")

    # 3.遍历电影列表获取详情链接
    all_movies_info = []
    for movie in movie_list:
        movie_urls = movie.xpath("./a/@href")
        if movie_urls:
            # 拼接电影详情url
            movie_info_url = TMDB_BASE_URL + movie_urls[0]
            # 发送请求,获取电影详情数据
            movie_info = get_movie_info(movie_info_url)
            all_movies_info.append(movie_info)

    # 4.保存数据到csv文件
    save_all_movies(all_movies_info)
if __name__ == '__main__':
    main()