import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1

    title_list = []
    href_list = []
    magnet_list = []
    final_list = [[title_list],[href_list],[magnet_list]]

    f = []

    compare_list = []
    for num in range(100):

        f = '('+ str(num)+')'
        compare_list.append(f)



    while page <= max_pages:
        url = "http://kickass.to/movies/" + str(page)
        source_code = requests.get(url)
        # just get the code, no headers or anything
        plain_text = source_code.text
        # BeautifulSoup objects can be sorted through easy
        soup = BeautifulSoup(plain_text)



        #    soup.find("li", { "class" : "test" },recursive=False)
        #    soup.find_all("li", { "class" : "test" },recursive=False)


        for link in soup.findAll({'class': 'cellmainlink'}):

                href = str(link.get('href'))
                href = href.replace('./','/')
                href = href.replace('./','/')

#                href = 'http://www.tosarang.net' + str(href)
                title = link.string  # just the text, not the HTML

                magnet = get_single_item_data(href)

                title_list.append(title)


                print(title)
    # Beneath the lines, only connected with display

                if title not in compare_list:
                    print(title)
                    print(href)
                    print(magnet)
                    print('\n')






        page += 1



'''
                for i in range(len(title_list)):
                    if title_list[i] != "(1)" and title_list[i] != "(2)" and title_list[i] != "(3)":
                        print(final_list[i])
'''







'''
            t_list = [title,href,magnet]
            print(t_list)

            torrent_list = open('torrent_list.txt','w')
            torrent_list.write('title \n')
            torrent_list.write('href \n')
            torrent_list.write('magnet \n')
            torrent_list.close()
'''






'''

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    # if you want to gather information from that page
    for item_name in soup.select("td.view_file a span"):
#        print(item_name.string)
    # if you want to gather links for a web crawler


        return(item_name.string)
'''

'''
    for link in soup.findAll('a'):
        href = "http://www.tosarang.net" + link.get('href')
        print(href)
'''
trade_spider(1)


