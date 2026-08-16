import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import streamlit as st
import pandas as pd
from pipeline.scam_detector.detector import ScamDetector

st.set_page_config(page_title="Scam Detection App", layout="wide")
st.title(" Scam Detection System")

# Initialize detector
detector = ScamDetector()

# Tab layout
tab1, tab2 = st.tabs(["Single Message", "Dataset Evaluation"])

# ----------- Single Message Analysis ----------
with tab1:
    st.header("Analyze a Single Message")
    user_input = st.text_area("Enter the message to analyze:", height=150, 
                             placeholder="Example: Congratulations! You've won $1000. Click here to claim...")
    
    if st.button("Analyze Message", type="primary"):
        if user_input.strip():
            with st.spinner("Analyzing message..."):
                try:
                    result = detector.detect(user_input)
                    
                    # Display results
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("Classification Result")
                        label = result.get("label", "Unknown")
                        
                        if label == "Scam":
                            st.error(f"🚨 **{label}**")
                        elif label == "Not Scam":
                            st.success(f"✅ **{label}**")
                        else:
                            st.warning(f"⚠️ **{label}**")
                    
                    with col2:
                        st.subheader("Intent")
                        st.write(result.get("intent", "Could not determine"))
                    
                    st.subheader("Reasoning")
                    st.write(result.get("reasoning", "No reasoning provided"))
                    
                    st.subheader("Risk Factors")
                    risk_factors = result.get("risk_factors", [])
                    if risk_factors:
                        for factor in risk_factors:
                            st.write(f"• {factor}")
                    else:
                        st.write("No specific risk factors identified.")
                        
                except Exception as e:
                    st.error(f"Error during analysis: {str(e)}")
        else:
            st.warning("Please enter a message to analyze.")

# ----------- Dataset Evaluation ----------
with tab2:
    st.header("Dataset Evaluation")
    
    uploaded_file = st.file_uploader("Upload a CSV file for batch analysis", type="csv")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write(f"Loaded dataset with {len(df)} rows")
            st.write("Sample data:")
            st.dataframe(df.head())
            
            # Find text column
            text_columns = ["text", "message_text", "message"]
            text_col = None
            for col in text_columns:
                if col in df.columns:
                    text_col = col
                    break
            
            if text_col:
                st.write(f"Using '{text_col}' as text column")
                
                # Limit for demo purposes
                max_rows = min(len(df), 10)
                if st.button(f"Analyze First {max_rows} Messages"):
                    with st.spinner(f"Analyzing {max_rows} messages..."):
                        messages = df[text_col].head(max_rows).tolist()
                        results = detector.detect_batch(messages)
                        
                        # Create results dataframe
                        results_df = pd.DataFrame(results)
                        
                        st.subheader("Analysis Results")
                        st.dataframe(results_df)
                        
                        # Summary statistics
                        label_counts = results_df['label'].value_counts()
                        st.subheader("Summary")
                        st.bar_chart(label_counts)
                        
            else:
                st.error(f"Could not find text column. Expected one of: {text_columns}")
                
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

