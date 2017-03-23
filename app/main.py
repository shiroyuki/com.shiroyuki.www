import codecs
import mimetypes
import os

from flask import abort, Flask, render_template, Response, redirect

app = Flask(__name__)

_local_cache  = {}


@app.route('/', methods = ['GET'])
def homepage():
    return render_template('index.html')

@app.route('/<path:doc_path>', methods = ['GET'])
def doc(doc_path):
    if not doc_path and doc_path == 'index.html':
        return redirect('/', 301)

    content = None

    actual_path = os.path.join('docs/build/html', doc_path)
    mimetype    = mimetypes.guess_type(doc_path, False)[0]

    if not os.path.exists(actual_path):
        return abort(404)

    read_mode = 'r' if 'text/' in mimetype else 'rb'

    try:
        content = _local_cache[doc_path]
    except KeyError:
        with codecs.open(actual_path, read_mode) as f:
            content = f.read()

        _local_cache[doc_path] = content

    return Response(content, 200, mimetype = mimetype, content_type = mimetype)
