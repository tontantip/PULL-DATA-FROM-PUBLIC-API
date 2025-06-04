## import library requests and pprint
import requests
from pprint import pprint
## set list of data
NO = []
สถานที่ = []
หมู่ที่ = []
หมู่บ้าน = []
ตำบล = []
อำเภอ  = []
จังหวัด = []
รหัสประเภทบ่อน้ำบาดาล = []
ประเภทบ่อน้ำบาดาล	 = []
สภาพน้ำ	= []
ความลึกเจาะ = []
ความลึกพัฒนา= []
ปริมาณน้ำ	= []
ระดับน้ำปกติ	= []
ระยะน้ำลด	= []
Zone_Number	= []
Zone_Designators = []
พิกัดออก_ตก	 = []
พิกัดเหนือ_ใต้	= []
ละติจูด = []
ลองจิจูด = []

## for loop API 1 to 117 path and append data to list data. 
for j in range(0,117):
    url = f"https://pasutara.dgr.go.th/api_well/api/FindWellAll?Page={j+1}"
    data = requests.get(url)
    if data.status_code == 200:
        all_data = data.json()
        result = all_data["result"]
        for i in result:
            NO.append(i["no"])
            สถานที่.append(i["locat"])
            หมู่ที่.append(i["mubanno"])
            หมู่บ้าน.append(i["mubanname"])
            ตำบล.append(i["tumbolname"])
            อำเภอ.append(i["ampurname"])
            จังหวัด.append(i["provincenam"])
            รหัสประเภทบ่อน้ำบาดาล.append(i["wtid"])
            ประเภทบ่อน้ำบาดาล.append(i["welltypename"])
            สภาพน้ำ.append(i["bwdname"])
            ความลึกเจาะ.append(i["deeptdrill"])
            ความลึกพัฒนา.append(i["deepdev"])
            ปริมาณน้ำ.append(i["yiel"])
            ระดับน้ำปกติ.append(i["static"])
            ระยะน้ำลด.append(i["wdd"])
            Zone_Number.append(i["utmez"])
            Zone_Designators.append(i["utmmz"])
            พิกัดออก_ตก.append(i["utmEasting"])
            พิกัดเหนือ_ใต้.append(i["utmNORTHING"])
            ละติจูด.append(i["lat"])
            ลองจิจูด.append(i["long"])        
        
    else:
        print("API ERROR")
    
    print(f'{j+1} Done')


## import pandas
import pandas as pd
## create data frame
df = pd.DataFrame({"NO": NO,
"สถานที่":สถานที่,
"หมู่ที่":หมู่ที่,
"หมู่บ้าน" : หมู่บ้าน,
"ตำบล":ตำบล,
"อำเภอ": อำเภอ,
'จังหวัด' : จังหวัด,
'รหัสประเภทบ่อน้ำบาดาล' : รหัสประเภทบ่อน้ำบาดาล,
'ประเภทบ่อน้ำบาดาล' : ประเภทบ่อน้ำบาดาล,
'สภาพน้ำ'	: สภาพน้ำ,
"ความลึกเจาะ" : ความลึกเจาะ,
'ความลึกพัฒนา' : ความลึกพัฒนา,
'ปริมาณน้ำ' : ปริมาณน้ำ,
'ระดับน้ำปกติ' : ระดับน้ำปกติ,
'ระยะน้ำลด' : ระยะน้ำลด,
"Zone_Number"	: Zone_Number,
'Zone_Designators' : Zone_Designators,
'พิกัดออก_ตก'	 : พิกัดออก_ตก,
'พิกัดเหนือ_ใต้'	: พิกัดเหนือ_ใต้,
'ละติจูด' : ละติจูด,
'ลองจิจูด' : ลองจิจูด
})
## print data frame
df
