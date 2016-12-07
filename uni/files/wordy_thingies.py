with open('more_text.txt', 'w') as new_file:
    new_file.write('')

import os
os.remove('more_text.txt')
