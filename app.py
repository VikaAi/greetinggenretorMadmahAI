import streamlit as st

st.set_page_config(page_title="מחולל ברכות תכנותיות", page_icon="✂️", layout="centered")

# עיצוב CSS מותאם אישית כדי ליצור כרטיסיות נפרדות לגזירה ועיצוב נקי
st.markdown("""
    <style>
    .card-box {
        background-color: #161b22;
        border: 2px dashed #58a6ff;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        font-family: 'Courier New', Courier, monospace;
        direction: ltr;
        text-align: left;
        color: #7ee787;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    .card-header {
        color: #8b949e;
        font-size: 0.85rem;
        margin-bottom: 10px;
        border-bottom: 1px solid #30363d;
        padding-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("✂️ מחולל כרטיסיות ברכה תכנותיות לגזירה")
st.write("מלאי את הפרמטרים וצרי כרטיסיות מעוצבות ומוכנות לגזירה לכיתה!")

# אזור הקלט למורה (נשתמש ב-selectbox פשוט ובטוח)
teacher_name = st.text_input("שם המורה:", value="נטע")
grade = st.selectbox("כיתה / שכבה:", ["כיתה י'", "כיתה י'א", "כיתה י'ב", "מגמת סייבר"])
topic = st.selectbox("שפת תכנות / נושא:", ["C#", "Python", "Java", "רקורסיה"])
event = st.selectbox("אירוע:", ["מבחן / בגרות", "חג פסח", "חנוכה", "סיום שנה"])

if st.button("✨ צור כרטיסיות לגזירה"):
    
    # יצירת ברכות מותאמות
    if "מבחן" in event:
        greeting_code = f"""try 
{{
    Console.WriteLine("התחלת פתרון מבחן ב-{topic}!");
    Student.SolveWithConfidence();
}}
catch (Exception ex)
{{
    Console.WriteLine("שגיאה נתפסה: הלחץ מבוטל!");
}}
finally 
{{
    Console.WriteLine("עשיתם את המקסימום. בהצלחה!");
}}

// {grade} | בהצלחה! מאמינה בכם ❤️
// {teacher_name}"""
    elif "פסח" in event:
        greeting_code = f"""// ניקוי חמץ מערכתי ל-{grade}
GC.Collect();
DELETE FROM Brain WHERE ItemType = 'Stress';
UPDATE Student SET Status = 'Chilling', Battery = 100;

// חג פסח שמח ומלא מנוחה! 🍷
// {teacher_name}"""
    elif "חנוכה" in event:
        greeting_code = f"""for (int c = 1; c <= 8; c++)
{{
    Console.WriteLine($"הדלקת נר #{{c}}: אור ואנרגיה ל{grade}!");
}}
Student.EnergyLevel += 500; // סופגניות

// חג חנוכה מאיר ושמח! 🕎
// {teacher_name}"""
    else:
        greeting_code = f"""public static void FinishYear()
{{
    Console.WriteLine("Exit Code 0: סיום מוצלח ל{grade} ב{topic}!");
}}

// כל הכבוד על הדרך! גאה בכם 🏆
// {teacher_name}"""

    st.success("הכרטיסיות נוצרו בהצלחה! ניתן לגזור אותן או להדפיס כ-PDF.")
    
    st.subheader("📋 כרטיסיות מוכנות לגזירה (תצוגה מקדימה):")
    
    # יצירת הדמיה של 3 כרטיסיות נפרדות ועצמאיות לגזירה (ריבועים)
    for i in range(1, 4):
        card_html = f"""
        <div class="card-box">
            <div class="card-header">✂️ כרטיסייה #{i} | {grade} - {event}</div>
            <pre style="margin:0; color: #7ee787; background: transparent;">{greeting_code}</pre>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        
    st.info("💡 להדפסת הכרטיסיות כקובץ PDF נקי לגזירה: לחצי על Ctrl+P (או Cmd+P) במקלדת ושמרי את העמוד כ-PDF.")
