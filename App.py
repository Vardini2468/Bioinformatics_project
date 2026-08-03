import streamlit as st
from Bio.Seq import Seq
from Bio.Align import PairwiseAligner
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import time

# 1. Page Title
st.title("🧬 Bioinformatics Toolkit")

# 🗂️ Create the tabs at the very top
tab1, tab2 = st.tabs(["Analyze DNA", "Sequence Alignment"])

# 2. User Input Area
# -----------------------------------------
# TAB 1: DNA & PROTEIN ANALYSIS
# -----------------------------------------
with tab1:
    st.subheader("DNA Analysis")
    dna_input = st.text_area("Enter your DNA sequence here:").upper()
    FASTA_input = st.file_uploader("Upload the file in FASTA format")
    if FASTA_input is not None:
     dna_input = FASTA_input.getvalue().decode("utf-8")
     dna_input = dna_input.split('\n', 1)[1]
# 3. Analyze Button
    if st.button("Analyze Sequence"):
     if dna_input:
        # Turn the text into a biological sequence object
        seq = Seq(dna_input)
        # 1. Start the loading animation
        with st.spinner("Analyzing DNA and extracting proteins... 🧬"):
            time.sleep(2)
            # 2. Your existing code goes here (indented under the spinner)
            seq = Seq(dna_input)
            # ... all your st.write() lines ...
            
    
        # 4. Calculate and Display Results
        st.subheader("📊 Results")
        st.write(f"**Length:** {len(seq)} nucleotides")
        
        gc_count = seq.count('G') + seq.count('C')
        st.write(f"**GC Content:** {round((gc_count / len(seq)) * 100, 2)}%")

        at_count = seq.count('A') + seq.count('T')
        st.write(f"**AT Content:** {round((at_count / len(seq)) * 100, 2)}%")

        st.write(f"**RNA Transcription:** {seq.transcribe()}")
        st.write(f"**Reverse Complement:** {seq.reverse_complement()}")
        st.write(f"**Protein Translation:** {seq.translate()}")

        protein_seq = seq.translate()
        
        analyzer = ProteinAnalysis(str(protein_seq).replace("*", ""))
        st.write(f"**Molecular Weight:** {analyzer.molecular_weight()}")
        aa_counts = analyzer.count_amino_acids()
        st.write(f"**Amino Acid Counts:** {analyzer.count_amino_acids()}")
        st.bar_chart(aa_counts)
     else:
        st.error("Please enter a DNA sequence first.")

with tab2:
 st.write("---") 

 st.subheader("🧬 Sequence Alignment")

# Create the two input boxes
 dna_input1 = st.text_area("Enter the first sequence here (Target):").upper()
 dna_input2 = st.text_area("Enter the second sequence here (Query):").upper()

 if st.button("Align Sequences"):
    if dna_input1 and dna_input2:
        with st.spinner("Aligning sequences... 📏"):
                time.sleep(2)
                
        aligner = PairwiseAligner()
        score = aligner.score(dna_input1, dna_input2)
        alignments = aligner.align(dna_input1, dna_input2)
        
        st.write(f"**Alignment Score:** {score}")
        st.text(alignments[0])
       