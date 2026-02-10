import streamlit as st

# 1. إعدادات الصفحة (الأيقونة في عنوان المتصفح)
st.set_page_config(
    page_title="ربيع القلوب 2026",
    page_icon="assets/quran.png",
    layout="centered"
)

# 2. تهيئة الذاكرة للتنقل
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 3. التصميم الملكي (أسود وذهبي)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; direction: rtl; }
    h1 { color: #d4af37 !important; text-align: center; font-family: 'Amiri', serif; text-shadow: 2px 2px 4px #000; }
    .stSelectbox label { color: #d4af37 !important; font-size: 18px; }
    audio { width: 100%; border-radius: 50px; background-color: #d4af37; margin-top: 10px; }
    .stButton button { background-color: #d4af37; color: #000; border-radius: 10px; font-weight: bold; width: 100%; }
    .stButton button:hover { background-color: #f1d592; color: #000; border: 1px solid #fff; }
    .footer { text-align: center; color: #666; font-size: 12px; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 4. عرض الأيقونة في صدر الصفحة (مناسبة للهاتف)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("assets/quran.png", width=100)

st.markdown("<h1 style='margin-top: -20px;'>🌙 تطبيق ربيع القلوب</h1>", unsafe_allow_html=True)

# 5. قاعدة بيانات الروابط (gethub)
base = "https://archive.org/download/audio4_quraan/gethub"
base_new = "https://archive.org/download/audio30__202602/gethub"

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
    ("الجوهرة 20 - تلاوة ختامية", f"{base}/audio1_.mp3"),
    # الإضافات الجديدة (الجواهر الـ 14 الإضافية)
    ("الجوهرة 21 - تلاوة مباركة 21", f"{base_new}/audio21_.mp3"),
    ("الجوهرة 22 - تلاوة مباركة 22", f"{base_new}/audio22_.mp3"),
    ("الجوهرة 23 - تلاوة مباركة 23", f"{base_new}/audio23_.mp3"),
    ("الجوهرة 24 - تلاوة مباركة 24", f"{base_new}/audio24_.mp3"),
    ("الجوهرة 25 - تلاوة مباركة 25", f"{base_new}/audio25_.mp3"),
    ("الجوهرة 26 - تلاوة مباركة 26", f"{base_new}/audio26_.mp3"),
    ("الجوهرة 27 - تلاوة مباركة 27", f"{base_new}/audio27_.mp3"),
    ("الجوهرة 28 - تلاوة مباركة 28", f"{base_new}/audio28_.mp3"),
    ("الجوهرة 29 - تلاوة مباركة 29", f"{base_new}/audio29_.mp3"),
    ("الجوهرة 30 - تلاوة مباركة 30", f"{base_new}/audio30_.mp3"),
    ("الجوهرة 31 - تلاوة مباركة 31", f"{base_new}/audio31_.mp3"),
    ("الجوهرة 32 - تلاوة مباركة 32", f"{base_new}/audio32_.mp3"),
    ("الجوهرة 33 - تلاوة مباركة 33", f"{base_new}/audio33_.mp3"),
    ("الجوهرة 34 - تلاوة مباركة 34", f"{base_new}/audio34_.mp3")

]

# 6. دوال التنقل
def next_track():
    if st.session_state.current_index < len(talaawat_list) - 1:
        st.session_state.current_index += 1

def prev_track():
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1

# 7. أزرار التحكم
col_p, col_n = st.columns(2)
with col_p:
    st.button("⏮️ التلاوة السابقة", on_click=prev_track)
with col_n:
    st.button("التلاوة التالية ⏭️", on_click=next_track)

# 8. قائمة الاختيار
titles = [x[0] for x in talaawat_list]
selected_title = st.selectbox("اختر من جواهر التلاوات:", titles, index=st.session_state.current_index)

# تحديث الفهرس
st.session_state.current_index = titles.index(selected_title)
current_name, current_url = talaawat_list[st.session_state.current_index]

st.markdown("---")

# 9. المشغل الصوتي
st.subheader(f"📖 {current_name}")
st.audio(current_url)

# 10. زر التحميل
st.markdown(f"""
    <div style="text-align: center; margin-top: 20px;">
        <a href="{current_url}" target="_blank" style="text-decoration: none;">
            <button style="background-color: #2e7d32; color: white; padding: 12px 24px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">
                📥 تحميل الملف الصوتي (MP3)
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

# تذييل الصفحة
st.markdown("<div class='footer'>برمجه وتطوير  م/ مجدي إسماعيل © 2026<br>صدقة جارية لكل من نشرها</div>", unsafe_allow_html=True)
