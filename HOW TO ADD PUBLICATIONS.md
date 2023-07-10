# Guide on adding a new publication to the website 

1. Add the metadata of the publication as a new entry in the `pages/publications.md` file. 

    Example: 

    ```
      - title: "A Toolbox for Realtime Timeseries Anomaly Detection"
        authors: Markus Bobel, Ilias Gerostathopoulos, Tomas Bures
        venue: "IEEE International Conference on Software Architecture (ICSA 2020), to appear."
        doi: https://doi.org/10.1109/ICSA-C50368.2020.00053
        pdf: 2021-ICSA-IG-anomaly_detection_tool.pdf
        url: https://iliasger.github.io/pubs/ICSA2020-tool.pdf (ignored if pdf is present!)
        year: 2020
        type: conference
    ```
    Notes: 
    * `title` should always be given in double quotes
    * `venue` should always be given in double quotes 
    * You can leave all of `doi`, `pdf` and `url` empty if you prefer.  
    * You should fill in either `pdf` or `url`. In case both are provided, the `url` is ignored. 
    If you specify a `pdf`, then add your PDF document as described in step 2. 
    A `url` should point to a PDF document (e.g. in your personal website).      
    * As `type`, you can use one of `article`,`conference` (for both conference and workshop papers),
    `book` (for both books and book chapters),`thesis` (for PhD theses only), and `other` 
    (mostly for technical reports)
    
    

2. (optional, only if you want to add a pre/post print) Add a PDF file to the `files/pubs` folder. 
    The name of the PDF has to match the name you specified in the metadata entry (e.g. `2021-ICSA-IG-anomaly_detection_tool.pdf`) 

    As a suggestion, we can use the following pattern: \
    `<year>-<venue>-<group member initials>-<anything else>.pdf`


