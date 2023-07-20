import os

"""
The functions below are used to perform a set of pipelined operations that:

* list_files       - Lists all the files in this directory
* filter_extension - Filters the file names, to only include files with the given extension
* read_lines       - Reads all the lines of these files
* grep             - Filters these lines, to only include lines containing the given pattern

At the moment these functions all return lists.

The code at the bottom of this file uses these functions to find the print(...)
statements from all python files in this directory and then display these one
at a time, each time the user hits 'Enter'

* Run this file, and look at the output. You should see that all of the python
  files are read before the first line is displayed.

* Update the four functions so they return generators instead of lists. You
  shouldn't need to change any code outside these files.

  Make sure to keep the line that prints "Reading file:" in `read_lines`

* Run the script again, and pay attention to when the files are read. You should
  now see that only the first file is read before the first matched line is
  displayed.

"""


def list_files(path):
    """Return all the files located in `path`"""
    for filename in os.listdir(path):
        yield os.path.join(path, filename)  # Create the full path


def filter_extension(filenames, extension):
    """Return only the filenames with the extension provided"""
    return (
        path
        for path in filenames
        if '.' in path
        and path.split('.')[-1] == extension
    )


def read_lines(filenames):
    """Return all of the lines from all the filenames"""
    for filename in filenames:
        print(f"Reading file: {filename}\n")
        with open(filename) as file:
            for item in file:
                yield item


def grep(lines, pattern):
    """Filter the lines to only those containing the pattern specified"""
    return (line for line in lines if pattern in line)


# DON'T EDIT THE CODE BELOW THIS LINE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

this_dir = os.path.dirname(os.path.abspath(__file__)) # The directory containing this file

# Pipelined operations to find all print statements in python files
print("\nSearching for print statements...\n")
filenames        = list_files(this_dir)
python_files     = filter_extension(filenames, 'py')
all_lines        = read_lines(python_files)
print_statements = grep(all_lines, 'print(')


# Step through the resulting lines one at a time
print("    First print statement found is:\n")
for line in print_statements:
    print('     ', line.strip())
    input("\n    Hit enter to see the next one...\n")
