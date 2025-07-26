# 📄 Connecting the Dots — Challenge 1A Solution

## 👋 Overview

This project is my submission for **Round 1A** of the **Adobe India Hackathon 2025**.  
It extracts a **structured outline** from each PDF — detecting headings (`H1`, `H2`, `H3`) using text font sizes — and saves the result as a valid JSON file for each PDF.

---

## ✅ **Approach**

- 📚 **Library Used:** [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (`fitz` in Python)
- 🗂️ The script loops through all PDFs in `/app/input` automatically.
- 🧩 It extracts all text spans and collects **font sizes**.
- 🔢 The largest font size is treated as `H1`, next as `H2`, next as `H3`.
- 🗂️ Each heading is saved with `level`, `text`, and `page` number.
- 📂 The output JSON file is named `<filename>.json` and stored in `/app/output`.

---

## ✅ **Requirements Satisfied**

✔️ Runs **fully offline** — no internet needed  
✔️ Uses **CPU only** — no large models, only PyMuPDF (~20 MB)  
✔️ Automatic — processes **multiple PDFs** in a loop  
✔️ Output format matches **the required schema** (`title` + `outline[]`)  
✔️ Compatible with **AMD64 (x86_64)** architecture  
✔️ Runs under **10 seconds** for typical 50-page PDFs (PyMuPDF is very fast)  
✔️ No file-specific hardcoding or web calls

---

## ✅ **Folder Structure**

```plaintext
connecting-the-dots/
 ├── extractor.py      # Main script
 ├── Dockerfile        # Container config
 ├── README.md         # This file
 ├── input/            # Place input PDFs here
 ├── output/           # Output JSONs will be written here
```
