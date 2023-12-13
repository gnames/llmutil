from flask import jsonify, Response, request
from llm import embed
from app import app

path = '/api/v1/'
ep_ary = ["ping", "version", "embed", "cross_embed"]

ep = {}
for v in ep_ary:
    ep[v] = v


@app.route('/', methods=['GET'])
@app.route('/api/', methods=['GET'])
def root():
    txt = 'Use path ' + path
    return Response(txt, content_type='text/plain')


@app.route(path, methods=['GET'])
def endpoints():
    eps = list(map(lambda x: "  " + path + x, ep_ary))
    txt = "Supported endpoints:\n\n" + "\n".join(eps)
    res = Response(txt, content_type='text/plain')
    return res


@app.route(path + ep['ping'], methods=['GET'])
def ping():
    return "Pong!\nAPI is online"


@app.route(path + ep['version'], methods=['GET'])
def version():
    return "Version " + app.version


@app.route(path + ep['embed'], methods=['POST'])
def embedTexts():
    payload = request.json
    res = embed.embed(payload['texts'])
    return jsonify(res.tolist())


@app.route(path + ep['cross_embed'], methods=['POST'])
def crossTexts():
    payload = request.json
    res = embed.cross_embed(payload['texts'])
    return jsonify(res.tolist())
