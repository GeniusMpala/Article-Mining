from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

def cluster_papers(papers):
    try:
        vectorizer = TfidfVectorizer(stop_words='english')
        abstracts = [paper['summary'] for paper in papers]
        X = vectorizer.fit_transform(abstracts)

        # Number of clusters can be tuned
        kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
        labels = kmeans.labels_

        # Append cluster labels to papers
        for paper, label in zip(papers, labels):
            paper['cluster'] = label

        return papers
    except Exception as e:
        print(f"Error in clustering papers: {e}")
        return papers  # Return papers without clustering if an error occurs
