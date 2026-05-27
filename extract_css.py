import json

with open('/workspace/复古macOS UI蓝（改1） (2).json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"主题名称: {data['name']}")
print(f"\nCustom CSS 长度: {len(data['custom_css'])} 字符")

# 保存完整的CSS到单独文件
with open('/workspace/original_css.txt', 'w', encoding='utf-8') as f:
    f.write(data['custom_css'])

print("\n完整CSS已保存到 original_css.txt")
print(f"\nCSS前2000字符预览:")
print("-" * 80)
print(data['custom_css'][:2000])
