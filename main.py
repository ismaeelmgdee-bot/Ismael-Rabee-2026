import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="ربيع القلوب 2026",
    page_icon="🌙",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. تهيئة الذاكرة
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 3. التصميم المطور (إخفاء الزوائد + تنسيق الأيقونة الكبيرة)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    div[data-testid="stStatusWidget"] {display: none;}
    .stDeployButton {display: none;}
    iframe[title="Manage app"] {display: none !important;}

    .stApp {
        background-color: #0d1117;
        background-image: url("https://www.transparenttextures.com/patterns/islamic-art.png");
        color: #ffffff; direction: rtl;
        overflow: hidden;
    }

    .main-title { 
        color: #d4af37; text-align: center; font-family: 'Amiri', serif; 
        font-size: 26px; margin-bottom: 10px; text-shadow: 2px 2px 5px #000;
    }

    audio { width: 100%; height: 45px; border-radius: 50px; border: 2px solid #d4af37; }

    .dev-footer {
        text-align: center; padding: 12px; margin-top: 20px;
        border-top: 1px solid rgba(212,175,55,0.3);
        background: rgba(0,0,0,0.4); border-radius: 12px;
    }
    .dev-footer a { color: #d4af37; text-decoration: none; font-weight: bold; }

    .lantern-container {
        position: fixed; top: -15px; left: 15px; z-index: 9999;
        animation: swing 3s infinite ease-in-out alternate;
        transform-origin: top center;
    }
    .lantern-img { width: 55px; filter: drop-shadow(0 0 10px #ffeb3b); }
    @keyframes swing { 0% { transform: rotate(6deg); } 100% { transform: rotate(-6deg); } }
    </style>
    
    <div class="lantern-container">
        <img src="https://cdn-icons-png.flaticon.com/512/3655/3655460.png" class="lantern-img">
    </div>
    """, unsafe_allow_html=True)

# 4. قاعدة البيانات (الرابط الموحد)
base = "https://archive.org/download/audio30__20260210/gethub"
img_url = "https://archive.org/download/audio30__20260210/assets/quran.png" # الرابط المباشر للأيقونة

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

def trigger_next():
    st.session_state.current_index = (st.session_state.current_index + 1) % len(talaawat_list)

# 5. الواجهة (تصحيح ظهور الأيقونة وتوسيطها)
st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center; padding-top: 10px; margin-bottom: 10px;">
        <img src="{img_url}" width="200" style="filter: drop-shadow(0px 5px 15px rgba(0,0,0,0.6));">
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>🌙 ربيع القلوب 2026</div>", unsafe_allow_html=True)

# زر التثبيت
if st.button("📱 اضغط هنا لتثبيت التطبيق على هاتفك", key="install_btn"):
    st.toast("انقر على النقاط الثلاث (⋮) ثم 'الإضافة إلى الشاشة الرئيسية'", icon="📲")

selected_title = st.selectbox("", titles, index=st.session_state.current_index, label_visibility="collapsed")
if titles.index(selected_title) != st.session_state.current_index:
    st.session_state.current_index = titles.index(selected_title)
    st.rerun()

current_name, current_url = talaawat_list[st.session_state.current_index]

st.markdown(f"<div style='text-align:center; color:#f1d592; font-size:14px; margin: 10px 0;'>📻 {current_name}</div>", unsafe_allow_html=True)
st.audio(current_url)

if st.button("Next_Sync", on_click=trigger_next):
    pass

# 6. الجافا سكريبت (MediaSession + Auto-Advance)
components.html(f"""
    <script>
    var audio = window.parent.document.querySelector('audio');
    window.open = function() {{ return null; }};

    if ('mediaSession' in navigator) {{
        navigator.mediaSession.metadata = new MediaMetadata({{
            title: '{current_name}',
            artist: 'الشيخ عبد الباسط',
            album: 'ربيع القلوب 2026',
            artwork: [{{ src: '{img_url}', sizes: '512x512', type: 'image/png' }}]
        }});
        navigator.mediaSession.setActionHandler('nexttrack', function() {{
            const btn = window.parent.document.querySelector('button[kind="secondary"]');
            if(btn) btn.click();
        }});
    }}

    if (audio) {{
        audio.play().catch(e => console.log("Ready"));
        audio.onended = function() {{
            const btn = window.parent.document.querySelector('button[kind="secondary"]');
            if(btn) btn.click();
        }};
    }}
    </script>
    """, height=0)

# 7. التذييل (المطور مجدي إسماعيل)
st.markdown(f"""
    <div style="text-align: center; margin-top: 15px;">
        <a href="{current_url}" target="_self" style="text-decoration: none;">
            <button style="background-color: #2e7d32; color: white; padding: 10px 25px; border: none; border-radius: 10px; cursor: pointer; font-size: 13px; font-weight: bold;">
                📥 تحميل مباشر (MP3)
            </button>
        </a>
    </div>

    <div class="dev-footer">
        برمجه وتطوير م/ <a href="https://www.facebook.com/share/1FuFVriwWP/" target="_blank">مجدي إسماعيل</a> © 2026<br>
        <p style="margin-top:5px;">🌙 صدقة جارية لمن قام بنشره | استماع متواصل</p>
    </div>
""", unsafe_allow_html=True)
