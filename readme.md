# tokenizer api

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

s1 = "Phó thủ tướng Malaysia Ahmad Zahid Hamidi hôm qua cho biết thi thể ông Kim Jong-nam đã được xác định dựa trên mẫu ADN con ông cung cấp."
s2 = "Phó thủ tướng Malaysia Ahmad Zahid Hamidi hôm qua cho biết thi thể ông Kim Jong-nam đã được xác định dựa trên mẫu ADN con ông cung cấp."

data = "\n".join([s1, s2])

r = requests.post("http://150.65.242.122:8224/api/tagger/vn/", data=data)

print r.text

```