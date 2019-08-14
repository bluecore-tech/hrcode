#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

url = "http://www.bluecore.com.cn/"
get_page = requests.get(url)
print(get_page.text)
