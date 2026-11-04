import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="מחולל כרטיסיות ברכה תכנותיות - AI", page_icon="⚡", layout="centered")

groq_api_key = st.secrets.get("GROQ_API_KEY", "")

if 'page' not in st.session_state:
    st.session_state['page'] = 'create'

if st.session_state['page'] == 'create':
    st.title("⚡ מחולל ברכות תכנותיות  ")
    st.write("צרו ברכה יצירתית, שנונה ומקורית בעזרת הבינה המלאכותית  !")

    teacher_name = st.text_input("שם המורה:", value="ויקה")
    grade_input = st.text_input("שם כיתה / שכבה חופשי:", value="כיתה י' האלופה")
    programming_language = "C#"
    
    topic = st.selectbox(
        "נושא תכנותי:", 
        ["תנאים (if/else)", "לולאות (Loops)", "קינון (Nested Loops)", "רקורסיה (Recursion)", "אחר"]
    )
    
    event = st.selectbox("אירוע:", ["מבחן", "בגרות", "חג פסח", "חנוכה", "סיום שנה"])
    custom_category = st.text_input("התאמה אישית לקטגוריה / הערה נוספת (אופציונלי):", value="")

    if st.button("✨ ג'נרט ברכה יצירתית  "):
        if not groq_api_key:
            st.error("נא להגדיר את מפתח ה-GROQ_API_KEY בהגדרות ה-Secrets של Streamlit.")
        else:
            with st.spinner(" מייצר עבורך משהו יצירתי במהירות הבזק... 🚀"):
                try:
                    client = OpenAI(
                        base_url="https://api.groq.com/openai/v1",
                        api_key=groq_api_key
                    )
                    
                    prompt = f"""
                    כתוב קוד C# קצרצר ומושלם ככרטיסיית ברכה לתלמידים.
                    הנושא שחובה להציג באופן המרכזי ביותר הוא: {topic}.
                    פרטים נוספים:
                    - עבור: {grade_input}
                    - אירוע: {event}
                    - הערה נוספת: {custom_category}
                    - שם המורה: {teacher_name}
                    
                    הנחיות קשיחות:
                    1. הקוד חייב להיות מינימליסטי (4-6 שורות בלבד) ולהדגים ישירות את {topic} בצורה פשוטה שמובנת לתלמידים.
                    2. שלב בתוך הקוד (כהערה או כטקסט פנימי) פאנץ' שנון או בדיחה קטנה שקשורה ל-{event} ול-{topic}.
                    3. אל תמציא לולאות ארוכות או לוגיקה מסובכת שלא קשורה.
                    4. פלט אך ורק את קוד ה-C# הנקי, בלי שום מילות הסבר מסביב, ומדגם כך שיסתיים בחתימה של {teacher_name}.
                    5. השתמש בירידות שורה ובמבנה נקי ומסודר של קוד (עם בלוקים וסוגריים מסולסלים כמקובל ב-C#).
                    """

                    response = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.6
                    )
                    
                    ai_code = response.choices[0].message.content.strip()
                    ai_code = ai_code.replace("```csharp", "").replace("```", "").strip()
                    
                    st.session_state['card_data'] = {
                        'teacher': teacher_name,
                        'grade': grade_input,
                        'topic': topic,
                        'event': event,
                        'code': ai_code,
                        'lang': programming_language
                    }
                    st.success("הברכה נוצרה בהצלחה! 🎉")
                except Exception as e:
                    st.error(f"שגיאה בהתחברות ל-Groq API: {e}")

    if 'card_data' in st.session_state:
        st.subheader("👀 עריכה ותצוגה מקדימה של הברכה:")
        st.info("💡 אפשר לערוך ולשנות את הקוד חופשי ישירות בתיבה למטה לפני ההדפסה!")
        
        edited_code = st.text_area(
            "ערוך את קוד הברכה:",
            value=st.session_state['card_data']['code'],
            height=180
        )
        st.session_state['card_data']['code'] = edited_code

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
