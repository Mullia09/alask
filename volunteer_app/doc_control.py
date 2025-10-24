"""Simple digital document control system with voucher reward."""

import csv
import os
import uuid

DOCS_FILE = os.path.join(os.path.dirname(__file__), 'documents.csv')
FIELDNAMES = ['id', 'title', 'category', 'reward']


def generate_doc_id() -> str:
    """Return a short unique id for a document."""
    return uuid.uuid4().hex[:8]


def register_document(title: str, category: str, reward: int = 10):
    """Register a document and award a fixed reward.

    Parameters
    ----------
    title: str
        Title or name of the document.
    category: str
        Classification of the document.
    reward: int, optional
        Reward points given for registering the document.

    Returns
    -------
    tuple
        The generated document id and reward points awarded.
    """
    doc_id = generate_doc_id()
    write_header = not os.path.exists(DOCS_FILE)
    with open(DOCS_FILE, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerow({'id': doc_id, 'title': title, 'category': category, 'reward': reward})
    return doc_id, reward


def list_documents():
    """Return a list of registered documents with numeric rewards."""
    if not os.path.exists(DOCS_FILE):
        return []
    with open(DOCS_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        docs = []
        for row in reader:
            try:
                row['reward'] = int(row['reward'])
            except (KeyError, ValueError):
                pass
            docs.append(row)
        return docs


def main():
    while True:
        print('\nDocument Control')
        print('1. Register document')
        print('2. List documents')
        print('3. Exit')
        choice = input('Choose an option: ').strip()
        if choice == '1':
            title = input('Title: ').strip()
            category = input('Category: ').strip()
            doc_id, reward = register_document(title, category)
            print(f'Document {doc_id} registered. Reward: {reward} points')
        elif choice == '2':
            docs = list_documents()
            if not docs:
                print('No documents registered yet.')
            for d in docs:
                print(f"{d['id']} - {d['title']} ({d['category']}) : {d['reward']} points")
        elif choice == '3':
            break
        else:
            print('Invalid choice')


if __name__ == '__main__':
    main()
