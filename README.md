# Unstructured-RAG-SEC-10K
 An RAG LLM served with Streamlit to work with unstructured data involving text and tables (ex. SEC 10-K forms) using neural networks, OCR etc with excellent retrieving from tables


├── 10k -                   ***Only Add New Files to be Indexed here, previously indexed files are stored in persistent storage***
│   ├── goog-10-k-2023 (1).pdf
│   ├── tsla-20231231-gen.pdf
│   └── uber-10-k-2023.pdf
├── LICENSE
├── README.md
├── __pycache__
│   ├── document_loader.cpython-312.pyc
│   ├── llm.cpython-312.pyc
│   └── models.cpython-312.pyc
├── app.py                  ***Only for testing, use "ui.py" to run full Streamlit app***
├── cdb                     ***persistent data storage for embeddings - indexed documents***
│   ├── 57c000df-8f33-4ee4-a672-545de668ac98
│   │   ├── data_level0.bin
│   │   ├── header.bin
│   │   ├── index_metadata.pickle
│   │   ├── length.bin
│   │   └── link_lists.bin
│   └── chroma.sqlite3
├── document_loader.py
├── llm.py
├── models.py
├── requirements.txt
└── ui.py



![Sample Screenshot]()

