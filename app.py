import streamlit as st
from data_fetcher import fetch_papers
from utils import display_paper, get_recommendations

st.title('ArXiv Paper Aggregator')
st.sidebar.header('Settings')
category = st.sidebar.selectbox(
    'Select Category',
    options=['Machine Learning (cs.LG)', 'Quantum Computing (quant-ph)'],
    index=0
)

st.header(f'Latest Papers in {category}')
papers = fetch_papers(category)

if 'selected_paper' not in st.session_state:
    st.session_state.selected_paper = None

if st.session_state.selected_paper is None:
    for i, paper in enumerate(papers):
        if st.button(paper.title):
            st.session_state.selected_paper = i
else:
    selected_paper = papers[st.session_state.selected_paper]
    display_paper(selected_paper)
    st.write("## Related Papers")
    recommendations = get_recommendations(papers, st.session_state.selected_paper)
    for paper in recommendations:
        display_paper(paper)
    if st.button("Back to all papers"):
        st.session_state.selected_paper = None
