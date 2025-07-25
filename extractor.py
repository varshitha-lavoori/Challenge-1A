import fitz  # PyMuPDF
import json
import os

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = os.path.basename(pdf_path).replace('.pdf', '')
    headings = []

    font_sizes = []

    # Gather all font sizes
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for s in l["spans"]:
                        font_sizes.append(s["size"])

    # Determine thresholds for H1, H2, H3 based on font size quantiles
    font_sizes = sorted(list(set(font_sizes)), reverse=True)
    h1_size = font_sizes[0] if len(font_sizes) > 0 else 0
    h2_size = font_sizes[1] if len(font_sizes) > 1 else h1_size - 1
    h3_size = font_sizes[2] if len(font_sizes) > 2 else h2_size - 1

    for i, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    line_text = ""
                    max_size = 0
                    for s in l["spans"]:
                        line_text += s["text"] + " "
                        if s["size"] > max_size:
                            max_size = s["size"]

                    line_text = line_text.strip()
                    if len(line_text) > 0:
                        level = None
                        if max_size >= h1_size:
                            level = "H1"
                        elif max_size >= h2_size:
                            level = "H2"
                        elif max_size >= h3_size:
                            level = "H3"
                        if level:
                            headings.append({
                                "level": level,
                                "text": line_text,
                                "page": i + 1
                            })

    result = {
        "title": title,
        "outline": headings
    }
    return result


if __name__ == "__main__":
    input_dir = "/app/input"
    output_dir = "/app/output"

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            output = extract_outline(pdf_path)
            output_filename = filename.replace(".pdf", ".json")
            with open(os.path.join(output_dir, output_filename), "w", encoding="utf-8") as f:
                json.dump(output, f, indent=2, ensure_ascii=False)
