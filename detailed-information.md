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
    compress and decompress module compatible with gzip  


## explanations

`# initial interface`: define a command line user interface useing "Commands command" to represent "git xxx"  

`function 'main'`: call different functions according to "command" in "Commands
command"  

`class WitRepository`: "worktree" means all the files under wit's control, "witdir" means the location "~/.wit"  
"force" disables all check, which allows tocreate repository even from invalid filesystem locations  

`function 'repo_path'`: path building function  

`function repo_file/repo_dir`: return and optionally create a path to a file or a directory  

`function repo_create`: create a repository and create some necessary paths  

`function repo_find`: find the root of the current repository  
