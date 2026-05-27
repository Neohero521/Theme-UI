import json

# 读取原始主题
with open('/workspace/复古macOS UI蓝（改1） (2).json', 'r', encoding='utf-8') as f:
    original = json.load(f)

# 创建魔法主题
theme = original.copy()
theme['name'] = '神秘紫色魔法主题'
theme['blur_strength'] = 5
theme['main_text_color'] = 'rgba(255, 215, 100, 1)'
theme['italics_text_color'] = 'rgba(230, 180, 255, 0.98)'
theme['underline_text_color'] = 'rgba(180, 140, 220, 1)'
theme['quote_text_color'] = 'rgba(200, 160, 240, 1)'
theme['blur_tint_color'] = 'rgba(30, 15, 60, 0.95)'
theme['chat_tint_color'] = 'rgba(15, 8, 30, 0.95)'
theme['shadow_color'] = 'rgba(100, 50, 150, 0.6)'
theme['shadow_width'] = 3
theme['border_color'] = 'rgba(180, 140, 220, 0.8)'
theme['font_scale'] = 0.9
theme['noShadows'] = False
theme['reduced_motion'] = False

# 自定义CSS
custom_css = """/* ==========================================================
   名称：神秘紫色魔法主题
   样式作者：@Junezz 改
   版本：v1.1
   基于：复古MacOS UI
   ========================================================== */

@import url("https://fontsapi.zeoseven.com/570/main/result.css");

body {
    font-family: "Fusion Pixel 12px Monospaced zh_hans";
    background: linear-gradient(135deg, #150828 0%, #1a0a35 30%, #2d154e 50%, #1a0a35 70%, #150828 100%);
    position: relative;
    min-height: 100vh;
}

body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    background-image: 
        radial-gradient(2px 2px at 20px 30px, rgba(255, 215, 100, 0.3), transparent),
        radial-gradient(2px 2px at 40px 70px, rgba(180, 140, 220, 0.3), transparent),
        radial-gradient(1px 1px at 90px 40px, rgba(255, 215, 100, 0.2), transparent),
        radial-gradient(2px 2px at 130px 80px, rgba(180, 140, 220, 0.25), transparent),
        radial-gradient(1px 1px at 160px 120px, rgba(255, 215, 100, 0.3), transparent);
    background-repeat: repeat;
    background-size: 200px 150px;
    animation: twinkleStars 8s ease-in-out infinite;
}

@keyframes twinkleStars {
    0%, 100% { opacity: 0.3; }
    50% { opacity: 0.7; }
}

code, textarea, #send_textarea, input, select, button, .text_pole, .font-family-reset {
  font-family: inherit;
}

:root {
    --mainFontSize: calc(var(--fontScale)* 16px);
    --genericRadius: 12px;
    --warning: #ff6b6b;
    --crimson70a: rgba(230, 180, 255, 0.4);
    --crimson-hover: color-mix(in srgb, rgba(255, 215, 100, 0.2), transparent 80%) !important;
    --utilityColor: rgba(230, 180, 255, 0.7);
    --navBackgroundColor: rgba(20, 10, 40, 0.98);
    --buttonFill: rgba(50, 25, 90, 0.85);
    --menuBackgroundColor: rgba(30, 15, 60, 0.98);
    --accentColor: rgba(255, 215, 100, 1);
    --accentColorOverlay: color-mix(in srgb, rgba(180, 140, 220, 0.5), transparent 85%);
    --scrollBarColor: rgba(180, 140, 220, 0.8);
    --boxShadowSubtle: 0 0 20px rgba(180, 140, 220, 0.3);
    --boxShadowSubtleAlt: 0 0 25px rgba(255, 215, 100, 0.3);
}

/* 聊天框 */
#chat {
    padding: 0 !important;
    overflow-y: scroll;
    border: none !important;
    background: transparent;
}

#top-bar, #send_form {
    background: linear-gradient(180deg, rgba(25, 12, 50, 0.98), rgba(15, 8, 30, 0.98)) !important;
    border: 1px solid rgba(180, 140, 220, 0.3);
    box-shadow: 0 0 15px rgba(100, 50, 150, 0.2);
}

/* 消息气泡 */
body.bubblechat .mes {
    border-radius: var(--genericRadius);
    padding: 0px 0px 16px 0px;
    display: flex;
    flex-direction: column;
    border: none !important;
    box-shadow: none !important;
}

.mesAvatarWrapper {
    background: linear-gradient(135deg, rgba(50, 25, 90, 0.7), rgba(30, 15, 60, 0.8));
    border-radius: var(--genericRadius);
    border: 1px solid rgba(180, 140, 220, 0.4);
    box-shadow: 0 0 15px rgba(100, 50, 150, 0.2);
}

.mes_block .ch_name {
    background: linear-gradient(135deg, rgba(50, 25, 90, 0.8), rgba(30, 15, 60, 0.9));
    border-radius: var(--genericRadius);
    border-bottom: 1px solid rgba(180, 140, 220, 0.4);
    box-shadow: 0 0 15px rgba(100, 50, 150, 0.2);
}

/* 引用块 */
.mes_text blockquote {
    background: linear-gradient(135deg, rgba(40, 20, 80, 0.7), rgba(30, 15, 60, 0.8));
    border-left: 3px solid rgba(255, 215, 100, 0.8);
    border-radius: 0 8px 8px 0;
    position: relative;
    box-shadow: 0 0 15px rgba(100, 50, 150, 0.2);
}

.mes_text blockquote::before {
    content: '"';
    position: absolute;
    top: -8px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 2.5em;
    color: rgba(255, 215, 100, 0.3);
    font-family: serif;
}

/* 按钮 */
.menu_button {
    background: linear-gradient(135deg, rgba(60, 30, 100, 0.9), rgba(40, 20, 80, 0.95));
    border: 1px solid rgba(180, 140, 220, 0.5);
    box-shadow: 0 0 10px rgba(100, 50, 150, 0.3);
}

.menu_button:hover {
    box-shadow: 0 0 20px rgba(255, 215, 100, 0.4);
    border-color: rgba(255, 215, 100, 0.6);
}

/* 滚动条 */
::-webkit-scrollbar {
    width: 4px;
    height: 4px;
}

::-webkit-scrollbar-track {
    background: rgba(15, 8, 30, 0.5);
    border-radius: 2px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, rgba(180, 140, 220, 0.8), rgba(140, 100, 180, 0.6));
    border-radius: 2px;
    box-shadow: 0 0 10px rgba(180, 140, 220, 0.4);
}

/* 输入框 */
#send_textarea {
    transition: all 0.3s ease !important;
}

#send_textarea:focus {
    box-shadow: 0 0 25px rgba(255, 215, 100, 0.3) !important;
}

/* 抽屉面板 */
.drawer-content, #right-nav-panel, #left-nav-panel {
    background-color: var(--menuBackgroundColor) !important;
    border: 1px solid rgba(180, 140, 220, 0.4);
    box-shadow: 0 0 20px rgba(100, 50, 150, 0.3);
}

/* 星星装饰 */
.star-decoration {
    position: absolute;
    width: 4px;
    height: 4px;
    background: rgba(255, 215, 100, 0.8);
    border-radius: 50%;
    animation: twinkle 3s ease-in-out infinite;
}

@keyframes twinkle {
    0%, 100% { opacity: 0.3; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.2); }
}

/* 引用卡片 */
.quote-card {
    background: linear-gradient(135deg, rgba(40, 20, 80, 0.6), rgba(30, 15, 60, 0.7));
    border: 1px solid rgba(180, 140, 220, 0.4);
    border-radius: var(--genericRadius);
    padding: 24px;
    text-align: center;
    position: relative;
    box-shadow: 0 0 25px rgba(100, 50, 150, 0.2);
}

.quote-card::before {
    content: '"';
    position: absolute;
    top: -15px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 4em;
    color: rgba(255, 215, 100, 0.25);
    font-family: serif;
}

/* 灵力消耗标签 */
.mana-cost {
    background: linear-gradient(135deg, rgba(50, 25, 90, 0.8), rgba(30, 15, 60, 0.9));
    border: 1px solid rgba(180, 140, 220, 0.5);
    border-radius: 20px;
    padding: 8px 16px;
    color: rgba(230, 180, 255, 0.8);
    box-shadow: 0 0 15px rgba(100, 50, 150, 0.2);
}

/* 页脚 */
.grimoire-footer {
    text-align: center;
    color: rgba(160, 120, 200, 0.5);
    padding: 20px;
    border-top: 1px solid rgba(180, 140, 220, 0.1);
}

/* 金色图标 */
.fa, .fa-solid {
    color: rgba(255, 215, 100, 1);
}

/* 顶栏图标 */
.drawer-icon::before {
    background-color: rgba(255, 215, 100, 1);
}

/* 进度条 */
input.neo-range-slider[type="range"]::-webkit-slider-thumb {
    background: linear-gradient(135deg, rgba(255, 215, 100, 1), rgba(255, 180, 100, 1)) !important;
    box-shadow: 0 0 10px rgba(255, 215, 100, 0.5) !important;
}

input.neo-range-slider[type="range"] {
    background: linear-gradient(90deg, rgba(180, 140, 220, 0.6), rgba(255, 215, 100, 0.6)) !important;
}

/* 表格 */
.mes_text table {
    background: linear-gradient(135deg, rgba(40, 20, 80, 0.7), rgba(30, 15, 60, 0.8));
    border: 1px solid rgba(180, 140, 220, 0.6);
    box-shadow: 0 0 20px rgba(100, 50, 150, 0.2);
}

/* 代码块 */
.mes_text pre {
    background: linear-gradient(135deg, rgba(40, 20, 80, 0.8), rgba(30, 15, 60, 0.9));
    border-left: 3px solid rgba(255, 215, 100, 0.8);
    box-shadow: 0 0 20px rgba(100, 50, 150, 0.2);
}

/* 分割线 */
hr {
    background: linear-gradient(90deg, transparent, rgba(255, 215, 100, 0.5), transparent);
    height: 1px;
    border: none;
}
"""

theme['custom_css'] = custom_css

# 保存
with open('/workspace/神秘紫色魔法主题.json', 'w', encoding='utf-8') as f:
    json.dump(theme, f, indent=2, ensure_ascii=False)

print('主题创建完成！')
