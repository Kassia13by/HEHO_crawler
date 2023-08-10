import re
import time
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

def extract_id_from_href(href):
    # Use regular expression to extract the number from the href
    match = re.search(r'\d+', href)
    if match:
        return int(match.group())
    else:
        return None

def single_page_crawler(url, output_file_dir):
    '''
    This crawls the webpage of 健康迷思 board from Heho.com.tw website. 
    In the 健康迷思 board, a total of 192 pages are listed. 
    In this function, it retrieves all the 10 articles displayed on one page, 
    transform the extracted information into a dataframe, 
    and write out into a tab-delimited file.
    '''

    # url = 'https://heho.com.tw/archives/category/health-care/health-myths/page/1'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    # 抓取文章標題列表 (裡面只有標題和文章連結，並未有文章內容)
    news_containers = html_soup.find_all('a', class_='plain')

    # 故需先抓取每一篇文章連結後，再進去抓內文。
    article_links_set = set()  # Use a set to store unique article links

    for i in news_containers:
        article_links_set.add(i['href'])

    article_links = list(article_links_set)  # Convert set back to a list

    # 寫個 loop 抓取每一篇文章標題、內容和摘要
    articles_dict = {'id': [], 'time': [], 'link': [], 'title': [], 'content': [], 'summary': []}

    for article_num, link in enumerate(article_links):
        try:
            article_response = get(link)
            article_html_soup = BeautifulSoup(article_response.text, 'html.parser')
            title = article_html_soup.find_all('h1', class_='entry-title')[0].text  # article title
            match = re.search(r'\d+', link)
            if match:
              id = int(match.group())

            try:
                time = article_html_soup.find_all('time', class_='entry-date published')[0].text  # article time
            except:
                time = article_html_soup.find_all('time', class_='entry-date published updated')[0].text  # article time updated

            entry_content = article_html_soup.find('div', class_='entry-content')
            blockquote = entry_content.find('blockquote', class_='wp-block-quote')
            summary = blockquote.get_text().strip() if blockquote else None

            # Extract content in the desired format
            article_content = ""
            for tag in entry_content.contents:
                if tag.name == 'h2' and tag.has_attr('class') and 'wp-block-heading' in tag['class']:
                    # Keep the <h2> tag as it is
                    article_content += str(tag)
                elif tag.name == 'p':
                    # Add the text content of <p> tags
                    article_content += tag.get_text()

            # Remove unwanted elements
            article_content = re.sub(r'延伸閱讀.*', '', article_content, flags=re.DOTALL)
            article_content = re.sub(r'圖、.*|文/.*|文／.*|文 /.*|圖/.*|圖／.*|圖 /.*|文、.*|圖、.*', '', article_content)

            # Save the extracted articles into a dictionary
            articles_dict['id'].append(id)
            articles_dict['title'].append(title)
            articles_dict['time'].append(time)
            articles_dict['content'].append(article_content.strip())
            articles_dict['link'].append(link)
            articles_dict['summary'].append(summary)

            print('succeed: the', article_num + 1, 'th article')
            articles_df = pd.DataFrame.from_dict(articles_dict)
            articles_df.to_csv(output_file_dir, sep='\t', index_label=False, index=False)

        except:
            print('** FAIL LINK **', link, ': please check id, time, title, content, and summary')
            next
    

def multiple_page_crawler(target_board_link, page_numbers, output_file_dir):

    all_page_links = [target_board_link + '/page/' +
                      str(page_number + 1) for page_number in range(page_numbers)]

    for page_num, link in enumerate(all_page_links):
        print('========= crawling page: ', page_num + 1, '=========')
        output_file = output_file_dir + \
            'heho_page' + str(page_num + 1) + '.txt'
        single_page = single_page_crawler(link, output_file)
        print('.... sleep for 60 seconds ....')
        time.sleep(60)


if __name__ == '__main__':
    # # ====== extract single article page =======
    # url = 'https://heho.com.tw/archives/category/ask-experts/doctor/page/1'
    # output_file_dir = '../data/heho_page1.txt'
    # single_page_crawler(url, output_file_dir)

    # ====== extract multiple pages =======
    target_board_link = 'https://heho.com.tw/archives/category/health-care/health-myths'
    pages = 192  # the number of pages to be extracted
    output_file_dir = '../data/crawled_heho_myths/'
    multiple_page_crawler(target_board_link, pages, output_file_dir)



