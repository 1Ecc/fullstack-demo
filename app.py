import os
from flask import Flask

app = Flask(__name__)

# 把路径改成 /api/ 让它能跟 Nginx 对接上
@app.route('/api/')
def hello():
    return "<h1>✅ 恭喜！后端自动化部署彻底成功！</h1><p>这是一次端到端的自动化闭环测试。</p>"

if __name__ == '__main__':
    # 获取环境变量中的 PORT，如果没有则默认 5000
    # 这对 Railway 等托管平台非常重要
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)