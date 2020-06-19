# dumbPythonScripts
Collection of short stupid scripts made by me to automate boring/stupid stuff, don't expect anything special, I do each script in less than 10 mins (or about 10 mins)
### copy_delete.py
#### multiplatform script (works on Windows, Linux and macOS)
Short script that deletes the copies marked with '(n)'. Where n is the number of copies

EXAMPLE OF A FILE: "IMG-130130.jpg"

EXAMPLE OF A COPY: "IMG-130130 (1).jpg"

The scripts deletes the copy and leaves the original file in the dir.

#### USAGE:
Put the script in the directory where the copies are found.
Execute in the terminal the command:

> python3 copy_delete.py

### lineCounter.py
#### multiplatform script (works on Windows, Linux and macOS)
#### script to count the lines of code in a C project.

The scripts counts all the lines of code in a C project except for the empty lines, but it doesn't exclude the lines of comments.

#### USAGE:
Put the script in the root directory of your C project, and run:

> python3 lineCounter.py

The script will find all the subdirectories and files and it will do the job by its own.
