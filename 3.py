class Coord:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
		
	def __add__(self,other):
		return Coord(self.x+other.x, self.y+other.y)
		
	def __str__(self):
		return "({}, {})".format(self.x,self.y)
	def __eq__(self,other):
		return (self.x==other.x and self.y==other.y)
		
class Santa:
	def __init__(self, visited_houses):
		self.visited_houses=visited_houses
		self.last_house=Coord()
		print(self.last_house)
	def move(self,dir):
		if dir == "^":
			self.last_house+=Coord(0,1)
		elif dir == "<":
			self.last_house+=Coord(-1,0)
		elif dir == ">":
			self.last_house+=Coord(1,0)
		elif dir == "v":
			self.last_house+=Coord(0,-1)
		if self.last_house.__str__() in self.visited_houses.keys():
			# print("already visited")
			self.visited_houses[self.last_house.__str__()] += 1
		else:
			self.visited_houses[self.last_house.__str__()] = 1
		
		# print("{} -- {}".format(self.last_house, self.visited_houses[self.last_house.__str__()]))
		
if __name__ == "__main__":
	input_file = open("input_3.txt", "r")
	input_data = input_file.read()
	
	start_house=Coord()
	
	current_house=start_house
	
	number_of_santas=2
	santas=[]

	i=0
	while i < number_of_santas:
		visited_houses={start_house.__str__():1}
		s = Santa(visited_houses)
		santas.append(s)
		i+=1
	
	n=0
	for dir in input_data:
		s = santas[n%number_of_santas]
		# print("Santa {}".format(n%number_of_santas))
		s.move(dir)
		n+=1
		
	combined_houses={}
	n=1
	for santa in santas:
		print("Santa {} visted {} houses".format(n,len(santa.visited_houses)))
		combined_houses.update(santa.visited_houses)
		n+=1
	print("Unique houses visited: {}".format(len(combined_houses)))
	# print("Number of houses visited: {}".format(len(visited_houses)))