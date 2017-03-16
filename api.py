#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import json
import codecs
import numpy as np
from vn_tokenizer.vn_tokenize import tokenize_vn
from vn_tagger.vn_tagger import tag_vn
from utils_io import  get_all_lines
import os

urls = (
        # '/api/tagging/text=(.*)', 'api_do_tagging',
        '/api/tokenizer/vn/', 'VnTokenizer',
        '/api/tagger/vn/', 'VnTagger',
        '/demo/(.*)', 'demo')

# print os.getcwd()


class VnTokenizer:
    def POST(self):

        workdir = os.getcwd()

        os.chdir("./vn_tokenizer")
        web.header('Content-Type', 'application/json')
        # post_data = web.input(_method='post')
        post_data = web.data()
        print post_data
        print type(post_data)
        # print post_data
        file_id = np.random.randint(1000000, 2000000)
        input_path = os.path.join("tmp", "user.%i.input.txt" % file_id)
        output_path = os.path.join("tmp", "user.%i.output.txt" % file_id)

        with codecs.open(input_path, "w", "utf-8") as f:
            # f.write(post_data["text"])
            # f.write(post_data)
            f.write(unicode(post_data, 'utf-8'))


        tokenize_vn(input_path, output_path)
        data = get_all_lines(output_path)
        os.remove(input_path)
        os.remove(output_path)

        os.chdir(workdir)

        return json.dumps(data, indent=4, sort_keys=True, encoding="utf-8")

class VnTagger:
    def POST(self):

        workdir = os.getcwd()

        os.chdir("./vn_tagger")
        web.header('Content-Type', 'application/xml')
        # post_data = web.input(_method='post') # form-data type
        post_data = web.data()

        file_id = np.random.randint(1000000, 2000000)
        input_path = os.path.join("tmp", "user.%i.input.txt" % file_id)
        output_path = os.path.join("tmp", "user.%i.output.txt" % file_id)

        with codecs.open(input_path, "w", "utf-8") as f:
            f.write(unicode(post_data, 'utf-8'))

        tag_vn(input_path, output_path)
        data = get_all_lines(output_path)
        os.remove(input_path)
        os.remove(output_path)
        os.chdir(workdir)

        # return json.dumps(data, indent=4, sort_keys=True, encoding="utf-8")
        return "\n".join(data)


class APIApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))


if __name__ == "__main__":
    app = APIApplication(urls, globals())
    app.run(port=8224)


