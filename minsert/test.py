from minsert import MarkdownFile
file = MarkdownFile('test.md')
things = {'thing1': 'hi hello',
          'thing2': 'ping pong',
          }
file.insert(things)
