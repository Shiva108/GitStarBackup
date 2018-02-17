#!/usr/bin/env python

try:
    from git import Repo
    import requests
    import json
    import multiprocessing
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
    try:
        # Arguments
        parser = argparse.ArgumentParser(description='Get Github Starred Repos - gitgitstar.py')
        parser.add_argument("name", help='Name of Github user eg. Shiva108')
        args = parser.parse_args()
        # Variables
        name = str(args.name)
        url = 'https://api.github.com/users/' + name + '/starred?page=1&per_page=10000'
        # print(url)
        starred_repos = json.loads(requests.get(url).text)
        # print(starred_repos)
    except RuntimeError or OSError as e:
        print(e)
        pass
    try:
        cpus = multiprocessing.cpu_count()
    except NotImplementedError:
        cpus = 4
    try:
        while True:
            pool = multiprocessing.Pool(processes=cpus)
            pool.map(my_funky_clone, [i['clone_url'] for i in starred_repos])
    except KeyboardInterrupt:
        print('Interrupted by user keypress!')
        pass

if __name__ == "__main__":
main()