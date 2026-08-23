import re
import requests
import csv
from lxml import html

# 定义常量
MOVIE_LIST_FILE = "csv_data/movie_list2.csv"
TMDB_BASE_URL = "https://www.themoviedb.org"    # 网站基础链接
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated" # 高分电影链接(第一页数据)
TMDB_TOP_URL_PAGE = "https://www.themoviedb.org/discover/movie/items"   # 分页请求的地址

# 清洗数据: 年份 (xxxx) -> xxxx
def get_movie_year(movie_years: list) -> str:
    year =  movie_years[0].strip() if movie_years else ''
    if year:
        year_match = re.search(r"\d{4}", year)
        return year_match.group() if year_match else ''
    else:
        return year

# 清洗数据: 上映时间 xxxx-xx-xx (xx) -> xxxx-xx-xx
def get_movie_start(movie_starts: list) -> str:
    start = movie_starts[0].strip() if movie_starts else ''
    if start:
        start_match = re.search(r"\d{4}-\d{2}-\d{2}", start)
        return start_match.group() if start_match else ''   # group()将match对象转成str字符串
    else:
        return start

# 清洗数据: 时长 xxh xxm -> xxm
def get_movie_times(movie_times: list) -> str:
    time = movie_times[0].strip() if movie_times else ''
    if not time:
        return time
    # 获取小时和分钟
    hour = re.search(r"(\d+)h", time)
    mint = re.search(r"(\d+)m", time)
    # 判断是否有值
    hour_res = int(hour.group(1)) if hour else 0    # search 返回的是match对象会匹配到h,用group()转换为xxh,所有使用group(1)指定第一组即h前面的数字
    min_res = int(mint.group(1)) if mint else 0
    if not min_res and not hour_res:
        return ''
    #总时长
    movie_time = hour_res * 60 + min_res
    return f"{movie_time}m"

# 根据电影详情链接获取电影详情数据
def get_movie_info(movie_info_url):
    # 1.获取电影详情响应
    response_movie_info = requests.get(movie_info_url, timeout=60)
    print(f"获取{movie_info_url}电影详情信息...")
    # 2.获取信息
    doc_info = html.fromstring(response_movie_info.text)
    movie_names = doc_info.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")    # 电影名
    movie_years = doc_info.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")    # 电影年份
    movie_starts = doc_info.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='release']/text()")    # 电影上映时间
    movie_tags = doc_info.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='genres']/a/text()")    # 电影类型
    movie_times = doc_info.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='runtime']/text()")    # 电影时长
    movie_scores = doc_info.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")    # 电影评分
    movie_languages = doc_info.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")    # 电影语言
    movie_directors = doc_info.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol//p[@class='character' and contains(text(), 'Director')]/preceding-sibling::p[1]/a/text()")    # 电影导演
    movie_authors = doc_info.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")    # 电影作者
    movie_slogans = doc_info.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[@class='tagline']/text()")    # 电影slogan
    movie_descriptions = doc_info.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")    # 电影简介

    # 3.构建成字典值
    movie_info = {
        "电影名": movie_names[0].strip() if movie_names else '',
        "年份": get_movie_year(movie_years),  # 清洗(1994) -> 1994
        "上映时间": get_movie_start(movie_starts),    # 清洗 1994-09-23 (US) -> 1994-09-23
        "类型": ','.join(movie_tags) if movie_tags else '',
        "时长": get_movie_times(movie_times),     # 清洗 2h22m -> 142m 时长改成分钟
        "评分": movie_scores[0].strip() if movie_scores else '',
        "语言": ','.join(movie_languages) if movie_languages else '',
        "导演": ','.join(movie_directors) if movie_directors else '',
        "作者": ','.join(movie_authors) if movie_authors else '',
        "宣传语": movie_slogans[0].strip() if movie_slogans else '',
        "简介": movie_descriptions[0].strip() if movie_descriptions else '',
    }
    return movie_info

# 保存电影详情信息到csv文件
def save_all_movies(all_movies_info):
    with open(MOVIE_LIST_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["电影名","年份","上映时间","类型","时长","评分","语言","导演","作者","宣传语","简介"])
        writer.writeheader()
        writer.writerows(all_movies_info)

# 主函数,定义核心逻辑
def main():
    all_movies_info = []    # 保存所有电影数据
    # 请求前100条
    for page_number in range(1, 6):
        if page_number == 1:
            # 第一页的地址
            request_url = TMDB_TOP_URL
            response = requests.get(request_url, timeout=60)
        else:
            request_url = TMDB_TOP_URL_PAGE
            response = requests.post(request_url,
                                     data=f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_number}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-02-21&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400",
                                     timeout=60)
        # 1.发送请求,获取高分电影榜单数据

        print(f"发送请求...获取第{page_number}页数据")

        # 2.解析响应的数据,获取电影列表信息
        doc = html.fromstring(response.text)
        movie_list =doc.xpath("//*[@class='media-list-results contents']//div[@class='relative w-full']")

        # 3.遍历电影列表获取详情链接
        for movie in movie_list:
            movie_urls = movie.xpath("./a/@href")
            if movie_urls:
                # 拼接电影详情url
                movie_info_url = TMDB_BASE_URL + movie_urls[0]
                # 发送请求,获取电影详情数据
                movie_info = get_movie_info(movie_info_url)
                all_movies_info.append(movie_info)

    # 4.保存数据到csv文件
    print("保存数据到csv文件...")
    save_all_movies(all_movies_info)
if __name__ == '__main__':
    main()