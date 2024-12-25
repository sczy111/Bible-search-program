from lxml import etree as ET
from bs4 import BeautifulSoup
import os
import re

def clean_text(text):
    """Remove invalid XML characters from the text."""
    def is_valid_xml_char(c):
        codepoint = ord(c)
        return (
            codepoint == 0x9 or
            codepoint == 0xA or
            codepoint == 0xD or
            (0x20 <= codepoint <= 0xD7FF) or
            (0xE000 <= codepoint <= 0xFFFD) or
            (0x10000 <= codepoint <= 0x10FFFF)
        )
    return ''.join(c for c in text if is_valid_xml_char(c))

def remove_notes(usx_root):
    """Remove all <note> elements from the USX tree."""
    notes = usx_root.findall('.//note')
    for note in notes:
        parent = note.getparent()
        if parent is not None:
            parent.remove(note)

def remove_english_chars(usx_root):
    """Remove <char> elements that contain English text."""
    chars = usx_root.findall('.//char')
    for char in chars:
        text_has_english = False
        if char.text and re.search(r'[a-zA-Z]', char.text):
            text_has_english = True
        if char.tail and re.search(r'[a-zA-Z]', char.tail):
            text_has_english = True
        if text_has_english:
            parent = char.getparent()
            if parent is not None:
                # If the char element has tail text, attach it to the parent
                if char.tail:
                    if parent.tail:
                        parent.tail += char.tail
                    else:
                        parent.tail = char.tail
                parent.remove(char)
        else:
            # Remove English words from char.text and char.tail
            if char.text:
                char.text = re.sub(r'[a-zA-Z]+', '', char.text).strip()
            if char.tail:
                char.tail = re.sub(r'[a-zA-Z]+', '', char.tail).strip()

def remove_english_text(usx_root):
    """Remove English words from the USX tree."""
    english_word_pattern = re.compile(r'[a-zA-Z]+')
    for elem in usx_root.iter():
        # Remove English words from elem.text
        if elem.text:
            new_text = english_word_pattern.sub('', elem.text)
            new_text = new_text.strip()
            elem.text = new_text if new_text else None
        # Remove English words from elem.tail
        if elem.tail:
            new_tail = english_word_pattern.sub('', elem.tail)
            new_tail = new_tail.strip()
            elem.tail = new_tail if new_tail else None

def parse_usx(usx_file):
    """Parse the USX file and collect verse elements."""
    verse_elements = {}
    tree = ET.parse(usx_file)
    root = tree.getroot()
    remove_notes(root)  # Remove all notes from the USX tree
    remove_english_chars(root)  # Remove <char> elements with English text
    current_chapter = None

    for elem in root.iter():
        if elem.tag == 'chapter':
            current_chapter = elem.get('number')
        elif elem.tag == 'verse':
            verse_number = elem.get('number')
            # Store the verse element for later modification
            verse_elements[(current_chapter, verse_number)] = elem
    return tree, root, verse_elements

def parse_html_chapter(html_file):
    """Parse an HTML file and extract verses."""
    # Try different encodings
    encodings = ['gb18030', 'gb2312', 'utf-8']
    for encoding in encodings:
        try:
            with open(html_file, 'r', encoding=encoding) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
    else:
        print(f"Error decoding file {html_file}")
        return {}
    soup = BeautifulSoup(content, 'html.parser')
    verse_texts = {}
    # Each verse is in a <tr> element
    for tr in soup.find_all('tr'):
        tds = tr.find_all('td')
        if len(tds) >= 2:
            verse_ref = tds[0].get_text(strip=True)
            verse_text = tds[1].get_text(strip=True)
            # Extract chapter and verse numbers
            if ':' in verse_ref:
                chapter_verse = verse_ref.split(':')
                if len(chapter_verse) == 2:
                    chapter_number = chapter_verse[0].strip()
                    verse_number = chapter_verse[1].strip()
                    # Clean verse_text to remove invalid characters
                    verse_text = clean_text(verse_text)
                    verse_texts[(chapter_number, verse_number)] = verse_text
    return verse_texts

def replace_verses(usx_tree, verse_elements, chinese_verses):
    """Replace verse texts in USX tree with Chinese verses."""
    for key, verse_elem in verse_elements.items():
        if key in chinese_verses:
            # Remove any child elements of verse_elem that are notes
            for child in list(verse_elem):
                if child.tag == 'note':
                    verse_elem.remove(child)
            # Clean the text to remove invalid XML characters
            verse_text = chinese_verses[key]
            verse_text = clean_text(verse_text)
            print(f"Processing Chapter {key[0]}, Verse {key[1]}")
            # Set the tail to the Chinese verse
            verse_elem.tail = verse_text
        else:
            print(f"Warning: Chinese verse not found for Chapter {key[0]}, Verse {key[1]}")
    return usx_tree

def main():
    usx_file = "E:/filetwo/Bible_documents/Bible/Bible_search/usx/66-REV.usx"
    usx_tree, root, verse_elements = parse_usx(usx_file)

    # Directory containing the HTML files
    html_dir = "E:/filetwo/Bible_documents/Bible/Bible_search/html/NT27revelation/Chapter/"

    # Collect all Chinese verses from HTML files
    chinese_verses = {}
    for chapter_num in range(1, 23):  # Genesis has 50 chapters
        html_file = os.path.join(html_dir, f"NT27rev_{chapter_num}.htm")
        if not os.path.exists(html_file):
            print(f"HTML file not found: {html_file}")
            continue
        chapter_verses = parse_html_chapter(html_file)
        chinese_verses.update(chapter_verses)

    # Replace verses in USX tree
    usx_tree = replace_verses(usx_tree, verse_elements, chinese_verses)

    # Remove English text from the entire USX tree
    remove_english_text(root)

    # Save the modified USX file
    output_usx_file = "66-modified_REV.usx"
    usx_tree.write(output_usx_file, encoding='UTF-8', xml_declaration=True, pretty_print=True)
    print(f"Modified USX file saved as {output_usx_file}")

if __name__ == "__main__":
    main()
