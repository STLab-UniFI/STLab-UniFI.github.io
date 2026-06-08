⚠️ This guide was AI-generated and then corrected manually. If you spot any mistakes or improvement points, please feel free to edit this documentation :) 

## **Editing Content and Adding Posts on the STLab webpage via GitHub Web Interface**

### **Step-by-Step Guide**

#### **1\. Access the Repository**

* **Navigate to the website repository:** [https://github.com/STLab-UniFI/STLab-UniFI.github.io](https://github.com/STLab-UniFI/STLab-UniFI.github.io)  
* **Login to GitHub**: Log in with your credentials in the upper-right corner.  
* **Request Access**: If you don’t have edit access to the repository, request an invite from the repository owner *via* the web interface.

#### **2\. Edit Existing Content**

All website content follows the Markdown markup language. Pages are automatically rendered in static HTML pages *via* a Markdown to HTML transpiler once your edit is committed.

A Markdown cheat sheet is available here: [https://www.markdownguide.org/cheat-sheet/](https://www.markdownguide.org/cheat-sheet/)

If needed, lines in pure HTML can also be directly embedded into Markdown files.

* **Editing pages**: Navigate to the `_pages` directory.  
  * Click on the file you want to edit.  
  * Click the pencil icon (✏️) in the top right corner to edit the file.  
  * Make your changes in the text editor.  
  * Scroll down to the bottom of the page, add a commit message, and click “Commit changes”.

#### **3\. Add a New Post (displayed in the home as a news)**

* Navigate to the `_posts` directory.  
* Click the “Add file” button and select “Create new file”.  
* Name your file in the format `YYYY-MM-DD-title.md` (e.g., `2024-05-22-title.md` for a post of the 22 May 2024\)  
* Add the following front matter at the top of the file:

```
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD HH:MM:SS +0000
categories: category1 category2 (e.g., awards, guest_lecture, or conference)
---
```

* Write your content below the front matter.  
* Scroll down to the bottom of the page, add a commit message, and click “Commit new file”.

#### **4\. Upload and Link Pictures**

* Navigate to the `/img` directory (or `/assets/img` for website template related logos, e.g., favicons and loading gifs).  
* Click the “Add file” button and select “Upload files”.  
* Drag and drop your image files or click “choose your files” to upload from your computer.  
* Once uploaded, click “Commit changes” to save the images.  
* To link an image in your markdown file, use the following syntax:

```
![alt text](image.jpg)
```

* Make sure that all uploaded images are optimized for the web (around 250KB). The bigger the image size, the worst the whole webpage will perform on web searches.   
* Regarding awards documents, please make sure the documents are of satisfying quality and frontally-framed (to enforce consistency of the awards page)

#### **5\. Commit and Push Changes**

* When you edit a file or add a new post, make sure to add a meaningful commit message.  
* Click “Commit changes” to save your changes directly to the repository.

#### **6\. Create a Pull Request (if necessary)**

If you’re working on a fork or a branch, create a pull request to merge your changes into the main repository.

#### **7\. Previewing Your Changes**

* Unfortunately, you cannot preview changes directly via GitHub Web. However, you can check the live site after committing your changes to see the updates. Alternatively, you can deploy the website locally first (see following Chapter).

## **Editing Content and Adding Posts on the STLab Webpage via Local Changes**

#### **1\. Clone the Repository Locally**

* Open your terminal or Git Bash.  
* Clone the repository to your local machine using the command:

```
git clone https://github.com/STLab-UniFI/STLab-UniFI.github.io.git
```

* Navigate into the website repository directory:

```
cd STLab-UniFI.github.io
```

  #### **2\. Install Jekyll and Dependencies**

* Ensure you have Ruby and Bundler installed. If not, install them:

```
gem install bundler jekyll
```

* Install the dependencies:

```
bundle install
```

  #### **3\. Edit Existing Content**

  All website content follows the Markdown markup language. Pages are automatically rendered into static HTML pages via a Markdown to HTML transpiler once your edit is committed.

  A Markdown cheat sheet is available here: [https://www.markdownguide.org/cheat-sheet/](https://www.markdownguide.org/cheat-sheet/)

  If needed, lines in pure HTML can also be directly embedded into Markdown files.

* **Editing pages**: Navigate to the `_pages` directory.  
  * Open the file you want to edit in your preferred text editor.  
  * Make your changes.  
  * Save the file.

  #### **4\. Add a New Post (displayed in the home as a news)**

* Navigate to the `_posts` directory.  
* Create a new file named in the format `YYYY-MM-DD-title.md` (e.g., `2024-05-22-title.md` for a post on May 22, 2024).  
* Add the following front matter at the top of the file:

```
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD HH:MM:SS +0000
categories: category1 category2 (e.g., awards, guest_lecture, or conference)
---
```

* Write your content below the front matter.  
* Save the file.

  #### **5\. Upload and Link Pictures**

* Navigate to the `/img` directory (or `/assets/img` for website template-related logos, e.g., favicons and loading gifs).  
* Place your image files in this directory.  
* To link an image in your markdown file, use the following syntax:

```
![alt text](image.jpg)
```

* Make sure that all uploaded images are optimized for the web (around 250KB). The bigger the image size, the worst the whole webpage will perform on web searches.   
* Regarding awards documents, please make sure the documents are of satisfying quality and frontally-framed (to enforce consistency of the awards page)

  #### **6\. Preview Your Changes Locally**

* Run the Jekyll server to preview your changes locally:

```
bundle exec jekyll serve
```

* Open your browser and go to `http://localhost:4000` to see your changes.

  #### **7\. Commit and Push Changes**

* Add your changes:

```
git add .
```

* Commit your changes:

```
git commit -m "Add new post or edit content"
```

* Push your changes to the repository:

```
git push origin main
```

  #### **8\. Create a Pull Request (if necessary)**

* If you’re working on a fork or a branch, create a pull request to merge your changes into the main repository.
