
from whoosh.index import create_in
from whoosh.fields import *
path = '/Users/silky/Documents/GitHub/textnovel/txt/'
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
ix = create_in(path, schema)
writer = ix.writer()
# writer.add_document(title=u"First document", path=u"/a",
#                      content=u"This is the first document we've added!")
# writer.add_document(title=u"Second document", path=u"/b",
#                     content=u"The second one is even more interesting!")
writer.commit()
from whoosh.qparser import QueryParser
import os
import re



for r, d, f in os.walk(path):
    for file in f:
        a=file
        file = path + '/' + file
        with open(file) as novel:
            noveltext=novel.readlines()
            writer.add_document(title=a, path=file,
                            content=noveltext)


with ix.searcher() as searcher:
     query = QueryParser("content", ix.schema).parse("first")
     results = searcher.search(query)
     results[0]

{"title": u"First document", "path": u"/a"}