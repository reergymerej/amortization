# Amortization

https://www.investopedia.com/terms/a/amortization.asp

This is so cool.

Everything is hardcoded in `main` right now.


```
$ ./main.py
period    	beginning balance    	total payment    	interest    	principle    	next balance
1         	$             500,000	$           3,326	$      2,916	$         409	$        499,590
2         	$             499,590	$           3,326	$      2,914	$         412	$        499,177
3         	$             499,177	$           3,326	$      2,911	$         414	$        498,763
4         	$             498,763	$           3,326	$      2,909	$         417	$        498,346
5         	$             498,346	$           3,326	$      2,907	$         419	$        497,926
6         	$             497,926	$           3,326	$      2,904	$         421	$        497,504
7         	$             497,504	$           3,326	$      2,902	$         424	$        497,080
8         	$             497,080	$           3,326	$      2,899	$         426	$        496,653
9         	$             496,653	$           3,326	$      2,897	$         429	$        496,224
10        	$             496,224	$           3,326	$      2,894	$         431	$        495,792
11        	$             495,792	$           3,326	$      2,892	$         434	$        495,357
12        	$             495,357	$           3,326	$      2,889	$         436	$        494,920
13        	$             494,920	$           3,326	$      2,887	$         439	$        494,481
14        	$             494,481	$           3,326	$      2,884	$         442	$        494,039
15        	$             494,039	$           3,326	$      2,881	$         444	$        493,594
16        	$             493,594	$           3,326	$      2,879	$         447	$        493,147
17        	$             493,147	$           3,326	$      2,876	$         449	$        492,697
18        	$             492,697	$           3,326	$      2,874	$         452	$        492,245
19        	$             492,245	$           3,326	$      2,871	$         455	$        491,790
20        	$             491,790	$           3,326	$      2,868	$         457	$        491,332
21        	$             491,332	$           3,326	$      2,866	$         460	$        490,872
22        	$             490,872	$           3,326	$      2,863	$         463	$        490,409
23        	$             490,409	$           3,326	$      2,860	$         465	$        489,943
24        	$             489,943	$           3,326	$      2,858	$         468	$        489,474
25        	$             489,474	$           3,326	$      2,855	$         471	$        489,003
26        	$             489,003	$           3,326	$      2,852	$         473	$        488,529
27        	$             488,529	$           3,326	$      2,849	$         476	$        488,052
28        	$             488,052	$           3,326	$      2,846	$         479	$        487,573
29        	$             487,573	$           3,326	$      2,844	$         482	$        487,090
30        	$             487,090	$           3,326	$      2,841	$         485	$        486,605
31        	$             486,605	$           3,326	$      2,838	$         487	$        486,117
32        	$             486,117	$           3,326	$      2,835	$         490	$        485,626
33        	$             485,626	$           3,326	$      2,832	$         493	$        485,133
34        	$             485,133	$           3,326	$      2,829	$         496	$        484,636
35        	$             484,636	$           3,326	$      2,827	$         499	$        484,137
36        	$             484,137	$           3,326	$      2,824	$         502	$        483,634
37        	$             483,634	$           3,326	$      2,821	$         505	$        483,129
38        	$             483,129	$           3,326	$      2,818	$         508	$        482,621
39        	$             482,621	$           3,326	$      2,815	$         511	$        482,110
40        	$             482,110	$           3,326	$      2,812	$         514	$        481,595
41        	$             481,595	$           3,326	$      2,809	$         517	$        481,078
42        	$             481,078	$           3,326	$      2,806	$         520	$        480,558
43        	$             480,558	$           3,326	$      2,803	$         523	$        480,035
44        	$             480,035	$           3,326	$      2,800	$         526	$        479,508
45        	$             479,508	$           3,326	$      2,797	$         529	$        478,979
46        	$             478,979	$           3,326	$      2,794	$         532	$        478,446
47        	$             478,446	$           3,326	$      2,790	$         535	$        477,911
48        	$             477,911	$           3,326	$      2,787	$         538	$        477,372
49        	$             477,372	$           3,326	$      2,784	$         541	$        476,830
50        	$             476,830	$           3,326	$      2,781	$         544	$        476,285
51        	$             476,285	$           3,326	$      2,778	$         548	$        475,737
52        	$             475,737	$           3,326	$      2,775	$         551	$        475,186
53        	$             475,186	$           3,326	$      2,771	$         554	$        474,631
54        	$             474,631	$           3,326	$      2,768	$         557	$        474,073
55        	$             474,073	$           3,326	$      2,765	$         561	$        473,512
56        	$             473,512	$           3,326	$      2,762	$         564	$        472,948
57        	$             472,948	$           3,326	$      2,758	$         567	$        472,380
58        	$             472,380	$           3,326	$      2,755	$         570	$        471,809
59        	$             471,809	$           3,326	$      2,752	$         574	$        471,235
60        	$             471,235	$           3,326	$      2,748	$         577	$        470,657
61        	$             470,657	$           3,326	$      2,745	$         581	$        470,076
62        	$             470,076	$           3,326	$      2,742	$         584	$        469,492
63        	$             469,492	$           3,326	$      2,738	$         587	$        468,904
64        	$             468,904	$           3,326	$      2,735	$         591	$        468,313
65        	$             468,313	$           3,326	$      2,731	$         594	$        467,718
66        	$             467,718	$           3,326	$      2,728	$         598	$        467,120
67        	$             467,120	$           3,326	$      2,724	$         601	$        466,519
68        	$             466,519	$           3,326	$      2,721	$         605	$        465,913
69        	$             465,913	$           3,326	$      2,717	$         608	$        465,305
70        	$             465,305	$           3,326	$      2,714	$         612	$        464,692
71        	$             464,692	$           3,326	$      2,710	$         615	$        464,077
72        	$             464,077	$           3,326	$      2,707	$         619	$        463,457
73        	$             463,457	$           3,326	$      2,703	$         623	$        462,834
74        	$             462,834	$           3,326	$      2,699	$         626	$        462,208
75        	$             462,208	$           3,326	$      2,696	$         630	$        461,577
76        	$             461,577	$           3,326	$      2,692	$         633	$        460,943
77        	$             460,943	$           3,326	$      2,688	$         637	$        460,306
78        	$             460,306	$           3,326	$      2,685	$         641	$        459,664
79        	$             459,664	$           3,326	$      2,681	$         645	$        459,019
80        	$             459,019	$           3,326	$      2,677	$         648	$        458,370
81        	$             458,370	$           3,326	$      2,673	$         652	$        457,718
82        	$             457,718	$           3,326	$      2,670	$         656	$        457,061
83        	$             457,061	$           3,326	$      2,666	$         660	$        456,401
84        	$             456,401	$           3,326	$      2,662	$         664	$        455,737
85        	$             455,737	$           3,326	$      2,658	$         668	$        455,069
86        	$             455,069	$           3,326	$      2,654	$         671	$        454,397
87        	$             454,397	$           3,326	$      2,650	$         675	$        453,721
88        	$             453,721	$           3,326	$      2,646	$         679	$        453,041
89        	$             453,041	$           3,326	$      2,642	$         683	$        452,357
90        	$             452,357	$           3,326	$      2,638	$         687	$        451,669
91        	$             451,669	$           3,326	$      2,634	$         691	$        450,978
92        	$             450,978	$           3,326	$      2,630	$         695	$        450,282
93        	$             450,282	$           3,326	$      2,626	$         699	$        449,582
94        	$             449,582	$           3,326	$      2,622	$         703	$        448,878
95        	$             448,878	$           3,326	$      2,618	$         708	$        448,170
96        	$             448,170	$           3,326	$      2,614	$         712	$        447,458
97        	$             447,458	$           3,326	$      2,610	$         716	$        446,741
98        	$             446,741	$           3,326	$      2,605	$         720	$        446,021
99        	$             446,021	$           3,326	$      2,601	$         724	$        445,296
100       	$             445,296	$           3,326	$      2,597	$         728	$        444,567
101       	$             444,567	$           3,326	$      2,593	$         733	$        443,834
102       	$             443,834	$           3,326	$      2,589	$         737	$        443,097
103       	$             443,097	$           3,326	$      2,584	$         741	$        442,355
104       	$             442,355	$           3,326	$      2,580	$         746	$        441,609
105       	$             441,609	$           3,326	$      2,576	$         750	$        440,858
106       	$             440,858	$           3,326	$      2,571	$         754	$        440,103
107       	$             440,103	$           3,326	$      2,567	$         759	$        439,344
108       	$             439,344	$           3,326	$      2,562	$         763	$        438,580
109       	$             438,580	$           3,326	$      2,558	$         768	$        437,812
110       	$             437,812	$           3,326	$      2,553	$         772	$        437,040
111       	$             437,040	$           3,326	$      2,549	$         777	$        436,263
112       	$             436,263	$           3,326	$      2,544	$         781	$        435,481
113       	$             435,481	$           3,326	$      2,540	$         786	$        434,695
114       	$             434,695	$           3,326	$      2,535	$         790	$        433,904
115       	$             433,904	$           3,326	$      2,531	$         795	$        433,109
116       	$             433,109	$           3,326	$      2,526	$         800	$        432,309
117       	$             432,309	$           3,326	$      2,521	$         804	$        431,504
118       	$             431,504	$           3,326	$      2,517	$         809	$        430,694
119       	$             430,694	$           3,326	$      2,512	$         814	$        429,880
120       	$             429,880	$           3,326	$      2,507	$         818	$        429,061
121       	$             429,061	$           3,326	$      2,502	$         823	$        428,238
122       	$             428,238	$           3,326	$      2,498	$         828	$        427,409
123       	$             427,409	$           3,326	$      2,493	$         833	$        426,576
124       	$             426,576	$           3,326	$      2,488	$         838	$        425,738
125       	$             425,738	$           3,326	$      2,483	$         843	$        424,895
126       	$             424,895	$           3,326	$      2,478	$         847	$        424,047
127       	$             424,047	$           3,326	$      2,473	$         852	$        423,194
128       	$             423,194	$           3,326	$      2,468	$         857	$        422,336
129       	$             422,336	$           3,326	$      2,463	$         862	$        421,473
130       	$             421,473	$           3,326	$      2,458	$         867	$        420,605
131       	$             420,605	$           3,326	$      2,453	$         872	$        419,732
132       	$             419,732	$           3,326	$      2,448	$         878	$        418,854
133       	$             418,854	$           3,326	$      2,443	$         883	$        417,971
134       	$             417,971	$           3,326	$      2,438	$         888	$        417,083
135       	$             417,083	$           3,326	$      2,432	$         893	$        416,189
136       	$             416,189	$           3,326	$      2,427	$         898	$        415,290
137       	$             415,290	$           3,326	$      2,422	$         903	$        414,386
138       	$             414,386	$           3,326	$      2,417	$         909	$        413,477
139       	$             413,477	$           3,326	$      2,411	$         914	$        412,563
140       	$             412,563	$           3,326	$      2,406	$         919	$        411,643
141       	$             411,643	$           3,326	$      2,401	$         925	$        410,717
142       	$             410,717	$           3,326	$      2,395	$         930	$        409,787
143       	$             409,787	$           3,326	$      2,390	$         936	$        408,851
144       	$             408,851	$           3,326	$      2,384	$         941	$        407,909
145       	$             407,909	$           3,326	$      2,379	$         947	$        406,962
146       	$             406,962	$           3,326	$      2,373	$         952	$        406,010
147       	$             406,010	$           3,326	$      2,368	$         958	$        405,051
148       	$             405,051	$           3,326	$      2,362	$         963	$        404,088
149       	$             404,088	$           3,326	$      2,357	$         969	$        403,118
150       	$             403,118	$           3,326	$      2,351	$         974	$        402,143
151       	$             402,143	$           3,326	$      2,345	$         980	$        401,163
152       	$             401,163	$           3,326	$      2,340	$         986	$        400,176
153       	$             400,176	$           3,326	$      2,334	$         992	$        399,184
154       	$             399,184	$           3,326	$      2,328	$         997	$        398,186
155       	$             398,186	$           3,326	$      2,322	$       1,003	$        397,183
156       	$             397,183	$           3,326	$      2,316	$       1,009	$        396,173
157       	$             396,173	$           3,326	$      2,311	$       1,015	$        395,157
158       	$             395,157	$           3,326	$      2,305	$       1,021	$        394,136
159       	$             394,136	$           3,326	$      2,299	$       1,027	$        393,109
160       	$             393,109	$           3,326	$      2,293	$       1,033	$        392,075
161       	$             392,075	$           3,326	$      2,287	$       1,039	$        391,036
162       	$             391,036	$           3,326	$      2,281	$       1,045	$        389,990
163       	$             389,990	$           3,326	$      2,274	$       1,051	$        388,939
164       	$             388,939	$           3,326	$      2,268	$       1,057	$        387,881
165       	$             387,881	$           3,326	$      2,262	$       1,063	$        386,817
166       	$             386,817	$           3,326	$      2,256	$       1,070	$        385,747
167       	$             385,747	$           3,326	$      2,250	$       1,076	$        384,671
168       	$             384,671	$           3,326	$      2,243	$       1,082	$        383,588
169       	$             383,588	$           3,326	$      2,237	$       1,088	$        382,499
170       	$             382,499	$           3,326	$      2,231	$       1,095	$        381,404
171       	$             381,404	$           3,326	$      2,224	$       1,101	$        380,302
172       	$             380,302	$           3,326	$      2,218	$       1,108	$        379,194
173       	$             379,194	$           3,326	$      2,211	$       1,114	$        378,080
174       	$             378,080	$           3,326	$      2,205	$       1,121	$        376,959
175       	$             376,959	$           3,326	$      2,198	$       1,127	$        375,831
176       	$             375,831	$           3,326	$      2,192	$       1,134	$        374,697
177       	$             374,697	$           3,326	$      2,185	$       1,140	$        373,556
178       	$             373,556	$           3,326	$      2,179	$       1,147	$        372,409
179       	$             372,409	$           3,326	$      2,172	$       1,154	$        371,255
180       	$             371,255	$           3,326	$      2,165	$       1,160	$        370,094
181       	$             370,094	$           3,326	$      2,158	$       1,167	$        368,926
182       	$             368,926	$           3,326	$      2,152	$       1,174	$        367,752
183       	$             367,752	$           3,326	$      2,145	$       1,181	$        366,570
184       	$             366,570	$           3,326	$      2,138	$       1,188	$        365,382
185       	$             365,382	$           3,326	$      2,131	$       1,195	$        364,187
186       	$             364,187	$           3,326	$      2,124	$       1,202	$        362,985
187       	$             362,985	$           3,326	$      2,117	$       1,209	$        361,776
188       	$             361,776	$           3,326	$      2,110	$       1,216	$        360,560
189       	$             360,560	$           3,326	$      2,103	$       1,223	$        359,337
190       	$             359,337	$           3,326	$      2,096	$       1,230	$        358,106
191       	$             358,106	$           3,326	$      2,088	$       1,237	$        356,869
192       	$             356,869	$           3,326	$      2,081	$       1,244	$        355,624
193       	$             355,624	$           3,326	$      2,074	$       1,252	$        354,372
194       	$             354,372	$           3,326	$      2,067	$       1,259	$        353,113
195       	$             353,113	$           3,326	$      2,059	$       1,266	$        351,846
196       	$             351,846	$           3,326	$      2,052	$       1,274	$        350,572
197       	$             350,572	$           3,326	$      2,045	$       1,281	$        349,290
198       	$             349,290	$           3,326	$      2,037	$       1,288	$        348,001
199       	$             348,001	$           3,326	$      2,030	$       1,296	$        346,705
200       	$             346,705	$           3,326	$      2,022	$       1,304	$        345,401
201       	$             345,401	$           3,326	$      2,014	$       1,311	$        344,089
202       	$             344,089	$           3,326	$      2,007	$       1,319	$        342,770
203       	$             342,770	$           3,326	$      1,999	$       1,327	$        341,443
204       	$             341,443	$           3,326	$      1,991	$       1,334	$        340,108
205       	$             340,108	$           3,326	$      1,983	$       1,342	$        338,765
206       	$             338,765	$           3,326	$      1,976	$       1,350	$        337,415
207       	$             337,415	$           3,326	$      1,968	$       1,358	$        336,057
208       	$             336,057	$           3,326	$      1,960	$       1,366	$        334,691
209       	$             334,691	$           3,326	$      1,952	$       1,374	$        333,316
210       	$             333,316	$           3,326	$      1,944	$       1,382	$        331,934
211       	$             331,934	$           3,326	$      1,936	$       1,390	$        330,544
212       	$             330,544	$           3,326	$      1,928	$       1,398	$        329,146
213       	$             329,146	$           3,326	$      1,920	$       1,406	$        327,739
214       	$             327,739	$           3,326	$      1,911	$       1,414	$        326,324
215       	$             326,324	$           3,326	$      1,903	$       1,422	$        324,902
216       	$             324,902	$           3,326	$      1,895	$       1,431	$        323,470
217       	$             323,470	$           3,326	$      1,886	$       1,439	$        322,031
218       	$             322,031	$           3,326	$      1,878	$       1,447	$        320,583
219       	$             320,583	$           3,326	$      1,870	$       1,456	$        319,126
220       	$             319,126	$           3,326	$      1,861	$       1,464	$        317,661
221       	$             317,661	$           3,326	$      1,853	$       1,473	$        316,188
222       	$             316,188	$           3,326	$      1,844	$       1,482	$        314,706
223       	$             314,706	$           3,326	$      1,835	$       1,490	$        313,215
224       	$             313,215	$           3,326	$      1,827	$       1,499	$        311,716
225       	$             311,716	$           3,326	$      1,818	$       1,508	$        310,207
226       	$             310,207	$           3,326	$      1,809	$       1,516	$        308,690
227       	$             308,690	$           3,326	$      1,800	$       1,525	$        307,165
228       	$             307,165	$           3,326	$      1,791	$       1,534	$        305,630
229       	$             305,630	$           3,326	$      1,782	$       1,543	$        304,086
230       	$             304,086	$           3,326	$      1,773	$       1,552	$        302,534
231       	$             302,534	$           3,326	$      1,764	$       1,561	$        300,972
232       	$             300,972	$           3,326	$      1,755	$       1,570	$        299,401
233       	$             299,401	$           3,326	$      1,746	$       1,580	$        297,821
234       	$             297,821	$           3,326	$      1,737	$       1,589	$        296,232
235       	$             296,232	$           3,326	$      1,728	$       1,598	$        294,633
236       	$             294,633	$           3,326	$      1,718	$       1,607	$        293,025
237       	$             293,025	$           3,326	$      1,709	$       1,617	$        291,408
238       	$             291,408	$           3,326	$      1,699	$       1,626	$        289,782
239       	$             289,782	$           3,326	$      1,690	$       1,636	$        288,146
240       	$             288,146	$           3,326	$      1,680	$       1,645	$        286,500
241       	$             286,500	$           3,326	$      1,671	$       1,655	$        284,845
242       	$             284,845	$           3,326	$      1,661	$       1,664	$        283,180
243       	$             283,180	$           3,326	$      1,651	$       1,674	$        281,505
244       	$             281,505	$           3,326	$      1,642	$       1,684	$        279,821
245       	$             279,821	$           3,326	$      1,632	$       1,694	$        278,126
246       	$             278,126	$           3,326	$      1,622	$       1,704	$        276,422
247       	$             276,422	$           3,326	$      1,612	$       1,714	$        274,708
248       	$             274,708	$           3,326	$      1,602	$       1,724	$        272,984
249       	$             272,984	$           3,326	$      1,592	$       1,734	$        271,250
250       	$             271,250	$           3,326	$      1,582	$       1,744	$        269,506
251       	$             269,506	$           3,326	$      1,572	$       1,754	$        267,752
252       	$             267,752	$           3,326	$      1,561	$       1,764	$        265,987
253       	$             265,987	$           3,326	$      1,551	$       1,774	$        264,212
254       	$             264,212	$           3,326	$      1,541	$       1,785	$        262,427
255       	$             262,427	$           3,326	$      1,530	$       1,795	$        260,631
256       	$             260,631	$           3,326	$      1,520	$       1,806	$        258,825
257       	$             258,825	$           3,326	$      1,509	$       1,816	$        257,008
258       	$             257,008	$           3,326	$      1,499	$       1,827	$        255,181
259       	$             255,181	$           3,326	$      1,488	$       1,837	$        253,343
260       	$             253,343	$           3,326	$      1,477	$       1,848	$        251,494
261       	$             251,494	$           3,326	$      1,467	$       1,859	$        249,635
262       	$             249,635	$           3,326	$      1,456	$       1,870	$        247,765
263       	$             247,765	$           3,326	$      1,445	$       1,881	$        245,883
264       	$             245,883	$           3,326	$      1,434	$       1,892	$        243,991
265       	$             243,991	$           3,326	$      1,423	$       1,903	$        242,088
266       	$             242,088	$           3,326	$      1,412	$       1,914	$        240,174
267       	$             240,174	$           3,326	$      1,401	$       1,925	$        238,248
268       	$             238,248	$           3,326	$      1,389	$       1,936	$        236,311
269       	$             236,311	$           3,326	$      1,378	$       1,948	$        234,363
270       	$             234,363	$           3,326	$      1,367	$       1,959	$        232,404
271       	$             232,404	$           3,326	$      1,355	$       1,970	$        230,433
272       	$             230,433	$           3,326	$      1,344	$       1,982	$        228,451
273       	$             228,451	$           3,326	$      1,332	$       1,993	$        226,457
274       	$             226,457	$           3,326	$      1,321	$       2,005	$        224,451
275       	$             224,451	$           3,326	$      1,309	$       2,017	$        222,434
276       	$             222,434	$           3,326	$      1,297	$       2,028	$        220,405
277       	$             220,405	$           3,326	$      1,285	$       2,040	$        218,364
278       	$             218,364	$           3,326	$      1,273	$       2,052	$        216,312
279       	$             216,312	$           3,326	$      1,261	$       2,064	$        214,247
280       	$             214,247	$           3,326	$      1,249	$       2,076	$        212,170
281       	$             212,170	$           3,326	$      1,237	$       2,088	$        210,081
282       	$             210,081	$           3,326	$      1,225	$       2,101	$        207,980
283       	$             207,980	$           3,326	$      1,213	$       2,113	$        205,867
284       	$             205,867	$           3,326	$      1,200	$       2,125	$        203,741
285       	$             203,741	$           3,326	$      1,188	$       2,138	$        201,603
286       	$             201,603	$           3,326	$      1,176	$       2,150	$        199,453
287       	$             199,453	$           3,326	$      1,163	$       2,163	$        197,290
288       	$             197,290	$           3,326	$      1,150	$       2,175	$        195,114
289       	$             195,114	$           3,326	$      1,138	$       2,188	$        192,926
290       	$             192,926	$           3,326	$      1,125	$       2,201	$        190,725
291       	$             190,725	$           3,326	$      1,112	$       2,213	$        188,511
292       	$             188,511	$           3,326	$      1,099	$       2,226	$        186,284
293       	$             186,284	$           3,326	$      1,086	$       2,239	$        184,044
294       	$             184,044	$           3,326	$      1,073	$       2,252	$        181,791
295       	$             181,791	$           3,326	$      1,060	$       2,266	$        179,525
296       	$             179,525	$           3,326	$      1,047	$       2,279	$        177,246
297       	$             177,246	$           3,326	$      1,033	$       2,292	$        174,953
298       	$             174,953	$           3,326	$      1,020	$       2,305	$        172,647
299       	$             172,647	$           3,326	$      1,007	$       2,319	$        170,328
300       	$             170,328	$           3,326	$        993	$       2,332	$        167,995
301       	$             167,995	$           3,326	$        979	$       2,346	$        165,648
302       	$             165,648	$           3,326	$        966	$       2,360	$        163,288
303       	$             163,288	$           3,326	$        952	$       2,373	$        160,914
304       	$             160,914	$           3,326	$        938	$       2,387	$        158,526
305       	$             158,526	$           3,326	$        924	$       2,401	$        156,125
306       	$             156,125	$           3,326	$        910	$       2,415	$        153,709
307       	$             153,709	$           3,326	$        896	$       2,429	$        151,279
308       	$             151,279	$           3,326	$        882	$       2,444	$        148,835
309       	$             148,835	$           3,326	$        868	$       2,458	$        146,377
310       	$             146,377	$           3,326	$        853	$       2,472	$        143,904
311       	$             143,904	$           3,326	$        839	$       2,487	$        141,417
312       	$             141,417	$           3,326	$        824	$       2,501	$        138,915
313       	$             138,915	$           3,326	$        810	$       2,516	$        136,399
314       	$             136,399	$           3,326	$        795	$       2,530	$        133,868
315       	$             133,868	$           3,326	$        780	$       2,545	$        131,323
316       	$             131,323	$           3,326	$        766	$       2,560	$        128,762
317       	$             128,762	$           3,326	$        751	$       2,575	$        126,187
318       	$             126,187	$           3,326	$        736	$       2,590	$        123,596
319       	$             123,596	$           3,326	$        720	$       2,605	$        120,991
320       	$             120,991	$           3,326	$        705	$       2,620	$        118,370
321       	$             118,370	$           3,326	$        690	$       2,636	$        115,734
322       	$             115,734	$           3,326	$        675	$       2,651	$        113,083
323       	$             113,083	$           3,326	$        659	$       2,666	$        110,416
324       	$             110,416	$           3,326	$        644	$       2,682	$        107,733
325       	$             107,733	$           3,326	$        628	$       2,698	$        105,035
326       	$             105,035	$           3,326	$        612	$       2,713	$        102,322
327       	$             102,322	$           3,326	$        596	$       2,729	$         99,592
328       	$              99,592	$           3,326	$        580	$       2,745	$         96,846
329       	$              96,846	$           3,326	$        564	$       2,761	$         94,085
330       	$              94,085	$           3,326	$        548	$       2,777	$         91,307
331       	$              91,307	$           3,326	$        532	$       2,793	$         88,513
332       	$              88,513	$           3,326	$        516	$       2,810	$         85,703
333       	$              85,703	$           3,326	$        499	$       2,826	$         82,877
334       	$              82,877	$           3,326	$        483	$       2,843	$         80,033
335       	$              80,033	$           3,326	$        466	$       2,859	$         77,174
336       	$              77,174	$           3,326	$        450	$       2,876	$         74,297
337       	$              74,297	$           3,326	$        433	$       2,893	$         71,404
338       	$              71,404	$           3,326	$        416	$       2,909	$         68,494
339       	$              68,494	$           3,326	$        399	$       2,926	$         65,567
340       	$              65,567	$           3,326	$        382	$       2,944	$         62,623
341       	$              62,623	$           3,326	$        365	$       2,961	$         59,662
342       	$              59,662	$           3,326	$        348	$       2,978	$         56,684
343       	$              56,684	$           3,326	$        330	$       2,995	$         53,688
344       	$              53,688	$           3,326	$        313	$       3,013	$         50,675
345       	$              50,675	$           3,326	$        295	$       3,030	$         47,644
346       	$              47,644	$           3,326	$        277	$       3,048	$         44,595
347       	$              44,595	$           3,326	$        260	$       3,066	$         41,529
348       	$              41,529	$           3,326	$        242	$       3,084	$         38,444
349       	$              38,444	$           3,326	$        224	$       3,102	$         35,342
350       	$              35,342	$           3,326	$        206	$       3,120	$         32,222
351       	$              32,222	$           3,326	$        187	$       3,138	$         29,083
352       	$              29,083	$           3,326	$        169	$       3,156	$         25,926
353       	$              25,926	$           3,326	$        151	$       3,175	$         22,751
354       	$              22,751	$           3,326	$        132	$       3,193	$         19,557
355       	$              19,557	$           3,326	$        114	$       3,212	$         16,345
356       	$              16,345	$           3,326	$         95	$       3,231	$         13,114
357       	$              13,114	$           3,326	$         76	$       3,250	$          9,864
358       	$               9,864	$           3,326	$         57	$       3,268	$          6,595
359       	$               6,595	$           3,326	$         38	$       3,288	$          3,307
360       	$               3,307	$           3,326	$         19	$       3,307	$              0
period    	beginning balance    	total payment    	interest    	principle    	next balance

