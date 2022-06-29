from flask import Flask, request
import ghhops_server as hs

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/scrape",
    name="scrape",
    description="Filters HTML by tags",
    inputs=[
        hs.HopsString("HTML parser", "HTML", "Enter a url to scrape from"),
        # hs.HopsString("Main text", "Main text", "what is the main text div"),
        hs.HopsString("Tags", "Tags", "tag to search for"),
        hs.HopsString("All Tags", "All Tags", "Find all tags within html")
    ],
    outputs=[
        hs.HopsString("Result")
    ],
)
@app.route('/urlend')
def scrape(link, tag, tags):
    from ast import Try
    from bs4 import BeautifulSoup
    import requests
    import csv

    source = requests.get(link)
    soup = BeautifulSoup(source.text, "html.parser")
    # main = soup.find(main_text).get_text()

    match = soup.find(tag).text
    all_tags = soup.find_all(tags)
    result = match, all_tags
    print(list(result))

    return list(result)
    # soup = BeautifulSoup(source, 'lxml')
    # # print(soup.prettify())

    # csv_file = open('cms_scrape.csv', 'w')

    # csv_writer = csv.writer(csv_file)
    # csv_writer.writerow(['headline', 'summary', 'video_link'])

    # for article in soup.find_all('article'):
    #     headline = article.h2.a.text
    #     print(headline)

    #     summary = article.find('div', class_='entry-content').p.text
    #     print(summary)

    #     try:
    #         vid_src = article.find('iframe', class_='youtube-player')['src']

    #         vid_id = vid_src.split('/')[4]
    #         vid_id = vid_id.split('?')[0]

    #         yt_link = f'https://youtube.com/watch?v={vid_id}'
    #     except Exception as e:
    #         yt_link = None

    #     print()
    #     csv_writer.writerow([headline, summary, yt_link])

    # csv_file.close()


if __name__ == "__main__":
    app.run()
