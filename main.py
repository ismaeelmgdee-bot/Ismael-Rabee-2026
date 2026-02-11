import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="ربيع القلوب 2026",
    page_icon="🌙",
    layout="centered"
)

# 2. تهيئة الذاكرة
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 3. التصميم الملكي (أندرويد + رمضان + No Scroll)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; background-image: url("https://www.transparenttextures.com/patterns/islamic-art.png"); color: #ffffff; direction: rtl; }
    .main-title { color: #d4af37; text-align: center; font-family: 'Amiri', serif; font-size: 26px; margin-top: -10px; }
    .ramadan-banner { background: rgba(212,175,55,0.1); text-align: center; color: #f1d592; padding: 8px; font-size: 16px; border-radius: 12px; border: 1px solid rgba(212,175,55,0.3); margin: 5px 0; }
    audio { width: 100%; height: 45px; border-radius: 50px; border: 2px solid #d4af37; }
    .stSelectbox label { color: #d4af37 !important; font-size: 14px !important; }
    ::-webkit-scrollbar { display: none; }
    .block-container { padding-top: 1rem !important; }
    /* إخفاء زر الانتقال الآلي ليبقى المظهر نظيفاً */
    .stButton { display: none; }
    </style>
    """, unsafe_allow_html=True)

# 4. القائمة الكاملة (34 جوهرة)
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
titles = [x[0] for x in talaawat_list]

# 5. منطق الانتقال الآلي
def move_next():
    st.session_state.current_index = (st.session_state.current_index + 1) % len(talaawat_list)

# 6. الواجهة
st.markdown("<div class='main-title'>🌙 ربيع القلوب 2026</div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([0.6, 1, 0.6])
with col2: st.image("assets/quran.png", width=120)
st.markdown("<div class='ramadan-banner'>🌙 رمضان كريم تقبل الله الصيام والقيام 🌙</div>", unsafe_allow_html=True)

selected_title = st.selectbox("اختر بداية الورد:", titles, index=st.session_state.current_index)

# تحديث الفهرس عند الاختيار اليدوي
if titles.index(selected_title) != st.session_state.current_index:
    st.session_state.current_index = titles.index(selected_title)
    st.rerun()

current_name, current_url = talaawat_list[st.session_state.current_index]

# 7. المشغل الصوتي (بدون KEY لحل مشكلة TypeError)
st.markdown(f"<div style='text-align:center; color:#f1d592; font-size:14px; margin-bottom:5px;'>🔔 جاري الاستماع: {current_name}</div>", unsafe_allow_html=True)
audio_placeholder = st.empty()
audio_placeholder.audio(current_url)

# 8. زر مخفي للانتقال (تستخدمه الجافا سكريبت)
st.button("NextTrigger", on_click=move_next)

# 9. حقن الجافا سكريبت الاحترافية (MediaSession + Auto-Advance)
components.html(f"""
    <script>
    var audio = window.parent.document.querySelector('audio');
    
    if ('mediaSession' in navigator) {{
        navigator.mediaSession.metadata = new MediaMetadata({{
            title: '{current_name}',
            artist: 'الشيخ عبد الباسط عبد الصمد',
            album: 'ربيع القلوب 2026',
            artwork: [{{ src: 'https://archive.org/download/audio30__20260210/assets/quran.png', sizes: '512x512', type: 'image/png' }}]
        }});
        
        navigator.mediaSession.setActionHandler('nexttrack', function() {{
            window.parent.document.querySelector('button').click();
        }});
    }}

    if (audio) {{
        audio.play().catch(e => console.log("Waiting for user interaction"));
        
        audio.onended = function() {{
            var btn = window.parent.document.querySelector('button');
            if(btn) btn.click();
        }};
    }}
    </script>
    """, height=0)

# 10. زر التحميل
st.markdown(f"""
    <div style="text-align: center; margin-top: 15px;">
        <a href="{current_url}" target="_blank" style="text-decoration: none;">
            <button style="background-color: #2e7d32; color: white; padding: 10px; border-radius: 12px; width: 80%; border: 1px solid #d4af37; cursor: pointer; font-size: 14px; font-weight: bold;">
                📥 تحميل الجوهرة (MP3)
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div style='text-align:center; color:#666; font-size:10px; margin-top:20px;'>م/ مجدي إسماعيل © 2026 | صدقة جارية</div>", unsafe_allow_html=True)
