class Present:
	def __init__(self, dims=[0,0,0]):
		self.l=dims[0]
		self.w=dims[1]
		self.h=dims[2]
		self.dims={"l":dims[0],"w":dims[1],"h":dims[2]}
		self.surface_area=0
		self.perimeter=0
		self.volume=0
		self.min_area=max(self.dims.values())*max(self.dims.values())
		self.min_perimeter=4*max(self.dims.values())
	def get_perimeter(self):
		pm = 0
		for d_1, val_1 in self.dims.items():
			for d_2, val_2 in self.dims.items():
				if d_1 == d_2 :
					continue
				p = 2*val_1+2*val_2
				pm+=p
				self.min_perimeter = self.min_perimeter if p > self.min_perimeter else p
		self.perimeter = pm
		return self.perimeter
	def get_surface_area(self):
		sa = 0
		for d_1, val_1 in self.dims.items():
			for d_2, val_2 in self.dims.items():
				if d_1 == d_2 :
					continue
				a = val_1*val_2
				sa+=a
				self.min_area = self.min_area if a > self.min_area else a
		self.surface_area = sa
		return self.surface_area
	def get_volume(self):
		vol = 1
		for v in self.dims.values():
			vol *= v
		self.volume = vol
		return self.volume
	def get_wrapping_paper_needed(self):
		sa = self.get_surface_area() if self.surface_area == 0 else self.surface_area
		min = self.min_area
		return sa+min
	def get_ribbon_needed(self):
		pm = self.get_perimeter() if self.perimeter == 0 else self.perimeter
		min = self.min_perimeter
		vol = self.get_volume() if self.volume == 0 else self.volume
		return min+vol
		
		

if __name__ == "__main__":
	input_file = open("input_2.txt", "r")
	total_paper = 0
	total_ribbon = 0
	for p in input_file:
		d = ["l","w","h","min","surface_area"]
		dim = p.replace("\n","").split("x")
		min_dim = 100
		sa = 2
		i = 0
		while i < len(dim):
			dim[i] = int(dim[i])
			i += 1
		present = Present(dim)
		paper = present.get_wrapping_paper_needed()
		ribbon = present.get_ribbon_needed()
		print("Present : {}x{}x{} -- {}/{}".format(present.l,present.w,present.h,paper,ribbon))
		total_paper += paper
		total_ribbon += ribbon
	print("Total Paper -- {}".format(total_paper))
	print("Total Ribbon -- {}".format(total_ribbon))
		
# 23x11x5
# 2*23*11 + 2*23*5 + 2*11*5
# 506+230+110
# 846 						+ 55