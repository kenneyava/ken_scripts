# Various Unix scripts

[Pull down the script using wget](https://medium.com/theloudcloud/download-a-file-from-github-using-linux-commands-f0ce4e154c25)

### In order to run these checks, wget the file down and run

```bash
rm wrldwriteable.py && \
  wget https://raw.githubusercontent.com//kenneyava/ken_scripts/main/wrldwriteable.py && \
  chmod u+x wrldwriteable.py

rm noownerorgrp.py && \
  wget https://raw.githubusercontent.com//kenneyava/ken_scripts/main/noownerorgrp.py && \
  chmod u+x noownerorgrp.py
```