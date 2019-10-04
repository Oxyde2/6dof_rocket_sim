import numpy as np
import math

# from: http://planning.cs.uiuc.edu/node102.html

def rotate_mat_yaw(angle):
	rot_mat_yaw = np.array(
	[[math.cos(angle), -math.sin(angle), 0],
	[math.sin(angle), math.cos(angle), 0], 
	[0, 0, 1]]
	)
	
	return rot_mat_yaw
	
def rotate_mat_pitch(angle):
	rot_mat_pitch = np.array(
	[[math.cos(angle), 0, math.sin(angle)],
	[0, 1, 0],
	[-math.sin(angle), 0, math.cos(angle)]]
	)
	
	return rot_mat_pitch
	
def rotate_mat_roll(angle):
	rot_mat_roll = np.array(
	[[1, 0, 0],
	[0, math.cos(angle), -math.sin(angle)],
	[0, math.sin(angle), math.cos(angle)]]
	)
	
	return rot_mat_roll

def rotate_vector(vector, angles_rotated):
	ang_roll = angles_rotated[0]
	ang_pitch = angles_rotated[1]
	ang_yaw = angles_rotated[2]
	
	rot_yaw = rotate_mat_yaw(ang_yaw)
	rot_pitch = rotate_mat_pitch(ang_pitch)
	rot_roll = rotate_mat_roll(ang_roll)
	rot_total = rot_yaw.dot(rot_pitch.dot(rot_roll))
	rotated_vec = rot_total.dot(np.array(vector))
	
	return rotated_vec
	
def rotate_matrix(matrix, angles_rotated):
	ang_roll = angles_rotated[0]
	ang_pitch = angles_rotated[1]
	ang_yaw = angles_rotated[2]
	
	rot_yaw = rotate_mat_yaw(ang_yaw)
	rot_pitch = rotate_mat_pitch(ang_pitch)
	rot_roll = rotate_mat_roll(ang_roll)
	rot_total = rot_yaw.dot(rot_pitch.dot(rot_roll))
	rotated_matrix = rot_total.dot(np.array(matrix)).dot(np.transpose(rot_total))
	
	return rotated_matrix
	
	
# moments of inertia: https://en.wikipedia.org/wiki/List_of_moments_of_inertia
def ring_inertia(mass, r1, r2):
	pass

