from whoosh.index import open_dir
from whoosh import qparser
from whoosh import highlight
import time
from pprint import pprint
import re
from flask import current_app
before=re.compile('&lt;a&gt;')
after=re.compile('&lt;/a&gt;')
final=re.compile('&lt;/a|a&gt;|&lt;a')
def full_textsearch(key,top,surround):
    ix = open_dir(current_app.config['engine'],"engine2") #作成したインデックスファイルのディレクトリを指定
    with ix.searcher() as searcher:
        parser = qparser.QueryParser("content", ix.schema)

        op = qparser.OperatorsPlugin(And="&", Or="\\|", Not="~")
        parser.replace_plugin(op) #opをセット
        words = key
        start = time.time()
        words = words.split()
        words = "".join(words)
        query = parser.parse(words)
        results = searcher.search(query, limit=50)
        # for result in results:asae_iku来る
        #     print(result.highlights('content'))
        results.fragmenter.maxchars=50
        results.fragmenter.surround=surround
        results.order = highlight.SCORE
        pprint(results)
        search_result=[]
        for fragment in results:
            dict={}

            dict['context']=final.sub('',after.sub('</a>',before.sub('<a>',fragment.highlights('content',top=top)),))
            dict['title']=fragment['title']
            dict['writer']=fragment['writer']
            search_result.append(dict)

            print('#'*30,'\n')
        print("計%d記事" %len(results))
        print(str((time.time() - start)*10000//10)+"ms") #時間計測用
        return search_result

