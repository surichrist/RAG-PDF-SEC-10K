from unstructured.partition.pdf import partition_pdf
from langchain_core.documents import Document
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from typing import List, Dict, Any
from unstructured.chunking.title import chunk_by_title



os.environ['EXTRACT_IMAGE_BLOCK_CROP_HORIZONTAL_PAD'] = '3'
os.environ['EXTRACT_IMAGE_BLOCK_CROP_VERTICAL_PAD'] = '3'

#TEXT_SPLITTER = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

def load_documents_into_database(model_name: str, documents_path: str) -> Chroma:
    """
    Loads documents from the specified directory into the Chroma database
    after splitting the text into chunks.

    Returns:
        Chroma: The Chroma database with loaded documents.
    """
    print("Loading documents")
    documents = load_documents(documents_path)
    #documents = TEXT_SPLITTER.split_documents(raw_documents)

    print("Creating embeddings and loading documents into Chroma")
    db = Chroma.from_documents(
        documents,
        OllamaEmbeddings(model=model_name),
        persist_directory="cdb"
    )
    
    return db

def filter_complex_metadata(metadata: Dict[str, Any]) -> Dict[str, Any]:
    """
    Filters out complex metadata, leaving only simple types.

    Args:
        metadata (dict): The original metadata dictionary.

    Returns:
        dict: Filtered metadata dictionary containing only simple types.
    """
    return {
        key: value for key, value in metadata.items()
        if isinstance(value, (str, int, float, bool)) and key in ['filename','page_number','text_as_html']
    }

def load_documents(path: str) -> List[Document]:
    """
    Loads PDF documents from the specified directory path using the unstructured library.

    This function processes PDF documents with `partition_pdf` for better text segmentation
    and metadata extraction. It checks if the provided path exists and raises a 
    FileNotFoundError if it does not.

    Args:
        path (str): The path to the directory containing documents to load.

    Returns:
        List[Document]: A list of loaded documents with text and metadata.

    Raises:
        FileNotFoundError: If the specified path does not exist.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"The specified path does not exist: {path}")

    print("Processing PDF files using the unstructured library")
    docs = []

    # Iterate over all PDF files in the directory
    for filename in os.listdir(path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(path, filename)
            elements = partition_pdf(
                filename=file_path,
                strategy="hi_res",
                infer_table_structure=True,
                chunking_strategy="by_title",
                multipage_sections=True,
                combine_text_under_n_chars=150,
                max_characters=900, 
                overlap=300
            )
            print(filename, 'Converted Unstructured to Structured')
            
            #chunks = chunk_by_title(elements, max_characters=1000, overlap = 200, overlap_all = True)
            for element in elements:
                text = element.text
                metadata = filter_complex_metadata(element.metadata.__dict__)  # Simplify metadata
                docs.append(Document(page_content=text, metadata=metadata))

    return docs
