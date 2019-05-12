from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# API キーの情報
# keyword='cat'
# num='3'
def image_get(keyword,num):
# if True:
    key = "119aff97d6cf86395bca3f235ea32bd8"
    secret = "1ccc399002989198"

    # 重要：リクエストを送るタイミングが短すぎると画像取得先のサーバを逼迫してしまうか、
    # スパムとみなされてしまう可能性があるので、待ち時間を 1 秒間設ける。
    wait_time = 1

    # コマンドライン引数の 1 番目の値を取得
    animalname = keyword
    # 画像を保存するディレクトリを指定
    savedir = "./" + animalname

    # FlickrAPI にアクセス

    # FlickrAPI(キー、シークレット、データフォーマット{json で受け取る})
    flickr = FlickrAPI(key, secret, format='parsed-json')
    result = flickr.photos.search(
        text=animalname,
        per_page=num,
        media='photos',
        sort='relevance',
        safe_search=1,
        extras='url_q, licence'
    )

    # 結果を表示
    photos = []
    # pprint(result['photos'])

    for i,a in zip(result['photos']['photo'],range(len(result['photos']))):
        # print(i)
        if 'url_q'in i :
            photos.append(i['url_q'])

    # pprint(photos)



    return photos


