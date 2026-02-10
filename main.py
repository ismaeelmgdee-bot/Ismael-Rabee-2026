import streamlit as st

st.set_page_config(page_title="ربيع القلوب 2026", page_icon="📖")

# التصميم الملكي
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; direction: rtl; }
    h1 { color: #d4af37 !important; text-align: center; }
    audio { width: 100%; border-radius: 50px; background-color: #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# القاعدة الصحيحة للروابط (تأكد من وجود download وشرطة مائلة في النهاية)
base = "https://archive.org/download/audio4_quraan/"

# قائمة الجواهر (جربت لك تعديل الأسماء لتكون أكثر دقة)
talaawat_list = [
    ("الجوهرة 1", f"{base}audio12_.mp3"),
    ("الجوهرة 2", f"{base}audio14_.mp3"),
    ("الجوهرة 11 (الإخلاص)", f"{base}Al-Ikhlas.mp3") # جرب هذا أولاً
]

st.title("🌙 مكتبة ربيع القلوب")

selection = st.selectbox("اختر التلاوة:", [x[0] for x in talaawat_list])

# البحث عن الرابط المختار
current_url = ""
for name, url in talaawat_list:
    if name == selection:
        current_url = url

st.write(f"جاري محاولة الاتصال بالملف...")

# المشغل
if current_url:
    st.audio(current_url)
    # هذا الرابط للمساعدة في اكتشاف الخطأ، اضغط عليه لتعرف هل يعمل أم لا
    st.markdown(f"[🔗 اضغط هنا لفتح الملف مباشرة والتأكد منه]({current_url})")

st.caption("إذا ظهرت صفحة 404 عند الضغط على الرابط أعلاه، فالاسم في الكود يختلف عن الاسم في الأرشيف.")
