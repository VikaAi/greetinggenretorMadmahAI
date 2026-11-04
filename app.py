import streamlit as st

st.set_page_config(page_title="מחולל כרטיסיות ברכה תכנותיות", page_icon="✂️", layout="centered")

st.title("✂️ מחולל כרטיסיות ברכה תכנותיות (C#)")
st.write("מלאי את הפרמטרים בחופשיות, צרי כרטיסיות בשחור-לבן והורידי קובץ מוכן לגזירה בלחיצת כפתור!")

# שדות קלט גמישים לחלוטין (בחירה או הקלדה חופשית)
teacher_name = st.text_input("שם המורה:", value="ויקה")

grade_options = ["כיתה י'", "כיתה י'א", "כיתה י'ב", "מגמת סייבר", "הקלד כיתה אחרת..."]
grade_selection = st.selectbox("בחר כיתה / שכבה:", grade_options)
if grade_selection == "הקלד כיתה אחרת...":
    grade = st.text_input("הקלד שם כיתה מותאם אישית:", value="כיתה ט'")
else:
    grade = grade_selection

programming_language = "C#"

topic = st.selectbox(
    "נושא תכנותי:", 
    ["תנאים (if/else)", "לולאות (Loops)", "קינון (Nested Loops)", "רקורסיה (Recursion)", "שרשרת חוליות (Linked List)"]
)

event = st.selectbox("אירוע:", ["מבחן", "בגרות", "חג פסח", "חנוכה", "סיום שנה"])
custom_category = st.text_input("התאמה אישית לקטגוריה / הערה בכרטיסייה (אופציונלי):", value="")

if st.button("✨ צור כרטיסיות לגזירה"):
    
    # בניית גוף הקוד בהתאם לנושא הנבחר ב-C#
    if "תנאים" in topic:
        code_body = "if (learned && practiced)\n{\n    Console.WriteLine(\"ההצלחה בדרך!\");\n}\nelse\n{\n    Console.WriteLine(\"תמשיך לנסות!\");\n}"
    elif "לולאות" in topic:
        code_body = "for (int i = 0; i < exam.Questions; i++)\n{\n    Console.WriteLine(\"פותר עוד שאלה בביטחון!\");\n}"
    elif "קינון" in topic:
        code_body = "for (int r = 0; r < rows; r++)\n{\n    for (int c = 0; c < cols; c++)\n        Console.Write(\"⭐ \");\n    Console.WriteLine();\n}"
    elif "רקורסיה" in topic:
        code_body = "public static void Solve(int level)\n{\n    if (level == 0) return; // תנאי עצירה\n    Solve(level - 1);\n}"
    else:  # שרשרת חוליות
        code_body = "Node current = head;\nwhile (current != null)\n{\n    current = current.next;\n}"

    category_label = f" | {custom_category}" if custom_category else ""
    
    # יצירת מבנה כרטיסייה נקי לגזירה בשחור-לבן
    single_card = f"""┌────────────────────────────────────────────────────────┐
│ // {grade} | {topic} | {event}{category_label}
{code_body}
│
│ // בהצלחה! מאמינה בכם ❤️
│ // {teacher_name}
└────────────────────────────────────────────────────────┘"""

    # יצירת דף שלם המכיל מספר כרטיסיות להדפסה
    full_page_content = "\n\n".join([f"--- כרטיסייה #{i} ---\n" + single_card for i in range(1, 5)])

    st.success("הכרטיסיות נוצרו בהצלחה!")
    
    st.subheader("📋 תצוגה מקדימה של הכרטיסיות:")
    st.code(full_page_content, language="text")

    # כפתור הורדה ישיר ואמיתי של קובץ טקסט מעוצב מוכן להדפסה
    st.download_button(
        label="📥 לחץ כאן להורדת קובץ הכרטיסיות לגזירה",
        data=full_page_content,
        file_name="tech_greetings_cards.txt",
        mime="text/plain"
    )
