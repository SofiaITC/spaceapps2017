
def Calculate_Sun(CellStart,CellStop, \
	LightingStart, LightingStop, \
	CoffeeStart, CoffeeStop, \
	DryerStart,DryerStop, \
	WasherSart, WasherStop, \
	FridgeStart, FridgeStop, \
	LaptopStart, LaptopStop):
				
	print "yay!"


	out1 = []
	out1.append([0, 27.3388888888889, 0])
	out1.append([0.0416666666666667, 24.6777777777778, 0])
	out1.append([0.0833333333333333, 22.0166666666667, 0])
	out1.append([0.125, 19.3555555555556, 0])
	out1.append([0.166666666666667, 16.6944444444444, 0])
	out1.append([0.208333333333333, 14.0333333333333, 0])
	out1.append([0.25, 11.3722222222222, 0])
	out1.append([0.291666666666667, 10.2219500964689, 1.34417231869112])
	out1.append([0.333333333333333, 10.1375278343533, 2.63668884899547])
	out1.append([0.375, 11.2442956287472, 3.82787890550506])
	out1.append([0.416666666666667, 13.3951502400114, 4.87196572237531])
	out1.append([0.458333333333333, 16.4028647576648, 5.72882562876454])
	out1.append([0.5, 20.0472836255565, 6.36552997900277])
	out1.append([0.541666666666667, 24.0837830964236, 6.75761058197826])
	out1.append([0.583333333333333, 28.2526719853125, 6.89])
	out1.append([0.625, 32.2891714561797, 6.75761058197826])
	out1.append([0.666666666666667, 35.9335903240713, 6.36552997900277])
	out1.append([0.708333333333333, 38.9413048417248, 5.72882562876454])
	out1.append([0.75, 41.092159452989, 4.87196572237531])
	out1.append([0.791666666666667, 42.1989272473829, 3.82787890550506])
	out1.append([0.833333333333333, 41.8145049852673, 2.63668884899547])
	out1.append([0.875, 37.9375661928473, 1.34417231869113])
	out1.append([0.916666666666667, 34.7164550817362, 8.44127285432039E-16])
	out1.append([0.958333333333333, 32.0553439706251, 0])
	out1.append([1, 29.3942328595139, 0])

	return out1
	
retval = Calculate_Sun(0,0,0,0,0,0,0,0,0,0,0,0,0,0)
print retval