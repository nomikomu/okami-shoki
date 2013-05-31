#############################################################################
#####   Import code and set gamelogic

import GameLogic
cont = GameLogic.getCurrentController()
own = cont.owner
mesh = own.meshes[0]

##############################################################################
#####   The code to set the position and colour of verts at the end of the process


def set_verts(m):	
		
	matID = 0	
	length = mesh.getVertexArrayLength(matID)
	
	divide = own['size'] / own['verts']
	
	mod = 1 / divide
		
					
	for v in range(0,length):
		vert = mesh.getVertex(matID,v)
		
		pos = vert.XYZ	
		
		
		x = int((pos[0] + (own['size'] *0.5)) * mod)
		y = int((pos[1] + (own['size'] *0.5)) * mod) 
		
			
		if x < own['verts'] and y < own['verts']:
			vert.XYZ = [pos[0],pos[1],m[x][y][0]]
			#vert.color = (0.5,0.5,0.5,1.0)
			vert.color = m[x][y][1]
		if x ==0 or y == 0 or y ==own['verts'] -1 or x == own['verts'] -1 or y ==own['verts']  or x == own['verts']:
			vert.XYZ = [pos[0],pos[1],0.0]
			vert.color = (0.0,0.0,0.0,1.0)	
		
				
	own.reinstancePhysicsMesh(own, mesh)			
				
		

#############################################################################
#####  A random function returns between 1 and -1

def rand():
	rander= int(round((2 * GameLogic.getRandomFloat()) -1.0))
	return rander
		
##############################################################################		
#####   The code for making rivers

def river_maker_2(m):
	
	def point(a,b):
		p1= a + int(32 * GameLogic.getRandomFloat())
		p2= b + int(32 * GameLogic.getRandomFloat())
		
		point = [p1,p2]
		
		return point
	
	max = 12
	points = 0
	p_list = []
	
	for p in range(0,max):
		if p == 0:
			a_point = [0,int(32 * GameLogic.getRandomFloat())]
			p_list.append(a_point)
		else:
			a_point = point(a_point[0],a_point[1])
			p_list.append(a_point)
		points +=1	
		
	chance = round(GameLogic.getRandomFloat())	
	
	if chance ==1:
		new_list = []
		
		for ob in p_list:
			ob2a = own['verts'] - (ob[0])
			ob2b =  (ob[1])
			new_list.append([ob2a,ob2b])
		p_list = new_list
	
		
	r_list =[]
	
	count = 0
	r_point = p_list[0]
	
	rand_gen = 1
	
	error = 0
	
	while count < points:
		if error >12000:
			count = 100
			print('error')
		
		elif r_point[0] == p_list[count][0] and r_point[1] == p_list[count][1]:
			count +=1
		else:
			if r_point[0] > p_list[count][0]:
				r_point[0] = int(r_point[0] -rand_gen)
			if r_point[0] < p_list[count][0]:
				r_point[0] = int(r_point[0] +rand_gen)
						
			if r_point[1] > p_list[count][1]:
				r_point[1] = int(r_point[1] -rand_gen)
			if r_point[1] < p_list[count][1]:
				r_point[1] = int(r_point[1] +rand_gen)
					
			point_1 = r_point[0]
			point_2 = r_point[1]
			point_r = [point_1,point_2]
						
			r_list.append(point_r)
			error +=1
			
	length = len(r_list)
	
	for v in range (0,length):
		if r_list[v][0] < own['verts'] and r_list[v][1] < own['verts']:
			if r_list[v][0] > 0 and r_list[v][1] > 0:
				if own['make_roads'] ==1:
					b = 1.0
				else:
					b = 0.5
					
				m[r_list[v][0]][r_list[v][1]] = [own['deep'],[0.5,1.0,b,1.0]]
		
		
	return m

#######################
def wrap(v,max):
	if v < max -1:
		v +=1
	else:
		v = v 
	return v

##############################################################################		
#####  blending

def vert_blend(m):

	n = [[[0.0,[0.5,0.5,0.5,1.0]] for i in range(own['verts'])] for i in range(own['verts'])]
	
		
	for x in range(0,own['verts']):
		for y in range(0,own['verts']):
						
			list = []
			
			list.append(m[x][y][0]) 
			list.append(m[x][wrap(y,own['verts'])][0]) 
			list.append(m[wrap(x,own['verts'])][y][0])
			list.append(m[wrap(x,own['verts'])][wrap(y,own['verts'])][0])
			list.append(m[x-1][y][0])
			list.append(m[wrap(x,own['verts'])][y-1][0])
			list.append(m[x-1][wrap(y,own['verts'])][0])
			list.append(m[x][y-1][0])
			list.append(m[x-1][y-1][0])
			
			total = 0
			
			for ob in list:
				total += ob 
			
			n[x][y][0] = (0.11111) * total
			
			list = []
			
			list.append(m[x][y][1][1]) 
			list.append(m[x][wrap(y,own['verts'])][1][1]) 
			list.append(m[wrap(x,own['verts'])][y][1][1])
			list.append(m[wrap(x,own['verts'])][wrap(y,own['verts'])][1][1])
			list.append(m[x-1][y][1][1])
			list.append(m[wrap(x,own['verts'])][y-1][1][1])
			list.append(m[x-1][wrap(y,own['verts'])][1][1])
			list.append(m[x][y-1][1][1])
			list.append(m[x-1][y-1][1][1])
			
			total = 0
			
			for ob in list:
				total += ob 
			
			n[x][y][1][1] = (0.11111) * total
			
			
			
	for x in range(0,own['verts']):
		for y in range(0,own['verts']): 
			m[x][y][0] = n[x][y][0]
			m[x][y][1][1] = n[x][y][1][1]
	
##############################################################################		
#####   The main code for handling the order of proceses
		
def main():
	
	#build first array
	
	m = [[[0.0,[0.5,0.5,0.5,1.0]] for i in range(own['verts'])] for i in range(own['verts'])]
				
	current_y = 0
	current_x = 0
	
	jump = own['spacing']
	
	for x in range(0,own['verts']):
		if x == current_x:
			for y in range(0,own['verts']):						
				if y == current_y:
					m[x][y][0] = (own['high'] * GameLogic.getRandomFloat())
										
					current_y += jump
					if current_y >= own['verts']:
						current_y = 0
			current_x += jump
			if current_x >= own['verts']:
				current_x = 0
	
	blend_amount = own['h_smooth']
	
	for i in range(0,blend_amount):
		vert_blend(m)			
	
	for i in range(0,own['valley']):
		m = river_maker_2(m)
	
	blend_amount = own['v_smooth']
	
	for i in range(0,blend_amount):
		vert_blend(m)

	set_verts(m)
	own.reinstancePhysicsMesh(own, mesh)
	own.state = 4
		
	
