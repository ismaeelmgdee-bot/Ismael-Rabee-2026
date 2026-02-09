import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="ربيع القلوب 2026", page_icon="🌙", layout="centered")

# لمسة جمالية للواجهة
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; direction: rtl; }
    h1 { color: #4CAF50; text-align: center; font-family: 'Amiri', serif; }
    .stAudio { width: 100%; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌙 ربيع القلوب")
st.write("<p style='text-align: center;'>نظام البث المباشر المستقر</p>", unsafe_allow_html=True)

# قاعدة البيانات (الروابط الصحيحة)
import streamlit as st

# إعدادات الواجهة
st.set_page_config(page_title="ربيع القلوب 2026", page_icon="🌙")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; direction: rtl; }
    h1 { color: #4CAF50; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌙 مكتبة ربيع القلوب الصوتية")

# --- قاعدة بيانات التلاوات (من 1 إلى 20) ---
talaawat = {
    "التلاوة الأولى (Audio 1)": "https://archive.org/download/audio1_/audio1_.mp3",
    "التلاوة الثانية (Audio 2)": "https://archive.org/download/audio2_/audio2_.mp3",
    "التلاوة الثالثة (Audio 3)": "https://archive.org/download/audio3_/audio3_.mp3",
    "التلاوة الرابعة (Audio 4)": "https://archive.org/download/audio4_/audio4_.mp3",
    "التلاوة الخامسة (Audio 5)": "https://archive.org/download/audio5_/audio5_.mp3",
    "التلاوة السادسة (Audio 6)": "https://archive.org/download/audio6_/audio6_.mp3",
    "التلاوة السابعة (Audio 7)": "https://archive.org/download/audio7_/audio7_.mp3",
    "التلاوة الثامنة (Audio 8)": "https://archive.org/download/audio8_/audio8_.mp3",
    "التلاوة التاسعة (Audio 9)": "https://archive.org/download/audio9_/audio9_.mp3",
    "التلاوة العاشرة (Audio 10)": "https://archive.org/download/audio10_/audio10_.mp3",
    "التلاوة الحادية عشر (Audio 11)": "https://archive.org/download/audio11_/audio11_.mp3",
    "التلاوة الثانية عشر (Audio 12)": "https://archive.org/download/audio12_/audio12_.mp3",
    "التلاوة الثالثة عشر (Audio 13)": "https://archive.org/download/audio13_/audio13_.mp3",
    "التلاوة الرابعة عشر (Audio 14)": "https://archive.org/download/audio14_/audio14_.mp3",
    "التلاوة الخامسة عشر (Audio 15)": "https://archive.org/download/audio15_/audio15_.mp3",
    "التلاوة السادسة عشر (Audio 16)": "https://archive.org/download/audio16_/audio16_.mp3",
    "التلاوة السابعة عشر (Audio 17)": "https://archive.org/download/audio17_/audio17_.mp3",
    "التلاوة الثامنة عشر (Audio 18)": "https://archive.org/download/audio18_/audio18_.mp3",
    "التلاوة التاسعة عشر (Audio 19)": "https://archive.org/download/audio19_/audio19_.mp3",
    "التلاوة العشرون (Audio 20)": "https://archive.org/download/audio20_/audio20_.mp3"
}

# واجهة الاختيار (ستظهر لك الآن جميع الخيارات في المتصفح)
choice = st.selectbox("اختر التلاوة المباركة:", list(talaawat.keys()))

st.write("---")

# الحصول على الرابط
url = talaawat[choice]

st.subheader(f"استماع: {choice}")
st.audio(url, format="audio/mp3")

st.info("💡 ملاحظة: تأكد من رفع كل ملف للأرشيف ليعمل الرابط بنجاح.")
st.caption("برمجة وتطوير: إسماعيل | ربيع القلوب 2026")

# واجهة الاختيار
selection = st.selectbox("اختر السورة أو التلاوة:", list(talaawat.keys()))
audio_url = talaawat[selection]

st.write("---")

# عرض صورة افتراضية أو شعار البرنامج
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<h1 style='font-size: 100px; text-align: center;'>📖</h1>", unsafe_allow_html=True)

st.subheader(f"الآن تستمع إلى: {selection}")

# مشغل الصوت الاحترافي (سيعمل الآن فوراً!)
st.audio(audio_url, format="audio/mp3")

st.success("✅ متصل بسحابة Archive.org")
st.caption("تطوير: إسماعيل | ربيع القلوب v1.1")