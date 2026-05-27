import json

# 读取现有的魔法主题
with open('/workspace/神秘紫色魔法主题.json', 'r', encoding='utf-8') as f:
    theme = json.load(f)

# 添加更多魔法风格的CSS
magic_css_additions = '''

/* === 星星装饰效果 === */
@keyframes twinkle {
  0%, 100% { opacity: 0.3; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.2); }
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-5px); }
}

@keyframes shimmer {
  0% { background-position: -200% center; }
  100% { background-position: 200% center; }
}

/* 星星装饰元素 */
.star-decoration {
  position: absolute;
  width: 6px;
  height: 6px;
  background: rgba(255, 215, 100, 0.9);
  border-radius: 50%;
  animation: twinkle 3s ease-in-out infinite;
  box-shadow: 0 0 8px rgba(255, 215, 100, 0.6);
}

.star-decoration::before {
  content: '✦';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 8px;
  color: rgba(255, 215, 100, 1);
}

/* 月亮装饰 */
.moon-decoration {
  position: absolute;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(255, 215, 100, 0.8), rgba(230, 200, 150, 0.6));
  box-shadow: 0 0 15px rgba(255, 215, 100, 0.5);
  animation: float 4s ease-in-out infinite;
}

.moon-decoration::after {
  content: '';
  position: absolute;
  width: 14px;
  height: 14px;
  background: #1a0a35;
  border-radius: 50%;
  top: 3px;
  right: 0;
}

/* === 波浪下划线效果 === */
.wave-underline {
  position: relative;
  display: inline-block;
}

.wave-underline::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 3px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 4'%3E%3Cpath d='M0 2 Q 12.5 0, 25 2 T 50 2 T 75 2 T 100 2' fill='none' stroke='rgba(255,215,100,0.6)' stroke-width='2'/%3E%3C/svg%3E");
  background-repeat: repeat-x;
  background-size: 25px 4px;
}

/* === 场景标题装饰 === */
.scene-title {
  position: relative;
  text-align: center;
  padding: 16px 0;
  margin: 16px 0;
}

.scene-title::before,
.scene-title::after {
  content: '';
  position: absolute;
  top: 50%;
  width: 25%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 215, 100, 0.4));
}

.scene-title::before {
  left: 0;
}

.scene-title::after {
  right: 0;
  background: linear-gradient(90deg, rgba(255, 215, 100, 0.4), transparent);
}

.scene-title .scene-dot {
  display: inline-block;
  width: 8px;
  height: 8px;
  background: rgba(255, 215, 100, 0.8);
  border-radius: 50%;
  margin: 0 8px;
  box-shadow: 0 0 8px rgba(255, 215, 100, 0.5);
}

.scene-title .scene-star {
  display: inline-block;
  color: rgba(255, 215, 100, 0.8);
  font-size: 12px;
}

/* === 金色边框卡片 === */
.gold-border-card {
  background: linear-gradient(135deg, rgba(20, 10, 40, 0.9), rgba(30, 15, 60, 0.85));
  border: 1px solid rgba(255, 215, 100, 0.3);
  border-radius: 12px;
  box-shadow: 
    0 0 20px rgba(180, 140, 220, 0.2),
    inset 0 0 20px rgba(0, 0, 0, 0.3);
  position: relative;
  overflow: hidden;
}

.gold-border-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 215, 100, 0.6), transparent);
}

.gold-border-card::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 215, 100, 0.4), transparent);
}

/* === 引用卡片样式 === */
.quote-card {
  background: linear-gradient(135deg, rgba(40, 20, 80, 0.7), rgba(30, 15, 60, 0.8));
  border: 1px solid rgba(180, 140, 220, 0.4);
  border-radius: 16px;
  padding: 24px;
  position: relative;
  margin: 16px 0;
}

.quote-card::before {
  content: '"';
  position: absolute;
  top: -10px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 48px;
  color: rgba(255, 215, 100, 0.2);
  font-family: serif;
}

.quote-card::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 8px;
  width: 2px;
  height: 60%;
  background: linear-gradient(180deg, rgba(255, 215, 100, 0.6), transparent);
  transform: translateY(-50%);
}

.quote-card .quote-content {
  font-style: italic;
  color: rgba(230, 180, 255, 0.9);
  text-align: center;
  line-height: 1.8;
  padding-left: 16px;
}

/* === 高亮文本框 === */
.highlight-box {
  background: linear-gradient(135deg, rgba(60, 30, 100, 0.7), rgba(50, 25, 80, 0.6));
  border-left: 3px solid rgba(255, 215, 100, 0.6);
  border-radius: 0 8px 8px 0;
  padding: 6px 12px;
  margin: 4px 0;
  display: inline-block;
}

.highlight-box-alt {
  background: linear-gradient(135deg, rgba(80, 40, 120, 0.6), rgba(60, 30, 100, 0.5));
  border: 1px solid rgba(255, 215, 100, 0.3);
  border-radius: 6px;
  padding: 4px 10px;
  margin: 4px 0;
  display: inline-block;
}

/* === 灵力量消耗标签 === */
.mana-cost {
  background: linear-gradient(135deg, rgba(180, 140, 220, 0.3), rgba(140, 100, 180, 0.2));
  border: 1px solid rgba(200, 160, 240, 0.4);
  border-radius: 20px;
  padding: 8px 16px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: rgba(230, 180, 255, 0.9);
  font-size: 0.9em;
  box-shadow: 0 0 10px rgba(180, 140, 220, 0.2);
}

.mana-cost .mana-icon {
  color: rgba(255, 215, 100, 0.9);
  font-size: 1.2em;
}

/* === 月亮状态指示器 === */
.moon-phase {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: rgba(230, 180, 255, 0.8);
  font-size: 0.85em;
}

.moon-phase .moon-icon {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(255, 215, 100, 0.9), rgba(230, 200, 150, 0.7));
  position: relative;
  box-shadow: 0 0 8px rgba(255, 215, 100, 0.4);
}

.moon-phase .moon-icon::after {
  content: '';
  position: absolute;
  width: 12px;
  height: 12px;
  background: #1a0a35;
  border-radius: 50%;
  top: 2px;
  right: 0;
}

/* === 魔法书页脚 === */
.grimoire-footer {
  text-align: center;
  color: rgba(160, 120, 200, 0.5);
  font-size: 0.75em;
  padding: 20px 0;
  border-top: 1px solid rgba(180, 140, 220, 0.1);
  letter-spacing: 2px;
}

.grimoire-footer::before {
  content: '✧';
  margin-right: 8px;
  color: rgba(255, 215, 100, 0.5);
}

.grimoire-footer::after {
  content: '✧';
  margin-left: 8px;
  color: rgba(255, 215, 100, 0.5);
}

/* === 魔法按钮 === */
.spell-button {
  background: linear-gradient(135deg, rgba(80, 40, 120, 0.9), rgba(60, 30, 100, 0.95));
  border: 2px solid rgba(255, 215, 100, 0.5);
  border-radius: 50%;
  width: 56px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255, 215, 100, 1);
  font-size: 1.4em;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 
    0 0 15px rgba(255, 215, 100, 0.3),
    inset 0 0 20px rgba(0, 0, 0, 0.2);
}

.spell-button:hover {
  border-color: rgba(255, 215, 100, 0.9);
  box-shadow: 
    0 0 25px rgba(255, 215, 100, 0.5),
    inset 0 0 20px rgba(255, 215, 100, 0.1);
  transform: scale(1.05);
}

.spell-button:active {
  transform: scale(0.98);
}

/* === 渐变边框聊天消息 === */
.magic-message-box {
  background: linear-gradient(135deg, rgba(30, 15, 60, 0.9), rgba(20, 10, 40, 0.95));
  border: 1px solid rgba(180, 140, 220, 0.3);
  border-radius: 16px;
  padding: 16px;
  position: relative;
  overflow: hidden;
}

.magic-message-box::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 215, 100, 0.5), 
    rgba(180, 140, 220, 0.5),
    rgba(255, 215, 100, 0.5),
    transparent
  );
  animation: shimmer 3s ease-in-out infinite;
  background-size: 200% 100%;
}

/* === 消息顶部装饰 === */
.message-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid rgba(180, 140, 220, 0.2);
}

.message-header .character-name {
  color: rgba(255, 215, 100, 1);
  font-weight: 600;
  text-shadow: 0 0 10px rgba(255, 215, 100, 0.3);
}

.message-header .message-time {
  color: rgba(200, 160, 240, 0.6);
  font-size: 0.85em;
}

/* === 场景分隔线 === */
.scene-divider {
  position: relative;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 20px 0;
}

.scene-divider::before {
  content: '';
  position: absolute;
  width: 30%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 215, 100, 0.3));
  left: 0;
}

.scene-divider::after {
  content: '';
  position: absolute;
  width: 30%;
  height: 1px;
  background: linear-gradient(90deg, rgba(255, 215, 100, 0.3), transparent);
  right: 0;
}

.scene-divider .divider-star {
  color: rgba(255, 215, 100, 0.6);
  font-size: 14px;
  margin: 0 12px;
}

.scene-divider .divider-text {
  color: rgba(200, 160, 240, 0.8);
  font-size: 0.9em;
  letter-spacing: 4px;
}

/* === 页面边框装饰 === */
.page-border {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  border: 2px solid rgba(255, 215, 100, 0.2);
  border-radius: 16px;
  margin: 8px;
  z-index: 9999;
  box-shadow: 
    inset 0 0 30px rgba(180, 140, 220, 0.1),
    0 0 30px rgba(180, 140, 220, 0.1);
}

.page-border::before {
  content: '';
  position: absolute;
  top: 4px;
  left: 4px;
  right: 4px;
  bottom: 4px;
  border: 1px solid rgba(255, 215, 100, 0.1);
  border-radius: 12px;
}

/* === 魔法发光效果 === */
.magic-glow {
  box-shadow: 
    0 0 10px rgba(255, 215, 100, 0.3),
    0 0 20px rgba(180, 140, 220, 0.2),
    0 0 30px rgba(100, 50, 150, 0.1);
}

/* === 文本发光效果 === */
.text-glow {
  text-shadow: 
    0 0 5px rgba(255, 215, 100, 0.5),
    0 0 10px rgba(255, 215, 100, 0.3),
    0 0 15px rgba(180, 140, 220, 0.2);
}

/* === 金色按钮悬停效果 === */
button.magic-btn {
  position: relative;
  overflow: hidden;
}

button.magic-btn::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 215, 100, 0.2), 
    transparent
  );
  transition: left 0.5s ease;
}

button.magic-btn:hover::after {
  left: 100%;
}
'''

# 将新增的CSS添加到现有CSS的末尾
theme['custom_css'] = theme['custom_css'] + magic_css_additions

# 更新主题名称
theme['name'] = '神秘紫色魔法主题 v2'

# 保存更新后的主题
with open('/workspace/神秘紫色魔法主题.json', 'w', encoding='utf-8') as f:
    json.dump(theme, f, indent=2, ensure_ascii=False)

print('主题已成功更新为神秘紫色魔法主题 v2！')
