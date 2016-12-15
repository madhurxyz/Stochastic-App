from flask import Flask, render_template
from histogram import get_words_list, create_histogram
from stochastic import get_prob_word, get_count
import os

app = Flask(__name__)

words_list = get_words_list('holmes.txt')
histogram = create_histogram(words_list)
count = get_count(histogram)

@app.route('/')
def word():
    prob_word = get_prob_word(histogram, count)
    return '''
<!doctype html>
<html>
  <head>
    <title>Random Word</title>
    <link rel="stylesheet" href="static/style.css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet">
  </head>
  <body>
    <div class="container">
      <h1>''' + prob_word + '''</h1>
</div>
</body>
</html>
'''

if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run()
