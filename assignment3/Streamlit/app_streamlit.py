from collections import Counter
from operator import itemgetter

import streamlit as st
import pandas as pd
import altair as alt
import graphviz

import ner_dep


example = (
        "When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

option = st.sidebar.radio("Select Task:", ("Named Entity Recognition", "Dependency Parsing"))

if option == "Named Entity Recognition":
    # st.set_page_config(layout='wide')
    st.markdown('## spaCy Named Entity Recognition')

    text = st.text_area('Text to process', value=example, height=100)

    doc = ner_dep.SpacyDocument(text)

    entities = doc.get_entities()
    tokens = doc.get_tokens()
    counter = Counter(tokens)
    words = list(sorted(counter.most_common(30)))

    # https://pandas.pydata.org
    chart = pd.DataFrame({
        'frequency': [w[1] for w in words],
        'word': [w[0] for w in words]})

    # https://pypi.org/project/altair/
    bar_chart = alt.Chart(chart).mark_bar().encode(x='word', y='frequency')

    st.markdown(f'Total number of tokens: {len(tokens)}<br/>'
                f'Total number of types: {len(counter)}', unsafe_allow_html=True)

    # https://docs.streamlit.io/library/api-reference/data/st.table
    st.table(entities)

    # https://docs.streamlit.io/library/api-reference/charts/st.altair_chart
    st.altair_chart(bar_chart)

else:
    st.markdown('## spaCy Dependencies Visualization')
    text = st.text_area('Text to process', value=example, height=100)
    doc = ner_dep.SpacyDocument(text)
    dependencies = doc.get_dependency()
    vis_option = st.selectbox("Visualization Option:", ("Table", "Graph"))
    if vis_option == "Table":
        table = pd.DataFrame({
            'word': [d[0] for d in dependencies],
            'dep': [d[1] for d in dependencies],
            'head': [d[2] for d in dependencies]})
        st.table(table)
    else:
        graph = graphviz.Digraph()
        for d in dependencies:
            graph.edge(d[2], d[0], label=d[1])
        st.graphviz_chart(graph)



