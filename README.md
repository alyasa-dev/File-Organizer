# File Organizer Script

A Python script that automatically sorts files in a folder into subfolders based on their file type.
Run it on any messy folder and it will clean it up instantly.

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
├── Image/
│   └── photo.jpg
├── Document/
│   ├── notes.txt
│   └── report.pdf
├── Audio/
│   └── song.mp3
└── Code/
    └── script.py
```

---

## Project Structure

```
file_organizer/
│
└── organizer.py    # The entire script lives here
```

---

## How to Run

**1. Make sure you have Python installed**

```bash
python --version    # should be 3.6 or higher
```

**2. Run the script**

```bash
python organizer.py
```

**3. Enter the folder path when prompted**

```
Enter the path of the folder to organize: /Users/you/Downloads
```

No external libraries needed. Uses Python standard library only (`os` and `shutil`).

---

## Supported File Categories

| Category  | Extensions                              |
|-----------|-----------------------------------------|
| Image     | `.jpg` `.jpeg` `.png` `.gif` `.svg`     |
| Audio     | `.mp3` `.wav` `.flac`                   |
| Document  | `.txt` `.pdf` `.docx` `.xlsx` `.pptx`   |
| Code      | `.py` `.js` `.html` `.css` `.java`      |
| Video     | `.mp4`                                  |
| Others    | Anything not in the list above          |

---

## Edge Cases Handled

- **Unknown file types** → moved into an `Others/` folder instead of being skipped
- **Duplicate filenames** → automatically renamed by adding a number, e.g. `photo_1.jpg`, `photo_2.jpg`
- **Running twice** → safe to run multiple times, already-organised files stay put and nothing crashes
- **Empty folder** → prints `Done! Total files moved: 0` and exits cleanly
- **File path entered instead of folder** → prints a clear error message and exits without crashing
- **Path doesn't exist** → prints a clear error message and exits without crashing

---

## Example Output

```
Moved: photo.jpg -> Image/
Moved: notes.txt -> Document/
Moved: song.mp3 -> Audio/
Moved: script.py -> Code/
Moved: unknown.xyz -> Others/
--- Done! Total files moved: 5 ---
```

---

## Notes

- The script only organises files in the **top level** of the folder — it does not go into subfolders
- The category subfolders it creates (`Image/`, `Audio/`, etc.) are not touched on re-runs
- To add a new file type, just add a line to the `EXTENSION_MAP` dictionary at the top of the script

---

## Possible Future Improvements

- [ ] `--dry-run` flag to preview what would be moved without actually moving anything
- [ ] Accept folder path directly from the command line using `sys.argv`
- [ ] Recurse into subfolders with an optional `--recursive` flag
- [ ] A log file that records every move with timestamps
- [ ] Undo feature that moves everything back to the original location

---

## Author

Built as a beginner Python project to practice file system operations,
dictionaries, and writing clean reusable functions.
