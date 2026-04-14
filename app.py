import streamlit as st

st.markdown("""
<style>
/* Parent grid */
.st-key-grid_wrapper > div[data-testid="stVerticalBlock"] {
    display: grid !important;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 12px !important;
    align-items: stretch;
}

/* Mobile */
@media (max-width: 768px) {
    .st-key-grid_wrapper > div[data-testid="stVerticalBlock"] {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

/* Card styling */
.st-key-card_1,
.st-key-card_2,
.st-key-card_3,
.st-key-card_4,
.st-key-card_5,
.st-key-card_6,
.st-key-card_7,
.st-key-card_8 {
    background: #1f1f1f;
    border-radius: 12px;
    padding: 16px;
    color: white;
}

/* Tighten spacing inside each card */
.st-key-card_1 > div[data-testid="stVerticalBlock"],
.st-key-card_2 > div[data-testid="stVerticalBlock"],
.st-key-card_3 > div[data-testid="stVerticalBlock"],
.st-key-card_4 > div[data-testid="stVerticalBlock"],
.st-key-card_5 > div[data-testid="stVerticalBlock"],
.st-key-card_6 > div[data-testid="stVerticalBlock"],
.st-key-card_7 > div[data-testid="stVerticalBlock"],
.st-key-card_8 > div[data-testid="stVerticalBlock"] {
    gap: 0.5rem !important;
}

/* Optional: center labels a bit */
.st-key-card_1 p,
.st-key-card_2 p,
.st-key-card_3 p,
.st-key-card_4 p,
.st-key-card_5 p,
.st-key-card_6 p,
.st-key-card_7 p,
.st-key-card_8 p {
    text-align: center;
    margin-bottom: 0.5rem;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Hardcoded Grid Layout")

with st.container(key="grid_wrapper"):

    with st.container(key="card_1"):
        st.write("Lights & Reflectors")
        st.radio("", ["OK", "Needs Repair"], key="item1", horizontal=True)

    with st.container(key="card_2"):
        st.write("Tires & Wheels")
        st.radio("", ["OK", "Needs Repair"], key="item2", horizontal=True)

    with st.container(key="card_3"):
        st.write("Brakes")
        st.radio("", ["OK", "Needs Repair"], key="item3", horizontal=True)

    with st.container(key="card_4"):
        st.write("Steering & Suspension")
        st.radio("", ["OK", "Needs Repair"], key="item4", horizontal=True)

    with st.container(key="card_5"):
        st.write("Fluid Levels")
        st.radio("", ["OK", "Needs Repair"], key="item5", horizontal=True)

    with st.container(key="card_6"):
        st.write("Horn & Mirrors")
        st.radio("", ["OK", "Needs Repair"], key="item6", horizontal=True)

    with st.container(key="card_7"):
        st.write("Safety Equipment")
        st.radio("", ["OK", "Needs Repair"], key="item7", horizontal=True)

    with st.container(key="card_8"):
        st.write("Cab Cleanliness")
        st.radio("", ["OK", "Needs Repair"], key="item8", horizontal=True)
