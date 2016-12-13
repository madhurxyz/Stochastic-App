from flask import Flask, render_template
from histogram import get_words_list, create_histogram

app = Flask(__name__)

words_list = get_words_list('holmes.txt')
histogram = create_histogram(words_list)
print histogram

@app.route('/')
def word():
    return "<h1>Hello World</h1>"

if __name__ == '__main__':
    app.run()
