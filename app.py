import streamlit as st

# --- 1. 頁面設定 ---
st.set_page_config(page_title="HK Trip 2025", page_icon="🇭🇰", layout="centered")

# --- 2. CSS 樣式重構 (復刻日系時間軸風格) ---
st.markdown("""
    <style>
    /* 全局設定 */
    .stApp {
        background-color: #F4F7F6; /* 米色底圖背景 */
    }
    body, p, div, span, h1, h2, h3, li {
        color: #333333 !important;
        font-family: "Helvetica Neue", Arial, sans-serif;
    }
    
    /* 隱藏 Streamlit 預設元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stTabs [data-baseweb="tab-list"] { display: none; } 
    [data-testid="stVerticalBlock"] { gap: 0rem; }

    /* --- 自定義元件樣式 --- */
    
    /* 1. 白色大卡片容器 */
    .main-card-container {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 25px 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-top: 20px;
        margin-bottom: 30px;
    }

    /* 2. 藍色日期標題標籤 */
    .day-header-badge {
        background-color: #4A90E2; /* 鮮藍色 */
        color: white !important;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 16px;
        display: inline-block;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(74, 144, 226, 0.3);
    }
    .day-header-text {
        font-size: 18px;
        font-weight: bold;
        margin-left: 10px;
        color: #333 !important;
    }

    /* 3. 淺藍色提示橫幅 */
    .alert-banner {
        background-color: #E6F0FF; /* 淺藍底 */
        color: #4A90E2 !important;
        text-align: center;
        padding: 12px;
        border-radius: 12px;
        font-weight: bold;
        font-size: 15px;
        margin-bottom: 25px;
    }

    /* --- 4. 時間軸核心樣式 (重點) --- */
    .timeline-container {
        position: relative; /* 為了讓灰線定位 */
        padding-left: 10px;
    }

    /* 那條貫穿的灰色直線 */
    .timeline-container::before {
        content: '';
        position: absolute;
        top: 15px;
        left: 84px; /* 調整線的位置以對齊圓點中心 */
        width: 2px;
        height: 95%;
        background-color: #E0E0E0;
        z-index: 0;
    }

    .timeline-row {
        display: flex;
        position: relative;
        margin-bottom: 25px;
        z-index: 1; /* 確保內容在灰線上方 */
    }

    /* 左側時間 */
    .t-time {
        min-width: 65px;
        font-weight: bold;
        color: #888888 !important;
        font-size: 14px;
        padding-top: 3px;
        text-align: right;
        margin-right: 15px;
    }

    /* 中間圓點容器 */
    .t-dot-container {
        width: 30px;
        display: flex;
        justify-content: center;
        margin-right: 15px;
    }

    /* 圓點本體 */
    .t-dot {
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background-color: #BDBDBD; /* 預設灰色 */
        border: 3px solid #FFFFFF; /* 白邊讓它跳脫灰線 */
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }
    /* 不同狀態的圓點顏色 */
    .dot-blue { background-color: #4A90E2; }
    .dot-red  { background-color: #FF5252; }
    .dot-gray { background-color: #BDBDBD; }

    /* 右側內容 */
    .t-content {
        flex: 1;
        padding-top: 0px;
    }
    .t-title {
        font-weight: bold;
        font-size: 17px;
        color: #222 !important;
        margin-bottom: 5px;
    }
    .t-note {
        color: #666666 !important;
        font-size: 14px;
        line-height: 1.5;
        margin-bottom: 8px;
    }

    /* 5. 黃色重點提示框 */
    .highlight-box {
        background-color: #FFFBE6; /* 米黃底 */
        border-left: 4px solid #FFD700; /* 金黃邊 */
        padding: 8px 12px;
        border-radius: 4px;
        font-size: 13px;
        color: #665C2A !important;
        margin-top: 8px;
    }
    
    /* 航班資訊區塊 */
    .flight-info-box {
        background-color: #FFFFFF;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 20px;
        border: 1px solid #E0E0E0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 新版函式：繪製單行時間軸 ---
def timeline(time, title, note="", status="gray", highlight=None):
    dot_class = f"dot-{status}"
    highlight_html = f'<div class="highlight-box">{highlight}</div>' if highlight else ""

    html_code = f"""
    <div class="timeline-row">
        <div class="t-time">{time}</div>
        <div class="t-dot-container">
            <div class="t-dot {dot_class}"></div>
        </div>
        <div class="t-content">
            <div class="t-title">{title}</div>
            <div class="t-note">{note}</div>
            {highlight_html}
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)

# --- 4. 輔助函式：繪製每一天的白色大卡片 ---
def draw_day_card(day_tag, day_title, sub_title):
    # 標題區塊
    st.markdown(f"""
        <div>
            <span class="day-header-badge">{day_tag}</span>
            <span class="day-header-text">{day_title}</span>
        </div>
    """, unsafe_allow_html=True)

    # 白色卡片開始
    st.markdown('<div class="main-card-container">', unsafe_allow_html=True)
    
    # 提示橫幅 (顯示當日主題)
    st.markdown(f'<div class="alert-banner">{sub_title}</div>', unsafe_allow_html=True)
    
    # 時間軸容器開始
    st.markdown('<div class="timeline-container">', unsafe_allow_html=True)

def end_day_card():
    st.markdown('</div></div>', unsafe_allow_html=True)


# ================= 頁面內容開始 =================

st.markdown("# 🇭🇰 香港三日遊")

# --- 航班資訊 ---
with st.expander("✈️ 查看航班資訊"):
    st.markdown("""
    <div class="flight-info-box">
        <strong>去程 (11/28)</strong><br> CX407 | 08:00 TPE → 10:15 HKG<br><br>
        <strong>回程 (11/30)</strong><br> CX402 | 18:35 HKG → 20:35 TPE
    </div>
    """, unsafe_allow_html=True)

# 選擇天數
selected_day = st.radio("選擇天數", ["Day 1 (五)", "Day 2 (六)", "Day 3 (日)"], horizontal=True, label_visibility="collapsed")

# === Day 1 內容 (文字皆使用您提供的版本) ===
if selected_day == "Day 1 (五)":
    draw_day_card(day_tag="Day 1", day_title="11/28 (五)", sub_title="✨ 迪士尼 + 在地宵夜 (主題：遊樂園)")
    
    timeline("08:00", "🛫 桃園機場出發", "國泰航空 CX407", status="blue")
    timeline("10:15", "🛬 抵達香港機場", "入境、領行李", status="blue")
    timeline("11:30", "🚗 寄行李", "第1停車場 12、13號位", status="blue")
    timeline("12:00", "🎢 香港迪士尼樂園", "冰雪奇緣gogo", status="blue")
    timeline("20:00", "🍲 十大碗粥麵專家", "推薦腸粉、豬手麵", status="gray")
    timeline("21:30", "🧁 HeSheEat", "旺角甜點名店", status="gray")
    timeline("22:30", "🛍️ 新世紀廣場/花墟", "逛到無聊去廟街 Day2 預習", status="gray")

    end_day_card()

# === Day 2 內容 (文字皆使用您提供的版本) ===
elif selected_day == "Day 2 (六)":
    draw_day_card(day_tag="Day 2", day_title="11/29 (六)", sub_title="📸 堅尼地城 + 港島爆食 (主題：city walk・街拍)")

    timeline("08:00", "☀️ 佐敦出發", "地鐵前往堅尼地城", status="blue")
    timeline("09:00", "🥟 新興食家", "港式飲茶老店", status="blue")
    timeline("10:30", "☕️ % Arabica", "拍照景點", status="blue", highlight="C出口籃球場海景")
    timeline("12:00", "🏙️ 中環/上環", "太平山摩羅上街、大館", status="gray")
    timeline("13:30", "🍖 龍邦燒味 / 沾仔記", "看哪家排隊人少", status="gray")
    timeline("15:00", "🍪 伴手禮大戰", "珍妮曲奇 / Bakehouse / Vission Bakery", status="gray")
    timeline("17:00", "🏙️ 灣仔逛逛", "藍屋、太原街", status="gray")
    timeline("19:30", "🌃 廟街夜市", "媽咪雞蛋仔、方太糕品舖", status="gray")

    end_day_card()

# === Day 3 內容 (文字皆使用您提供的版本) ===
elif selected_day == "Day 3 (日)":
    draw_day_card(day_tag="Day 3", day_title="11/30 (日)", sub_title="🛍️ 九龍衝刺 + 機場補貨 (主題：購物)")

    timeline("08:30", "🥟 倫敦大酒店", "傳統手推車港點", status="blue")
    timeline("10:30", "🛍️ 尖沙咀 海港城", "Pop Mart、Bakehouse、生煎包", status="gray")
    timeline("13:00", "🥤 霸王茶姬", "有求必應", status="gray")
    timeline("13:30", "🍪 帝苑餅店", "蝴蝶酥必買", status="gray")
    timeline("15:00", "🚌 前往機場", "巴士A22", status="red")
    timeline("16:00", "✈️ 機場 最後的補貨", "榮華小桃酥、黯然銷魂飯", status="gray")
    timeline("18:35", "🛫 飛機起飛 回台灣", "CX402 -> 20:35 抵達", status="gray")

    end_day_card()

# --- 底部 ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Reference: Threads @chenasquirrel")
