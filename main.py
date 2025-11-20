import cv2
from PIL import Image
import pytesseract
import os

# Configure Tesseract path (update this path for your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Output directory (relative path)
output_dir = "ocr_output"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "quiz_text.txt")

def get_next_question_number(file_path):
    if not os.path.exists(file_path):
        return 1
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    return data.count("Question ") + 1

def main():
    question_number = get_next_question_number(output_file)
    
    # Get image path from user
    img_path = input("Path to your quiz screenshot: ").strip().strip('"')
    if not os.path.isfile(img_path):
        print("File not found. Check the path and try again.")
        return

    # Image preprocessing
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    pil_img = Image.fromarray(thresh)

    # OCR processing
    text = pytesseract.image_to_string(pil_img, lang="deu").strip()
    if not text:
        print("No text detected. Try a higher resolution or clearer screenshot.")
        return

    # Clean and split text
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        print("No readable lines found in the OCR result.")
        return

    # Separate question and answers
    question_lines = []
    answer_lines = []
    question_done = False

    for line in lines:
        if not question_done and line.endswith("?"):
            question_lines.append(line)
            question_done = True
        elif not question_done:
            question_lines.append(line)
        else:
            answer_lines.append(line)

    # Format output
    clean_output = (f"Question {question_number}\n"
                   f"-------------------------\n"
                   + "\n".join(question_lines) + "\n\n"
                   + "\n".join(answer_lines) + "\n\n")

    print("\n--- OCR RESULT ---")
    print(clean_output)

    # Save to file
    with open(output_file, "a", encoding="utf-8") as f:
        f.write(clean_output)
    print(f"Results appended to {output_file}")

if __name__ == "__main__":
    main()