import requests
from config import BACKEND_URL

TIMEOUT = 30


def upload_pdf(file):
    try:
        return requests.post(
            f"{BACKEND_URL}/upload/",
            files={
                "file": (
                    file.name,
                    file,
                    "application/pdf"
                )
            },
            timeout=TIMEOUT
        )
    except requests.RequestException:
        return None


def ask_question(question):
    try:
        return requests.post(
            f"{BACKEND_URL}/chat/",
            json={
                "question": question
            },
            timeout=TIMEOUT
        )
    except requests.RequestException:
        return None


def get_documents():
    try:
        return requests.get(
            f"{BACKEND_URL}/documents/",
            timeout=TIMEOUT
        )
    except requests.RequestException:
        return None


def get_dashboard():
    try:
        return requests.get(
            f"{BACKEND_URL}/documents/dashboard",
            timeout=TIMEOUT
        )
    except requests.RequestException:
        return None


def delete_document(filename):
    try:
        return requests.delete(
            f"{BACKEND_URL}/documents/{filename}",
            timeout=TIMEOUT
        )
    except requests.RequestException:
        return None
    
def compare_documents(file1, file2):
    try:
        return requests.post(
            f"{BACKEND_URL}/compare/",
            files={
                "file1": (
                    file1.name,
                    file1,
                    "application/pdf"
                ),

                "file2": (
                    file2.name,
                    file2,
                    "application/pdf"
                )
            },
            timeout=60
        )
    except requests.RequestException:

        return None