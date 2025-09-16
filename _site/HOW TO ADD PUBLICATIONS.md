# How to update the publications

1. Browse to https://dblp.org/pers/
2. Search for all group members and find their identifiers (last two numbers of the URL on DBLP before “.html”)
3. Customize DBLP identifiers  in the variable “author_ids” of the script “dblp2bib.py” that is in the root directory of the  website repository
4. Run the script dblp2bib.py, it will generate a .bib file in the root directory
5. Browse to https://bibbase.org/
6. Click on “Get started”
7. Upload file by dropping the .bib file in 
8. “Drop .bib file here” (If not already done, create account)
9. Copy Javascript one-liner 
10. Update Javascript one-liner at the end of “publications.md” page
