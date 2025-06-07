import streamlit as st

if "bg_color" not in st.session_state:
    st.session_state.bg_color = "#FDF6E3"
if "box_color" not in st.session_state:
    st.session_state.box_color = "#FFFFFF"
if "checked_color" not in st.session_state:
    st.session_state.checked_color = "#4CAF50"

if 'collected_numbers' not in st.session_state:
    st.session_state.collected_numbers = {i: [False] * 7 for i in range(1, 13)}

st.set_page_config(layout="centered")

# CSS för bakgrund, text och checkboxar
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {st.session_state.bg_color};
        color: #111111;
    }}
    .stMarkdown, .stText, .st-bb, .st-cq, .st-cv, .st-cw {{
        color: #111111 !important;
    }}
    /* Anpassa checkbox-rutor */
    div[data-testid="stCheckbox"] > div {{
        background: {st.session_state.bg_color} !important;
        border-radius: 16px !important;
        border: 2px solid #111 !important;
        width: 80px !important;
        height: 80px !important;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 10px auto !important;
    }}
    /* Anpassa själva checkboxen */
    input[type="checkbox"] {{
        width: 32px;
        height: 32px;
        accent-color: #111;
        border-radius: 8px;
        border: 2px solid #111;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Centrera rubrik och text
st.markdown(
    """
    <h1 style='text-align:center; font-size:2.6em; color:#111111; font-weight:bold; margin-bottom:0.2em;'>TILL HÖGER</h1>
    <div style='text-align:center; color:#111111; font-size:1.3em; margin-bottom:1.5em;'>Må bäste man eller kvinna vinna!</div>
    """,
    unsafe_allow_html=True
)

for number in range(1, 13):
    col_list = st.columns([1, 7, 1])

    # Vänster: Siffra (stor och centrerad)
    with col_list[0]:
        st.markdown(
            f"<div style='display:flex;align-items:center;justify-content:center;height:100%;font-size:4em;font-weight:bold;color:#111111'>{number}</div>",
            unsafe_allow_html=True
        )

    # Mitten: Siffror överst och "rutor" under
    with col_list[1]:
        cols = st.columns(7)
        # Siffror överst (centrerade)
        for i, col in enumerate(cols):
            with col:
                st.markdown(
                    f"<div style='text-align:center; color:#111111; font-weight:bold; font-size:2em'>{i+1}</div>",
                    unsafe_allow_html=True
                )
        # "Rutorna" under (en checkbox per ruta)
        checked = st.session_state.collected_numbers[number].copy()
        for i in range(7):
            with cols[i]:
                new_val = st.checkbox(
                    "",
                    value=checked[i],
                    key=f"chk_{number}_{i}",
                )
                # Om man bockar i en ruta, bocka även i alla till vänster
                if new_val and not checked[i]:
                    for j in range(i + 1):
                        checked[j] = True
                    st.session_state.collected_numbers[number] = checked
                # Om man bockar ur en ruta, bocka även ur alla till höger
                elif not new_val and checked[i]:
                    for j in range(i, 7):
                        checked[j] = False
                    st.session_state.collected_numbers[number] = checked

    # Höger: KLAR-ring om alla är ibockade
    with col_list[2]:
        if all(st.session_state.collected_numbers[number]):
            st.markdown(
                """
                <div style='display:flex;align-items:center;justify-content:center;height:100%;'>
                    <div style='
                        width:64px;
                        height:64px;
                        border-radius:50%;
                        background:#4CAF50;
                        color:#fff;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        font-weight:bold;
                        font-size:1.3em;
                        border: 4px solid #388e3c;
                        box-shadow: 0 0 6px #388e3c55;
                    '>Klar</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown("&nbsp;", unsafe_allow_html=True)