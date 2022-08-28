from b_utils import m_call

def mult_and_square(pair):
    a = pair[0]
    b = pair[1]
    output = a*b
    for i in range(1,a):
        last_output = output
        for j in range(1,b):
            output = (((output*i)+(output*j))%last_output)+1
            
    return output    

if __name__ == "__main__":

    samples = [[2076, 28], [217, 2039], [2031, 1488], [2665, 2019], [918, 962], [714, 722], [2099, 1952], [1350, 2143], [955, 502], [2832, 12], [2632, 1654], [1479, 873], [1053, 1220], [1588, 584], [762, 736], [689, 2269], [2491, 1426], [1558, 2797], [1528, 348], [2631, 1524], [745, 615], [388, 237], [1313, 620], [79, 2634], [2899, 678], [2134, 667], [2243, 1785], [615, 143], [2096, 4], [26, 1837], [557, 1400], [1639, 1458], [2480, 1529], [2895, 2949], [2099, 910], [2393, 2743], [2849, 1754], [2590, 2186], [1771, 2711], [331, 2446], [1684, 2951], [1744, 2542], [515, 621], [682, 1189], [352, 1597], [1391, 123], [1553, 2987], [2352, 1252], [2312, 2124], [2116, 1092], [156, 341], [375, 84], [2048, 2737], [850, 801], [2139, 1679], [1364, 159], [1773, 2603], [56, 448], [2779, 938], [2739, 256], [825, 20], [1306, 13], [1426, 519], [1499, 2393], [1489, 2568], [573, 1509], [2216, 2890], [2018, 2731], [2153, 1750], [2610, 1557], [2972, 1827], [1878, 1101], [833, 2379], [218, 290], [2603, 2466], [1505, 769], [1801, 1900], [1840, 1046], [2012, 0], [2019, 2260], [1231, 340], [2437, 528], [2172, 735], [2830, 1440], [1746, 2880], [1159, 2092], [1113, 1022], [1098, 2005], [80, 2511], [570, 1039], [2774, 715], [2724, 1183], [402, 2710], [1146, 1424], [834, 2285], [2936, 1438], [2930, 345], [903, 1878], [103, 107], [2842, 66], [2188, 2571], [271, 1480], [2397, 690], [2026, 566], [1773, 134], [1864, 636], [515, 2885], [2192, 1272], [890, 2137], [1861, 1444], [2054, 1394], [566, 1028], [877, 633], [2949, 1603], [1949, 1737], [814, 2296], [1601, 2772], [981, 1169], [1367, 198], [1480, 1834], [1717, 2714], [406, 313], [887, 1628], [2164, 74], [2641, 320], [1018, 1347], [742, 1066], [1560, 1880], [2022, 2600], [775, 2937], [363, 259], [1912, 554], [518, 486], [981, 1745], [2453, 304], [780, 952], [1817, 2729], [1653, 693], [597, 2575], [1845, 2860], [2152, 1422], [2044, 2846], [296, 2313], [2316, 2556], [276, 2428], [2423, 1160], [1081, 1876], [2752, 2773], [1063, 881], [7, 2431], 
            [1187, 1743], [2607, 1648], [1140, 2292], [1810, 1151], [2525, 53], [395, 222], [1083, 1241], [2340, 250], [573, 158], [2459, 500], [1595, 1951], [2436, 1604], [849, 2127], [2861,1068], [642, 845], [1116, 978], [749, 364], [2226, 274], [991, 2466], [1409, 230], [2491, 2331], [1761, 2651], [567, 719], [1201, 1314], [1528, 2950], [2768, 1047], [1167, 1844], [1617, 150], [1394, 1865], [2693, 394], [764, 425], [2231, 500], [1375, 585], [2717, 1404], [1715, 670], [2264, 2811], [264, 1343], [467, 493], [2769, 603], [1829, 2748], [2155, 13], [2178, 285], [1533, 2909], [1832, 2221], [1170, 1165], [2934, 1232], [196, 6], [2303, 1373], [34, 725], [2549, 2866], [124, 2349], [1373, 2967], [2392, 117], [844, 416], [1769, 1002], [633, 2271], [2226, 1254], [2247, 1163], [527, 1278], [1451, 866], [1850, 1827], [1882, 2651], [2446, 2461], [1198, 2435], [784, 388], [48, 2327], [993, 2784], [1579, 2731], 
            [2021, 1919], [1581, 2644], [1269, 1421], [309, 1677], [454, 2057], [1160, 1361], [925, 1316], [2782, 2684], [961, 170], [164, 2111], [902, 2047], [1303, 1333], [887, 595], [2574, 1279], [2539, 2335], [16, 2830], [1316, 1543], [95, 2523], [746, 2816], [2330, 1202], [296, 2519], [1436, 889], [2983, 537], [2641, 1537], [822, 1805], [1522, 415], [678, 2774], [2990, 1963], [2509, 2674], [2105, 366], [1568, 2154], [970, 158], [2760, 2369], [1830, 638], [1870, 2846], [1316, 459], [2226, 544], [618, 2636], [1754, 1712], [416, 2935], [2681, 2704], [2223, 2759], [2650, 2035], [1289, 905], [746, 2452], [1717, 981], [951, 798], [1661, 1461], [732, 1865], [893, 1261], [197, 1347], [660, 2], [2403, 2327], [2053, 550], [429, 409], [215, 2403], [2281, 2494], [1889, 225], [1537, 495], [827, 2698], [1907, 467], [1845, 560], [582, 72], [1722, 1204], [1032, 1752], [1104, 2606], [1674, 202], [2252, 812], [2270, 295], [604, 2571], [2705, 1826], [2424, 1892], [2209, 2774], [758, 2812], [2547, 2346], [1014, 2588], [2962, 1800], [2370, 2544], [1685, 65], [2464, 2776], [1659, 79]]  
    samples = samples[:15]

    print(m_call(mult_and_square,samples,8,"p"))
    print(m_call(mult_and_square,samples,8,"s"))
    print(m_call(mult_and_square,samples,8,"t"))


