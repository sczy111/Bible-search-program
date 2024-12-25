import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import xml.etree.ElementTree as ET

import tkinter.font as tkFont


import sys, os



script_dir = os.path.dirname(os.path.abspath(__file__))
# Path to the 'Modified_usx_cn' directory
modified_usx_dir = os.path.join(script_dir, 'usx')

# List of available books in Chinese
bible_books = [
    'Genesis',
    'Exodus',
    'Leviticus',
    'Numbers',
    'Deuteronomy',
    'Joshua',
    'Judges',
    'Ruth',
    '1 Samuel',
    '2 Samuel',
    '1 Kings',
    '2 Kings',
    '1 Chronicles',
    '2 Chronicles',
    'Ezra',
    'Nehemiah',
    'Esther',
    'Job',
    'Psalms',
    'Proverbs',
    'Ecclesiastes',
    'Song of Songs',
    'Isaiah',
    'Jeremiah',
    'Lamentations',
    'Ezekiel',
    'Daniel',
    'Hosea',
    'Joel',
    'Amos',
    'Obadiah',
    'Jonah',
    'Micah',
    'Nahum',
    'Habakkuk',
    'Zephaniah',
    'Haggai',
    'Zechariah',
    'Malachi',
    'Matthew',
    'Mark',
    'Luke',
    'John',
    'Acts',
    'Romans',
    '1 Corinthians',
    '2 Corinthians',
    'Galatians',
    'Ephesians',
    'Philippians',
    'Colossians',
    '1 Thessalonians',
    '2 Thessalonians',
    '1 Timothy',
    '2 Timothy',
    'Titus',
    'Philemon',
    'Hebrews',
    'James',
    '1 Peter',
    '2 Peter',
    '1 John',
    '2 John',
    '3 John',
    'Jude',
    'Revelation'
]


# Mapping of book names to file paths
usx_files = {
    'Genesis': os.path.join(modified_usx_dir, '01-GEN.usx'),
    'Exodus': os.path.join(modified_usx_dir, '02-EXO.usx'),
    'Leviticus': os.path.join(modified_usx_dir, '03-LEV.usx'),
    'Numbers': os.path.join(modified_usx_dir, '04-NUM.usx'),
    'Deuteronomy': os.path.join(modified_usx_dir, '05-DEU.usx'),
    'Joshua': os.path.join(modified_usx_dir, '06-JOS.usx'),
    'Judges': os.path.join(modified_usx_dir, '07-JDG.usx'),
    'Ruth': os.path.join(modified_usx_dir, '08-RUT.usx'),
    '1 Samuel': os.path.join(modified_usx_dir, '09-1SA.usx'),
    '2 Samuel': os.path.join(modified_usx_dir, '10-2SA.usx'),
    '1 Kings': os.path.join(modified_usx_dir, '11-1KI.usx'),
    '2 Kings': os.path.join(modified_usx_dir, '12-2KI.usx'),
    '1 Chronicles': os.path.join(modified_usx_dir, '13-1CH.usx'),
    '2 Chronicles': os.path.join(modified_usx_dir, '14-2CH.usx'),
    'Ezra': os.path.join(modified_usx_dir, '15-EZR.usx'),
    'Nehemiah': os.path.join(modified_usx_dir, '16-NEH.usx'),
    'Esther': os.path.join(modified_usx_dir, '17-EST.usx'),
    'Job': os.path.join(modified_usx_dir, '18-JOB.usx'),
    'Psalms': os.path.join(modified_usx_dir, '19-PSA.usx'),
    'Proverbs': os.path.join(modified_usx_dir, '20-PRO.usx'),
    'Ecclesiastes': os.path.join(modified_usx_dir, '21-ECC.usx'),
    'Song of Songs': os.path.join(modified_usx_dir, '22-SNG.usx'),
    'Isaiah': os.path.join(modified_usx_dir, '23-ISA.usx'),
    'Jeremiah': os.path.join(modified_usx_dir, '24-JER.usx'),
    'Lamentations': os.path.join(modified_usx_dir, '25-LAM.usx'),
    'Ezekiel': os.path.join(modified_usx_dir, '26-EZK.usx'),
    'Daniel': os.path.join(modified_usx_dir, '27-DAN.usx'),
    'Hosea': os.path.join(modified_usx_dir, '28-HOS.usx'),
    'Joel': os.path.join(modified_usx_dir, '29-JOL.usx'),
    'Amos': os.path.join(modified_usx_dir, '30-AMO.usx'),
    'Obadiah': os.path.join(modified_usx_dir, '31-OBA.usx'),
    'Jonah': os.path.join(modified_usx_dir, '32-JON.usx'),
    'Micah': os.path.join(modified_usx_dir, '33-MIC.usx'),
    'Nahum': os.path.join(modified_usx_dir, '34-NAM.usx'),
    'Habakkuk': os.path.join(modified_usx_dir, '35-HAB.usx'),
    'Zephaniah': os.path.join(modified_usx_dir, '36-ZEP.usx'),
    'Haggai': os.path.join(modified_usx_dir, '37-HAG.usx'),
    'Zechariah': os.path.join(modified_usx_dir, '38-ZEC.usx'),
    'Malachi': os.path.join(modified_usx_dir, '39-MAL.usx'),
    'Matthew': os.path.join(modified_usx_dir, '40-MAT.usx'),
    'Mark': os.path.join(modified_usx_dir, '41-MRK.usx'),
    'Luke': os.path.join(modified_usx_dir, '42-LUK.usx'),
    'John': os.path.join(modified_usx_dir, '43-JHN.usx'),
    'Acts': os.path.join(modified_usx_dir, '44-ACT.usx'),
    'Romans': os.path.join(modified_usx_dir, '45-ROM.usx'),
    '1 Corinthians': os.path.join(modified_usx_dir, '46-1CO.usx'),
    '2 Corinthians': os.path.join(modified_usx_dir, '47-2CO.usx'),
    'Galatians': os.path.join(modified_usx_dir, '48-GAL.usx'),
    'Ephesians': os.path.join(modified_usx_dir, '49-EPH.usx'),
    'Philippians': os.path.join(modified_usx_dir, '50-PHP.usx'),
    'Colossians': os.path.join(modified_usx_dir, '51-COL.usx'),
    '1 Thessalonians': os.path.join(modified_usx_dir, '52-1TH.usx'),
    '2 Thessalonians': os.path.join(modified_usx_dir, '53-2TH.usx'),
    '1 Timothy': os.path.join(modified_usx_dir, '54-1TI.usx'),
    '2 Timothy': os.path.join(modified_usx_dir, '55-2TI.usx'),
    'Titus': os.path.join(modified_usx_dir, '56-TIT.usx'),
    'Philemon': os.path.join(modified_usx_dir, '57-PHM.usx'),
    'Hebrews': os.path.join(modified_usx_dir, '58-HEB.usx'),
    'James': os.path.join(modified_usx_dir, '59-JAS.usx'),
    '1 Peter': os.path.join(modified_usx_dir, '60-1PE.usx'),
    '2 Peter': os.path.join(modified_usx_dir, '61-2PE.usx'),
    '1 John': os.path.join(modified_usx_dir, '62-1JN.usx'),
    '2 John': os.path.join(modified_usx_dir, '63-2JN.usx'),
    '3 John': os.path.join(modified_usx_dir, '64-3JN.usx'),
    'Jude': os.path.join(modified_usx_dir, '65-JUD.usx'),
    'Revelation': os.path.join(modified_usx_dir, '66-REV.usx')
}


def load_usx(file_path):
    """Load and parse the USX file."""
    tree = ET.parse(file_path)
    return tree.getroot()

def search_verses(usx_roots, keyword):
    results = []
    for usx_root in usx_roots:
        book_name = None
        
        current_chapter = None
        current_verse = None
        current_text = ""

        for elem in usx_root.iter():
            if elem.tag == 'book':
                # Record the book name
                book_name = elem.text or elem.get('code')

            elif elem.tag == 'chapter':
                # 1) Close out the previous verse if needed
                if current_verse and keyword.lower() in current_text.lower():
                    results.append({
                        'book': book_name,
                        'chapter': current_chapter,
                        'verse': current_verse,
                        'text': current_text.strip(),
                    })
                
                # 2) Now update the current chapter
                current_chapter = elem.get('number')
                
                # Reset current_verse and current_text so we don’t accidentally carry them
                current_verse = None
                current_text = ""

            elif elem.tag == 'verse':
                # 1) Close out the previous verse if needed
                if current_verse and keyword.lower() in current_text.lower():
                    results.append({
                        'book': book_name,
                        'chapter': current_chapter,
                        'verse': current_verse,
                        'text': current_text.strip(),
                    })
                
                # 2) Now update to the new verse
                current_verse = elem.get('number')
                
                # Start fresh text for this verse
                current_text = elem.tail or ""

            elif elem.tag == 'note':
                # Typically we skip note’s text but keep the tail
                if elem.tail:
                    current_text += elem.tail

            else:
                # Accumulate text in current_text
                if elem.text:
                    current_text += elem.text
                if elem.tail:
                    current_text += elem.tail

        # After iterating through all elements in this USX root,
        # we might have a “last verse” not closed out yet:
        if current_verse and keyword.lower() in current_text.lower():
            results.append({
                'book': book_name,
                'chapter': current_chapter,
                'verse': current_verse,
                'text': current_text.strip(),
            })
    return results


def adjust_font_size(font_obj, delta, display_label):
    """Adjust the font size by delta and update the display label."""
    current_size = font_obj.cget("size")
    new_size = current_size + delta
    if new_size < 8:  # Set a minimum font size
        new_size = 8
    elif new_size > 48:  # Set a maximum font size
        new_size = 48
    font_obj.configure(size=new_size)
    # Update the display label
    display_label.config(text=f"{new_size} pt")

def center_window(root, width=640, height=480):
    """Center the window on the screen."""
    # Update the window to get the correct width and height
    root.update_idletasks()
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Calculate position x and y coordinates
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f'{width}x{height}+{x}+{y}')

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Bible_search")
    center_window(root, 640, 480)  # Set and center the window size
    root.minsize(640, 480)         # Set the minimum window size

    # Create a Font object for the result text
    default_font_size = 12  # Set the default font size
    result_font = tkFont.Font(family="TkDefaultFont", size=default_font_size)
    
    # Create and place the widgets
    tk.Label(root, text="Select：").grid(row=0, column=0, padx=5, pady=5, sticky='w')
    
    # Starting book dropdown
    start_book_var = tk.StringVar(value=bible_books[0])
    start_book_combo = ttk.Combobox(root, textvariable=start_book_var, values=bible_books, state='readonly')
    start_book_combo.grid(row=0, column=1, padx=5, pady=5, sticky='we')
    
    tk.Label(root, text="to").grid(row=0, column=2)
    
    # Ending book dropdown
    end_book_var = tk.StringVar(value=bible_books[-1])
    end_book_combo = ttk.Combobox(root, textvariable=end_book_var, values=bible_books, state='readonly')
    end_book_combo.grid(row=0, column=3, padx=5, pady=5, sticky='we')
    
    # Keyword entry
    tk.Label(root, text="Keyword：").grid(row=1, column=0, padx=5, pady=5, sticky='w')
    keyword_entry = tk.Entry(root)
    keyword_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky='we')
    
    # Search button
    search_button = tk.Button(root, text="Search", command=lambda: perform_search(
        start_book_var.get(), end_book_var.get(), keyword_entry.get(), result_text),width = 10,height =2)
    search_button.grid(row=2, column=2, padx=5, pady=5)
    
    # Font size adjustment buttons
    font_size_label = tk.Label(root, text="font：")
    font_size_label.grid(row=2, column=3, padx=5, pady=5, sticky='e')
    
    # Create a frame to hold the font adjustment buttons
    font_adjust_frame = tk.Frame(root)
    font_adjust_frame.grid(row=2, column=4, padx=0, pady=5, sticky='w')

    # Decrease font size button
    decrease_font_button = tk.Button(
        font_adjust_frame,
        text="-",
        command=lambda: adjust_font_size(result_font, -1, font_size_display)
    )
    decrease_font_button.pack(side=tk.LEFT, padx=1)

    # Increase font size button
    increase_font_button = tk.Button(
        font_adjust_frame,
        text="+",
        command=lambda: adjust_font_size(result_font, 1, font_size_display)
    )
    increase_font_button.pack(side=tk.LEFT, padx=1)
    
    # Font size display
    font_size_display = tk.Label(root, text=f"{default_font_size} pt")
    font_size_display.grid(row=2, column=5, padx=5, pady=5, sticky='w')
    
    # Result display area
    result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=result_font)
    result_text.grid(row=3, column=0, columnspan=5, padx=5, pady=5, sticky='nsew')
    
    # Configure column weights
    for i in range(5):
        root.columnconfigure(i, weight=1)
    
    # Configure row weights
    root.rowconfigure(3, weight=1)
    
    # Bind keyboard shortcuts for font size adjustment
    root.bind('<Control-plus>', lambda event: adjust_font_size(result_font, 1, font_size_display))
    root.bind('<Control-minus>', lambda event: adjust_font_size(result_font, -1, font_size_display))
    
    root.mainloop()



def perform_search(start_book, end_book, keyword, result_text_widget):
    # Clear previous results
    result_text_widget.delete(1.0, tk.END)

    if not keyword.strip():
        messagebox.showwarning("Input Error", "Please enter a keyword to search.")
        return

    # Get the indices of the start and end books
    try:
        start_index = bible_books.index(start_book)
        end_index = bible_books.index(end_book)
    except ValueError:
        messagebox.showerror("Selection Error", "Selected books are not available.")
        return

    if start_index > end_index:
        messagebox.showerror("Selection Error", "Start book must come before end book.")
        return

    # Collect the USX roots for the selected books
    selected_books = bible_books[start_index:end_index + 1]
    usx_roots = []
    for book_code in selected_books:
        usx_file = usx_files.get(book_code)
        if usx_file and os.path.exists(usx_file):
            usx_root = load_usx(usx_file)
            usx_roots.append(usx_root)
        else:
            messagebox.showwarning("File Not Found", f"USX file for {book_code} not found.")
            return

    # Perform the search
    results = search_verses(usx_roots, keyword)

    # Display the results
    if results:
        result_text_widget.insert(tk.END, f"Found {len(results)} results for '{keyword}':\n\n")
        for result in results:
            result_text_widget.insert(tk.END, f"{result['book']} {result['chapter']}:{result['verse']} - {result['text']}\n\n")
    else:
        result_text_widget.insert(tk.END, f"No results found for '{keyword}'.")

if __name__ == "__main__":
    main()
