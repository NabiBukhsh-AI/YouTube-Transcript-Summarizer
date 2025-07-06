# YouTube Transcript Summarizer

A Streamlit-powered web application that extracts transcripts from YouTube videos and generates concise summaries using AI models via the OpenRouter API. Choose from short, medium, or long summaries to quickly grasp the key points of any YouTube video with available transcripts.

![YouTube Transcript Summarizer Demo](https://via.placeholder.com/800x400.png?text=YouTube+Transcript+Summarizer+Demo)

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- Extracts transcripts from YouTube videos using the YouTube Transcript API.
- Generates AI-powered summaries (short, medium, or long) using OpenRouter's language models.
- User-friendly Streamlit interface with customizable summary lengths.
- Supports YouTube URLs or video IDs as input.
- Error handling for invalid URLs, unavailable transcripts, or API issues.
- Styled UI with a clean, modern look for an enhanced user experience.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/NabiBukhsh-AI/YouTube-Transcript-Summarizer.git
   cd YouTube-Transcript-Summarizer
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the project root and add your OpenRouter API key:
   ```bash
   OPENROUTER_API_KEY=your_openrouter_api_key
   ```
   Get your API key from [OpenRouter](https://openrouter.ai).

## Configuration
The `config.yml` file specifies the AI models used for summarization. The default configuration includes:
```yaml
models:
  - "google/gemini-flash-1.5-8b"
  - "google/gemini-2.0-flash-exp:free"
  - "google/gemini-exp-1121:free"
```
Modify `config.yml` to use different models supported by OpenRouter, if needed.

## Usage
1. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   This will launch the web app in your default browser.

2. **Interact with the App**:
   - Enter a YouTube video URL or ID (e.g., `https://www.youtube.com/watch?v=abcdef12345` or `abcdef12345`).
   - Select a summary length (short, medium, or long).
   - Click "Generate Summary" to fetch the transcript and view the AI-generated summary.

Example:
```bash
streamlit run app.py
```
Then, input a URL like `https://www.youtube.com/watch?v=dQw4w9WgXcQ` and choose "short" for a bullet-point summary.

## Project Structure
```
YouTube-Transcript-Summarizer/
├── app.py              # Main Streamlit application
├── config.yml          # Configuration for AI models
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked in Git)
└── README.md          # Project documentation
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details (create this file if you wish to formalize contribution guidelines).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
Created by [NabiBukhsh-AI](https://github.com/NabiBukhsh-AI). For feedback or suggestions, feel free to open an issue or contact me via GitHub.
