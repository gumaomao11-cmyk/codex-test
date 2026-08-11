from flask import Flask

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>小店</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:system-ui,sans-serif;background:#f5f5f5;color:#333}
header{background:#fff;padding:16px;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,.1)}
header h1{font-size:20px;color:#e44}
.hero{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;text-align:center;padding:40px 16px}
.hero h2{font-size:24px;margin-bottom:8px}
.hero p{opacity:.85}
.products{max-width:960px;margin:24px auto;padding:0 16px;display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px}
.card{background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.08);transition:transform .2s}
.card:hover{transform:translateY(-2px)}
.card img{width:100%;height:160px;object-fit:cover;background:#eee}
.card .info{padding:12px}
.card .name{font-size:15px;font-weight:600;margin-bottom:4px}
.card .price{color:#e44;font-size:18px;font-weight:700}
.card .btn{display:block;margin-top:8px;padding:8px;text-align:center;background:#e44;color:#fff;border-radius:6px;text-decoration:none;font-size:14px}
footer{text-align:center;padding:24px;color:#999;font-size:13px}
</style>
</head>
<body>
<header><h1>🏪 小店</h1></header>
<section class="hero">
<h2>新店开业 · 全场特惠</h2>
<p>精选好物，品质保证</p>
</section>
<main class="products">
<div class="card"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='160'%3E%3Crect fill='%23f0e6d3' width='200' height='160'/%3E%3Ctext x='100' y='85' text-anchor='middle' fill='%23999' font-size='14'%3E📱%3C/text%3E%3C/svg%3E" alt="商品1"><div class="info"><div class="name">无线蓝牙耳机</div><div class="price">¥199</div><a class="btn" href="#">立即购买</a></div></div>
<div class="card"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='160'%3E%3Crect fill='%23d3e6f0' width='200' height='160'/%3E%3Ctext x='100' y='85' text-anchor='middle' fill='%23999' font-size='14'%3E⌚%3C/text%3E%3C/svg%3E" alt="商品2"><div class="info"><div class="name">智能手表</div><div class="price">¥599</div><a class="btn" href="#">立即购买</a></div></div>
<div class="card"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='160'%3E%3Crect fill='%23e6d3f0' width='200' height='160'/%3E%3Ctext x='100' y='85' text-anchor='middle' fill='%23999' font-size='14'%3E🎧%3C/text%3E%3C/svg%3E" alt="商品3"><div class="info"><div class="name">降噪头戴耳机</div><div class="price">¥399</div><a class="btn" href="#">立即购买</a></div></div>
<div class="card"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='160'%3E%3Crect fill='%23d3f0e6' width='200' height='160'/%3E%3Ctext x='100' y='85' text-anchor='middle' fill='%23999' font-size='14'%3E🔋%3C/text%3E%3C/svg%3E" alt="商品4"><div class="info"><div class="name">快充移动电源</div><div class="price">¥129</div><a class="btn" href="#">立即购买</a></div></div>
</main>
<footer>© 2026 小店 · 用心服务每一位顾客</footer>
</body>
</html>"""

@app.route("/")
def home():
    return HTML

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
