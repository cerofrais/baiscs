from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from ml import nlp

app = FastAPI()

@app.get("/")
def read_main():
    return ("Message : Hello World")

class Article(BaseModel):
    content: str
    any_comments: list = []
    comments: List[str] = []

@app.get("/article/{article_id}")
def analyze_article (article_id:int,q:str=None):
    """Eample of path variable as input, article_id is required and q is optional

    """
    # also convert string to integer as it expects an interger
    cnt =0
    if q:
        doc = nlp(q)
        cnt = len(doc.ents)

    return {"article_id":article_id, "q":q, "count": cnt }

@app.post("/article_2/")
def analyze_article2(body:dict):
    """example to input data using body

    """
    return body


@app.post("/article_3/")
def analyze_article3(article: Article):
    """example to take input using a defined basemodel 

    """

    return {"message": article.content, "comments": article.comments}

@app.post("/article_4")
def analyze_article4(article: Article):
    """example to  run ML model of input given by body

    """
    ents =[]
    doc = nlp(article.content)
    for ent in doc.ents:
        ents.append({"text":ent.text,"label":ent.label_})

    return {"message": article.content,"comments": article.comments, "ents": ents}

@app.post("/article_5")
def analyze_article5(articles: List[Article]):
    """example to  run *ML model* of **List of inputs**
        * comment1
        * comment2

    """
    ents =[]
    for article in articles:
        doc = nlp(article.content)
        for ent in doc.ents:
            ents.append({"text":ent.text,"label":ent.label_})

    return {"message": article.content,"comments": article.comments, "ents": ents}