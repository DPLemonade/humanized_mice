wt_file = open('WT_sequences.txt', 'r')
gaps_file = open('sequence_with_gaps.txt', 'r')
nwt_file = open('NWT_sequences.txt', 'r')

wt = wt_file.readlines()
gaps = gaps_file.readlines()
nwt = nwt_file.readlines()

for i in range(0, len(wt)):
    wt[i] = int(wt[i])

for i in range(0, len(gaps)):
    gaps[i] = int(gaps[i])

for i in range(0, len(nwt)):
    nwt[i] = int(nwt[i])

combined = wt + gaps + nwt
combined.sort()


for i in range(1, len(combined)):
    if combined[i] - i != combined[i - 1] - (i - 1):
        print(combined[i] - 1)

'''
No hits found:
503
5033
28764
29929
33895
39773
41145
50367
59957

Multiple hits:
394
1247
1462
1640
1690
1775
1939
1970
2047
2237
2295
2854
2913
3210
3801
3822
3985
4083
4648
4700
6583
6800
6926
6993
7080
8246
8290
8444
8868
8889
9098
9132
9244
9443
9641
9947
10778
11549
11850
12244
12305
12552
12576
12711
12922
13132
13265
13410
13589
13778
13860
14158
14318
14338
14644
15056
16011
16382
16766
16865
16979
17499
17578
18024
18209
19161
19298
19303
19704
20230
21180
21223
21722
22323
22433
22859
23000
23109
23111
23153
23544
23550
23617
23852
24466
24507
24522
24548
24549
24973
25067
25268
25301
26047
27054
27123
27261
27313
27690
28720
28904
29313
29763
29900
30232
30401
30986
31665
32199
32451
32698
32783
32960
33387
33437
33853
33926
34401
34650
34754
34968
35216
35376
36101
36532
36717
36835
37095
37648
37649
37785
38103
39461
39740
40408
40474
41987
42049
42113
42234
42305
43365
43991
45399
45706
46062
46330
46639
47812
47828
48016
48085
48969
48971
49046
49132
49188
49236
49488
49563
49587
49595
51821
51995
52272
52918
53090
53476
54237
54424
54945
55173
55246
55292
55349
55602
56087
56988
57015
57279
58271
58514
58954
59152
59243
59362
59975
60022
60516
60864
60922
61075
61943
62080
62402
62817
63039
63060
63652
63729
'''

