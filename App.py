import streamlit as st
from Bio.Seq import Seq

# 1. Page Title
st.title("🧬 Bioinformatics Toolkit")

# 2. User Input Area
dna_input = st.text_area("Enter your DNA sequence here:").upper()

# 3. Analyze Button
if st.button("Analyze Sequence"):
    if dna_input:
        # Turn the text into a biological sequence object
        seq = Seq(dna_input)
        
        # 4. Calculate and Display Results
        st.subheader("📊 Results")
        st.write(f"**Length:** {len(seq)} nucleotides")
        
        gc_count = seq.count('G') + seq.count('C')
        st.write(f"**GC Content:** {round((gc_count / len(seq)) * 100, 2)}%")
        
        st.write(f"**RNA Transcription:** {seq.transcribe()}")
        st.write(f"**Reverse Complement:** {seq.reverse_complement()}")
    else:
        st.error("Please enter a DNA sequence first.")