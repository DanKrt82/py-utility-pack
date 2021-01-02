''' A command-line tool to organize files into category directories. '''
structure = {'images': ['png', 'jpg', 'jpeg'],
             'videos': ['mp4', 'webp'],
             'docs': ['pdf', 'txt', 'md'],
             'animations': ['gif'],
             'ebooks': ['epub'],
             'archives': ['zip', 'tar', 'gz'],
             'databases': ['csv', 'xlsx', 'xls', 'db'],
             'configs': ['yaml', 'ini', 'env', 'yml'],
             'android': ['apk'],
             'webpages': ['html'],
             'scripts': ['py', 'sh', 'java', 'cpp', 'c', 'js']}

import yaml
with open('s.yml') as f:
    dd = yaml.full_load(f)
    assert dd == structure

