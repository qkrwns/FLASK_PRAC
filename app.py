from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ('GET', 'POST')) # 접속하는 url
def index():
  return render_template('index.html',user="반원",data={'level':60,'point':360,'exp':45000})

if __name__=="__main__":
  app.run(debug=True)



