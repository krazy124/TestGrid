import streamlit as st

# =========================
# MOBILE ONLY GRID
# =========================
st.markdown("""
<style>

/* ONLY apply on mobile */
@media (max-width: 768px) {

    /* Turn container into grid */
    .st-key-test_grid div[data-testid="stVerticalBlock"] {
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        gap: 10px !important;
    }

}

</style>
""", unsafe_allow_html=True)

st.title("Mobile Grid Test")

# =========================
# GRID CONTAINER
# =========================
with st.container(key="test_grid"):

    st.text_input("Input 1", key="input1")
    st.text_input("Input 2", key="input2")
