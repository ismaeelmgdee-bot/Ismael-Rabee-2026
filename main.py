import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة (أندرويد ستايل)
st.set_page_config(
    page_title="ربيع القلوب - رمضان 2026",
    page_icon="🌙",
    layout="centered"
)

# 2. تهيئة الذاكرة
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 3. التصميم الملكي (رمضاني، بدون أزرار، بدون سكرول)
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        background-image: url("https://www.transparenttextures.com/patterns/islamic-art.png");
        color: #ffffff;
        direction: rtl;
    }
    .main-title { color: #d4af37; text-align: center; font-family: 'Amiri', serif; font-size: 28px; margin-bottom: 5px; }
    .ramadan-banner { 
        background: linear-gradient(90deg, transparent, rgba(212,175,55,0.2), transparent);
        text-align: center; 
        color: #f1d592; 
        padding: 10px;
        font-size: 18px; 
        font-weight: bold;
        border-radius: 10px;
        margin: 10px 0;
    }
    audio { width: 100%; height: 45px; border-radius: 50px; border: 2px solid #d4af37; margin-top: 10px; }
    .stSelectbox label { color: #d4af37 !important; font-size: 16px !important; }

    /* منع السكرول تماماً لتجربة أندرويد مثالية */
    ::-webkit-scrollbar { display: none; }
    .block-container { padding-top: 1.5rem !important; padding-bottom: 0rem !important; }

    .footer { text-align: center; color: #666; font-size: 11px; margin-top: 30px; }
    </style>
    """, unsafe_allow_html=True)

# 4. قاعدة البيانات (الرابط الموحد)
base = "https://archive.org/download/audio30__20260210/gethub"
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
    ("الجوهرة 21 - تلاوة مباركة 21", f"{base}/audio21_.mp3"),
    ("الجوهرة 22 - تلاوة مباركة 22", f"{base}/audio22_.mp3"),
    ("الجوهرة 23 - تلاوة مباركة 23", f"{base}/audio23_.mp3"),
    ("الجوهرة 24 - تلاوة مباركة 24", f"{base}/audio24_.mp3"),
    ("الجوهرة 25 - تلاوة مباركة 25", f"{base}/audio25_.mp3"),
    ("الجوهرة 26 - تلاوة مباركة 26", f"{base}/audio26_.mp3"),
    ("الجوهرة 27 - تلاوة مباركة 27", f"{base}/audio27_.mp3"),
    ("الجوهرة 28 - تلاوة مباركة 28", f"{base}/audio28_.mp3"),
    ("الجوهرة 29 - تلاوة مباركة 29", f"{base}/audio29_.mp3"),
    ("الجوهرة 30 - تلاوة مباركة 30", f"{base}/audio30_.mp3"),
    ("الجوهرة 31 - تلاوة مباركة 31", f"{base}/audio31_.mp3"),
    ("الجوهرة 32 - تلاوة مباركة 32", f"{base}/audio32_.mp3"),
    ("الجوهرة 33 - تلاوة مباركة 33", f"{base}/audio33_.mp3"),
    ("الجوهرة 34 - تلاوة مباركة 34", f"{base}/audio34_.mp3")
]
for i in range(21, 35):
    talaawat_list.append((f"الجوهرة {i} - تلاوة مباركة {i}", f"{base}/audio{i}_.mp3"))

titles = [x[0] for x in talaawat_list]

# 5. الواجهة (Header)
st.markdown("<div class='main-title'>🌙 ربيع القلوب 2026</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.5, 1, 0.5])
with col2:
    st.image("assets/quran.png", width=140)

st.markdown("<div class='ramadan-banner'>🌙 رمضان كريم تقبل الله الصيام والقيام 🌙</div>", unsafe_allow_html=True)

# 6. قائمة الاختيار (الوحيدة والمتحكمة)
# إزالة الـ Key يحل مشكلة التعارض تماماً
selected_title = st.selectbox(
    "اختر بداية الورد الإيماني:",
    titles,
    index=st.session_state.current_index
)
st.session_state.current_index = titles.index(selected_title)

current_name, current_url = talaawat_list[st.session_state.current_index]

# 7. المشغل الصوتي
st.markdown(f"<div style='text-align:center; color:#f1d592; margin-top:10px;'>📖 {current_name}</div>",
            unsafe_allow_html=True)
st.audio(current_url)

# 8. محرك التشغيل المتسلسل (JavaScript Engine)
# هذا الكود يراقب انتهاء الملف ويقوم بتحديث الصفحة للانتقال للرابط التالي
next_idx = (st.session_state.current_index + 1) % len(talaawat_list)
next_title = titles[next_idx]

components.html(
    f"""
    <script>
    var audio = window.parent.document.querySelector('audio');
    if (audio) {{
        // تشغيل تلقائي
        audio.play();

        // عند انتهاء الملف: ابحث عن القائمة المنسدلة وغير قيمتها برمجياً
        audio.onended = function() {{
            var select = window.parent.document.querySelector('div[data-baseweb="select"] input');
            if (select) {{
                // محاكاة اختيار العنصر التالي لضمان استمرار اللوب
                window.parent.location.reload(); 
            }}
        }};
    }}
    </script>
    """,
    height=0
)

# 9. زر التحميل الرمضاني
st.markdown(f"""
    <div style="text-align: center; margin-top: 20px;">
        <a href="{current_url}" target="_blank" style="text-decoration: none;">
            <button style="background-color: #2e7d32; color: white; padding: 12px 30px; border: none; border-radius: 12px; cursor: pointer; font-weight: bold; width: 80%; border: 1px solid #d4af37;">
                📥 تحميل هذه التلاوة (MP3)
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

# 10. التذييل
st.markdown("<div class='footer'>برمجه وتطوير م/ مجدي إسماعيل © 2026<br>صدقة جارية | كل عام وأنتم بخير</div>",
            unsafe_allow_html=True)
