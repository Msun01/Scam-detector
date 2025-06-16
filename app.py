
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import pandas as pd

# Sample training data
scam_samples = [
    "Congratulations! You've won a free iPhone. Click here to claim.",
    "Your bank account has been locked. Click to verify your identity.",
    "Give me $100 now or your account will be closed.",
    "You have been selected for a prize. Send your info to claim.",
    "Please send $50 in iTunes gift cards to unlock your computer.",
    "We detected suspicious activity. Pay $200 to restore access.",
    "Send Bitcoin to this address to avoid arrest.",
    "Get rich quick! Invest in this program today.",
    "URGENT: Your Social Security number has been compromised.",
    "This is Microsoft support. We need $100 in gift cards to fix your PC."
]
real_samples = [
    "Hi John, just checking if we’re still on for dinner tomorrow.",
    "The report is ready and attached to this email.",
    "Reminder: Your dentist appointment is on Friday at 3pm.",
    "Thanks for your purchase! Your order will arrive soon.",
    "Meeting rescheduled to Monday, please confirm availability.",
    "Can you review this document before our meeting?",
    "Happy birthday! Wishing you a great year ahead.",
    "Looking forward to seeing you at the conference next week.",
    "Please submit your timesheet by end of day.",
    "Don’t forget to RSVP for the company party."
]

texts = scam_samples + real_samples
labels = [1]*len(scam_samples) + [0]*len(real_samples)

# Training the model
pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('clf', RandomForestClassifier())
])

pipeline.fit(texts, labels)

# Streamlit app
st.title("🛡️ Scam Detector")

user_input = st.text_area("Enter a message or email content below:", height=150)

if st.button("Check for Scam"):
    if user_input.strip() == "":
        st.warning("Please enter a message first.")
    else:
        prediction = pipeline.predict([user_input])[0]
        if "give me $" in user_input.lower():
            prediction = 1
        if prediction == 1:
            st.error("⚠️ This message appears to be a SCAM.")
        else:
            st.success("✅ This message appears to be safe.")
