import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="ربيع القلوب 2026",
    page_icon="assets/quran.png",
    layout="centered"
)

# 2. تهيئة الذاكرة
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 3. التصميم المطور (واجهة أندرويد احترافية)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; direction: rtl; }
    h1 { color: #d4af37 !important; text-align: center; font-family: 'Amiri', serif; font-size: 24px !important; margin-top: 5px; }
    .stSelectbox label { color: #d4af37 !important; font-size: 15px !important; }
    audio { width: 100%; height: 45px; border-radius: 50px; background-color: #d4af37; margin-top: 5px; }
    .stButton button { background-color: #d4af37 !important; color: #000 !important; border-radius: 10px; font-weight: bold; height: 40px; }
    .footer { text-align: center; color: #666; font-size: 11px; margin-top: 15px; }
    .block-container { padding-top: 1rem !important; }
    /* إخفاء السكرول بار */
    ::-webkit-scrollbar { display: none; }
    </style>
    """, unsafe_allow_html=True)

# 4. قاعدة بيانات الروابط الموحدة
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


# 5. دوال التنقل
def sync_selection():
    st.session_state.current_index = titles.index(st.session_state.selector_key)


def next_track():
    if st.session_state.current_index < len(talaawat_list) - 1:
        st.session_state.current_index += 1
        st.session_state.selector_key = titles[st.session_state.current_index]


def prev_track():
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1
        st.session_state.selector_key = titles[st.session_state.current_index]


# 6. الواجهة (الأيقونة والعنوان)
col1, col2, col3 = st.columns([0.5, 1, 0.5])
with col2:
    st.image("assets/quran.png", width=120)
st.markdown("<h1>🌙 تطبيق ربيع القلوب</h1>", unsafe_allow_html=True)

# 7. الأزرار
col_p, col_n = st.columns(2)
with col_p:
    st.button("⏮️ السابق", on_click=prev_track, use_container_width=True)
with col_n:
    st.button("التالي ⏭️", on_click=next_track, use_container_width=True)

selected_title = st.selectbox(
    "اختر من جواهر التلاوات:",
    titles,
    index=st.session_state.current_index,
    key="selector_key",
    on_change=sync_selection
)

current_name, current_url = talaawat_list[st.session_state.current_index]

st.markdown("---")

# 8. المشغل الصوتي (تم حذف الـ key المسبب للخطأ)
st.markdown(f"<div style='text-align:center; font-size:16px; color:#d4af37; font-weight:bold;'>📖 {current_name}</div>",
            unsafe_allow_html=True)
st.audio(current_url)

# 9. ذكاء الجافا سكريبت (للتشغيل التلقائي والمزامنة)
components.html(
    f"""
    <script>
    var audio = window.parent.document.querySelector('audio');
    if (audio) {{
        // كود لضمان أن المتصفح يدرك تغيير الرابط ويشغله فوراً
        if (audio.src != "{current_url}") {{
            audio.src = "{current_url}";
            audio.play();
        }}

        audio.onended = function() {{
            var buttons = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < buttons.length; i++) {{
                if (buttons[i].innerText.includes('التالي')) {{
                    buttons[i].click();
                    break;
                }}
            }}
        }};
    }}
    </script>
    """,
    height=0
)

# 10. زر التحميل
st.markdown(f"""
    <div style="text-align: center; margin-top: 15px;">
        <a href="{current_url}" target="_blank" style="text-decoration: none;">
            <button style="background-color: #2e7d32; color: white; padding: 10px 20px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; width: 70%;">
                📥 تحميل الملف (MP3)
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='footer'>برمجه وتطوير م/ مجدي إسماعيل © 2026<br>صدقة جارية لكل من نشرها</div>",
            unsafe_allow_html=True)
