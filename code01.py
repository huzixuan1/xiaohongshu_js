

import execjs

def getXS(s,i):
    with open('./xhs.js', 'r', encoding='UTF-8') as f:
        js_code = f.read()
    context = execjs.compile(js_code)
    result = context.call("_webmsxyw", s, i) 
    
    return result

if __name__ == "__main__":

    s = "/api/redcaptcha/v2/getconfig"
    i = {
        'keyword': '旅游',
        'page': 2,
        'page_size': 20,
        'search_id': '2cwmqmb3d2mo5uwusa06h',
        'sort': 'general',
        'note_type': 0,
        'ext_flags': [],
        'image_formats': [
            'jpg',
            'webp',
            'avif',
        ],
    }

    res = getXS(s,i)
    print(res)
