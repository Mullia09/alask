import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from volunteer_app import doc_control


def test_generate_doc_id_length():
    doc_id = doc_control.generate_doc_id()
    assert len(doc_id) == 8
    int(doc_id, 16)  # should be hex


def test_register_document(tmp_path, monkeypatch):
    tmp_file = tmp_path / 'docs.csv'
    monkeypatch.setattr(doc_control, 'DOCS_FILE', str(tmp_file))
    doc_id, reward = doc_control.register_document('Contract', 'confidential', reward=5)
    assert reward == 5
    assert len(doc_id) == 8
    assert tmp_file.exists()
    lines = tmp_file.read_text().strip().splitlines()
    assert len(lines) == 2  # header + row


def test_list_documents(tmp_path, monkeypatch):
    tmp_file = tmp_path / 'docs.csv'
    monkeypatch.setattr(doc_control, 'DOCS_FILE', str(tmp_file))
    doc_control.register_document('Letter', 'official', reward=3)
    docs = doc_control.list_documents()
    assert len(docs) == 1
    assert docs[0]['title'] == 'Letter'
    assert docs[0]['category'] == 'official'
    assert docs[0]['reward'] == 3
