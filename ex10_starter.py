import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
for filename in glob.glob(pattern):
    print(filename)

# TODO: use os.path.getsize to find each file's size
for filename in glob.glob(pattern):
    print(os.path.getsize(filename))

# TODO: Add a test to only display files that are not zero length
for filename in glob.glob(pattern):
    if os.path.getsize(filename) > 0:
        print(os.path.getsize(filename))

# TODO: Remove the leading directory name(s) from each filename before you print it -

for filename in glob.glob(pattern):
    print(os.path.basename(filename))

