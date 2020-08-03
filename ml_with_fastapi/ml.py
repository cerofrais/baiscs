import spacy


nlp = spacy.load("en_core_web_sm") # pretrained model

# doc = nlp("Apple buys U.K. startup for $1billion")
# for ent in doc.ents:
#     print(ent.text, ent.label_)
