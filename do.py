import os
from minsert import MarkdownFile


def readme():
    packs = []
    for thing in os.listdir(os.getcwd()):
        if os.path.isdir(thing) and os.path.isfile(os.path.join(thing, 'setup.py')):
            if thing == 'template':
                continue
            desc = open(f'{thing}/README.md').readlines()[2]
            packs.append((thing, desc))

    table_of_packages = '| Package | Description |\n|--|--|\n'

    for pack, desc in packs:
        table_of_packages += f'| [{pack}](/{pack}/README.md) | {desc.strip()} |\n'

    file = MarkdownFile('README.md')
    file.insert({'packages': table_of_packages})
