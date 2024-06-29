import gradio as gr
import pandas as pd
import os
import json

# Function to load JSON data into a Pandas DataFrame
def load_json_to_dataframe(directory):
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    data = []
    for filename in json_files:
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            email_data = json.load(f)
            data.append(email_data)
    df = pd.DataFrame(data)
    return df

# Load your classified emails from the directory
classified_emails_directory = "classified_emails"
emails_df = load_json_to_dataframe(classified_emails_directory)

# Directly pass the dataframe to the Interface
iface = gr.Interface(
    fn=lambda: emails_df,  # Pass the dataframe directly
    inputs=[],
    outputs=gr.Dataframe(),
    title="Emails Spam Classifier",
    description="View classified emails with filter options"
)

# Custom CSS to make table stretch the entire page and enable vertical scrolling
css = """
    .gradio-container {
        width: 100%;
        overflow-x: auto;
    }
    table.dataframe {
        width: 100%;
        table-layout: fixed;
        word-wrap: break-word;
    }
    .dataframe-container {
        max-height: 90vh;
        overflow-y: auto;
    }
"""

# Launch Gradio interface with custom CSS
iface.launch(inline=True)
