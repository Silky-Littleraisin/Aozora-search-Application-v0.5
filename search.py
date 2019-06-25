import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import MeCab
from .db import get_db
from .search_engine import full_textsearch

bp=Blueprint('search',__name__,url_prefix='/search')

@bp.route('/key=<keyword>',methods=('GET','POST'))
def result(keyword):
    db = get_db()
    List_writer=[]
    List_work=[]
    List_free=[]
    keyword=keyword.rstrip()
    m = MeCab.Tagger("-Ochasen")
    for chunk in m.parse(keyword).splitlines()[:-1]:
        word = chunk.rstrip().split('\t')[0] #分かち書きされた語
        proto = chunk.rstrip().split('\t')[2] #上の語の品詞
        word=word.rstrip()
        # a='%'+word+'%'
        # print('a',a)

        writers = db.execute(
            'SELECT 人物ID,著者名 FROM works WHERE 著者名 like ?',('%'+word+'%',)
        ).fetchall()
        works=db.execute(
            'SELECT 人物ID,著者名,作品ID,作品名 FROM works WHERE 作品名 like ?',('%'+word+'%',)
        ).fetchall()
        for writer in writers:
            tem=list(writer)
            print(List_writer)
            if not len(List_writer)or tem[1]!=List_writer[-1][1] :
                tem.append('https://www.aozora.gr.jp/index_pages/person'+str(int(writer[0]))+'.html')
                writer=tuple(tem)
                List_writer.append(writer)
        for work in works:
            tem=list(work)
            tem.append('https://www.aozora.gr.jp/cards/'+work[0]+'/card'+str(int(work[2]))+'.html')
            work=tuple(tem)
            List_work.append(work)
        Orign_free=full_textsearch(proto,2,10)
        for free in Orign_free:
            writer=free['writer'].rstrip()
            work=free['title'].rstrip()
            cards=db.execute(
            'SELECT 人物ID,作品ID FROM works WHERE 著者名 like ? AND 作品名 like ?',('%'+writer[-1]+'%','%'+work+'%',)
            ).fetchone()
            print(writer[-1],'cards',cards)
            # card=cur.execute('SELECT 作品ID FROM works WHERE 作品名 like ?',('%'+work+'%',)
            # ).fetchone()
            # print('card',card[0])
            card_t=cards[1]
            cards_t=cards[0]
            free['url']='https://www.aozora.gr.jp/cards/'+cards_t+'/card'+str(int(card_t))+'.html'
            List_free.append(free)





    return render_template('search/Search_result.html',list_writer=List_writer,list_work=List_work,list_free=List_free)
