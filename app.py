import streamlit as st

# =========================
# CSS (Hardcoded Grid)
# =========================
st.markdown("""
<style>

.flex-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    justify-content: center;
    margin-top: 20px;
}

.grid-item {
    flex: 1 1 calc(25% - 12px);
    max-width: calc(25% - 12px);
}

.grid-box {
    background: #1f1f1f;
    padding: 20px;
    border-radius: 12px;
    color: white;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

/* MOBILE */
@media (max-width: 768px) {
    .grid-item {
        flex: 1 1 calc(50% - 12px);
        max-width: calc(50% - 12px);
    }
}

</style>
""", unsafe_allow_html=True)

st.title("Hardcoded Grid Layout")

# =========================
# GRID START
# =========================
st.markdown('<div class="flex-grid">', unsafe_allow_html=True)

# ---------- ITEM 1 ----------
st.markdown('<div class="grid-item">', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="grid-box">', unsafe_allow_html=True)
    st.write("Lights & Reflectors")
    st.radio("",
        ["OK", "Needs Repair"],
        key="item1",
        horizontal=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- ITEM 2 ----------
st.markdown('<div class="grid-item">', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="grid-box">', unsafe_allow_html=True)
    st.write("Tires & Wheels")
    st.radio("",
        ["OK", "Needs Repair"],
        key="item2",
        horizontal=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- ITEM 3 ----------
st.markdown('<div class="grid-item">', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="grid-box">', unsafe_allow_html=True)
    st.write("Brakes")
    st.radio("",
        ["OK", "Needs Repair"],
        key="item3",
        horizontal=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- ITEM 4 ----------
st.markdown('<div class="grid-item">', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="grid-box">', unsafe_allow_html=True)
    st.write("Steering & Suspension")
    st.radio("",
        ["OK", "Needs Repair"],
        key="item4",
        horizontal=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- ITEM 5 ----------
st.markdown('<div class="grid-item">', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="grid-box">', unsafe_allow_html=True)
    st.write("Fluid Levels")
    st.radio("",
        ["OK", "Needs Repair"],
        key="item5",
        horizontal=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- ITEM 6 ----------
st.markdown('<div class="grid-item">', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="grid-box">', unsafe_allow_html=True)
    st.write("Horn & Mirrors")
    st.radio("",
        ["OK", "Needs Repair"],
        key="item6",
        horizontal=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- ITEM 7 ----------
st.markdown('<div class="grid-item">', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="grid-box">', unsafe_allow_html=True)
    st.write("Safety Equipment")
    st.radio("",
        ["OK", "Needs Repair"],
        key="item7",
        horizontal=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- ITEM 8 ----------
st.markdown('<div class="grid-item">', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="grid-box">', unsafe_allow_html=True)
    st.write("Cab Cleanliness")
    st.radio("",
        ["OK", "Needs Repair"],
        key="item8",
        horizontal=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# =========================
# GRID END
# =========================
st.markdown('</div>', unsafe_allow_html=True)
