
![Logo](https://imgur.com/z5RPfor.png)

# Email Spam Detection NLP Project

This project aims to detect spam emails using a fine-tuned NLP model. It involves extracting emails from an IMAP server, classifying them as spam or not, and visualizing the results through a user-friendly interface. The entire process is streamlined for easy integration and provides insightful analytics to help manage and understand your email data.

## Table of Contents

- [Screenshots](#Screenshots)
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Directory Structure](#directory-structure)
- [Usage](#usage)
- [License](#license)

## Screenshots

![App Screenshot](https://imgur.com/458mK6d.png)


## Features

- **Email Extraction**: Connect to an IMAP server to extract emails and save them in JSON format.
- **Spam Classification**: Use a fine-tuned NLP model to classify emails as spam or not.
- **Data Storage**: Save classified email data in a structured JSON format.
- **Interactive Visualization**: Visualize email data using a Gradio interface with filtering options.

## Dependencies

- **Python 3.7+**: Programming language used for development.
- **Gradio**: For creating an interactive UI.
- **Pandas**: For data manipulation and analysis.
- **IMAPlib**: For email extraction from the server.
- **Hugging Face Transformers**: For using the fine-tuned NLP model.

### Model

- **Pre-trained Model**: [`h-e-l-l-o/email-spam-classification-merged`](https://huggingface.co/h-e-l-l-o/email-spam-classification-merged)

### Dataset used to Fine-tune my Model

- **Dataset**: [`legacy107/spamming-email-classification`](https://huggingface.co/datasets/legacy107/spamming-email-classification)

### My Model

- **Model**: [`JrX44/gemma-2b-it-fine-tune-email-spam`](https://huggingface.co/JrX44/gemma-2b-it-fine-tune-email-spam)

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/abhie7/email-spam-detection-nlp.git
cd email-spam-detection-nlp
pip install -r requirements.txt
```
    
## Directory Structure

```bash
email-spam-detection-nlp/
│
├── email_extraction/
│   ├── imap_client.py           # Script to fetch emails from IMAP server
│   └── extracted_emails/        # Directory to store extracted emails in JSON format
|
├── fine-tuning/
│   └── gemma-fine-tuning-email.ipynb   # Fine Tuning Python Notebook
|
├── model_classifier.py          # Script to classify emails using pre-trained NLP model
│
├── gradio_frontend.py           # Script to visualize classified emails using Gradio
│
├── requirements.txt             # Project dependencies
│
├── .env                         # Environment variables (not included in version control)
│
└── README.md                    # Project documentation
```
## Usage

#### Extract Emails
Run the email extraction script to fetch emails from your inbox and spam folder:

```bash
python email_extraction/imap_client.py
```

#### Classify Emails
Run the classification script to classify the extracted emails as spam or not:

```bash
python model_classifier.py
```

#### Visualize Results
Run the Gradio interface to visualize the classified email data:

```bash
python gradio_frontend.py
```
## License

[MIT](https://choosealicense.com/licenses/mit/)

