import streamlit as st
import pandas as pd
import os

st.title("📚 Rate Our Teacher's Class")
st.write("Please give your honest feedback and rating 💛")

# Rating slider (1 to 5)
rating = st.slider("How would you rate the class? ⭐", 1, 5, 3)

# Text feedback
feedback = st.text_area("Write your message for the teacher ✍️", "")

# Submit button
if st.button("Submit Feedback"):
    if feedback.strip() == "":
        st.warning("Please write a short message before submitting.")
    else:
        # Save to CSV file
        data = {"Rating": [rating], "Feedback": [feedback]}
        df = pd.DataFrame(data)

        # Append to existing file or create new one
        if os.path.exists("feedback.csv"):
            df.to_csv("feedback.csv", mode='a', header=False, index=False)
        else:
            df.to_csv("feedback.csv", index=False)

        st.success("✅ Thank you for your feedback!")
