import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import xml.etree.ElementTree as ET

import tkinter.font as tkFont


import sys, os



script_dir = os.path.dirname(os.path.abspath(__file__))
# Path to the 'Modified_usx_cn' directory
modified_usx_dir = os.path.join(script_dir, 'Modified_usx_cn')

# List of available books in Chinese
bible_books = [
    '创世纪',    # Genesis
    '出埃及记',  # Exodus
    '利未记',    # Leviticus
    '民数记',    # Numbers
    '申命记',    # Deuteronomy
    '约书亚记',
    '士师记',
    '路得记',
    '撒母耳记上',
    '撒母耳记下',
    '列王记上',
    '列王纪下',
    '历代志上',
    '历代志下',
    '以斯拉记',
    '尼希米记',
    '以斯帖记',
    '约伯记',
    '诗篇',
    '箴言',
    '传道书',
    '雅歌',
    '以赛亚书',
    '耶利米书',
    '耶利米哀歌',
    '以西结书',
    '但以理书',
    '何西阿书',
    '约珥书',
    '阿摩司书',
    '俄巴底亚书',
    '约拿书',
    '弥迦书',
    '那鸿书',
    '哈巴谷书',
    '西番雅书',
    '哈该书',
    '撒玛利亚书',
    '玛拉基书',
    '马太福音',
    '马可福音',
    '路加福音',
    '约翰福音',
    '使徒行传',
    '罗马书',
    '哥林多前书',
    '哥林多后书',
    '加拉太书',
    '以弗所书',
    '腓立比书',
    '歌罗西书',
    '帖撒罗尼迦前书',
    '帖撒罗尼迦后书',
    '提摩太前书',
    '提摩太后书',
    '提多书',
    '腓利门书',
    '希伯来书',
    '雅各书',
    '彼得前书',
    '彼得后书',
    '约翰一书',
    '约翰二书',
    '约翰三书',
    '犹大书',
    '启示录',
    # Add more books as you process them
]

# Mapping of book names to file paths
usx_files = {
    '创世纪': os.path.join(modified_usx_dir, '01-modified_GEN.usx'),
    '出埃及记': os.path.join(modified_usx_dir, '02-modified_EXO.usx'),
    '利未记': os.path.join(modified_usx_dir, '03-modified_LEV.usx'),
    '民数记': os.path.join(modified_usx_dir, '04-modified_NUM.usx'),
    '申命记': os.path.join(modified_usx_dir, '05-modified_DEU.usx'),
    '约书亚记': os.path.join(modified_usx_dir, '06-modified_JOS.usx'),
    '士师记': os.path.join(modified_usx_dir, '07-modified_JDG.usx'),
    '路得记': os.path.join(modified_usx_dir, '08-modified_RUT.usx'),
    '撒母耳记上': os.path.join(modified_usx_dir, '09-modified_1SA.usx'),
    '撒母耳记下': os.path.join(modified_usx_dir, '10-modified_2SA.usx'),
    '列王记上': os.path.join(modified_usx_dir, '11-modified_1KI.usx'),
    '列王纪下': os.path.join(modified_usx_dir, '12-modified_2KI.usx'),
    '历代志上': os.path.join(modified_usx_dir, '13-modified_1CH.usx'),
    '历代志下': os.path.join(modified_usx_dir, '14-modified_2CH.usx'),
    '以斯拉记': os.path.join(modified_usx_dir, '15-modified_EZR.usx'),
    '尼希米记': os.path.join(modified_usx_dir, '16-modified_NEH.usx'),
    '以斯帖记': os.path.join(modified_usx_dir, '17-modified_EST.usx'),
    '约伯记': os.path.join(modified_usx_dir, '18-modified_JOB.usx'),
    '诗篇': os.path.join(modified_usx_dir, '19-modified_PSA.usx'),
    '箴言': os.path.join(modified_usx_dir, '20-modified_PRO.usx'),
    '传道书': os.path.join(modified_usx_dir, '21-modified_ECC.usx'),
    '雅歌': os.path.join(modified_usx_dir, '22-modified_SNG.usx'),
    '以赛亚书': os.path.join(modified_usx_dir, '23-modified_ISA.usx'),
    '耶利米书': os.path.join(modified_usx_dir, '24-modified_JER.usx'),
    '耶利米哀歌': os.path.join(modified_usx_dir, '25-modified_LAM.usx'),
    '以西结书': os.path.join(modified_usx_dir, '26-modified_EZK.usx'),
    '但以理书': os.path.join(modified_usx_dir, '27-modified_DAN.usx'),
    '何西阿书': os.path.join(modified_usx_dir, '28-modified_HOS.usx'),
    '约珥书': os.path.join(modified_usx_dir, '29-modified_JOL.usx'),
    '阿摩司书': os.path.join(modified_usx_dir, '30-modified_AMO.usx'),
    '俄巴底亚书': os.path.join(modified_usx_dir, '31-modified_OBA.usx'),
    '约拿书': os.path.join(modified_usx_dir, '32-modified_JON.usx'),
    '弥迦书': os.path.join(modified_usx_dir, '33-modified_MIC.usx'),
    '那鸿书': os.path.join(modified_usx_dir, '34-modified_NAM.usx'),
    '哈巴谷书': os.path.join(modified_usx_dir, '35-modified_HAB.usx'),
    '西番雅书': os.path.join(modified_usx_dir, '36-modified_ZEP.usx'),
    '哈该书': os.path.join(modified_usx_dir, '37-modified_HAG.usx'),
    '撒玛利亚书': os.path.join(modified_usx_dir, '38-modified_ZEC.usx'),
    '玛拉基书': os.path.join(modified_usx_dir, '39-modified_MAL.usx'),
    '马太福音': os.path.join(modified_usx_dir, '40-modified_MAT.usx'),
    '马可福音': os.path.join(modified_usx_dir, '41-modified_MRK.usx'),
    '路加福音': os.path.join(modified_usx_dir, '42-modified_LUK.usx'),
    '约翰福音': os.path.join(modified_usx_dir, '43-modified_JHN.usx'),
    '使徒行传': os.path.join(modified_usx_dir, '44-modified_ACT.usx'),
    '罗马书': os.path.join(modified_usx_dir, '45-modified_ROM.usx'),
    '哥林多前书': os.path.join(modified_usx_dir, '46-modified_1CO.usx'),
    '哥林多后书': os.path.join(modified_usx_dir, '47-modified_2CO.usx'),
    '加拉太书': os.path.join(modified_usx_dir, '48-modified_GAL.usx'),
    '以弗所书': os.path.join(modified_usx_dir, '49-modified_EPH.usx'),
    '腓立比书': os.path.join(modified_usx_dir, '50-modified_PHP.usx'),
    '歌罗西书': os.path.join(modified_usx_dir, '51-modified_COL.usx'),
    '帖撒罗尼迦前书': os.path.join(modified_usx_dir, '52-modified_1TH.usx'),
    '帖撒罗尼迦后书': os.path.join(modified_usx_dir, '53-modified_2TH.usx'),
    '提摩太前书': os.path.join(modified_usx_dir, '54-modified_1TI.usx'),
    '提摩太后书': os.path.join(modified_usx_dir, '55-modified_2TI.usx'),
    '提多书': os.path.join(modified_usx_dir, '56-modified_TIT.usx'),
    '腓利门书': os.path.join(modified_usx_dir, '57-modified_PHM.usx'),
    '希伯来书': os.path.join(modified_usx_dir, '58-modified_HEB.usx'),
    '雅各书': os.path.join(modified_usx_dir, '59-modified_JAS.usx'),
    '彼得前书': os.path.join(modified_usx_dir, '60-modified_1PE.usx'),
    '彼得后书': os.path.join(modified_usx_dir, '61-modified_2PE.usx'),
    '约翰一书': os.path.join(modified_usx_dir, '62-modified_1JN.usx'),
    '约翰二书': os.path.join(modified_usx_dir, '63-modified_2JN.usx'),
    '约翰三书': os.path.join(modified_usx_dir, '64-modified_3JN.usx'),
    '犹大书': os.path.join(modified_usx_dir, '65-modified_JUD.usx'),
    '启示录': os.path.join(modified_usx_dir, '66-modified_REV.usx'),
    
    # Add more mappings as you have more USX files
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
    font_size_label = tk.Label(root, text="字体大小：")
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
