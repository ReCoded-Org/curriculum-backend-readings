"""
This script takes tab delimited input file like so and automatically
creates the folder structure for readings along with empty README files, per the
contributing guidelines. If you copy-paste from Google sheets, it will
automatically add tabs.

Sorry, didn't feel like handling labs, so you just need to delete the lab folder
when it gets created or rename it manually.

* Copy-paste the file below into `outline.txt` (too lazy to parameterize this
script) in the directory of the module that you want to use, i.e.,
`module5-testing/outline.txt`
* cd to the correct directory (this step is important for the working directory
to be correct)
* Run `python3 ../make_structure.py` (not python2)
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
import string
import sys
import os

# https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
def remove_punctuation(s):
  return s.translate(str.maketrans('', '', string.punctuation))

def main():
  with open('outline.txt', 'r') as f:
    text = f.read().strip().strip('\n')
    module_lines = text.split('\n')
    for line in module_lines:
      chapter_num, chapter_name = line.split('\t')
      
      # Convert casing: "Example code" to "example-code"
      normalized_chapter_name = remove_punctuation(chapter_name).replace(' ', '-').lower()
      # Make directories
      dir_name = "r" + chapter_num.strip() + '-' + normalized_chapter_name.strip()
      subprocess.run(["mkdir", "-p", os.path.join(os.getcwd(), dir_name)])
      # Make README files
      subprocess.run(["touch", os.path.join(os.getcwd(), dir_name, "README.md")])

if __name__ == '__main__':
  main()
