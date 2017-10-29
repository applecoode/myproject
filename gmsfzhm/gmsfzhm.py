def gmsfzhm(sfzh):
    if len(sfzh)!=15 and len(sfzh)!=17 and len(sfzh)!=18:
        return {sfzh:'身份证号位数不对'}
    elif not sfzh.isalnum():
        return {sfzh:'身份证号包含非数字字符'}
    if len(sfzh) == 15:
        sfzh = sfzh[:6]+'19'+sfzh[6:15]
    if int(sfzh[10:12]) > 12 or int(sfzh[12:14]) > 31:
        return {sfzh:'身份证号出生日期有问题'}
    seq = sfzh[:17]
    t = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    s = sum(map(lambda x:x[0]*x[1],zip(t,map(int,seq))))
    b = s % 11
    bd={
            0: '1',
            1: '0',
            2: 'x',
            3: '9',
            4: '8',
            5: '7',
            6: '6',
            7: '5',
            8: '4',
            9: '3',
           10: '2'
        }
    gmsfhm = sfzh[:17] + bd[b]
    return {sfzh:gmsfhm}
print(gmsfzhm('372401198005190019'))