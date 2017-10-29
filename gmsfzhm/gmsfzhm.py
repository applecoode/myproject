def(sfzh):
    if len(sfzh)!=15 and len(sfzh)!=17 and len(sfzh)!=18:
        return {sfzh,'身份证号位数不对'}
    elif not sfz.isalnum():
        return {sfzh,'身份证号包含非数字字符'}
    elif:
        len(sfzh) = 15
        sfzh = sfzh[:6]+'19'+sfzh[7:15]