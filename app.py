import streamlit as st

# =========================
# CSS
# =========================
st.markdown("""
<style>

@media (max-width: 768px) {

    /* GRID PARENT */
    .st-key-grid_parent div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] {
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        gap: 10px !important;
    }

    /* MAKE EACH CHILD CONTAINER A GRID ITEM */
    .st-key-cell_1,
    .st-key-cell_2 {
        background: #1f1f1f;
        padding: 10px;
        border-radius: 8px;
    }

}

</style>
""", unsafe_allow_html=True)

st.title("Container Grid Test")

# =========================
# GRID STRUCTURE
# =========================
with st.container(key="grid_parent"):

    with st.container(key="cell_1"):
        st.text_input("Input 1", key="input1")

    with st.container(key="cell_2"):
        st.text_input("Input 2", key="input2")
