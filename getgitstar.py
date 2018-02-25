#!/usr/bin/env python

# Written in python 3.5
# curl "https://api.github.com/users/shiva108/starred?page=1&per_page=10000" | grep -e 'git_url*' | cut -d \" -f 4 |   xargs -L1 git clone

try:
    from git import Repo
    import requests
    import json
    import multiprocessing
    import threading
    import os
    import argparse
except ImportError.args as e:
    print('Make sure modules are installed correctly! ')
except RuntimeError:
    print('Something went wrong! Module Import Runtime Error')


def my_funky_clone(url):
    dir_name = url.split('/')[-1][:-4]
    try:
        os.mkdir(dir_name)
        Repo.clone_from(url, dir_name)
        print(url)
    except RuntimeError:
        pass
    except KeyboardInterrupt:
        print('Interrupted by user keypress!')
        pass


def main():
    global starred_repos
    try:
        # Arguments
        parser = argparse.ArgumentParser(description='Get Github Starred Repos - getgitstar.py')
        parser.add_argument("name", help='Name of Github user eg. Shiva108')
        args = parser.parse_args()
        # Variables
        name = str(args.name)
        url = 'https://api.github.com/users/' + name + '/starred?page=1&per_page=10000'
        # print(url)
        starred_repos = json.loads(requests.get(url).text)
        print(starred_repos)
    except RuntimeError or OSError as e:
        print(e)
        for i in starred_repos['url']:
            t = threading.Thread(target=my_funky_clone(), args=url)
            t.start()
    except KeyboardInterrupt
        print('Interrupted by user keypress!')
        pass


if __name__ == "__main__":
    main()
    
