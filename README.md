# Markdown到微信公众号转换器

一个强大的Python工具，可以将Markdown格式的文章转换为符合微信公众号文章格式的HTML代码，支持直接复制粘贴到微信公众号编辑器。

## ✨ 功能特点

- 🎯 **完美适配**: 专门为微信公众号编辑器优化
- 🎨 **8种风格**: 提供通用性、科技风、金融风、网红风等多种排版风格
- 📝 **样式丰富**: 支持标题、段落、代码、表格、引用等多种格式
- 🖼️ **图片支持**: 自动优化图片显示效果
- 📱 **响应式**: 适配移动端阅读体验
- 🚀 **简单易用**: 命令行和Python API两种使用方式
- 📋 **一键复制**: 生成的HTML可直接粘贴到微信公众号编辑器
- 🎨 **风格选择**: 支持多种预设风格，满足不同内容需求

## 🛠️ 安装依赖

```bash
pip install -r requirements.txt
```

## 📖 使用方法

### 1. 命令行使用

```bash
# 基本转换
python markdown2wechat.py sample_article.md

# 指定输出文件和标题
python markdown2wechat.py sample_article.md -o output.html -t "我的文章标题" -s "副标题"

# 使用指定风格
python markdown2wechat.py sample_article.md --style tech -t "技术文章"

# 查看所有可用风格
python markdown2wechat.py --list-styles

# 查看帮助
python markdown2wechat.py -h
```

### 2. Python API使用

```python
from markdown2wechat import MarkdownToWeChatConverter

# 创建转换器（默认风格）
converter = MarkdownToWeChatConverter()

# 创建指定风格的转换器
converter = MarkdownToWeChatConverter(style="tech")

# 转换文件
converter.convert_file('input.md', 'output.html', '文章标题', '副标题')

# 转换文本
markdown_text = "# 标题\n这是内容"
html_result = converter.convert_text(markdown_text, '标题', '副标题')
```

### 3. 运行演示

```bash
# 运行基本演示
python demo.py

# 演示所有风格
python demo.py --all-styles
```

## 🎨 可用风格

| 风格 | 特点 | 适用场景 |
|------|------|----------|
| `default` | 简洁专业，蓝色主题 | 通用文章 |
| `tech` | 现代科技，深色主题 | 技术博客 |
| `finance` | 稳重金融，金色主题 | 财经内容 |
| `influencer` | 活泼时尚，粉色主题 | 生活分享 |
| `minimal` | 极简黑白，简洁优雅 | 深度阅读 |
| `colorful` | 彩虹主题，活泼有趣 | 创意内容 |
| `dark` | 暗黑主题，护眼舒适 | 夜间阅读 |
| `elegant` | 古典雅致，深蓝主题 | 文学内容 |

## 📝 支持的Markdown格式

- ✅ **标题**: H1-H6 标题
- ✅ **段落**: 普通文本段落
- ✅ **列表**: 有序和无序列表
- ✅ **代码**: 行内代码和代码块
- ✅ **表格**: 完整表格支持
- ✅ **引用**: 引用块
- ✅ **链接**: 超链接
- ✅ **图片**: 图片显示
- ✅ **分割线**: 水平分割线
- ✅ **强调**: 粗体和斜体

## 🎨 样式特点

- **字体**: 使用系统默认字体，确保最佳阅读体验
- **颜色**: 精心调配的颜色方案，符合微信公众号风格
- **间距**: 合理的行间距和段落间距
- **代码高亮**: 深色主题的代码块
- **表格**: 带边框的表格，支持斑马纹
- **响应式**: 自适应不同屏幕尺寸

## 📋 使用步骤

1. **准备Markdown文件**: 使用任何编辑器编写Markdown文章
2. **运行转换器**: 使用命令行或Python API转换文件
3. **复制HTML**: 将生成的HTML内容复制到剪贴板
4. **粘贴发布**: 在微信公众号编辑器中粘贴HTML内容
5. **预览发布**: 预览效果后发布文章

## 🔧 技术实现

- **Markdown解析**: 使用Python `markdown` 库
- **HTML优化**: 使用 `BeautifulSoup` 进行HTML处理
- **样式设计**: 内嵌CSS样式，确保微信公众号兼容性
- **编码支持**: 完全支持中文字符

## 📁 项目结构

```
markdown2wechat/
├── markdown2wechat.py    # 主转换器代码
├── wechat_styles.py     # 样式模板库
├── requirements.txt      # 依赖包列表
├── demo.py              # 使用演示
├── sample_article.md    # 示例文章
├── 风格使用指南.md       # 详细风格说明
├── 使用指南.md          # 使用说明
├── 测试报告.md          # 功能测试报告
└── README.md            # 说明文档
```

## 🚀 快速开始

1. 克隆或下载项目文件
2. 安装依赖: `pip install -r requirements.txt`
3. 运行演示: `python demo.py`
4. 转换您的文章: `python markdown2wechat.py your_article.md`

## 💡 使用技巧

- **标题优化**: 建议使用H1作为文章主标题
- **代码块**: 支持多种编程语言的语法高亮
- **图片处理**: 确保图片URL可访问
- **表格宽度**: 表格会自动适应容器宽度
- **移动端**: 生成的HTML在手机上显示效果良好

## ❓ 常见问题

**Q: 转换后的HTML在微信公众号编辑器中显示异常？**
A: 确保复制了完整的HTML内容，包括`<style>`标签。

**Q: 支持自定义样式吗？**
A: 可以修改`MarkdownToWeChatConverter`类中的`wechat_styles`属性来自定义样式。

**Q: 图片无法显示？**
A: 确保图片URL是公开可访问的，微信公众号不支持本地图片。

**Q: 代码高亮不生效？**
A: 确保安装了`pygments`库：`pip install pygments`

## 📄 许可证

本项目采用MIT许可证，可自由使用和修改。

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

---

**开始您的微信公众号文章创作之旅吧！** ✨
