import json

def wcpretreatment(path):
    path = r'C:\Python38\Lib\site-packages\pyflink\examples\python\table\batch\practice-flink-wordcount\input\data.json'
    with open(path, 'r') as f:
        jd = json.loads(f.read())
    sb = ''
    for d in jd['records']:
         if not d['popData2019'] == None:
            sb += d['popData2019']['cases_weekly'] + d['popData2019']['deaths_weekly'] + '\n'
        # if not d['properties']['SW_DIRECT'] == None:
        #     sb += d['properties']['COUNTY_NA'] + d['properties']['VILL_NAME'] + '\n'
    with open('./input', 'w', encoding='utf-8') as f:
        f.write(sb)
