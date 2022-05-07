from flask import Flask, render_template, request
from flask_api import status
from werkzeug.utils import secure_filename
import json
from script import *
app = Flask(__name__)

@app.route('/home')
def greeting():
    return render_template('home.html')

@app.route('/help')
def gohelp():
    return render_template('help.html')

@app.route('/dev')
def godev():
    return render_template('dev.html')

@app.route('/about')
def goabout():
    return render_template('about.html')

@app.route('/loading')
def goloading():
    return render_template('loading.html')

@app.route('/result')
def goresult():
    return render_template('result.html')

@app.route('/addword',  methods = ['POST'])
def addwords():
    if request.method == 'POST':
       value = request.form['id_words']
       value = str(value)
       #return value
    return greeting()

#업로드 HTML 렌더링
@app.route('/upload')
def render_file():
   return json.dumps(add(6,2))

#파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #저장할 경로 + 파일명
      f.save('./upload/'+secure_filename(f.filename))
      return render_template('loading.html')

if __name__ == '__main__':
    #서버 실행
   app.run(debug = True, host='0.0.0.0')

#이 밑으로는 어떻게 사용해야할지 모름. 그리고 테스트용임.
#   ****어쨋든 python 돌아간다****
#@app.route('/add', methods=['POST'])
# def get_add():
#     if request.method == 'POST':
#         a = request.json["a"]
#         b = request.json["b"]
#         c = add(a,b)
#         result = json.dumps(c)
#     return result, status.HTTP_200_OK, {"Content-Type": "application/json; charset=utf-8", "Access-Control-Allow-Origin": "*"}
#
# @app.route('/same', methods=['POST'])
# def get_same():
#     if request.method == 'POST':
#         a = request.json["a"]
#         b = request.json["b"]
#         c = same(a,b)
#         result = json.dumps(c)
#     return result, status.HTTP_200_OK, {"Content-Type": "application/json; charset=utf-8", "Access-Control-Allow-Origin": "*"}
