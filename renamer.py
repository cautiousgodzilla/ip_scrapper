import glob
import os

dr = "D:\Projects\scraps\ipo_data"
for i in glob.glob(os.path.join(dr,"*.pdf")):
    path = i.split('\\')
    name = path[-1].split('_')
    #print(name)
    rename_ = 'D:\\Projects\\scraps\\ipo_data\\ '.strip()+ name[1][:4] + '_' + name[0] + ".pdf"
    print(rename_)
    os.rename(i, rename_)