import codecs
import mimetypes
import os

from flask import abort, Flask, render_template, Response, redirect, request

app = Flask(__name__)

_local_cache = {}
_etag_cache  = {}


@app.route('/', methods = ['GET'])
def homepage():
    return render_template('index.html')

@app.route('/<path:doc_path>', methods = ['GET'])
def doc(doc_path):
    if not doc_path and doc_path == 'index.html':
        return redirect('/', 301)

    content       = None
    response_etag = _etag_cache[doc_path] if doc_path in _etag_cache else None

    request_etag = request.headers.get('If-None-Match')
    actual_path  = os.path.join('docs/build/html', doc_path)
    mimetype     = mimetypes.guess_type(doc_path, False)[0]

    if not os.path.exists(actual_path):
        return abort(404)

    request_etag = request_etag[1:-1] if request_etag else None

    print('Request {}: {} → {}'.format(doc_path, request_etag, response_etag))

    if request_etag == response_etag:
        print('Cache: HIT')
        return Response(status = 304)

    print('Cache: MISS')
    read_mode = 'r' if 'text/' in mimetype else 'rb'

    try:
        content = _local_cache[doc_path]
    except KeyError:
        with codecs.open(actual_path, read_mode) as f:
            content = f.read()

        _local_cache[doc_path] = content
        # _etag_cache[doc_path]  = response_etag

    response = Response(content, 200, mimetype = mimetype, content_type = mimetype)
    response.add_etag()

    _etag_cache[doc_path] = response.get_etag()[0]

    return response
