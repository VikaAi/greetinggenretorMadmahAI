import streamlit as st
from fpdf import FPDF
import tempfile
import os

st.set_page_config(page_title="מחולל כרטיסיות ברכה תכנותיות", page_icon="✂️", layout="centered")

st.title("✂️ מחולל כרטיסיות ברכה תכנותיות (C#) ל-PDF")
st.write("מלאי את הפרמטרים (או השאירי חופשי), צרי כרטיסיות בשחור-לבן והורידי קובץ PDF מוכן לגזירה בלחיצת כפתור!")

# שדות קלט גמישים לחלוטין (גם בחירה וגם הקלדה חופשית)
teacher_name = st.text_input("שם המורה:", value="ויקה")

# שדה כיתה מאפשר גם בחירה מהרשימה וגם הקלדה ידנית חופשית
grade_options = ["כיתה י'", "כיתה י'א", "כיתה י'ב", "מגמת סייבר", "אחר..."]
grade_selection = st.selectbox("בחר או הקלד כיתה / שכבה:", grade_options)
if grade_selection == "אחר...":
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
    full_card_content = f"// {grade} | {topic} | {event}{category_label}\n{code_body}\n\n// בהצלחה! מאמינה בכם ❤️\n// {teacher_name}"

    st.success("הכרטיסיות נוצרו בהצלחה!")
    
    # יצירת קובץ PDF אמיתי באמצעות FPDF עם מסגרות מקווקושות/נקיות לגזירה
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    
    # הגדרת פונט בסיסי תואם אנגלית ותווים
    pdf.set_font("Courier", size=10)
    
    # נחלק את העמוד לכרטיסיות (למשל 4 כרטיסיות בעמוד)
    box_width = 180
    box_height = 55
    start_x = 15
    start_y = 15
    spacing = 8
    
    for i in range(1, 5):
        current_y = start_y + (i - 1) * (box_height + spacing)
        
        # ציור מסגרת מלבנית לכרטיסייה (שחור-לבן נקי לגזירה)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_line_width(0.5)
        pdf.rect(start_x, current_y, box_width, box_height)
        
        # הוספת טקסט לתוך הכרטיסייה
        pdf.set_xy(start_x + 4, current_y + 4)
        header_text = f"✂️ Card #{i} | {grade} ({programming_language})"
        pdf.set_font("Arial", 'B', 9)
        pdf.cell(box_width - 8, 6, txt=header_text, ln=True)
        
        pdf.set_xy(start_x + 4, current_y + 12)
        pdf.set_font("Courier", size=9)
        
        # פיצול השורות לצורך כתיבה מדויקת ב-PDF
        for line in full_card_content.split('\n'):
            pdf.set_x(start_x + 4)
            pdf.cell(box_width - 8, 4.5, txt=line, ln=True)

    # שמירת ה-PDF לקובץ זמני
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(tmp_file.name)
    tmp_file.close()

    # קריאת הקובץ להורדה ישירה דרך כפתור Streamlit אמיתי
    with open(tmp_file.name, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.markdown("---")
    st.subheader("📥 הורדת קובץ ה-PDF המוכן:")
    
    # כפתור הורדת PDF רשמי שעובד בלחיצה אחת בלי שום טריקים של הדפדפן
    st.download_button(
        label="📄 לחץ כאן להורדת כרטיסיות ה-PDF לגזירה",
        data=PDFbyte,
        file_name="tech_greetings_cards.pdf",
        mime="application/octet-stream"
    )
    
    # ניקוי קבצים זמניים
    if os.path.exists(tmp_file.name):
        os.unlink(tmp_file.name)
