import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="ربيع القلوب 2026", page_icon="📖", layout="centered")

# 2. تهيئة الذاكرة
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 3. التصميم الملكي
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; direction: rtl; }
    h1 { color: #d4af37 !important; text-align: center; font-family: 'Amiri', serif; }
    .stButton button { background-color: #d4af37; color: #000; border-radius: 12px; font-weight: bold; width: 100%; border: none; }
    audio { width: 100%; border-radius: 50px; background-color: #d4af37; margin-top: 20px; }
    audio::-webkit-media-controls-panel { background-color: #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# 4. روابط مباشرة وصحيحة 100% من سيرفر الأرشيف
# لاحظ استخدمنا الرابط المباشر لكل ملف لضمان عدم حدوث خطأ
base = "https://archive.org/download/audio4_quraan"

talaawat_list = [
    ("الجوهرة 1 - سورة الكهف وقصار السور", f"{base}/audio12_.mp3"),
    ("الجوهرة 2 - سورة يوسف (حلب 1956)", f"{base}/audio14_.mp3"),
    ("الجوهرة 3 - تلاوة نادرة (الحج)", f"{base}/audio7_.mp3"),
    ("الجوهرة 4 - الواقعة والطارق (1956)", f"{base}/audio8_.mp3"),
    ("الجوهرة 5 - قصة موسى (القصص)", f"{base}/audio2_.mp3"),
    ("الجوهرة 6 - وجاءوا أباهم عشاء (يوسف)", f"{base}/audio18_.mp3"),
    ("الجوهرة 7 - التلاوة الأروع على الإطلاق", f"{base}/audio16_.mp3"),
    ("الجوهرة 8 - تلاوة فوق السحاب (1)", f"{base}/audio4_.mp3"),
    ("الجوهرة 9 - تلاوة فوق السحاب (2)", f"{base}/audio5_.mp3"),
    ("الجوهرة 10 - مقطع نادر جودة عالية", f"{base}/audio19_.mp3"),
    ("الجوهرة 11 - سورة الإخلاص", f"{base}/Al-Ikhlas.mp3"),
    ("الجوهرة 12 - تلاوة مباركة 10", f"{base}/audio10_.mp3"),
    ("الجوهرة 13 - تلاوة مباركة 11", f"{base}/audio11_.mp3"),
    ("الجوهرة 14 - تلاوة مباركة 13", f"{base}/audio13_.mp3"),
    ("الجوهرة 15 - تلاوة مباركة 15", f"{base}/audio15_.mp3"),
    ("الجوهرة 16 - تلاوة مباركة 17", f"{base}/audio17_.mp3"),
    ("الجوهرة 17 - تلاوة مباركة 3", f"{base}/audio3_.mp3"),
    ("الجوهرة 18 - تلاوة مباركة 6", f"{base}/audio6_.mp3"),
    ("الجوهرة 19 - تلاوة مباركة 9", f"{base}/audio9_.mp3"),
    ("الجوهرة 20 - تلاوة ختامية", f"{base}/audio1_.mp3")
]

# 5. دوال التحكم
def next_track():
    if st.session_state.current_index < len(talaawat_list) - 1:
        st.session_state.current_index += 1

def prev_track():
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1

# 6. الواجهة
st.title("🌙 مكتبة ربيع القلوب الصوتية")

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⏮️ السابق"): prev_track()
with col3:
    if st.button("التالي ⏭️"): next_track()

current_name, current_url = talaawat_list[st.session_state.current_index]

st.selectbox("اختر من الجواهر:", [x[0] for x in talaawat_list], 
             index=st.session_state.current_index, key="sb_nav")

# تحديث الفهرس بناءً على اختيار القائمة
for i, item in enumerate(talaawat_list):
    if item[0] == st.session_state.sb_nav:
        st.session_state.current_index = i

st.markdown("---")
st.markdown("<h1 style='font-size: 100px; margin-top: -30px;'>📖</h1>", unsafe_allow_html=True)
st.subheader(f"قيد الاستماع: {current_name}")

# 7. مشغل الصوت مع فحص الرابط
st.audio(current_url, format="audio/mp3")

st.info(f"🔗 رابط الملف الحالي للتأكد: {current_url}")
st.caption("جميع الحقوق محفوظة © مجدي إسماعيل 2026")
