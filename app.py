from flask import Flask, render_template #render_tamplate 
from data import Articles
app = Flask(__name__) #app이라는 인스턴스를 생성시킴 app인스턴스 안에는 Flask클래스를 실행

@app.route('/hello') 
def hello_world():
    return 'Hello World!'

@app.route('/', methods=['GET','POST']) # @: decoration . route메소드는 플라스크가 가진 메소드 #()는 인자값 #.route경로처리
def index():
    name = 'KIM'
    return render_template('index.html', data=name)        #끌어오고자 하는 html파일 가져오기
    
    # key값으로 data를 보냄 
    
@app.route('/articles', methods=['GET','POST'])
def articles():
    list_data = Articles()
    return render_template('articles.html', data = list_data)

if __name__ == '__main__':   #플라스크 라이브러리를 이용해서 서버를 띄움
    app.run( debug=True)

