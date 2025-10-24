#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多风格转换器测试脚本
验证所有风格是否正常工作
"""

from markdown2wechat import MarkdownToWeChatConverter
from wechat_styles import WeChatStyleTemplates

def test_all_styles():
    """测试所有风格"""
    print("🧪 多风格转换器测试")
    print("=" * 50)
    
    # 测试用的Markdown内容
    test_markdown = """
# 风格测试文章

> 这是一个用于测试不同风格的示例文章

## 功能测试

- ✅ 标题样式
- ✅ 段落文本
- ✅ 代码块
- ✅ 表格
- ✅ 引用块

## 代码示例

```python
def test_function():
    return "Hello, World!"
```

## 数据表格

| 风格 | 状态 | 评分 |
|------|------|------|
| default | ✅ | 9/10 |
| tech | ✅ | 9/10 |
| finance | ✅ | 9/10 |

**测试完成！** 🎉
"""
    
    # 获取所有可用风格
    available_styles = WeChatStyleTemplates.get_available_styles()
    
    print(f"正在测试 {len(available_styles)} 种风格...")
    print()
    
    success_count = 0
    failed_styles = []
    
    for style in available_styles:
        print(f"🔍 测试 {style} 风格...", end=" ")
        
        try:
            # 创建转换器
            converter = MarkdownToWeChatConverter(style=style)
            
            # 转换文本
            html_result = converter.convert_text(
                test_markdown,
                title=f"{style.title()}风格测试",
                subtitle=f"测试 {WeChatStyleTemplates.get_style_description(style)}"
            )
            
            if html_result and len(html_result) > 1000:  # 确保生成了完整的HTML
                print("✅ 成功")
                success_count += 1
                
                # 保存测试结果
                output_file = f"test_{style}_style.html"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(html_result)
                print(f"   保存到: {output_file}")
            else:
                print("❌ 失败 - HTML内容不完整")
                failed_styles.append(style)
                
        except Exception as e:
            print(f"❌ 失败 - {str(e)}")
            failed_styles.append(style)
        
        print()
    
    # 测试结果汇总
    print("📊 测试结果汇总")
    print("=" * 50)
    print(f"总风格数: {len(available_styles)}")
    print(f"成功: {success_count}")
    print(f"失败: {len(failed_styles)}")
    
    if failed_styles:
        print(f"失败的风格: {', '.join(failed_styles)}")
    else:
        print("🎉 所有风格测试通过！")
    
    print("\n📁 生成的测试文件:")
    for style in available_styles:
        if style not in failed_styles:
            print(f"  - test_{style}_style.html")
    
    return success_count == len(available_styles)

def test_style_descriptions():
    """测试风格描述"""
    print("\n📝 风格描述测试")
    print("=" * 50)
    
    available_styles = WeChatStyleTemplates.get_available_styles()
    
    for style in available_styles:
        description = WeChatStyleTemplates.get_style_description(style)
        print(f"{style:12} - {description}")
    
    print(f"\n✅ 共 {len(available_styles)} 种风格描述正常")

if __name__ == "__main__":
    # 运行测试
    test_success = test_all_styles()
    test_style_descriptions()
    
    print("\n" + "=" * 50)
    if test_success:
        print("🎉 所有测试通过！多风格转换器工作正常！")
    else:
        print("⚠️  部分测试失败，请检查相关代码")
    
    print("\n💡 使用建议:")
    print("1. 打开生成的HTML文件查看各风格效果")
    print("2. 选择喜欢的风格进行实际转换")
    print("3. 参考风格使用指南了解各风格特点")
