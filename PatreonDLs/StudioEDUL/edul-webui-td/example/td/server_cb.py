# Web Server DAT callbacks: HTTP serves the page files from text DATs, the WebSocket carries JSON control.
# Notes (TD 2025): the query string is NOT in request['uri'] - it comes split into request['pars'];
# extra response headers are plain keys (response['content-type'] = ...).
import json

FILES = {
    '/': ('web_index', 'text/html; charset=utf-8'),
    '/index.html': ('web_index', 'text/html; charset=utf-8'),
    '/app.js': ('web_app', 'text/javascript; charset=utf-8'),     # ES modules need a JS MIME type
    '/style.css': ('web_css', 'text/css; charset=utf-8'),
}


def L():
    return op.HtmlUI.op('logic').module


def onHTTPRequest(dat, request, response):
    f = FILES.get(request.get('uri', '/'))
    if f is None:
        response['statusCode'] = 404
        response['statusReason'] = 'Not Found'
        response['data'] = 'not found'
        return response
    response['statusCode'] = 200
    response['statusReason'] = 'OK'
    response['content-type'] = f[1]
    response['cache-control'] = 'no-cache'                       # edits on disk show on the next reload
    response['data'] = op.HtmlUI.op(f[0]).text
    return response


def onWebSocketOpen(dat, client, uri):
    L().ClientOpen(client)


def onWebSocketClose(dat, client):
    L().ClientClose(client)


def onWebSocketReceiveText(dat, client, data):
    try:
        msg = json.loads(data)
    except Exception:
        return
    if isinstance(msg, dict):
        L().Receive(client, msg)


def onWebSocketReceiveBinary(dat, client, data):
    return


def onWebSocketReceivePing(dat, client, data):
    dat.webSocketSendPong(client, data=data)


def onWebSocketReceivePong(dat, client, data):
    return


def onServerStart(dat):
    return


def onServerStop(dat):
    return
