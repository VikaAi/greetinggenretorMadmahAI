import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import tempfile
import os

st.set_page_config(page_title="מחולל כרטיסיות ברכה תכנותיות", page_icon="✂️", layout="centered")

st.title("✂️ מחולל כרטיסיות ברכה תכנותיות (C#) ל-PDF")
st.write("מלאי את הפרמטרים, צרי כרטיסיות שחור-לבן והורידי קובץ PDF מוכן לגזירה בלחיצת כפתור!")

# שדות קלט גמישים לחלוטין (הקלדה חופשית מלאה)
teacher_name = st.text_input("שם המורה:", value="ויקה")

# שדה כיתה המאפשר בחירה או הקלדה חופשית לגמרי
grade_input = st.text_input("הקלד שם כיתה / שכבה (למשל: י' 3, מגמת סייבר):", value="כיתה י'")

programming_language = "C#"

topic = st.selectbox(
    "נושא תכנותי:", 
    ["תנאים (if/else)", "לולאות (Loops)", "קינון (Nested Loops)", "רקורסיה (Recursion)", "שרשרת חוליות (Linked List)"]
)

event = st.selectbox("אירוע:", ["מבחן", "בגרות", "חג פסח", "חנוכה", "סיום שנה"])
custom_category = st.text_input("התאמה אישית לקטגוריה / הערה נוספת (אופציונלי):", value="")

if st.button("✨ צור קובץ PDF לגזירה"):
    
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
    card_title = f"// {grade_input} | {topic} | {event}{category_label}"
    card_footer1 = "// בהצלחה! מאמינה בכם ❤️"
    card_footer2 = f"// {teacher_name}"

    # יצירת קובץ PDF אמיתי באמצעות ReportLab
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf_path = tmp_file.name
    tmp_file.close()

    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4  # מידות דף A4 בנקודות

    # הגדרת מידות לכרטיסיות (4 כרטיסיות בעמוד, מסגרת שחור-לבן מקווקושת/נקייה)
    box_width = 500
    box_height = 140
    margin_x = (width - box_width) / 2
    start_y = height - 160
    spacing = 20

    for i in range(1, 5):
        current_y = start_y - (i - 1) * (box_height + spacing)
        
        # ציור מסגרת מלבנית בשחור-לבן לכל כרטיסייה
        c.setLineWidth(1)
        c.setDash(4, 4)  # קו מקווקו לגזירה
        c.rect(margin_x, current_y, box_width, box_height)
        c.setDash()      # איפוס הקו למלא עבור הטקסט
        
        # כתיבת תוכן הקוד בתוך הכרטיסייה (פונט מונוספייס)
        c.setFont("Courier", 10)
        text_x = margin_x + 15
        text_y = current_y + box_height - 25
        
        # שורות ההדפסה בתוך הכרטיסייה
        lines = [
            f"✂️ כרטיסייה #{i} | {card_title}",
            "--------------------------------------------------",
            *code_body.split('\n'),
            "",
            card_footer1,
            card_footer2
        ]
        
        for line in lines:
            c.drawString(text_x, text_y, line)
            text_y -= 13  # מרווח שורות

    c.save()

    # קריאת קובץ ה-PDF שנוצר לצורך כפתור ההורדה
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    st.success("קובץ ה-PDF נוצר בהצלחה!")
    
    # כפתור הורדה אמיתי ל-PDF
    st.download_button(
        label="📥 לחץ כאן להורדת קובץ ה-PDF לגזירה",
        data=pdf_bytes,
        file_name="tech_greetings_cards.pdf",
        mime="application/pdf"
    )

    if os.path.exists(pdf_path):
        os.unlink(pdf_path)
