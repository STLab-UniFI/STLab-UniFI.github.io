# install package before running:
# pip install bibtexparser

import bibtexparser

with open('publications.bib') as bibtex_file:
    # bib_database = bibtexparser.load(bibtex_file)
    bib_database = bibtexparser.bparser.BibTexParser(common_strings=True).parse_file(bibtex_file)

md_string = ""
for entry in bib_database.entries:
    bib_type = entry["ENTRYTYPE"]
    if bib_type == "article":
        venue = entry["journal"]
        md_type = "article"
    elif bib_type == "inproceedings":
        venue = entry["booktitle"]
        md_type = "conference"
    elif bib_type == "inbook":
        venue = entry["title"]
        md_type = "book"
    elif bib_type == "phdthesis":
        venue = entry["organization"]
        md_type = "thesis"
    elif bib_type == "misc":
        venue = ""
        md_type = "other"
    elif bib_type == "book":
        venue = entry["publisher"]
        md_type = "book"
    else:
        print(bib_type)
    md_string += "  - title: "
    md_string += "\"" + entry["title"] + "\"\n"
    md_string += "    authors: "
    md_string += entry["author"] + "\n"
    md_string += "    type: "
    md_string += md_type + "\n"
    md_string += "    venue: "
    md_string += "\"" + venue + "\"\n"
    md_string += "    doi: "
    doi = entry["doi"] if "doi" in entry else ""
    md_string += doi + "\n"
    md_string += "    url: "
    url = entry["url"] if "url" in entry else ""
    md_string += url + "\n"
    md_string += "    year: "
    md_string += entry["year"] + "\n"
    # break

# print(md_string)
with open('output-raw.md', "w") as out:
    out.write(md_string)

# - title: "Online Experiment-Driven Learning and Adaptation"
# authors: Ilias Gerostathopoulos, Alexander Auf der Strasse
# venue: "Model-Based Engineering of Collaborative Embedded Systems, Springer"
# doi: https://doi.org/10.1007/978-3-030-62136-0_15
# pdf: 2021-CrestBook-IG-chapter.pdf
# year: 2021
# type: bookChapters