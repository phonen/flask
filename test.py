from flask import Flask,request
import requests
from vendor.alimama import api, appinfo
CODE_URL = 'https://oauth.taobao.com/authorize'
TOKEN_URL = 'https://oauth.taobao.com/token'
APP_KEY = '23287975'
APP_SECRET = '6f2f866a280672983f279dd78299edab'
REST = 'http://gw.api.taobao.com/router/rest'
app=Flask(__name__)
def apply_commission(item_id, guide_id, ad_zone_id,access_token):
    req = api.TbkPrivilegeGetRequest()
    req.set_app_info(appinfo(APP_KEY, APP_SECRET))
    req.item_id = item_id
    req.adzone_id = ad_zone_id
    req.site_id = guide_id
    try:
        resp = req.getResponse(access_token)
        data = resp['tbk_privilege_get_response']['result']['data']
        return data

    except Exception as e:
        return True



@app.route('/')
def hello_world():
    return "Hello World~~~"


@app.route('/bag')
def bag_tburl():
    iid = request.args.get('id')
    pid = request.args.get('pid')
    access_token="700021012020351e205ff164a70608898659a76b2a547ffde8b1e5afa68a3c5dde19a972503084439"


    if pid:
        t = pid.split('_')
        guide_id = t[2]
        ad_zone_id = t[3]

        res = apply_commission(iid, guide_id, ad_zone_id,access_token)
        if res is True:
            return 'pass'
        else:
            coupon_click_url = res['coupon_click_url']
            
            return coupon_click_url

@app.route('/tth')
def tth_tburl():
    iid = request.args.get('id')
    pid = request.args.get('pid')
    access_token = "700021012020351e205ff164a70608898659a76b2a547ffde8b1e5afa68a3c5dde19a972503084439"


    if pid:
        t = pid.split('_')
        guide_id = t[2]
        ad_zone_id = t[3]

        res = apply_commission(iid, guide_id, ad_zone_id,access_token)
        if res is True:
            return 'pass'
        else:
            coupon_click_url = res['coupon_click_url']
            tburl = '{}&activityId={}'.format(coupon_click_url, goods['quan_id'])
            return tburl




if __name__ == '__main__':
    app.run('10.47.133.104', 8899)