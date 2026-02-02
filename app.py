from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>🐍 Python 后端部署成功！</h1><p>我是由 Systemd 自动启动的。</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)