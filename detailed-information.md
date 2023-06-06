# detailed information and explanations

## modules used

1. argparse  
    url:https://docs.python.org/3/library/argparse.html  
    create command line user interfaces  

2. collections  
    url:https://docs.python.org/3/library/collections.html  

3. configparser  
    url:https://docs.python.org/3/library/configparser.html  
    help create configuration file whose format is similar to MS Windows INI  

4. hashlib  
    url:https://docs.python.org/3/library/hashlib.html  

5. os  
    url:https://docs.python.org/3/library/os.html  

6. sys  
    url:https://docs.python.org/3/library/sys.html  

7. zlib  
    url:https://docs.python.org/3/library/zlib.html


## explanations

line 11-13: define a command line user interface
    use "Commands command" to represent "git xxx"

line 16-33: call different functions according to "command" in "Commands
command"

line 38-40: "worktree" means all the files under wit's control, "witdir" means
the location "~/.wit"

line 42-61: "force" disables all check, which allows tocreate repository even
from invalid filesystem locations

line 63-65: path building function

line 67-86: return and optionally create a path to a file or a directory

line 92-124: create a repository and create some necessary paths

