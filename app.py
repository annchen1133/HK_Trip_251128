import streamlit as st

# --- 設定網頁標題與圖示 ---
st.set_page_config(page_title="🇭🇰 HK Vibe Trip", page_icon="✈️")

# --- CSS 美化 (讓手機版更好看) ---
st.markdown("""
    <style>
    .stButton>button {width: 100%; border-radius: 20px;}
    .big-font {font-size:20px !important; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

# --- 標題區 ---
st.title("🇭🇰 香港 1128-1130 Vibe Trip")
st.caption("行程僅供參考，有更好的選擇就 gogo！🚀")
st.divider()

# --- 側邊欄 (基本資訊) ---
with st.sidebar:
    st.header("🔍 行前準備")
    st.checkbox("護照 & 簽證 (港簽/台胞證)")
    st.checkbox("八達通 (手機版)")
    st.checkbox("網卡/漫遊")
    st.info("✈️ 去程: CX407 (08:00-10:15)\n✈️ 回程: CX402 (18:35-20:35)")

# --- 行程邏輯 ---
tab1, tab2, tab3 = st.tabs(["Day 1 (五)", "Day 2 (六)", "Day 3 (日)"])

with tab1:
    st.header("🎡 Day 1: 迪士尼與宵夜")
    st.info("📍 12:00 包車出發迪士尼")
    
    col1, col2 = st.columns([1, 3])
    with col1: st.checkbox("寄行李", key="d1_1")
    with col2: st.write("第1停車場 12、13號位")
    
    st.markdown("### 🎢 主線任務")
    if st.checkbox("迪士尼暢玩", key="d1_disney"):
        st.balloons() # 點擊會有氣球特效！
        st.success("Have a magical day!")
        
    st.markdown("### 🍲 晚餐/宵夜 (旺角/太子)")
    with st.expander("港仔推薦清單 (點擊展開)"):
        st.write("- **十大碗粥麵專家**: 腸粉、豬手麵")
        st.write("- **HeSheEat**: 甜點")
        st.write("- **新世紀廣場**: Hollister, Sanrio")
    
    st.warning("💡 還有體力？去廟街！沒體力？回飯店睡覺💤")

with tab2:
    st.header("📸 Day 2: 港島文青行")
    st.write("08:00 佐敦 -> 堅尼地城")
    
    st.checkbox("☕️ % Arabica (堅尼地城籃球場拍照)", key="d2_1")
    st.checkbox("🥟 新興食家 (早茶)", key="d2_2")
    
    st.divider()
    st.markdown("#### 🇭🇰 中環/上環 City Walk")
    places = st.multiselect(
        "你想去哪裡逛？(可多選)",
        ["太平山摩羅上街", "大館", "中環街市", "香港摩天輪", "Vission Bakery", "Bakehouse", "珍妮曲奇"],
        default=["Vission Bakery", "大館"]
    )
    if places:
        st.write(f"GoGo! 目標: {', '.join(places)}")

    st.divider()
    st.markdown("#### 🌃 晚上: 灣仔 & 廟街")
    st.checkbox("🍽️ 晚餐: 竺扶大班燒味 / 維港冰室", key="d2_dinner")
    st.checkbox("🌙 廟街: 媽咪雞蛋仔 / 方太糕品", key="d2_temple")

with tab3:
    st.header("🛍️ Day 3: 最後衝刺")
    st.checkbox("🥟 倫敦大酒店 (早茶)", key="d3_1")
    st.checkbox("🛍️ 海港城 (泡泡瑪特/Bakehouse)", key="d3_2")
    st.checkbox("🍪 帝苑餅店 (蝴蝶酥)", key="d3_3")
    
    st.divider()
    st.error("🚨 15:00 必須出發去機場 (Bus A22)")
    with st.expander("✈️ 機場必買"):
        st.write("- 榮華餅店小桃酥")
        st.write("- 蛋塔王")
        st.write("- 黯然銷魂飯")
