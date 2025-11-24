import streamlit as st

# --- 1. 頁面設定 ---
st.set_page_config(page_title="HK Trip 2025", page_icon="🇭🇰", layout="centered")

# --- 2. CSS 樣式 (包含手機版強制橫排設定) ---
st.markdown("""
    <style>
    /* 強制設定為淺色背景 */
    .stApp {
        background-color: #FFFFFF;
    }
    
    /* 全局文字顏色 */
    body, p, div, span, h1, h2, h3 {
        color: #333333 !important;
    }
    
    /* 標題特別色 */
    h1 { color: #000000 !important; font-weight: 800 !important;}
    
    /* 卡片樣式 */
    .card {
        background-color: #F9F9F9;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
        border-left: 5px solid #FFC107;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* 標籤樣式 */
    .tag {
        background-color: #FFF3CD;
        color: #856404 !important;
        padding: 3px 10px;
        border-radius: 15px;
        font-size: 12px;
        font-weight: 600;
        margin-right: 5px;
        display: inline-block;
        border: 1px solid #FFEEBA;
    }

    /* --- 重點：手機版時間軸強制橫排 (Flexbox) --- */
    /* 這一區塊是讓手機不會跑版的關鍵 */
    .timeline-row {
        display: flex;       /* 強制橫向排列 */
        align-items: flex-start;
        margin-bottom: 12px;
        padding-bottom: 8px;
        border-bottom: 1px solid #EEEEEE; 
    }
    
    .t-time {
        min-width: 55px;     /* 固定時間寬度，手機上才不會被擠扁 */
        font-weight: bold;
        color: #888888 !important;
        font-size: 14px;
        padding-top: 2px;
    }
    
    .t-icon {
        min-width: 30px;     /* 固定圖示寬度 */
        font-size: 20px;
        text-align: center;
        margin-right: 10px;
    }
    
    .t-content {
        flex: 1;             /* 剩下的空間都給文字 */
    }
    
    .t-title {
        font-weight: 700;
        font-size: 16px;
        color: #222 !important;
        line-height: 1.4;
    }
    
    .t-note {
        color: #666666 !important;
        font-size: 13px;
        margin-top: 2px;
    }
    
    /* 隱藏多餘選單 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. 新版函式：使用 HTML 繪製行程 (手機不跑版核心) ---
def timeline(time, icon, title, note=""):
    # 這裡直接用 HTML 寫入，不再依賴 st.columns，確保手機顯示正常
    html_code = f"""
    <div class="timeline-row">
        <div class="t-time">{time}</div>
        <div class="t-icon">{icon}</div>
        <div class="t-content">
            <div class="t-title">{title}</div>
            <div class="t-note">{note}</div>
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)

# --- 4. 頂部資訊區 ---
st.markdown("# 🇭🇰 香港三日遊")
st.markdown("**日期：** 11/28 ~ 11/30")
st.markdown("<br>", unsafe_allow_html=True) # 空行

# --- 5. 航班資訊 ---
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
st.write("") 
tab1, tab2, tab3 = st.tabs(["Day 1 (五)", "Day 2 (六)", "Day 3 (日)"])

# === Day 1 ===
with tab1:
    st.markdown("""
        <div class="card">
            <div style="font-size:18px; font-weight:bold; color:#333 !important;">✨ 迪士尼 + 在地宵夜</div>
            <div style="font-size:12px; color:#666 !important;">主題：遊樂園</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 🕒 行程時間軸")
    timeline("08:00", "🛫", "桃園機場出發", "國泰航空 CX407")
    timeline("10:15", "🛬", "抵達香港機場", "入境、領行李")
    timeline("11:30", "🚗", "寄行李", "第1停車場 12、13號位")
    timeline("12:00", "🎢", "香港迪士尼樂園", "冰雪奇緣gogo")
    timeline("20:00", "🍲", "十大碗粥麵專家", "推薦腸粉、豬手麵")
    timeline("21:30", "🧁", "HeSheEat", "旺角甜點名店")
    timeline("22:30", "🛍️", "新世紀廣場/花墟", "逛到無聊去廟街 Day2 預習")

# === Day 2 ===
with tab2:
    st.markdown("""
        <div class="card">
            <div style="font-size:18px; font-weight:bold; color:#333 !important;">📸 堅尼地城 + 港島爆食</div>
            <div style="font-size:12px; color:#666 !important;">主題：city walk・街拍</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 🕒 行程時間軸")
    timeline("08:00", "☀️", "佐敦出發", "地鐵前往堅尼地城")
    timeline("09:00", "🥟", "新興食家", "港式飲茶老店")
    timeline("10:30", "☕️", "% Arabica", "拍照景點")
    timeline("12:00", "🏙️", "中環/上環", "太平山摩羅上街、大館")
    timeline("13:30", "🍖", "龍邦燒味 / 沾仔記", "看哪家排隊人少")
    timeline("15:00", "🍪", "伴手禮大戰", "珍妮曲奇 / Bakehouse / Vission Bakery")
    timeline("17:00", "🏙️", "灣仔逛逛", "藍屋、太原街")
    timeline("19:30", "🌃", "廟街夜市", "媽咪雞蛋仔、方太糕品舖")

# === Day 3 ===
with tab3:
    st.markdown("""
        <div class="card">
            <div style="font-size:18px; font-weight:bold; color:#333 !important;">🛍️ 九龍衝刺 + 機場補貨</div>
            <div style="font-size:12px; color:#666 !important;">主題：購物</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 🕒 行程時間軸")
    timeline("08:30", "🥟", "倫敦大酒店", "傳統手推車港點")
    timeline("10:30", "🛍️", "尖沙咀 海港城", "Pop Mart、Bakehouse、生煎包")
    timeline("13:00", "🥤", "霸王茶姬", "有求必應")
    timeline("13:30", "🍪", "帝苑餅店", "蝴蝶酥必買")
    timeline("15:00", "🚌", "前往機場", "巴士A22")
    timeline("16:00", "✈️", "機場 最後的補貨", "榮華小桃酥、黯然銷魂飯")
    timeline("18:35", "🛫", "飛機起飛 回台灣", "CX402 -> 20:35 抵達")
