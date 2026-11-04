import streamlit as st

st.set_page_config(page_title="מחולל כרטיסיות ברכה תכנותיות", page_icon="✂️", layout="centered")

# ניהול מצב (Session State) כדי לעבור בין מסך היצירה למסך ההדפסה
if 'page' not in st.session_state:
    st.session_state['page'] = 'create'

# --- מסך 1: יצירה ועריכה ---
if st.session_state['page'] == 'create':
    st.title("✂️ מחולל כרטיסיות ברכה תכנותיות (C#)")
    st.write("צרי כרטיסייה אישית, בחני אותה, וכשתהיי מוכנה עברי לעמוד ההדפסה והגזירה!")

    # שדות קלט חופשיים לגמרי
    teacher_name = st.text_input("שם המורה:", value="ויקה")
    grade_input = st.text_input("שם כיתה / שכבה חופשי:", value="כיתה י'")
    programming_language = "C#"
    
    topic = st.selectbox(
        "נושא תכנותי:", 
        ["תנאים (if/else)", "לולאות (Loops)", "קינון (Nested Loops)", "רקורסיה (Recursion)", "שרשרת חוליות (Linked List)"]
    )
    
    event = st.selectbox("אירוע:", ["מבחן", "בגרות", "חג פסח", "חנוכה", "סיום שנה"])
    custom_category = st.text_input("התאמה אישית לקטגוריה / הערה נוספת (אופציונלי):", value="")

    # בניית גוף הקוד בהתאם לנושא
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
    
    # שמירת הנתונים ב-Session State כדי שיועברו למסך הבא
    st.session_state['card_data'] = {
        'teacher': teacher_name,
        'grade': grade_input,
        'topic': topic,
        'event': event,
        'category': category_label,
        'code': code_body,
        'lang': programming_language
    }

    st.subheader("👀 תצוגה מקדימה של הברכה הבודדת:")
    preview_box = f"""┌────────────────────────────────────────────────────────┐
│ // {grade_input} | {topic} | {event}{category_label}
{code_body}
│
│ // בהצלחה! מאמינה בכם ❤️
│ // {teacher_name}
└────────────────────────────────────────────────────────┘"""
    st.code(preview_box, language="text")

    if st.button("🖨️ מעבר לדף ההדפסה והגזירה (4 כרטיסיות בדף)"):
        st.session_state['page'] = 'print'
        st.rerun()

# --- מסך 2: דף ההדפסה והגזירה הנקי ---
elif st.session_state['page'] == 'print':
    # עיצוב CSS מיוחד שמסתיר את התפריטים של האתר בזמן הדפסה
    st.markdown("""
        <style>
        .card-box {
            background-color: #ffffff;
            border: 2px dashed #000000;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 15px;
            font-family: 'Courier New', Courier, monospace;
            direction: ltr;
            text-align: left;
            color: #000000;
            page-break-inside: avoid;
        }
        .card-header {
            color: #555555;
            font-size: 0.8rem;
            margin-bottom: 6px;
            border-bottom: 1px solid #cccccc;
            padding-bottom: 3px;
            font-family: Arial, sans-serif;
        }
        @media print {
            .stButton, header, footer, .sidebar, title, .stInfo {
                display: none !important;
            }
            body {
                margin: 0 !important;
                padding: 0 !important;
            }
            .card-box {
                border: 1.5px dashed #000000 !important;
                padding: 8px !important;
                margin-bottom: 10px !important;
                font-size: 0.85rem !important;
            }
            pre {
                font-size: 0.85rem !important;
                line-height: 1.2 !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    if st.button("⬅️ חזרה לעריכה ויצירה"):
        st.session_state['page'] = 'create'
        st.rerun()

    st.title("🖨️ עמוד הדפסה וגזירה")
    st.info("💡 זהו עמוד ההדפסה הנקי. לחצי על Ctrl+P (או Cmd+P) במקלדת כדי לשמור כ-PDF או להדפיס את הכרטיסיות ישירות!")

    data = st.session_state['card_data']
    
    full_card_content = f"""// {data['grade']} | {data['topic']} | {data['event']}{data['category']}
{data['code']}

// בהצלחה! מאמינה בכם ❤️
// {data['teacher']}"""

    # הצגת 4 כרטיסיות זהות מוכנות לגזירה בשחור-לבן
    for i in range(1, 5):
        card_html = f"""
        <div class="card-box">
            <div class="card-header">✂️ כרטיסייה #{i} | {data['grade']} ({data['lang']})</div>
            <pre style="margin:0; color: #000000; background: transparent; font-weight: bold; font-size: 0.95rem;">{full_card_content}</pre>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
