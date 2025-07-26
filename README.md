📄 Connecting the Dots — Challenge 1A Solution
👋 Overview
This repository contains my submission for Round 1A of the Adobe India Hackathon 2025.
It extracts a structured outline from each PDF — automatically detecting headings (H1, H2, H3) using relative font sizes — and generates a valid JSON file for each PDF.

✅ Approach
📚 Library Used: PyMuPDF (fitz in Python)

🗂️ The script automatically loops through all PDFs in /app/input.

🔍 It extracts all text spans and gathers unique font sizes.

🔢 The largest font size is treated as H1, the next as H2, and the next as H3.

🏷️ Each heading is saved with its level, text, and page number.

📄 The output JSON is named <filename>.json and saved to /app/output.

✅ Requirements Satisfied
✔️ Runs fully offline — no internet needed
✔️ Uses CPU only — no large models (PyMuPDF only, ~20 MB)
✔️ Processes multiple PDFs automatically
✔️ Output format matches the required schema (title + outline[])
✔️ Compatible with AMD64 (x86_64) architecture
✔️ Executes in under 10 seconds for typical 50-page PDFs
✔️ No file-specific hardcoding or external API calls

✅ Project Structure
graphql
Copy
Edit
connecting-the-dots/
├── extractor.py # Main Python script
├── Dockerfile # Docker container configuration
├── README.md # This file
├── input/ # Place input PDFs here
├── output/ # Output JSON files will be generated here
✅ Build Instructions
1️⃣ Build the Docker image:

bash
Copy
Edit
docker build --platform linux/amd64 -t connecting-the-dots-solution .
2️⃣ Run the container:

bash
Copy
Edit
docker run --rm \
 -v "${PWD}/input:/app/input" \
  -v "${PWD}/output:/app/output" \
 --network none connecting-the-dots-solution
On Windows PowerShell, use \ for line breaks or run it as a single line.

⚡ How It Works
The container reads all .pdf files in /app/input (read-only).

Generates a matching .json in /app/output for each input PDF.

Fully offline — requires no internet access at runtime.

📌 Notes
✅ Please test with simple and complex PDFs.
✅ Tune your heading detection logic further for maximum accuracy.
✅ Keep this repository private until the competition deadline.
✅ No output JSON files are stored in the repo — they are generated at runtime.

Good luck connecting the dots! 🚀
