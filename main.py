import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="ربيع القلوب 2026", page_icon="📖", layout="centered")

# 2. تهيئة الذاكرة
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 3. التصميم الملكي (مع إصلاح مشغل الصوت)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; direction: rtl; }
    h1 { color: #d4af37 !important; text-align: center; font-family: 'Amiri', serif; }
    .stButton button { background-color: #d4af37; color: #000; border-radius: 12px; font-weight: bold; width: 100%; border: none; }
    audio { width: 100%; border-radius: 50px; background-color: #d4af37; }
    audio::-webkit-media-controls-panel { background-color: #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# 4. قاعدة بيانات "الروابط الآمنة" (باستخدام أسماء الملفات البرمجية)
base_url = "https://archive.org/download/audio4_quraan"

# قمت بمطابقة كل اسم تلاوة برابط الملف البرمجي الصحيح له من سيرفرك
talaawat_list = [
    ("الجوهرة 1 - سورة الكهف وقصار السور", f"{base_url}/audio12_.mp3"),
    ("الجوهرة 2 - سورة يوسف (حلب 1956)", f"{base_url}/audio14_.mp3"),
    ("الجوهرة 3 - تلاوة نادرة (الحج)", f"{base_url}/audio7_.mp3"),
    ("الجوهرة 4 - الواقعة والطارق (1956)", f"{base_url}/audio8_.mp3"),
    ("الجوهرة 5 - قصة موسى (القصص)", f"{base_url}/audio2_.mp3"),
    ("الجوهرة 6 - وجاءوا أباهم عشاء (يوسف)", f"{base_url}/audio18_.mp3"),
    ("الجوهرة 7 - التلاوة الأروع على الإطلاق", f"{base_url}/audio16_.mp3"),
    ("الجوهرة 8 - تلاوة فوق السحاب (1)", f"{base_url}/audio4_.mp3"),
    ("الجوهرة 9 - تلاوة فوق السحاب (2)", f"{base_url}/audio5_.mp3"),
    ("الجوهرة 10 - مقطع نادر جودة عالية", f"{base_url}/audio19_.mp3"),
    ("الجوهرة 11 - سورة الإخلاص", f"{base_url}/Al-Ikhlas.mp3"),
    ("الجوهرة 12 - تلاوة مباركة 10", f"{base_url}/audio10_.mp3"),
    ("الجوهرة 13 - تلاوة مباركة 11", f"{base_url}/audio11_.mp3"),
    ("الجوهرة 14 - تلاوة مباركة 13", f"{base_url}/audio13_.mp3"),
    ("الجوهرة 15 - تلاوة مباركة 15", f"{base_url}/audio15_.mp3"),
    ("الجوهرة 16 - تلاوة مباركة 17", f"{base_url}/audio17_.mp3"),
    ("الجوهرة 17 - تلاوة مباركة 3", f"{base_url}/audio3_.mp3"),
    ("الجوهرة 18 - تلاوة مباركة 6", f"{base_url}/audio6_.mp3"),
    ("الجوهرة 19 - تلاوة مباركة 9", f"{base_url}/audio9_.mp3"),
    ("الجوهرة 20 - تلاوة ختامية", f"{base_url}/audio1_.mp3")
]

# 5. دوال التحكم
def next_track():
    if st.session_state.current_index < len(talaawat_list) - 1:
        st.session_state.current_index += 1

def prev_track():
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1

def update_selection():
    selection = st.session_state.selectbox_selection
    for idx, item in enumerate(talaawat_list):
        if item[0] == selection:
            st.session_state.current_index = idx
            break

# 6. واجهة التحكم
st.title("🌙 مكتبة ربيع القلوب الصوتية")
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⏮️ السابق"): prev_track()
with col3:
    if st.button("التالي ⏭️"): next_track()

current_name, current_url = talaawat_list[st.session_state.current_index]

st.selectbox("قائمة الجواهر:", options=[item[0] for item in talaawat_list], 
             index=st.session_state.current_index, key="selectbox_selection", on_change=update_selection)

st.markdown("---")
st.markdown("<h1 style='font-size: 80px;'>📖</h1>", unsafe_allow_html=True)
st.subheader(f"الآن تستمع إلى: {current_name}")

# 7. تشغيل الصوت
st.audio(current_url, format="audio/mp3", autoplay=True)

st.success("✅ تم تحديث مسارات الصوت الآمنة")
st.caption("جميع الحقوق محفوظة © مجدي إسماعيل 2026")
