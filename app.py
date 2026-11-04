import streamlit as st

st.set_page_config(page_title="מחולל כרטיסיות ברכה תכנותיות", page_icon="✂️", layout="centered")

# עיצוב CSS מותאם אישית: שחור-לבן נקי, כרטיסיות מנוקדות לגזירה, והסתרת תפריטים בהדפסה ל-PDF
st.markdown("""
    <style>
    body {
        background-color: #f8f9fa;
        color: #212529;
    }
    
    /* סגנון כרטיסייה נפרדת לגזירה (שחור לבן נקי עם מסגרת מנוקדת) */
    .card-box {
        background-color: #ffffff;
        border: 2px dashed #000000;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 20px;
        font-family: 'Courier New', Courier, monospace;
        direction: ltr;
        text-align: left;
        color: #000000;
        page-break-inside: avoid;
    }
    
    .card-header {
        color: #555555;
        font-size: 0.85rem;
        margin-bottom: 8px;
        border-bottom: 1px solid #cccccc;
        padding-bottom: 4px;
        font-family: Arial, sans-serif;
    }

    /* הגדרות להדפסת PDF: מסתיר את כל תפריטי המערכת ומציג רק את הכרטיסיות */
    @media print {
        body * {
            visibility: hidden;
        }
        #printable-cards, #printable-cards * {
            visibility: visible;
        }
        #printable-cards {
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
        }
        .stButton, .stTextInput, .stSelectbox, header, footer {
            display: none !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.title("✂️ מחולל כרטיסיות ברכה תכנותיות (C#)")
st.write("מלאי את הפרמטרים, צרי כרטיסיות בשחור-לבן ושמרי מיד כקובץ PDF נקי לגזירה!")

# שדות קלט למורה
teacher_name = st.text_input("שם המורה:", value="ויקה")
grade = st.selectbox("כיתה / שכבה:", ["כיתה י'", "כיתה י'א", "כיתה י'ב"])

programming_language = "C#"

topic = st.selectbox(
    "נושא תכנותי:", 
    ["תנאים (if/else)", "לולאות (Loops)", "קינון (Nested Loops)", "רקורסיה (Recursion)", "שרשרת חוליות (Linked List)"]
)

event = st.selectbox("אירוע:", ["מבחן","בגרות", "חג פסח", "חנוכה", "סיום שנה"])
custom_category = st.text_input("התאמה אישית לקטגוריה / הערה בכרטיסייה (אופציונלי):", value="")

if st.button("✨ יצר כרטיסיות לגזירה"):
    
    # בניית גוף הקוד בהתאם לנושא הנבחר ב-C#
    if "תנאים" in topic:
        code_body = f"""if (learned && practiced) 
{{
    Console.WriteLine("ההצלחה בדרך!");
}}
else 
{{
    Console.WriteLine("תמשיך לנסות!");
}}"""
    elif "לולאות" in topic:
        code_body = f"""for (int i = 0; i < exam.Questions; i++)
{{
    Console.WriteLine("פותר עוד שאלה בביטחון!");
}}"""
    elif "קינון" in topic:
        code_body = f"""for (int r = 0; r < rows; r++)
{{
    for (int c = 0; c < cols; c++)
        Console.Write("⭐ ");
    Console.WriteLine();
}}"""
    elif "רקורסיה" in topic:
        code_body = f"""public static void Solve(int level)
{{
    if (level == 0) return; // תנאי עצירה
    Solve(level - 1);
}}"""
    else:  # שרשרת חוליות (תוקן תקינות ההערה)
        code_body = f"""Node current = head;
while (current != null)
{{
    current = current.next;
}}"""

    category_label = f" | {custom_category}" if custom_category else ""
    full_card_content = f"""// {grade} | {topic} | {event}{category_label}
{code_body}

// בהצלחה! מאמינה בכם ❤️
// {teacher_name}"""

    st.success("הכרטיסיות נוצרו בהצלחה!")
    
    # אזור ייעודי להדפסה שיוצג ב-PDF נקי בלי הפילטרים והכפתורים של האתר
    st.markdown('<div id="printable-cards">', unsafe_allow_html=True)
    st.subheader("📋 כרטיסיות מוכנות להדפסה וגזירה (תצוגה מקדימה):")
    
    # יצירת 4 כרטיסיות נפרדות בשחור-לבן לגזירה נוחה בדף
    for i in range(1, 5):
        card_html = f"""
        <div class="card-box">
            <div class="card-header">✂️ כרטיסייה #{i} | {grade} ({programming_language})</div>
            <pre style="margin:0; color: #000000; background: transparent; font-weight: bold;">{full_card_content}</pre>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("🖨️ **איך שומרים כ-PDF נקי לגזירה?** לחצי על מקשי **Ctrl + P** (או **Cmd + P** במק) במקלדת, בחרי באפשרות שמירה כ-PDF. העיצוב החדש יעלים את כפתורי המערכת וידפיס אך ורק את ריבועי הכרטיסיות בשחור-לבן!")
