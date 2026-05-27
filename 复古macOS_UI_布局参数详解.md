# 复古macOS UI蓝（改1）CSS布局参数详解

## 一、基础配置参数

### 1.1 全局布局设置
- **头像基础宽度**: `--avatar-base-width: 48px`
- **头像基础高度**: `--avatar-base-height: 48px`
- **通用圆角**: `--genericRadius: 0px`（所有元素无圆角）
- **滚动条宽度**: `--scrollBarWidth: 3px`
- **页面内边距**: `--pagePadding: calc(var(--scrollBarWidth) + 9px)` → 12px
- **通用行高**: `--genericLineHeight: calc(var(--mainFontSize) * 1.9)`

### 1.2 字体相关
- **主字体大小**: `--mainFontSize: calc(var(--fontScale) * 16px)`
- **顶栏图标大小**: `--topbarIconSize: calc(var(--mainFontSize) * 1.3)`
- **底部表单图标大小**: `--bottomFormIconSize: calc(var(--mainFontSize) * 1.5)`
- **底部表单块内边距**: `--bottomFormBlockPadding: calc(var(--mainFontSize) / 1.5)`

---

## 二、聊天区域布局

### 2.1 消息容器（.mes）
```css
.mes {
    display: flex;
    margin: 0px !important;
    padding-bottom: 0px !important;
    border: none;
    background-color: transparent !important;
}
```

### 2.2 消息块（.mes_block）
```css
.mes_block {
    display: flex;
    flex-direction: column;
    flex: 1 1 auto;
    padding-top: 8px;
    padding-left: 0px !important;
    overflow: hidden;
}
```

---

## 三、头像布局

### 3.1 头像容器（.mesAvatarWrapper）
```css
.mes .mesAvatarWrapper {
    flex: 0 0 auto;
    display: flex;
    align-items: flex-start;
    position: relative;
    padding: 8px 8px 0 0px !important;
    pointer-events: auto;
}
```

### 3.2 用户消息头像（右侧）
```css
.mes[is_user="true"] .mesAvatarWrapper {
    padding: 8px 0px 0 8px !important;
}
```

### 3.3 最后一条消息的头像
```css
.last_mes .mesAvatarWrapper {
    padding-bottom: 16px !important;
}
```

### 3.4 普通消息最后一条
```css
.last_mes .mesAvatarWrapper {
    padding-bottom: 5px !important;
}
```

### 3.5 头像样式
```css
.mes .mesAvatarWrapper .avatar {
    border-radius: var(--genericRadius) !important;
    filter: drop-shadow(0px 0px 2px var(--buttonFill));
}
```

---

## 四、名字区域布局

### 4.1 名字容器（.ch_name）
```css
.mes .ch_name {
    display: flex;
    flex-direction: row;
    align-items: baseline;
    gap: 8px;
    border-radius: var(--genericRadius);
    padding: 16px;
    margin-bottom: 8px;
    border-bottom: 1px solid var(--SmartThemeBorderColor);
}
```

### 4.2 名字容器的flex容器
```css
.mes_block .ch_name .flex-container {
    min-width: 0;
    flex: 1 1 auto;
}
```

### 4.3 用户消息名字（反向排列）
```css
body .mes[is_user="true"] .mes_block .ch_name,
body .mes[is_user="true"] .mes_block .ch_name .flex-container {
    flex-direction: row-reverse;
}
```

---

## 五、文本区域布局

### 5.1 文本容器（.mes_text）
```css
.mes_text {
    padding: 0px 2px !important;
    line-height: var(--genericLineHeight);
}
```

### 5.2 段落样式
```css
.mes_text p {
    margin-bottom: 12px;
}
```

### 5.3 编辑按钮容器
```css
.mes_edit_buttons {
    filter: drop-shadow(0px 0px 2px var(--buttonFill));
}
```

---

## 六、引用和代码样式

### 6.1 引用块
```css
.mes_text blockquote,
.mes_reasoning blockquote {
    background-color: var(--accentColorOverlay);
    border-left: var(--accentColor) 2px solid;
    padding: 8px;
    margin-bottom: 8px;
}
```

### 6.2 对白样式（q标签）
```css
.mes_text q {
    color: var(--SmartThemeQuoteColor);
    background-color: var(--accentColorOverlay);
    margin: 0px 6px 0px 3px;
    padding: 5px 4px;
    font-size: calc(var(--mainFontSize) * 0.98);
    box-shadow: inset -1.5px -1.5px 0px var(--SmartThemeQuoteColor);
}
```

### 6.3 行内代码
```css
code {
    background-color: var(--accentColorOverlay);
    color: var(--SmartThemeUnderlineColor);
    border: none;
    border-bottom: 1.5px dashed var(--SmartThemeUnderlineColor);
    border-radius: var(--genericRadius);
    font-size: calc(var(--mainFontSize) * 0.98);
    padding: 4px 3px;
}
```

### 6.4 代码块
```css
.mes_text pre {
    background-color: var(--accentColorOverlay);
    padding: 12px 14px;
    border-radius: var(--genericRadius);
    font-size: calc(var(--mainFontSize) * 0.95);
    letter-spacing: 0.3px;
    border-left: 2px solid var(--SmartThemeUnderlineColor);
}
```

---

## 七、按钮和控件布局

### 7.1 快捷回复按钮
```css
.menu_button {
    filter: none !important;
    background-color: var(--buttonFill);
    box-shadow: var(--boxShadowSubtle);
}
```

### 7.2 输入框和控件
```css
select,
.range-block-counter input,
.text_pole,
textarea,
.neo-range-input {
    filter: none !important;
    background-color: var(--buttonFill) !important;
    border: 1px solid var(--SmartThemeBorderColor) !important;
    margin: 4px 0px !important;
    border-radius: var(--genericRadius);
    box-shadow: var(--boxShadowSubtle);
}
```

### 7.3 发送按钮输入框
```css
#send_textarea {
    background-color: transparent !important;
    font-size: calc(var(--mainFontSize) - 1px);
}
```

### 7.4 滑块样式
```css
input.neo-range-slider[type="range"]::-webkit-slider-thumb {
    border-radius: var(--genericRadius) !important;
    width: 12px;
    height: 12px;
    border: none;
    box-shadow: none !important;
    background-color: var(--scrollBarColor) !important;
}
```

---

## 八、顶栏和底栏布局

### 8.1 顶栏和发送表单
```css
#top-bar,
#send_form {
    background-color: color-mix(in srgb, var(--navBackgroundColor) 50%, transparent 50%) !important;
    padding: 6px 8px;
    border: 1px solid var(--SmartThemeBorderColor);
}
```

### 8.2 顶栏和发送表单（无模糊）
```css
body.no-blur #top-bar,
body.no-blur #send_form {
    background-color: var(--navBackgroundColor) !important;
    padding: 6px 8px;
}
```

---

## 九、角色选择区域

### 9.1 角色分页器
```css
#rm_print_characters_pagination {
    background-color: var(--menuBackgroundColor);
    border-radius: var(--genericRadius);
    padding: 8px;
    margin: 8px;
}
```

### 9.2 角色头像容器
```css
.avatar-container.selected {
    border: 2px solid var(--SmartThemeBorderColor);
    border-radius: var(--genericRadius);
    box-shadow: var(--boxShadowSubtle);
}
```

---

## 十、思维链区域布局

### 10.1 思维链内容
```css
.mes_reasoning_details .mes_reasoning_summary,
.mes_reasoning,
.reasoning_edit_textarea {
    margin-left: 16px !important;
    margin-right: 16px !important;
}
```

### 10.2 思维链头部
```css
.mes_reasoning_header {
    border: 1px solid var(--accentColor);
    border-radius: var(--genericRadius);
    background-color: transparent;
    justify-content: center;
    letter-spacing: 0.5px;
    margin: 0px;
    transition: all 0.25s ease;
    cursor: pointer;
    box-shadow: var(--boxShadowSubtleAlt);
}
```

### 10.3 思维链头部块
```css
.mes_reasoning_header_block {
    margin-top: 8px;
    margin-bottom: 16px;
}
```

### 10.4 思维链主体
```css
.mes_reasoning {
    border-left: var(--SmartThemeUnderlineColor) solid 2px;
    color: var(--SmartThemeBodyColor);
}
```

---

## 十一、滚动条布局

```css
::-webkit-scrollbar {
    width: var(--scrollBarWidth);
    height: var(--scrollBarWidth);
}

::-webkit-scrollbar-track {
    background: transparent;
}

::-webkit-scrollbar-thumb:vertical,
::-webkit-scrollbar-thumb:horizontal {
    border-radius: var(--genericRadius);
    background-color: var(--scrollBarColor);
    border: none;
    box-shadow: none;
}
```

---

## 十二、分页和滑动区域

### 12.1 最后一条助手消息
```css
div[is_user="false"].last_mes .mes_block {
    padding-bottom: 48px;
}
```

### 12.2 滑动计数器
```css
.swipes-counter {
    margin: 0px;
    min-width: max-content;
}
```

### 12.3 滑动区域
```css
.flex-container.swipeRightBlock {
    display: flex;
    flex-direction: row-reverse;
    padding-bottom: 20px;
    margin-right: 16px;
}
```

---

## 十三、预设管理区域

### 13.1 预设列表
```css
#completion_prompt_manager_list {
    background-color: var(--menuBackgroundColor) !important;
    padding: 0px 8px;
    border: none !important;
    box-shadow: none !important;
}
```

### 13.2 预设项
```css
#completion_prompt_manager #completion_prompt_manager_list li.completion_prompt_manager_prompt {
    background-color: var(--buttonFill);
    border: 1px solid var(--SmartThemeBorderColor);
    border-radius: 2px;
    padding: 8px;
    margin-bottom: 8px;
}
```

---

## 十四、热切换角色区

```css
#HotSwapWrapper > div {
    overflow: auto hidden;
    flex-wrap: nowrap;
    justify-content: flex-start;
    gap: 8px;
    min-height: calc(var(--avatar-base-height) * 1.5);
}

#HotSwapWrapper {
    overflow: hidden;
}
```

---

## 十五、表格样式

```css
.mes_text table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    border-radius: var(--genericRadius);
    overflow: hidden;
}

.mes_text th,
.mes_text td {
    border: none;
    border-right: 1px solid var(--accentColor);
    padding: 10px 14px;
    text-align: left;
    border-bottom: 1px solid var(--accentColor);
}
```

---

## 十六、其他通用间距

### 16.1 设置行
```css
#userSettingsRowOne {
    margin: 8px 0px;
}
```

### 16.2 范围块标题
```css
.range-block-title {
    margin: 8px 0px;
    text-align: left;
}
```

### 16.3 范围块
```css
.range-block {
    margin-bottom: 8px;
}
```

### 16.4 复选框标签
```css
.checkbox_label {
    margin: 2px 0px;
}
```

### 16.5 分割线
```css
hr {
    background-image: none;
    background-color: var(--SmartThemeUnderlineColor);
    margin: 12px 0px;
}
```

---

## 十七、响应式设计

### 17.1 手机适配（max-width: 600px）

```css
@media (max-width: 600px) {
    #rm_extensions_block {
        padding-right: 24px;
    }
    
    #bg_menu_content {
        width: 100%;
    }
    
    #character-script-list,
    #global-script-list,
    #saved_scoped_scripts,
    #saved_regex_scripts {
        flex-wrap: wrap !important;
        max-width: 75vw;
    }
    
    .regex-script-label,
    #global-script-list .script-item,
    #character-script-list .script-item {
        max-width: 75vw;
        flex-wrap: wrap;
        border-radius: var(--genericRadius) !important;
        background-color: var(--buttonFill) !important;
        gap: 4px !important;
        padding-top: 8px !important;
        padding-bottom: 4px !important;
        border: 1px solid var(--SmartThemeBorderColor) !important;
        box-shadow: var(--boxShadowSubtle) !important;
    }
    
    #extensions_url,
    #extensions_api_key {
        max-width: 100px !important;
    }
}
```

### 17.2 Safari适配

```css
@supports (-webkit-touch-callout: none) {
    #chat {
        padding-right: var(--pagePadding);
    }
    
    .drawer-content:not(#left-nav-panel):not(#right-nav-panel) {
        max-width: 100dvw;
    }
    
    #world_popup {
        width: 100%;
    }
}
```

### 17.3 iPad Safari适配（min-width: 768px）

```css
@supports (-webkit-touch-callout: none) {
    @media screen and (min-width: 768px) {
        #sheld {
            width: var(--sheldWidth);
            margin-left: auto;
            margin-right: auto;
        }
        
        #top-bar,
        #top-settings-holder .drawer .drawer-content {
            width: var(--sheldWidth);
        }
        
        #left-nav-panel,
        #right-nav-panel,
        #character_popup,
        #world_popup,
        .drawer-content {
            top: var(--topBarBlockSize);
        }
        
        #character_popup,
        #world_popup,
        .drawer-content {
            margin-top: 0px;
            top: var(--topBarBlockSize);
        }
    }
}
```

---

## 十八、世界书选择器

```css
#rightSendForm > #global-combined-selector-button {
    width: var(--bottomFormBlockSize);
    height: var(--bottomFormBlockSize);
    background-color: var(--navBackgroundColor) !important;
    border: none !important;
    padding: 0px !important;
    margin-left: 0px !important;
    opacity: 0.7;
}

#rightSendForm > #global-combined-selector-button:hover {
    opacity: 1 !important;
    background-color: var(--navBackgroundColor) !important;
}
```

---

## 十九、插件适配样式

### 19.1 快捷回复菜单
```css
#quick-reply-menu {
    border-radius: var(--genericRadius) !important;
    border: 1px solid var(--SmartThemeBorderColor) !important;
    background-color: var(--menuBackgroundColor) !important;
    box-shadow: var(--boxShadowSubtle) !important;
}

.quick-reply-list {
    border: 1px solid var(--accentColor) !important;
    border-radius: var(--genericRadius) !important;
}

.quick-reply-item {
    background-color: var(--buttonFill) !important;
    color: var(--SmartThemeBodyColor) !important;
    border-radius: var(--genericRadius) !important;
}
```

### 19.2 酒馆助手
```css
.title-item-active {
    background-color: var(--accentColorOverlay) !important;
    border-bottom: 1.5px solid var(--SmartThemeUnderlineColor);
}
```

### 19.3 记忆插件
```css
#table_drawer_content {
    padding-left: 8px !important;
    padding-right: 8px !important;
}
```

---

## 二十、总结：核心布局数值

| 元素 | 属性 | 数值 |
|------|------|------|
| 头像宽度 | width | 48px |
| 头像高度 | height | 48px |
| 头像间距 | padding | 8px |
| 用户头像右间距 | padding-right | 8px |
| 用户头像左间距 | padding-left | 8px |
| 消息间距 | margin | 0px |
| 名字间距 | gap | 8px |
| 名字内边距 | padding | 16px |
| 名字底部边距 | margin-bottom | 8px |
| 文本左右边距 | padding | 0px 2px |
| 段落间距 | margin-bottom | 12px |
| 按钮阴影偏移 | box-shadow | 2px 2px 0px |
| 控件间距 | margin | 4px |
| 段落间距 | margin-bottom | 12px |
| 范围块间距 | margin-bottom | 8px |
| 思维链左右边距 | margin | 16px |
| 最后消息底部间距 | padding-bottom | 48px |
| 滑块尺寸 | width/height | 12px |
| 圆角 | border-radius | 0px |
| 滚动条宽度 | width/height | 3px |
