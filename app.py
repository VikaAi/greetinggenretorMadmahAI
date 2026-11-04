import streamlit as st

st.set_page_config(page_title="מחולל ברכות תכנותיות", page_icon="🚀")

st.title("🚀 מחולל ברכות תכנותיות למורים")
st.write("בחרי את הפרמטרים וצרי ברכה מבוססת AI לתלמידים!")

# שדות קלט למורה
teacher_name = st.text_input("שם המורה", value="נטע")
grade = st.selectbox("כיתה / שכבה", ["כיתה י'", "כיתה י'א", "כיתה י'ב", "מגמת סייבר"])
topic = st.selectbox("שפת תכנות / נושא", ["C#", "Python", "Java", "רקורסיה"])
event = st.selectbox("אירוע", ["מבחן / בגרות", "חג פסח", "חנוכה", "סיום שנה"])

if st.button("צור ברכה עם AI ✨"):
    # כאן אפשר לחבר את הקוד ששולח את הבקשה ל-AI או לייצר את הטקסט בצורה דינמית
    greeting = f"""
    // ברכה מיוחדת ל{grade} ב-{topic}
    // אירוע: {event}
    
    try 
    {
        Console.WriteLine("התחלת פתרון המבחן בהצלחה!");
        Student.SolveWithConfidence();
    }
    catch (StressException ex)
    {
        Console.WriteLine("שגיאה נתפסה: הלחץ מבוטל!");
    }
    finally 
    {
        Console.WriteLine("כל הכבוד על הדרך שעשיתם!");
    }

    // בהצלחה ענקית! 
    // באהבה, {teacher_name}
    """
    
    st.subheader("הברכה המוכנה:")
    st.code(greeting, language="csharp")
    st.success("הברכה נוצרה בהצלחה!")
