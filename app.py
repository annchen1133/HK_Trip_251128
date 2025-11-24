import streamlit as st

# --- 1. 頁面設定 (必須是第一行) ---
st.set_page_config(page_title="HK Trip 2025", page_icon="🇭🇰", layout="centered")

# --- 2. CSS 魔法 (讓它長得像 App 的關鍵) ---
st.markdown("""
    <style>
    /* 全局字體與顏色 */
    .main {
        background-color: #1E1E1E; /* 深灰背景 */
        color: #FFFFFF;
    }
    
    /* 標題樣式 */
    h1 { color: #FFD700 !important; font-size: 28px !important; }
    h3 { color: #FFA500 !important; }
    
    /* 模擬截圖中的黃色標籤 */
    .tag {
        background-color: #D4AF37;
        color: black;
        padding: 4px 12px;
        border-radius: 15px;
        font-size: 14px;
        font-weight: bold;
        margin-right: 5px;
        display: inline-block;
    }
    
    /* 行程卡片區塊 */
    .card {
        background-color: #2D2D2D;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border-left: 4px solid #D4AF37;
    }
    
    /* 時間軸樣式 */
    .time-col { color: #AAAAAA; font-weight: bold; font-size: 14px; }
    .content-title { font-weight: bold; font-size: 16px; margin-bottom: 0px;}
    .content-note { color: #888888; font-size: 13px; }
    
    /* 隱藏預設選單 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. 自定義函式：畫出一行行程 ---
def timeline(time, icon, title, note=""):
    # 使用欄位來模擬時間軸: [時間] [圖示] [內容]
    col1, col2, col3 = st.columns([1, 0.5, 4.5])
    with col1:
        st.markdown(f'<div class="time-col" style="padding-top:5px;">{time}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div style="font-size:20px;">{icon}</div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="content-title">{title}</div>', unsafe_allow_html=True)
        if note:
            st.markdown(f'<div class="content-note">{note}</div>', unsafe_allow_html=True)
    st.markdown('<div style="margin-bottom: 15px;"></div>', unsafe_allow_html=True) # 間距

# --- 4. 頂部資訊區 ---
st.markdown("# 🇭🇰 香港三日・美食漫遊")
st.markdown("日期：11/28 ~ 11/30 (3天2夜) | 4人朋友旅行")
st.markdown("""
    <div>
        <span class="tag">迪士尼 Disney</span>
        <span class="tag">堅尼地城</span>
        <span class="tag">爆食之旅</span>
    </div>
    <br>
""", unsafe_allow_html=True)

# --- 5. 航班資訊 (兩欄排列) ---
with st.container(border=True):
    st.markdown("### ✈️ 航班資訊")
    f1, f2 = st.columns(2)
    with f1:
        st.markdown("**去程 (11/28)**")
        st.caption("CX407 | 08:00 TPE → 10:15 HKG")
    with f2:
        st.markdown("**回程 (11/30)**")
        st.caption("CX402 | 18:35 HKG → 20:35 TPE")

# --- 6. 每日行程 (Tabs) ---
tab1, tab2, tab3 = st.tabs(["Day 1 (五)", "Day 2 (六)", "Day 3 (日)"])

# === Day 1 ===
with tab1:
    # 當日主題卡片
    st.markdown("""
        <div class="card">
            <div style="font-size:18px; font-weight:bold;">✨ 迪士尼童話 + 在地宵夜</div>
            <div style="font-size:12px; color:#ccc;">主題：樂園・童趣</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 🕒 每日行程時間軸")
    timeline("08:00", "🛫", "桃園機場出發", "國泰航空 CX407")
    timeline("10:15", "🛬", "抵達香港機場", "入境、領行李")
    timeline("11:30", "🚗", "寄放行李 @ 迪士尼", "第1停車場 12、13號位")
    timeline("12:00", "🎢", "香港迪士尼樂園", "盡情玩樂！看煙火！")
    timeline("20:00", "🍲", "晚餐：十大碗粥麵專家", "必點：腸粉、豬手麵")
    timeline("21:30", "🧁", "甜點：HeSheEat", "旺角甜點名店")
    timeline("22:30", "🛍️", "散步：新世紀廣場/花墟", "還有體力就去廟街！")

# === Day 2 ===
with tab2:
    st.markdown("""
        <div class="card">
            <div style="font-size:18px; font-weight:bold;">📸 堅尼地城 + 港島爆食</div>
            <div style="font-size:12px; color:#ccc;">主題：文青・街拍・名店</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 🕒 每日行程時間軸")
    timeline("08:00", "☀️", "佐敦出發", "地鐵前往堅尼地城")
    timeline("09:00", "🥟", "早餐：新興食家", "港式飲茶老店")
    timeline("10:30", "☕️", "打卡：% Arabica", "C出口籃球場海景")
    timeline("12:00", "🏙️", "中環/上環 City Walk", "太平山摩羅上街、大館")
    timeline("13:30", "🍖", "午餐：龍邦燒味 / 沾仔記", "看哪家排隊人少")
    timeline("15:00", "🍪", "伴手禮大戰", "珍妮曲奇 / Bakehouse / Vission Bakery")
    timeline("17:00", "🏙️", "灣仔散策", "藍屋、太原街")
    timeline("19:30", "🌃", "晚餐/宵夜：廟街夜市", "媽咪雞蛋仔、方太糕品舖")

# === Day 3 ===
with tab3:
    st.markdown("""
        <div class="card">
            <div style="font-size:18px; font-weight:bold;">🛍️ 九龍衝刺 + 機場補貨</div>
            <div style="font-size:12px; color:#ccc;">主題：購物・返程</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 🕒 每日行程時間軸")
    timeline("08:30", "🥟", "早茶：倫敦大酒店", "傳統手推車港點")
    timeline("10:30", "🛍️", "尖沙咀 海港城", "Pop Mart、Bakehouse、生煎包")
    timeline("13:00", "🥤", "手搖：霸王茶姬", "最後一杯飲料")
    timeline("13:30", "🍪", "伴手禮：帝苑餅店", "蝴蝶酥必買")
    timeline("15:00", "🚌", "搭巴士 A22 前往機場", "跟香港說拜拜")
    timeline("16:00", "✈️", "機場最後血拼", "榮華小桃酥、黯然銷魂飯")
    timeline("18:35", "🛫", "飛機起飛 回台灣", "CX402 -> 20:35 抵達 TPE")

#
