# 小店 / shop

一个轻量的 Flask 示例项目，包含两部分：

1. **`app.py`** — Flask 小店首页（4 个商品的瀑布流卡片）。
2. **`optimize_aipick.py`** — AiPick PPT 文本清洗流水线（修正目录大小写、错别字、术语统一为 `AiPick`，并追加总结页）。

`renders/` 下保存了三套 PNG 预览：`aipick_orig`（原始）、`aipick_hd`（高清版）、`aipick_new`（新版），可直接预览每页效果。

## 快速开始

```bash
pip install -r requirements.txt
python app.py
# 浏览器打开 http://localhost:5000
```

## 运行 PPT 优化脚本

```bash
python optimize_aipick.py
# 输入：aipick_working.pptx
# 输出：aipick_optimized.pptx（覆盖）
```

## 目录结构

```
shop/
├── app.py                    # Flask 小店首页
├── optimize_aipick.py        # PPT 文本清洗
├── requirements.txt
├── aipick_working.pptx       # 原始 PPT
├── aipick_optimized.pptx     # 优化后 PPT
├── agents.md.txt
└── renders/                  # 渲染预览
    ├── aipick_orig/
    ├── aipick_hd/
    ├── aipick_new/
    ├── aipick_new_montage.png
    └── before_after.png
```

## 依赖

- Python 3.8+
- Flask
- python-pptx（仅运行 `optimize_aipick.py` 需要）

## 注意事项

- `tmp_ppt/` 是中间工作目录（含虚拟环境和 600MB+ 素材），已通过 `.gitignore` 排除。
