import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة (أندرويد ستايل)
st.set_page_config(
    page_title="ربيع القلوب 2026",
    page_icon="🌙",
    layout="centered"
)

# 2. تهيئة الذاكرة
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 3. سحر التصميم (CSS) - الفانوس، إخفاء السكرول، والوضع الليلي
st.markdown("""
    <style>
    /* إعدادات الخلفية والخطوط */
    .stApp {
        background-color: #0d1117;
        background-image: url("https://www.transparenttextures.com/patterns/islamic-art.png");
        color: #ffffff; direction: rtl;
    }
    
    /* إخفاء السكرول بار تماماً */
    ::-webkit-scrollbar { display: none; }
    .block-container { 
        padding-top: 2rem !important; 
        padding-bottom: 5rem !important;
        overflow: hidden; /* منع التمرير الزائد */
    }

    /* تنسيق العناوين */
    .main-title { 
        color: #d4af37; text-align: center; font-family: 'Amiri', serif; 
        font-size: 28px; margin-top: 10px; text-shadow: 2px 2px 5px #000; 
        z-index: 2; position: relative;
    }
    
    /* تنسيق الفانوس المتحرك */
    .lantern-container {
        position: fixed;
        top: -20px;
        left: 20px;
        z-index: 999;
        animation: swing 3s infinite ease-in-out alternate;
        transform-origin: top center;
    }
    .lantern-img { width: 60px; filter: drop-shadow(0 0 10px #ffeb3b); }
    
    @keyframes swing {
        0% { transform: rotate(5deg); }
        100% { transform: rotate(-5deg); }
    }

    /* تنسيق المشغل والقائمة */
    audio { width: 100%; height: 45px; border-radius: 50px; border: 2px solid #d4af37; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.2); }
    .stSelectbox label { color: #d4af37 !important; font-size: 16px !important; }
    
    /* تنسيق التذييل */
    .footer { 
        text-align: center; color: #888; font-size: 12px; 
        margin-top: 20px; border-top: 1px solid rgba(212,175,55,0.2); 
        padding-top: 10px;
    }
    .footer a { color: #d4af37; text-decoration: none; font-weight: bold; }
    
    /* إخفاء الأزرار التقنية */
    .stButton { display: none; } 
    </style>
    
    <div class="lantern-container">
        <img src="https://cdn-icons-png.flaticon.com/512/3655/3655460.png" class="lantern-img">
    </div>
    """, unsafe_allow_html=True)

# 4. قائمة الجواهر (الموحدة والثابتة)
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
def trigger_next():
    st.session_state.current_index = (st.session_state.current_index + 1) % len(talaawat_list)

# 6. الواجهة
col1, col2, col3 = st.columns([0.2, 1, 0.2])
with col2:
    st.image("assets/quran.png", width=120)

st.markdown("<div class='main-title'>🌙 ربيع القلوب 2026</div>", unsafe_allow_html=True)

# القائمة المنسدلة (بدون أخطاء Key)
selected_title = st.selectbox(
    "اختر بداية الورد الإيماني:",
    titles,
    index=st.session_state.current_index
)

# تحديث الحالة عند التغيير اليدوي
if titles.index(selected_title) != st.session_state.current_index:
    st.session_state.current_index = titles.index(selected_title)
    st.rerun()

current_name, current_url = talaawat_list[st.session_state.current_index]

st.markdown("---")

# 7. المشغل الصوتي (مستقر)
st.markdown(f"<div style='text-align:center; color:#f1d592; margin-bottom:10px;'>🔉 {current_name}</div>", unsafe_allow_html=True)
audio_placeholder = st.empty()
audio_placeholder.audio(current_url)

# زر مخفي للمزامنة
st.button("Next_Sync", on_click=trigger_next)

# 8. الجافا سكريبت (MediaSession + Auto-Play)
components.html(f"""
    <script>
    var audio = window.parent.document.querySelector('audio');
    
    // إعدادات الميديا في شريط الإشعارات
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
        audio.play().catch(e => console.log("Waiting for interaction..."));
        audio.onended = function() {{
            var btn = window.parent.document.querySelector('button');
            if(btn) btn.click();
        }};
    }}
    </script>
    """, height=0)

# 9. زر التحميل وتذييل الصفحة
st.markdown(f"""
    <div style="text-align: center; margin-top: 15px;">
        <a href="{current_url}" target="_blank" style="text-decoration: none;">
            <button style="background-color: #2e7d32; color: white; padding: 10px 20px; border: none; border-radius: 12px; cursor: pointer; font-weight: bold; width: 85%; box-shadow: 0 2px 5px rgba(0,0,0,0.3);">
                📥 تحميل الجوهرة (MP3)
            </button>
        </a>
    </div>
    
    <div class='footer'>
        برمجه وتطوير م/ <a href="https://www.facebook.com/share/1FuFVriwWP/" target="_blank">مجدي إسماعيل</a> © 2026<br>
        <div style="margin-top:8px; font-size:13px; color:#d4af37;">✨ صدقة جارية | رمضان مبارك ✨</div>
    </div>
""", unsafe_allow_html=True)
