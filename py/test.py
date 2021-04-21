import os
import pandas as pd
from utils.read_file import eachFile, readJson, writeCSV, writeOneJSON
os.chdir(r'D:\data\地铁数据\地铁\161718od')
'''
此文件用于计算地铁线路断面客流量
计算步骤：1、找到最短路径；
2、计算每个段面的客流量（使用数学分析法,需要每个断面的运行时间，将每个时间段的断面人数算出来）
0,1,2,3,4,5,6,7,8
7,21,2016-02-07 15:57:02,268024,深大站,22,2016-02-07 16:30:07,260028,香梅北站
2016	6.28	11	碧头-福田
2016	10.28	7	太安-西丽湖
2016	10.28	9	文锦-红树湾南
2017			
2018			
'''

def findLine(start,end):
    start_line = yearStop[yearStop['name']==start]
    if start_line.shape[0]>0:
        start_line = start_line.iat[0,2]
    end_line = yearStop[yearStop['name']==end]
    if end_line.shape[0]>0:
        end_line = end_line.iat[0,2]
        key = str(start_line)+'-'+start+'_'+str(end_line)+'-'+end
        return key
    return 'a'

def addOne(split,start_day,start_hour):
    if split not in routeSplitJson.keys():
        routeSplitJson[split] = {}
    if start_day not in routeSplitJson[split].keys():
        routeSplitJson[split][start_day] = {}
    if start_hour not in routeSplitJson[split][start_day].keys():
        routeSplitJson[split][start_day][start_hour] = 0
    routeSplitJson[split][start_day][start_hour] = routeSplitJson[split][start_day][start_hour] + 1


def get_datetime(str_datetime):
    try:
        time = datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')
        return time
    except:
        time = datetime.strptime(str_datetime, '%Y/%m/%d %H:%M:%S')
        return time

def changeFile(df):
    df['start'] = df['start'].map(lambda x: int(x))
    yearStop['线路'] = yearStop['线路'].map(lambda x: x.split('号')[0])
    df['end'] = df['end'].map(lambda x: int(x))
    df = pd.merge(df, yearStop, left_on='start', right_on='站点编号', how='left')
    yearStop.rename(columns={'start_line': 'end_line'})
    df = pd.merge(df, yearStop, left_on='end', right_on='站点编号', how='left')
    df['start_time'] = df['start_time'].map(lambda x: get_datetime(x))
    df['date_origin'] = df['start_time'].map(lambda x: x.day)
    df['hour_origin'] = df['start_time'].map(lambda x: x.hour)
    return df[['date_origin','hour_origin','站点名称_x','线路_x','站点名称_y','线路_y']]

def routeSplit(df):
    noWays = []
    for row in df.itertuples(index=False):
        start_day  = getattr(row,'date_origin')
        start_hour  = getattr(row,'hour_origin')
        start =getattr(row,'hour_origin')
        start_line = getattr(row,'start_line')
        end = getattr(row,'end')
        end_line = getattr(row,'end_line')
        if start != end:
            key = str(start_line) + '-' + start + '_' + str(end_line) + '-' + end
            if key in minWays2018.keys():
                minStations = minWays2018[key]
                name0 = minStations[0]
                split = str(start_line) + '-' + start + '_' + name0
                addOne(split,start_day,start_hour)
                for i in range(0,len(minStations)):
                    if i+1<len(minStations):
                        split = minStations[i] + '_' + minStations[i+1]
                        addOne(split, start_day, start_hour)
                    else:
                        split = minStations[i] + '_' + str(end_line) + '-' + end
                        addOne(split, start_day, start_hour)
            else:
                noWays.append([start_day,start_hour,start,start_line,end,end_line])
    writeCSV(noWays,saveDir+'noWays.csv')

if __name__ == '__main__':
    min_route_floyd = 'D:\data\地铁数据\SZ_Metro\min_way\min_route_floyd_key\\'
    src = 'D:\学习文件\项目文件\分析系统\data\SZ_Metro_LineSUM_Stoppoint\\'
    od_dir = r'D:\data\地铁数据\地铁\161718od\\'
    jsonDir = 'D:\data\地铁数据\SZ_Metro\min_way\min_subway_json\\'
    saveDir = 'D:\data\地铁数据\地铁\split\\'
    files = eachFile(od_dir)
    file2018 = files[24:36]
    minWays2018 = readJson(min_route_floyd + '2018.json')
    yearStop = pd.read_csv(src + 'SZ_Metro_LineSUM_Stoppoint_{}_GCJ02.csv'.format('2018'),usecols=[1,2],names=['name','start_line'],encoding='gbk')
    for file in file2018:
        df = pd.read_csv(od_dir+file, usecols=[2,4,8])
        # df = pd.read_csv(od_dir+'Metro_Statistics_OD_20171002-20171008.txt', usecols=[2,4,8])
        df = changeFile(df)
        routeSplitJson = {}
        routeSplit(df)
        writeOneJSON(routeSplitJson, saveDir + file + '.json')
