import streamlit as st
import requests
import feedparser
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import numpy as np

def display_paper(paper):
    st.write(f"### {paper.title}")
    st.write(f"**Authors:** {', '.join(author.name for author in paper.authors)}")
    st.write(f"**Published:** {paper.published}")
    st.write(f"**Summary:** {paper.summary}")
    st.write(f"[Read More]({paper.link})")

def compute_tfidf_vectors(papers):
    documents = [f"{paper.title} {paper.summary}" for paper in papers]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    return tfidf_matrix

def get_recommendations(papers, selected_paper_index, n_neighbors=5):
    tfidf_matrix = compute_tfidf_vectors(papers)
    knn = NearestNeighbors(n_neighbors=n_neighbors, metric='cosine').fit(tfidf_matrix)
    distances, indices = knn.kneighbors(tfidf_matrix[selected_paper_index:selected_paper_index + 1])
    recommended_indices = indices[0][1:]  # exclude the selected paper itself
    return [papers[i] for i in recommended_indices]
