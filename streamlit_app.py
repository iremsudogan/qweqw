import streamlit as st
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

# Dummy custom transformer
class CustomTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X

def main():
    st.title('My Streamlit App')
    st.write('Scikit-learn is installed and working!')

if __name__ == '__main__':
    main()
