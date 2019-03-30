from flask import Flask, request, jsonify
from flask_cors import CORS
from math import atan, degrees
from base64 import b64decode
from json import loads

app = Flask(__name__)
#CORS(app, support_credentials = True)
cache = []
@app.route('/', methods=['GET'])
def index():
    global cache 
    typ = request.args.get('type')
    if typ == 'js':
        points_str = b64decode(request.args.get('data')).decode('UTF-8')
        points = loads(points_str)
        angles = get_angles(points)
        cache.append(angles)
        return "YES"
    elif typ == 'unity':
        if len(cache) == 1:
          return cache[-1]
        elif len(cache)>1:
          return jsonify(cache.pop())
        return "EMPTY"
    
def get_angles(points):

    points = (dict(points))['keypoints']
    lsy, lsx, fls = points[5]['position']['y'], points[5]['position']['x'], points[5]['isdummy']
    rsy, rsx, frs = points[6]['position']['y'], points[6]['position']['x'], points[6]['isdummy']
    ley, lex, fle = points[7]['position']['y'], points[7]['position']['x'], points[7]['isdummy']
    rey, rex, fre = points[8]['position']['y'], points[8]['position']['x'], points[8]['isdummy']
    lwy, lwx, flw = points[9]['position']['y'], points[9]['position']['x'], points[9]['isdummy']
    rwy, rwx, frw = points[10]['position']['y'], points[10]['position']['x'], points[10]['isdummy']
    lhy, lhx, flh = points[11]['position']['y'], points[11]['position']['x'], points[11]['isdummy']
    rhy, rhx, frh = points[12]['position']['y'], points[12]['position']['x'], points[12]['isdummy']
    lky, lkx, flk = points[13]['position']['y'], points[13]['position']['x'], points[13]['isdummy']
    rky, rkx, frk = points[14]['position']['y'], points[14]['position']['x'], points[14]['isdummy']
    lay, lax, fla = points[15]['position']['y'], points[15]['position']['x'], points[15]['isdummy']
    ray, rax, fra = points[16]['position']['y'], points[16]['position']['x'], points[16]['isdummy']

    angles = []

    angles.append({'desc': 'left shoulder-arm', 'angle': 0, 'isdummy': fls and fle and frs}) # 7 5 6
    if not angles[-1]['isdummy']:
      m1 = (ley-lsy)/(lex-lsx)
      m2 = (lsy-rsy)/(lsx-rsx)
      angles[0]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'right shoulder-arm', 'angle': 0, 'isdummy': fls and fre and frs}) # 8 6 5
    if not angles[-1]['isdummy']:
      m1 = (rey-rsy)/(rex-rsx)
      m2 = (lsy-rsy)/(lsx-rsx)
      angles[1]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))


    angles.append({'desc': 'left arm-body',  'angle': 0, 'isdummy': fls and flh and fle}) # 7 5 11
    if not angles[-1]['isdummy']:
      m1 = (ley-lsy)/(lex-lsx)
      m2 = (lsy-lhy)/(lsx-lhx)
      angles[2]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'right arm-body', 'angle': 0, 'isdummy': frs and fre and frh}) # 8 6 12
    if not angles[-1]['isdummy']:
      m1 = (rey-rsy)/(rex-rsx)
      m2 = (rsy-rhy)/(rsx-rhx)
      angles[3]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))
    
    angles.append({'desc': 'left elbow','angle': 0, 'isdummy': fls and fle and flw}) # 5 7 9
    if not angles[-1]['isdummy']:
      m1 = (ley-lsy)/(lex-lsx)
      m2 = (ley-lwy)/(lex-lwx)
      angles[4]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))
    
    angles.append({'desc': 'right elbow', 'angle': 0,'isdummy': frw and fre and frs}) # 6 8 10
    if not angles[-1]['isdummy']:
      m1 = (rey-rsy)/(rex-rsx)
      m2 = (rey-rwy)/(rex-rwx)
      angles[5]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'left upperbody-leg', 'angle': 0,'isdummy': fls and flh and flk}) # 5 11 13
    if not angles[-1]['isdummy']:
      m1 = (lhy-lsy)/(lhx-lsx)
      m2 = (lhy-lky)/(lhx-lkx)
      angles[6]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))

    angles.append({'desc': 'right upperbody-leg', 'angle': 0,'isdummy': frk and frh and frs}) # 6 12 14
    if not angles[-1]['isdummy']:
     m1 = (rhy-rsy)/(rhx-rsx)
     m2 = (rhy-rky)/(rhx-rkx)
     angles[7]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))
 
    angles.append({'desc': 'left lowerbody-leg', 'angle': 0,'isdummy': flh and flk and frh}) # 12 11 13
    if not angles[-1]['isdummy']:
      m1 = (lhy-rhy)/(lhx-rhx)
      m2 = (lhy-lky)/(lhx-lkx)
      angles[8]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))
 
    angles.append({'desc': 'right lowerbody-leg', 'angle': 0,'isdummy': flh and frh and frk}) # 11 12 14
    if not angles[-1]['isdummy']:
      m1 = (lhy-rhy)/(lhx-rhx)
      m2 = (rhy-rky)/(rhx-rkx)
      angles[9]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))
 
    angles.append({'desc': 'left knee', 'angle': 0,'isdummy': flk and fla and flh}) # 11 13 15
    if not angles[-1]['isdummy']:    
      m1 = (lky-lay)/(lkx-lax)
      m2 = (lhy-lky)/(lhx-lkx)
      angles[10]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))
 
    angles.append({'desc': 'right knee', 'angle': 0,'isdummy': frk and fra and frh}) # 12 14 16
    if not angles[-1]['isdummy']:
      m1 = (rky-ray)/(rkx-rax)
      m2 = (rhy-rky)/(rhx-rkx)
      angles[11]['angle'] = degrees(atan((m1-m2)/(1+m1*m2)))
 
    return angles

if __name__ == '__main__':
    # app.run(host= '192.168.0.100', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=False)

