import json

# 读取原始主题
with open('/workspace/复古macOS UI蓝（改1） (2).json', 'r', encoding='utf-8') as f:
    original_theme = json.load(f)

# 创建新主题
purple_theme = original_theme.copy()
purple_theme['name'] = '神秘紫色魔法主题'

# 修改配色
purple_theme['main_text_color'] = 'rgba(255, 215, 100, 1)'
purple_theme['italics_text_color'] = 'rgba(230, 180, 255, 0.98)'
purple_theme['underline_text_color'] = 'rgba(180, 140, 220, 1)'
purple_theme['quote_text_color'] = 'rgba(200, 160, 240, 1)'
purple_theme['blur_tint_color'] = 'rgba(30, 15, 60, 0.95)'
purple_theme['chat_tint_color'] = 'rgba(20, 10, 40, 0.9)'
purple_theme['user_mes_blur_tint_color'] = 'rgba(40, 20, 80, 0.85)'
purple_theme['bot_mes_blur_tint_color'] = 'rgba(50, 25, 100, 0.85)'
purple_theme['shadow_color'] = 'rgba(100, 50, 150, 0.6)'
purple_theme['shadow_width'] = 3
purple_theme['border_color'] = 'rgba(180, 140, 220, 0.8)'
purple_theme['font_scale'] = 0.9
purple_theme['noShadows'] = False
purple_theme['reduced_motion'] = False

# 替换 custom_css
original_css = original_theme['custom_css']

# 1. 修改顶部注释
modified_css = original_css.replace(
    '/* ==========================================================\n   名称：复古MacOS UI\n   样式作者：@Junezz\n   版本：v1.0\n   发布于：类脑 Discord 社区\n\n   本样式仅供个人使用与参考，禁止任何形式的商用。\n   可二改不可二传。请保留本注释和原作者署名。\n   ========================================================== */',
    '/* ==========================================================\n   名称：神秘紫色魔法主题\n   样式作者：@Junezz 改\n   版本：v1.0\n   基于：复古MacOS UI\n\n   神秘紫色魔法风格主题，带有金色装饰\n   ========================================================== */'
)

# 2. 修改 body 背景
modified_css = modified_css.replace(
    'body {\n    font-family: "Fusion Pixel 12px Monospaced zh_hans";\n    font-weight: normal;\n}',
    'body {\n    font-family: "Fusion Pixel 12px Monospaced zh_hans";\n    font-weight: normal;\n    background: linear-gradient(135deg, #1a0a35 0%, #2d154e 50%, #1a0a35 100%);\n}'
)

# 3. 修改 :root 颜色变量
old_root = '''  :root {
    --mainFontSize: calc(var(--fontScale)* 16px); /* 主字体大小 */
    --avatar-base-width: 48px; /* 头像宽度 */
    --avatar-base-height: 48px; /* 头像高度 */
    --topbarIconSize: calc(var(--mainFontSize)* 1.3); /* 顶栏图标大小 */
    --genericRadius: 0px; /* 通用圆角 */
    --warning: #ce3636;
    --crimson70a: #acacac63;
    --crimson-hover: color-mix(in srgb, var(--SmartThemeUnderlineColor), transparent 90%) !important;
    --standardIconSize: calc(var(--mainFontSize)* 1);
    --bottomFormIconSize: calc(var(--mainFontSize)* 1.5);
    --bottomFormBlockPadding: calc(var(--mainFontSize) / 1.5);
    --scrollBarWidth: 3px;
    --pagePadding: calc(var(--scrollBarWidth) + 9px);
    --genericLineHeight: calc(var(--mainFontSize)* 1.9); /* 通用行高 */

    /* === 所有颜色定义 === */
    --utilityColor: var(--black50a); /* 说明文字 */
    --navBackgroundColor: var(--SmartThemeBlurTintColor); /* 顶栏和底栏背景颜色 */
    --buttonFill: rgb(255, 255, 255); /* 按钮背景颜色 */
    --menuBackgroundColor: var(--navBackgroundColor); /* 菜单背景颜色 */
    --accentColor: var(--SmartThemeUnderlineColor); /* 装饰色1 思维链，文字装饰，段落装饰等 */
    --accentColorOverlay: color-mix(in srgb, var(--SmartThemeBorderColor), transparent 95%); /* 装饰色2半透明 消息里头像和名字的背景颜色 */
    --scrollBarColor: var(--SmartThemeUnderlineColor); /* 滚动条颜色 */
    --boxShadowSubtle: 2px 2px 0px var(--SmartThemeBorderColor); /* 阴影颜色 */
    --boxShadowSubtleAlt: 2px 2px 0px var(--SmartThemeUnderlineColor); /* 阴影颜色 */
  }'''

new_root = '''  :root {
    --mainFontSize: calc(var(--fontScale)* 16px); /* 主字体大小 */
    --avatar-base-width: 48px; /* 头像宽度 */
    --avatar-base-height: 48px; /* 头像高度 */
    --topbarIconSize: calc(var(--mainFontSize)* 1.3); /* 顶栏图标大小 */
    --genericRadius: 8px; /* 通用圆角 - 魔法风格使用圆角 */
    --warning: #ff6b6b;
    --crimson70a: rgba(230, 180, 255, 0.4);
    --crimson-hover: color-mix(in srgb, rgba(255, 215, 100, 0.2), transparent 80%) !important;
    --standardIconSize: calc(var(--mainFontSize)* 1);
    --bottomFormIconSize: calc(var(--mainFontSize)* 1.5);
    --bottomFormBlockPadding: calc(var(--mainFontSize) / 1.5);
    --scrollBarWidth: 4px;
    --pagePadding: calc(var(--scrollBarWidth) + 9px);
    --genericLineHeight: calc(var(--mainFontSize)* 1.8); /* 通用行高 */

    /* === 所有颜色定义 - 魔法紫 === */
    --utilityColor: rgba(230, 180, 255, 0.7); /* 说明文字 */
    --navBackgroundColor: rgba(30, 15, 60, 0.95); /* 顶栏和底栏背景颜色 */
    --buttonFill: rgba(60, 30, 100, 0.8); /* 按钮背景颜色 */
    --menuBackgroundColor: rgba(40, 20, 80, 0.98); /* 菜单背景颜色 */
    --accentColor: rgba(255, 215, 100, 1); /* 装饰色1 思维链，文字装饰，段落装饰等 - 金色 */
    --accentColorOverlay: color-mix(in srgb, rgba(180, 140, 220, 0.5), transparent 85%); /* 装饰色2半透明 */
    --scrollBarColor: rgba(180, 140, 220, 0.8); /* 滚动条颜色 */
    --boxShadowSubtle: 0 0 15px rgba(180, 140, 220, 0.3); /* 紫色光晕阴影 */
    --boxShadowSubtleAlt: 0 0 20px rgba(255, 215, 100, 0.3); /* 金色光晕阴影 */
  }'''

modified_css = modified_css.replace(old_root, new_root)

# 4. 在CSS末尾添加魔法主题的额外样式
magic_extra = '''
  /* === 神秘紫色魔法主题额外样式 === */
  
  /* 发送框发光效果 */
  #send_textarea {
    transition: all 0.3s ease !important;
  }
  
  #send_textarea:focus {
    box-shadow: 0 0 20px rgba(255, 215, 100, 0.3) !important;
  }
  
  /* 按钮悬停发光 */
  .menu_button:hover,
  button:hover {
    box-shadow: 0 0 15px rgba(255, 215, 100, 0.4) !important;
  }
  
  /* 名字和头像发光 */
  .mes_block .ch_name {
    box-shadow: 0 0 10px rgba(180, 140, 220, 0.2);
  }
  
  /* 对话框气泡装饰 */
  body.bubblechat .mes[is_user="false"] {
    position: relative;
  }
  
  /* 引号装饰 */
  .mes_text blockquote::before {
    content: '✦';
    position: absolute;
    left: -10px;
    top: 0;
    color: rgba(255, 215, 100, 0.5);
    font-size: 1.2em;
  }
  
  .mes_text blockquote {
    position: relative;
  }
  
  /* 顶部和底部栏紫色渐变 */
  #top-bar, #send_form {
    background: linear-gradient(180deg, rgba(30, 15, 60, 0.98), rgba(20, 10, 40, 0.95)) !important;
  }
  
  /* 滚动条渐变 */
  ::-webkit-scrollbar-thumb:vertical,
  ::-webkit-scrollbar-thumb:horizontal {
    background: linear-gradient(180deg, rgba(180, 140, 220, 0.8), rgba(140, 100, 180, 0.6)) !important;
  }
  
  /* 思维链紫色边框 */
  .mes_reasoning {
    border-left: 2px solid rgba(255, 215, 100, 0.6) !important;
  }
  
  /* 代码块紫色渐变边框 */
  .mes_text pre {
    border-left: 2px solid rgba(180, 140, 220, 0.8) !important;
    box-shadow: 0 0 15px rgba(100, 50, 150, 0.2) !important;
  }
  
  /* 引用块金色边框 */
  .mes_text blockquote {
    border-left: 3px solid rgba(255, 215, 100, 0.6) !important;
  }
  
  /* 魔法风格的表格 */
  .mes_text table {
    border: 1px solid rgba(180, 140, 220, 0.6) !important;
    box-shadow: 0 0 15px rgba(100, 50, 150, 0.2) !important;
  }
'''

# 找到 media query 之前的位置插入
insert_pos = modified_css.find('/* 手机适配 */')
if insert_pos != -1:
    modified_css = modified_css[:insert_pos] + magic_extra + modified_css[insert_pos:]
else:
    modified_css = modified_css + magic_extra

purple_theme['custom_css'] = modified_css

# 保存新主题
with open('/workspace/神秘紫色魔法主题.json', 'w', encoding='utf-8') as f:
    json.dump(purple_theme, f, indent=2, ensure_ascii=False)

print('神秘紫色魔法主题已成功创建！')
