import streamlit as st
import pandas as pd
import altair as alt

def DNA_nucleotide_count(seq):
    d = {
        'A': seq.count('A'),
        'T': seq.count('T'),
        'G': seq.count('G'),
        'C': seq.count('C') 
    }
    return d

st.image("dna-logo-webapp.png", width=400)

st.title("Web App de Contagem de Nucleotídeos de DNA")
st.write("Contagem de composição de nucleotídeos de um dna")
st.write("""---""")

st.header("Insira a sequencia")
sequence_input = "> DNA Query\nAATCAGCTGTAGACTTAGTCAGATCCTGTA\nGGGTTAAACCAAGGGGTTTTCCCAAAGGGA\nACGTCGACTGCAATCGACTTAGTTGGTGTA\nTGGGTTAATCGGGCATAGGCTGGGTATGTA"

sequence = st.text_area("Sequencia", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)
st.write("""---""")

st.header("Inserção (DNA Query)")
sequence

st.header("Saída (Contagem de nucleotídeos)")

st.subheader("Dicionário")
X = DNA_nucleotide_count(sequence)
X_label = list(X)
X_values = list(X.values())
X

st.subheader("Texto")
elements = ["Adenina(s)", "Timina(s)", "Guanina(s)", "Citosina(s)"]
for char, el in zip(X, elements):
    st.write(f"A sequência possui {X[char]} {el}")

st.subheader("Dataframe")
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: "qtd"}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotídeo'})
df

st.subheader("Gráfico de barras")
p = alt.Chart(df).mark_bar().encode(
    x="nucleotídeo",
    y="qtd"
)
p = p.properties(
    width=alt.Step(80)
)
p