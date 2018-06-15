# -*- coding: utf-8 -*-
import os  
# import sys  
# line = sys.argv[1]  
line = '# -*- coding: utf-8 -*-'  
py_files = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']  
for filename in py_files:  
    if filename == 'addoneline.py':  
        continue  
    with open (filename, 'r',encoding='utf-8') as f:  
        orig_f = f.read()
    if 'utf-8' not in orig_f[0:20]:  
        new_f = line + '\n' + orig_f  
        with open (filename, 'w') as f:  
            f.write(new_f)  