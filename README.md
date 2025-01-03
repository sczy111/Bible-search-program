# Bible Search Program

- A Bible search program written by Python 3.10 for both Chinese and English users to use offline.
- The project relies on external sources for Bible data, including the ASV version and Chinese translations.
- Contributions are welcome, and updates to support other versions may be added in the future.
---

## For General Users

If you just want to use this program, download it from the release:  
[Download the Bible Search Program](https://github.com/sczy111/Bible-search-program/releases)


---

## For Developers

### How to Use:
1. Download the source code.
2. Run `main.py` which is Chinese version or `main_en.py` which is English version to execute the program.
> **Notes**:
> - Ensure you have Python installed on your system before running the program.
> - The program may require minor modifications if you use a different directory structure or system setup.

---

### Project Structure and Details:

#### Key Files:
- **`main.py or main_en.py`**: The main program required to run the project.
- **`usx` folder**: Contains files sourced from [Open Bible Info](https://github.com/openbibleinfo/American-Standard-Version-Bible), which are the American Standard Version (ASV) of the Bible.
- **`Modified_usx_cn` folder**: Contains the Chinese version of the Bible for each book.
- **`Version_update.py`**: Includes the program used to update the English version to the Chinese version. You can use this to update your own language.


#### Code Highlights:
The key code segment for the version update process (from `Version_update`) is from **lines 142–162**:

```python
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


