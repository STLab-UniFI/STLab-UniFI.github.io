import requests
from pybtex.database import parse_string, BibliographyData
import os

def download_bibtex(author_ids):
    bibtex_entries = []
    for author_id in author_ids:
        url = f"https://dblp.org/pid/{author_id}.bib?param=1"
        response = requests.get(url)
        if response.status_code == 200:
            bibtex_entries.append(response.text)
        else:
            print(f"Failed to download bibliography for author id: {author_id}")

    return bibtex_entries

def merge_bibtex(bibtex_entries):
    merged_bib = BibliographyData()
    for bibtex_entry in bibtex_entries:
        bib_data = parse_string(bibtex_entry, 'bibtex')
        for entry_key, entry in bib_data.entries.items():
            if entry_key not in merged_bib.entries:
                merged_bib.entries[entry_key] = entry

    return merged_bib

def save_bibtex(bib_data, filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    with open(file_path, 'w') as bibfile:
        bibfile.write(bib_data.to_string('bibtex'))

if __name__ == "__main__":
    author_ids = ["210/6216", "50/3792", "214/2069", "380/5383", "380/5231", "225/6724", "377/9232", "77/5805", "f/AlessandroFantechi", "195/3412", "169/4171", "290/3983"]
    bibtex_entries = download_bibtex(author_ids)
    merged_bib = merge_bibtex(bibtex_entries)
    save_bibtex(merged_bib, "STLab.bib")