from flask import Flask

app = Flask(__name__)

# 把路径改成 /api/ 让它能跟 Nginx 对接上
@app.route('/api/')
def hello():
    return "<h1>✅ 恭喜！后端自动化部署彻底成功！</h1><p>这是一次端到端的自动化闭环测试。</p>"

if __name__ == '__main__':
    # 注意：实际上 Gunicorn 会接管端口，但本地测试还是保留 5000
    app.run(host='0.0.0.0', port=5000)