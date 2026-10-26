"""
Export DOCX Media Utility
=========================
Extracts embedded screenshots from Word documents into respective screenshot folders.

Author: Muhammad Umer Basit (Civil Engineering Student)
"""

import os
import zipfile

def extract_docx_media(docx_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    if not os.path.exists(docx_path):
        print(f"File not found: {docx_path}")
        return
    with zipfile.ZipFile(docx_path, 'r') as z:
        for m in z.namelist():
            if m.startswith('word/media/'):
                fname = os.path.basename(m)
                data = z.read(m)
                with open(os.path.join(out_dir, fname), 'wb') as f:
                    f.write(data)
    print(f"Extracted media from {os.path.basename(docx_path)} into {out_dir}")

if __name__ == "__main__":
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tasks = [
        (os.path.join(repo_root, "lab-tasks-and-exercises", "lab-05-devcpp-basics", "Lab-05-DevCPP-Basics-and-Operators.docx"),
         os.path.join(repo_root, "lab-tasks-and-exercises", "lab-05-devcpp-basics", "screenshots")),
        (os.path.join(repo_root, "lab-tasks-and-exercises", "lab-08-control-structures", "Lab-08-Control-Statements-and-Loops.docx"),
         os.path.join(repo_root, "lab-tasks-and-exercises", "lab-08-control-structures", "screenshots")),
        (os.path.join(repo_root, "lab-tasks-and-exercises", "lab-10-functions-part-2", "Lab-10-Functions-Scope-and-Parameters.docx"),
         os.path.join(repo_root, "lab-tasks-and-exercises", "lab-10-functions-part-2", "screenshots"))
    ]
    for doc, out in tasks:
        extract_docx_media(doc, out)
