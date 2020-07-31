import re
from unidecode import unidecode
from flask import request, redirect, url_for
from urllib.parse import urlparse, urljoin


_punct_re = re.compile(r'[\t !"#$&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-', max_len=None):
    """Generates and ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        result.extend(unidecode(word).lower().split())

    slug = str(delim.join(result))
    return slug[:max_len] if max_len else slug


def is_safe_url(target):
    """保证域名相同"""
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def redirect_back(default='blog.index', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))

