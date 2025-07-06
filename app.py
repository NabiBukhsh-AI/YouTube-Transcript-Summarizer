import os
import streamlit as st
from dotenv import load_dotenv
import requests
import yaml
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from urllib.parse import urlparse, parse_qs

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def extract_video_id(input_str):
    try:
        parsed = urlparse(input_str)
        if parsed.netloc in ['www.youtube.com', 'youtube.com']:
            query = parse_qs(parsed.query)
            video_id = query.get('v')
            if video_id and len(video_id[0]) == 11:
                return video_id[0]
        elif parsed.netloc in ['youtu.be']:
            video_id = parsed.path.lstrip('/')
            if len(video_id) == 11:
                return video_id
    except Exception as e:
        st.error(f"Error extracting video ID: {e}")
    
    if len(input_str) == 11 and all(c.isalnum() or c in ['-', '_'] for c in input_str):
        return input_str

    raise ValueError("Invalid YouTube video URL or ID.")

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        full_text = " ".join([entry['text'] for entry in transcript])
        return full_text
    except (TranscriptsDisabled, NoTranscriptFound) as e:
        st.error(f"Transcript error: {e}")
        return None

def summarize_text_with_openrouter(transcript, length='short'):
    prompts = {
        'short': "Summarize the following transcript in three bullet points highlighting the main takeaways:\n\n",
        'medium': "Provide a short paragraph summary of the following transcript:\n\n",
        'long': "Write a detailed multi-paragraph report based on the following transcript:\n\n"
    }

    if length not in prompts:
        raise ValueError("Summary length must be 'short', 'medium', or 'long'.")

    prompt = prompts[length] + transcript

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    with open("config.yml", "r") as file:
        config = yaml.safe_load(file)
    
    models = config.get("models", [])
    if not models:
        st.error("No models found in the config.yml file. Please check your configuration.")
        return None

    models_to_use = config.get("models", [])[:2]
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json={
            "models": models_to_use,
            "messages": [{"role": "user", "content": prompt}],
        },
    )

    if response.status_code != 200:
        st.error(f"OpenRouter API request failed: {response.status_code} - {response.text}")
        return None

    result = response.json()

    try:
        content = result["choices"][0]["message"]["content"]
        return content
    except Exception as e:
        st.error(f"Failed to parse AI response: {str(e)}")
        return None

st.title("YouTube Transcript Summarizer")
st.markdown("""
    <style>
        .stButton>button {
            background-color: #FF6347;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            padding: 10px 20px;
        }
        .stTextInput>div>div>input {
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True)

video_url = st.text_input("Enter YouTube Video URL or ID", "")

summary_length = st.selectbox("Choose Summary Length", ["short", "medium", "long"])

if st.button("Generate Summary"):
    if video_url:
        try:
            video_id = extract_video_id(video_url)
            st.write(f"Extracted Video ID: {video_id}")
            
            with st.spinner('Fetching transcript...'):
                transcript = get_transcript(video_id)

            if transcript:
                st.write("Transcript fetched successfully!")

                with st.spinner('Generating summary...'):
                    summary = summarize_text_with_openrouter(transcript, summary_length)
                
                if summary:
                    st.subheader("Summary")
                    st.write(summary)
                else:
                    st.error("Failed to generate summary. Please try again.")
            else:
                st.error("Failed to fetch transcript. The video might not have captions or the transcript may be unavailable.")
        
        except ValueError as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid YouTube video URL or ID.")
