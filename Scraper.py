from bs4 import BeautifulSoup
import requests
import os
import csv
import time
import random

DIRNAME = os.path.dirname(os.path.realpath(__file__))

REPLACE = ['<div class="storytext xcontrast_txt nocopy" id="storytext">', '<p style="text-align:center;">', '<div>', '</div>', '</p>', '<p>', '</em>', '<em>', '<strong>', '</strong>', '<hr', '/>', 'size="1"', 'noshade=""']

cookie = "cookies=yes; cf_clearance=efcyecP4m3p.2pk51CgiULwpCApJJD97r6pA.vaNZ6E-1710271437-1.0.1.1-2AMivVlFSO06iNSnGUhZAHNXMYaCmo6RBvLcDtNkQOT32gqZ3u0Pz53NICRqCuccVq7yXW5gbrODJvOjS.ovvQ; __cf_bm=.rn2Q_rSbOVjicGb._xxxCf6el7wNE3dhNrRp4RlLw4-1710277917-1.0.1.1-2cRNcyo6Qs0R043I4l1Sa9mvNfEdguSHOlHQlYDdfeMN6H.UjislvSqElYHp6Tl2E6ZlZDxz1H0SfRoXYfKF2Q"

header1 = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control':'max-age=0',
    'Cookie': f'{cookie}',
    'Sec-Ch-Ua':'"Not A(Brand";v="99", "Opera GX";v="107", "Chromium";v="121"',
    'Sec-Ch-Ua-Arch':'"x86"',
    'Sec-Ch-Ua-Bitness':'"64"',
    'Sec-Ch-Ua-Full-Version':'"107.0.5045.60"',
    'Sec-Ch-Ua-Full-Version-List':'"Not A(Brand";v="99.0.0.0", "Opera GX";v="107.0.5045.60", "Chromium";v="121.0.6167.186"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Model':'""',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Ch-Ua-Platform-Version':'"15.0.0"',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'none',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0'
}

# Scrape out Story text
def StoryScraper(soup):
    StoryUnfixed = soup.find(attrs={'id':'storytext'})
    StoryFixedNoARR = str(StoryUnfixed).replace('</p><p>', '[/][/]')

    for x in REPLACE:
        StoryFixedNoARR = StoryFixedNoARR.replace(x, '')

    StoryFixed = StoryFixedNoARR.split('[/][/]')

    del StoryFixedNoARR, StoryUnfixed, soup

    return StoryFixed

# Go and downloadwebsite
def GoToWebsite(link):
    PageToScrape = requests.get(f'https://www.fanfiction.net{link}', headers=header1)

    if PageToScrape.status_code == 200:
        soup = BeautifulSoup(PageToScrape.text, "html.parser")

        Story = StoryScraper(soup)
        return Story
    else:
        print(f'StatusCode = {PageToScrape.status_code} & {PageToScrape.headers}')
        return PageToScrape.status_code


with open('FilteredData.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["Promt", "Responce"])

def main():
    listofcsv = os.listdir(f'{DIRNAME}/Scrape')
    for x in listofcsv:
        file = open(f'{DIRNAME}/Scrape/{x}')
        type(file)
        csvreader = csv.reader(file)

        header = []
        header = next(csvreader)

        for row in csvreader:
            with open('FilteredData.csv', 'a') as writefile:
                Story = GoToWebsite(row[0])

                if Story == 429:
                    time.sleep(65)

                writer = csv.writer(writefile)
                print(f'Bandom: {row[0]}')

                StringStory = ''
                for x in Story:
                    StringStory += x.replace(',', '_')

                writer.writerow([f'write {row[1]} fanfic about {row[2]}', StringStory])

main()