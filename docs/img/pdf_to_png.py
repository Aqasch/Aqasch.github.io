from pdf2image import convert_from_path

img = 'tensorrl-qas'

# Convert PDF to image objects
pages = convert_from_path(f'{img}.pdf', dpi=300)

# Save each page as PNG
for i, page in enumerate(pages):
    page.save(f'{img}.png', 'PNG')