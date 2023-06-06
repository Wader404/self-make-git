import argparse         # parse cmd arguments
import collections      # for more container types
import configparser     # read and write a file whose format is used as a configuration file by git
import hashlib          # git use SHA-1
from math import ceil
import os               # provide some nice filesystem abstraction routines
import re               # regex
import sys              # access the actual cmd arguments
import zlib             # git compresses everything using zlib

argparser = argparse.ArgumentParser(description="The stupidest conten tracker")
argparsers = argparser.add_subparsers(title="Commands", dest="command")
argparsers.required = True


def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)

    if   args.command == "add"          : cmd_add(args)
    elif args.command == "cat-file"     : cmd_cat_file(args)
    elif args.command == "checkout"     : cmd_checkout(args)
    elif args.command == "commit"       : cmd_commit(args)
    elif args.command == "hash-object"  : cmd_hash_object(args)
    elif args.command == "init"         : cmd_init(args)
    elif args.command == "log"          : cmd_log(args)
    elif args.command == "ls-files"     : cmd_ls_files(args)
    elif args.command == "ls-tree"      : cmd_ls_tree(args)
    elif args.command == "merge"        : cmd_merge(args)
    elif args.command == "rebase"       : cmd_rebase(args)
    elif args.command == "rev-parse"    : cmd_rev_parse(args)
    elif args.command == "rm"           : cmd_rm(args)
    elif args.command == "show-ref"     : cmd_show_ref(args)
    elif args.command == "tag"          : cmd_tag(args)


class WitReopsitory (object):
    """A wit repository"""
    worktree = None
    witdir = None
    conf = None

    def __init__(self, path, force=False):
        self.worktree = path
        self.witdir = os.path.join(path, ".wit")

        if not (force or os.path.isdir(self.witdir)):
            raise Exception("Not a Wit reopsitory %s" % path)

        # Read configuration file in .git/config
        self.conf = configparser.ConfigParser()
        cf = repo_file(self, "config")

        if cf and os.path.exists(cf):
            self.conf.read([cf])
        elif not force:
            raise Exception("Configuration file missing")

        if not force:
            vers = int(self.conf.get("core", "repositoryformatversion"))
            if vers != 0:
                raise Exception("Unsupported repositoryformatversion %s" %vers)

    def repo_path(repo, *path):
        """Compute path under repo's witdir"""
        return os.path.join(repo.witdir, *path)

    def repo_file(repo, *path, mkdir=False):
        """Same as repo_path, but create dirname(*path) if absent. For example, repo_file(r, \"refs\", \"remotes\", \"origin\", \"HEAD\") will create .git/refs/remotes/origin"""
        if repo_dir(repo, *path[:-1], mkdir=mkdir):
            return repo_path(repo, *path)

    def repo_dir(repo, *path, mkdir=False):
        """Same as repo_path, but mkdir *path if absent if mkdir"""
        path = repo_path(repo, *path)

        if os.path.exists(path):
            if (os.path.isdir(path)):
                return path
            else:
                raise Exception("Not a directory" %path)

        if mkdir:
            os.makedirs(path)
            return path
        else:
            return None

    def repo_create(path):
        """Create a new repository at path."""
    
        repo = GitRepository(path, True)
    
        # First, we make sure the path either doesn't exist or is an empty dir
    
        if os.path.exists(repo.worktree):
            if not os.path.isdir(repo.worktree):
                raise Exception ("%s is not a directory!" % path)
            if os.listdir(repo.worktree):
                raise Exception("%s is not empty!" % path)
        else:
            os.makedirs(repo.worktree)
    
        assert(repo_dir(repo, "branches", mkdir=True))
        assert(repo_dir(repo, "objects", mkdir=True))
        assert(repo_dir(repo, "refs", "tags", mkdir=True))
        assert(repo_dir(repo, "refs", "heads", mkdir=True))
    
        # .git/description
        with open(repo_file(repo, "description"), "w") as f:
            f.write("Unnamed repository; edit this file 'description' to name the repository.\n")
    
        # .git/HEAD
        with open(repo_file(repo, "HEAD"), "w") as f:
            f.write("ref: refs/heads/master\n")
    
        with open(repo_file(repo, "config"), "w") as f:
            config = repo_default_config()
            config.write(f)
    
        return repo

    def repo_default_config():
        ret = configparser.ConfigParser()
    
        ret.add_section("core")
        ret.set("core", "repositoryformatversion", "0")
        ret.set("core", "filemode", "false")
        ret.set("core", "bare", "false")
    
        return ret
