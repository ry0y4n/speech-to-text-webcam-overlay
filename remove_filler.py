import cotohappy
from flask import Flask, request
import re

coy = cotohappy.API()
text = "えーっと、それでは今からプレゼンを、始めさせていただこうかと思います。"
do_segment = True
remove_filler_li = coy.remove_filler(text, do_segment) 
for remove_filler in remove_filler_li:
    remove_filler = str(remove_filler)
print(remove_filler.lstrip(text).lstrip())

app = Flask(__name__)

# CORSの設定
@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    return response

@app.route("/")
def index():
  return "Hello, World!"

@app.route("/remove_filler")
def remove_filler():
    text = request.args.get('text')

    coy = cotohappy.API()
    # text = "えーっと、それでは今からプレゼンを、始めさせていただこうかと思います。"
    do_segment = True
    remove_filler_li = coy.remove_filler(text, do_segment) 
    for remove_filler in remove_filler_li:
        remove_filler = str(remove_filler)
    return re.sub('^\S+', '', remove_filler).lstrip()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000, threaded=True)
