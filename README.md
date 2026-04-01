# File Organizer Script

A Python script that automatically sorts files in a folder into subfolders based on their file type.
Run it on any messy folder and it will clean it up instantly.

---

## ⚠️ Warning

This script moves files on your system. Please use it carefully:

- Double-check the folder path before running
- Avoid running it on system or important directories (e.g. `C:\Windows`, `/usr/bin`)
- Test it on a small sample folder first before using it on anything important

---

## How It Works

The script scans the folder you point it at, checks each file's extension,
and moves it into the matching category subfolder. If a subfolder doesn't exist yet, it creates it.

```
Before:
my_folder/
├── photo.jpg
├── notes.txt
├── song.mp3
├── script.py
└── report.pdf

After:
my_folder/
├── Images/
│   └── photo.jpg
├── Documents/
│   ├── notes.txt
│   └── report.pdf
├── Audio/
│   └── song.mp3
└── Code/
    └── script.py
```

---

## Requirements

- Python 3.6+
- No external dependencies — uses standard library only (`os` and `shutil`)

---

## How to Run

**1. Run the script**

```bash
python organizer.py
```

**2. Enter the folder path when prompted**

```
Enter the path of the folder to organize: /Users/you/Downloads
```

**Example paths by operating system:**

| OS            | Example Path                        |
|---------------|-------------------------------------|
| macOS / Linux | `/Users/you/Downloads`              |
| Windows       | `C:\Users\You\Downloads`            |

---

## Project Structure

```
file_organizer/
│
└── organizer.py    # The entire script lives here
```

---

## Supported File Categories

| Category  | Extensions                                |
|-----------|-------------------------------------------|
| Images    | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`   |
| Audio     | `.mp3`, `.wav`, `.flac`                   |
| Documents | `.txt`, `.pdf`, `.docx`, `.xlsx`, `.pptx` |
| Code      | `.py`, `.js`, `.html`, `.css`, `.java`    |
| Video     | `.mp4`                                    |
| Others    | Anything not in the list above            |

---

## Edge Cases Handled

- **Unknown file types** → moved into an `Others/` folder instead of being skipped
- **Duplicate filenames** → automatically renamed by adding a number, e.g. `photo_1.jpg`, `photo_2.jpg`
- **Running twice** → safe to run multiple times; existing category folders are reused and files are added into them
- **Empty folder** → prints `Done! Total files moved: 0` and exits cleanly
- **File path entered instead of folder** → prints a clear error message and exits without crashing
- **Path doesn't exist** → prints a clear error message and exits without crashing
- **Extension case sensitivity** → handled case-insensitively, so `.JPG` and `.jpg` are treated the same

---

## Limitations

- Only organises files in the **top level** of the folder — does not go into subfolders
- Does not detect file content — relies on file extensions only, so a renamed file may be sorted incorrectly
- Does not undo changes automatically — once files are moved, you would have to move them back manually

---

## Example Output

```
Moved: photo.jpg -> Images/
Moved: notes.txt -> Documents/
Moved: song.mp3 -> Audio/
Moved: script.py -> Code/
Moved: unknown.xyz -> Others/
--- Done! Total files moved: 5 ---
```

---

## Notes

- To add support for a new file type, just add a line to the `EXTENSION_MAP` dictionary at the top of `organizer.py`

---

## Possible Future Improvements

- [ ] `--dry-run` flag to preview what would be moved without actually moving anything
- [ ] Accept folder path directly from the command line: `python organizer.py /path/to/folder`
- [ ] Recurse into subfolders with an optional `--recursive` flag
- [ ] A log file that records every move with timestamps
- [ ] Undo feature that moves everything back to the original location

---

## License

This project is open source and free to use under the MIT License.

---

## Author

Built as a beginner Python project to practice file system operations,
dictionaries, and writing clean reusable functions.
