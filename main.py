from flask import Flask, render_template, request, abort, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)  # 开启debug模式后修改文件内容能够自动重启服务器
