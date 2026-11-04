import streamlit as st

st.set_page_config(page_title="מחולל ברכות תכנותיות", page_icon="🚀")

st.title("🚀 מחולל ברכות תכנותיות למורים")
st.write("בחרי את הפרמטרים, צרי ברכה מגניבה והדפיסי אותה ישירות כקובץ PDF מוכן לגזירה!")

# שדות קלט למורה
teacher_name = st.text_input("שם המורה", value="נטע")
grade = st.selectbox("כיתה / שכבה", ["כיתה י'", "כיתה י'א", "כיתה י'ב", "מגמת סייבר"])
topic = st.selectbox("שפת תכנות / נושא", ["C#", "Python", "Java", "רקורסיה"])
event = st.selectbox("אירוע", ["מבחן / בגרות", "חג פסח", "חנוכה", "סיום שנה"])

if st.button("צור ברכה עם AI ✨"):
    # קוד מעוצב ונקי ללא בעיות תחביר
    greeting = f"""// ברכה מיוחדת ל{grade} ב-{topic}
// אירוע: {event}

try 
{{
    Console.WriteLine("התחלת פתרון המבחן בהצלחה!");
    Student.SolveWithConfidence();
}}
catch (Exception ex)
{{
    Console.WriteLine("שגיאה נתפסה: הלחץ מבוטל!");
}}
finally 
{{
    Console.WriteLine("עשיתם את המקסימום. בהצלחה ענקית!");
}}

// בהצלחה! מאמינה בכם ❤️
// {teacher_name}"""

    # שמירה בזיכרון של ה-Session כדי שנוכל להדפיס או להוריד בקלות
    st.session_state['last_greeting'] = greeting

if 'last_greeting' in st.session_state:
    st.subheader("הברכה המוכנה:")
    st.code(st.session_state['last_greeting'], language="csharp")
    
    # כפתור מובנה להורדה כקובץ טקסט / הדפסה ל-PDF
    st.download_button(
        label="📥 הורד כקובץ טקסט לכרטיסייה",
        data=st.session_state['last_greeting'],
        file_name="tech_greeting.txt",
        mime="text/plain"
    )
    
    # הנחיה קטנה למורים להדפסה מושלמת כ-PDF
    st.info("💡 טיפ להדפסה כ-PDF: אפשר ללחוץ על ה-Code Block או להשתמש בקיצור המקלדת Ctrl+P (או Cmd+P) ולשמור את העמוד כ-PDF מוכן לגזירה!")
