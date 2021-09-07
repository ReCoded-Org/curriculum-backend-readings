"""
This script takes tab delimited input file like so and automatically
creates the folder structure along with empty README files, per the contributing
guidelines. If you copy-paste from Google sheets, it will automatically add
tabs.

* Copy-paste the file below into `outline.txt` (too lazy to parameterize this
script) in the directory of the module that you want to use, i.e.,
`module5-testing/outline.txt`
* cd to the correct directory (this step is important for the working directory
to be correct)
* Run `python ../make_structure.py`
* Enjoy your created structure

1	What is a test?
1.1	Why testing is important?
2.1	Test-driven development
2.2	Example code
2.3	Properties of a good test
3	Types of tests
3.1	Popular testing libraries for JavaScript 
4	Testing lab
"""
import subprocess
import sys
import os

def main():
  with open('outline.txt', 'r') as f:
    text = f.read().strip().strip('\n')
    module_lines = text.split('\n')
    for line in module_lines:
      chapter_num, chapter_name = line.split('\t')
      
      # Convert casing: "Example code" to "example-code"
      normalized_chapter_name = chapter_name.replace(' ', '-').lower()
      subprocess.run(["mkdir", "-p", os.path.join(os.getcwd(),
                                                  normalized_chapter_name)])
      subprocess.run(["touch", os.path.join(os.getcwd(), normalized_chapter_name,
                                            "README.md")])

if __name__ == '__main__':
  main()
