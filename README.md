# Unstructured-RAG-SEC-10K
 An RAG LLM served with Streamlit to work with unstructured data involving text and tables (ex. SEC 10-K forms) using neural networks, OCR etc with excellent retrieving from tables

Directory Structure: 

<img width="1010" alt="Screenshot 2024-11-13 at 11 26 03 PM" src="https://github.com/user-attachments/assets/8859d855-f773-4913-9e33-9d8109197643">


To run, install requirements, then:
For Streamlit UI:
  "streamlit run ui.py"

For exploration you may also use:
  "streamlit run app.py"


1) On starting the first time, add files to the **k10** directory, alternatively you may also specify another folder path for ingesting the pdfs.

2) Press the Index Documents button 

3) Type your query in the Question Box and press Return

4) For each session your previous messages are stored for context and passed to the LLM along with the query, upon restarting a session this contextual data is lost from previous conversations.
   Note: The documents ingested remain so across sessions in the persistent ChromaDB storage via a sqlite database stored in the **cdb** directory

Feel free to drop any suggestions, requests or questions!


Sample Screenshots:

<img width="1440" alt="Screenshot 2024-11-13" src="https://github.com/user-attachments/assets/a92d6c88-42ec-4125-b4f5-e96362fcb854">

<img width="1552" alt="Screenshot 2024-11-13" src="https://github.com/user-attachments/assets/d71216a0-e833-4ae7-a83d-6de1992e47b7">

<img width="1440" alt="Screenshot 2024-11-13" src="https://github.com/user-attachments/assets/e96df204-d6c5-4e9a-bed9-91ddccfe77c3">




