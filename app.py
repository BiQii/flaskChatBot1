
import nltk
import emoji
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    tokens = nltk.word_tokenize(userText)
    nlist = []
    x = 0

    while x < len(tokens):

        text =  tokens[x]

        if (x + 1) < len(tokens):
            next_text = tokens[x + 1]
        else:
            next_text = ""

        new_token = ":" + text.lower() + ":"
        replace = emoji.emojize(new_token)

        if replace is not new_token:
            nlist.append(replace)
            nlist.append(" " * len(replace))
            x += 1
        else:
            two_text = text.lower() + "_" + next_text.lower()
            two_token = ":" + two_text + ":"
            two_replace = emoji.emojize(two_token)
            if two_replace is not two_token:
                nlist.append(two_replace)
                nlist.append(" " * len(two_replace))
                x += 2
            else:
                nlist.append(text)
                nlist.append(" ")
                x += 1

    new_sentence = "".join(nlist)
    return new_sentence
    

if __name__ == '__main__':
    app.run()
