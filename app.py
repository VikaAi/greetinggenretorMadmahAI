import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="מחולל כרטיסיות ברכה תכנותיות מבוסס Gemini", page_icon="🤖", layout="centered")

# הגדרת מפתח ה-API של Gemini מתוך ה-Secrets
gemini_api_key = st.secrets.get("GEMINI_API_KEY", "")

if gemini_api_key:
    genai.configure(api_key=gemini_api_key)

if 'page' not in st.session_state:
    st.session_state['page'] = 'create'

if st.session_state['page'] == 'create':
    st.title("🤖 מחולל ברכות תכנותיות מבוסס Gemini (C#)")
    st.write("צרי ברכה יצירתית, שנונה ומקורית בעזרת הבינה המלאכותית של גוגל!")

    teacher_name = st.text_input("שם המורה:", value="ויקה")
    grade_input = st.text_input("שם כיתה / שכבה חופשי:", value="כיתה י' האלופה")
    programming_language = "C#"
    
    topic = st.selectbox(
        "נושא תכנותי:", 
        ["תנאים (if/else)", "לולאות (Loops)", "קינון (Nested Loops)", "רקורסיה (Recursion)", "שרשרת חוליות (Linked List)"]
    )
    
    event = st.selectbox("אירוע:", ["מבחן", "בגרות", "חג פסח", "חנוכה", "סיום שנה"])
    custom_category = st.text_input("התאמה אישית לקטגוריה / הערה נוספת (אופציונלי):", value="")

    if st.button("✨ ג'נרט ברכה יצירתית עם Gemini"):
        if not gemini_api_key:
            st.error("נא להגדיר את מפתח ה-GEMINI_API_KEY בהגדרות ה-Secrets של Streamlit.")
        else:
            with st.spinner("Gemini חושב על קוד יצירתי במיוחד בשבילך... 🚀"):
                try:
                    # עדכון שם המודל לגרסה יציבה
                    model = genai.GenerativeModel('gemini-1.5-pro')
                    
                    prompt = f"""
                    כתוב קוד ברכה קצר, חכם ומצחיק לתלמידים בתחביר של שפת C#.
                    פרטים:
                    - עבור: {grade_input}
                    - נושא בתכנות: {topic}
                    - אירוע: {event}
                    - הערה נוספת: {custom_category}
                    - שם המורה: {teacher_name}
                    
                    הנחיות:
                    1. השתמש בתחביר נקי של C# (לדוגמה Console.WriteLine, מבני בקרה וכו').
                    2. שלב הומור גיקי שקשור לנושא.
                    3. אל תוסיף הסברים מסביב, רק את קוד ה-C# עצמו שמתחיל בהערה עם פרטי הברכה ומסתיים בחתימת המורה.
                    """

                    response = model.generate_content(prompt)
                    ai_code = response.text.strip()
                    ai_code = ai_code.replace("```csharp", "").replace("```", "").strip()
                    
                    st.session_state['card_data'] = {
                        'teacher': teacher_name,
                        'grade': grade_input,
                        'topic': topic,
                        'event': event,
                        'code': ai_code,
                        'lang': programming_language
                    }
                    st.success("הברכה נוצרה בהצלחה על ידי Gemini! 🎉")
                except Exception as e:
                    st.error(f"שגיאה בהתחברות ל-Gemini API: {e}")

    if 'card_data' in st.session_state:
        st.subheader("👀 תצוגה מקדימה של הברכה:")
        st.code(st.session_state['card_data']['code'], language="csharp")

        if st.button("🖨️ מעבר לדף ההדפסה והגזירה (4 כרטיסיות בדף)"):
            st.session_state['page'] = 'print'
            st.rerun()

elif st.session_state['page'] == 'print':
    st.markdown("""
        <style>
        .card-box {
            background-color: #ffffff;
            border: 2px dashed #000000;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 12px;
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
                padding: 6px !important;
                margin-bottom: 8px !important;
                font-size: 0.8rem !important;
            }
            pre {
                font-size: 0.8rem !important;
                line-height: 1.15 !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    if st.button("⬅️ חזרה לעריכה ויצירה"):
        st.session_state['page'] = 'create'
        st.rerun()

    st.title("🖨️ עמוד הדפסה וגזירה")
    st.info("💡 לחצי על Ctrl+P (או Cmd+P) במקלדת כדי לשמור כ-PDF או להדפיס את 4 הכרטיסיות נקיות בשחור-לבן!")

    data = st.session_state['card_data']

    for i in range(1, 5):
        card_html = f"""
        <div class="card-box">
            <div class="card-header">✂️ כרטיסייה #{i} | {data['grade']} ({data['lang']})</div>
            <pre style="margin:0; color: #000000; background: transparent; font-weight: bold;">{data['code']}</pre>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
