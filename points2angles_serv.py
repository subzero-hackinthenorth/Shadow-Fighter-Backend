from flask import Flask, request, jsonify
from flask_cors import CORS
from math import atan, degrees
from base64 import b64decode
from json import loads

app = Flask(__name__)
CORS(app, support_credentials = True)

@app.route('/')
def hello():
    return 'Team Sub Zero - HINT'

@app.route('/<uuid>', methods=['GET'])
def add_message(uuid):
    typ = request.args.get('type')
    if typ == 'unity':
        points_str = b64decode(request.args.get('data')).decode('UTF-8')
        points = loads(points_str)
        angles = get_angles(points)
        return jsonify(angles)
    elif typ == 'js':
        return jsonify({"data":"NULL"})
    
def get_angles(points):

    points = (dict(points))['keypoints']
    lsy, lsx = points[5]['position']['y'], points[5]['position']['x']
    rsy, rsx = points[6]['position']['y'], points[6]['position']['x']
    ley, lex = points[7]['position']['y'], points[7]['position']['x']
    rey, rex = points[8]['position']['y'], points[8]['position']['x']
    lwy, lwx = points[9]['position']['y'], points[9]['position']['x']
    rwy, rwx = points[10]['position']['y'], points[10]['position']['x']
    lhy, lhx = points[11]['position']['y'], points[11]['position']['x']
    rhy, rhx = points[12]['position']['y'], points[12]['position']['x']
    lky, lkx = points[13]['position']['y'], points[13]['position']['x']
    rky, rkx = points[14]['position']['y'], points[14]['position']['x']
    lay, lax = points[15]['position']['y'], points[15]['position']['x']
    ray, rax = points[16]['position']['y'], points[16]['position']['x']

    angles = []

    angles.append({'desc': 'left shoulder-arm'}) # 7 5 6
    m1 = (ley-lsy)/(lex-lsx)
    m2 = (lsy-rsy)/(lsx-rsx)
    angles[0]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'right shoulder-arm'}) # 8 6 5
    m1 = (rey-rsy)/(rex-rsx)
    m2 = (lsy-rsy)/(lsx-rsx)
    angles[1]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'left arm-body'}) # 7 5 11
    m1 = (ley-lsy)/(lex-lsx)
    m2 = (lsy-lhy)/(lsx-lhx)
    angles[2]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'right arm-body'}) # 8 6 12
    m1 = (rey-rsy)/(rex-rsx)
    m2 = (rsy-rhy)/(rsx-rhx)
    angles[3]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'left elbow'}) # 5 7 9
    m1 = (ley-lsy)/(lex-lsx)
    m2 = (ley-lwy)/(lex-lwx)
    angles[4]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'right elbow'}) # 6 8 10
    m1 = (rey-rsy)/(rex-rsx)
    m2 = (rey-rwy)/(rex-rwx)
    angles[5]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'left upperbody-leg'}) # 5 11 13
    m1 = (lhy-lsy)/(lhx-lsx)
    m2 = (lhy-lky)/(lhx-lkx)
    angles[6]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'right upperbody-leg'}) # 6 12 14
    m1 = (rhy-rsy)/(rhx-rsx)
    m2 = (rhy-rky)/(rhx-rkx)
    angles[7]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'left lowerbody-leg'}) # 12 11 13
    m1 = (lhy-rhy)/(lhx-rhx)
    m2 = (lhy-lky)/(lhx-lkx)
    angles[8]['angle'] = math.degrees(math.atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'right lowerbody-leg'}) # 11 12 14
    m1 = (lhy-rhy)/(lhx-rhx)
    m2 = (rhy-rky)/(rhx-rkx)
    angles[9]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'left knee'}) # 11 13 15
    m1 = (lky-lay)/(lkx-lax)
    m2 = (lhy-lky)/(lhx-lkx)
    angles[10]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'right knee'}) # 12 14 16
    m1 = (rky-ray)/(rkx-rax)
    m2 = (rhy-rky)/(rhx-rkx)
    angles[11]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    return angles
    
if __name__ == '__main__':
    # app.run(host= '192.168.0.100', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)

