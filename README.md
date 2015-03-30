# files
Script recursively walk the “root_dir” and detect all the files under that dir contains “keywords” and count the number of files for that sub dir. All results saved in a key:value array with key being subdir string, and value being counts of file contains the key line.
Output:
Output array of all the data, for example {'D:\\TEMP\\test\\New folder\\New folder (3)': 2, 'D:\\TEMP\\test\\New folder': 1, 'D:\\TEMP\\test\\New folder (2)': 3}
An output graph with a plot with X as subdir name string, Y as count values.

To run it:
filesop.py -rd D:\TEMP\test -kw ^[a-zA-Z]+_TESTResult.*
