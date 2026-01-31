# Prerequsites
sudo apt update
sudo apt install pandoc python3-pip

# Auto-generate output filename
python3 markdown_to_docx.py README.md

# Specify output filename  
python3 markdown_to_docx.py README.md ISMS-Crypto-Suite-Documentation.docx

# Use reference doc for styling
python3 markdown_to_docx.py README.md output.docx company_template.docx

# Bash one-liner
./md2docx README.md