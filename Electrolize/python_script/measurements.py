m_catode_0 = 8.90 / 1000. # Was in grams
m_catode_1 = 9.29 / 1000. # 

m_anode_0 = 36.49 / 1000. # 
m_anode_1 = 35.96 / 1000. # 

my_current_time_dependency = [ # (Sec; time)
	( 0, 	0.98 ),
	( 10, 	0.87 ),
	( 20, 	0.91 ),
	( 30, 	0.84 ),
	( 40, 	0.87 ),
	( 50, 	0.87 ),
	( 60, 	0.88 ),
	( 100, 	0.89 ),
	( 120, 	0.85 ),
	( 150, 	0.86 ),
	( 180, 	0.91 ),
	( 240, 	0.94 ),
	( 300, 	0.95 ),
	( 360, 	0.96 ),
	( 420, 	1.00 ),
	( 480, 	1.02 ),
	( 540, 	1.04 ),
	( 600, 	1.00 ),
	( 660, 	1.08 ),
	( 720, 	1.09 ),
	( 840, 	1.12 ),
	( 960, 	1.12 ),
	( 1080, 1.19 ),
	( 1200, 1.24 ),
	( 1320, 1.20 ),
	( 1440, 1.27 ),
	( 1500, 1.27 ),
]


goshas_time_shift = -1 # Gosha's time = my time - 1
raw_goshas_current_time_dependency = [ # (Sec; time)

]


goshas_current_time_dependency = [ (v[0] + goshas_time_shift, v[1])  \
								for v in raw_goshas_current_time_dependency]


