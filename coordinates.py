#!/usr/bin/python

import sys
import os
import csv
import string
import math

def xyz_to_rthetaz((x, y, z)):
  r = math.sqrt(x * x + y * y)
  theta = math.asin(y / r)
  if(x >= 0):
    return (r, theta, z)
  else:
    return (r, (math.pi - theta), z)

def rotate((r, theta, z), dtheta):
  return (r, theta + dtheta, z)

def rotate_by_axis((x, y, z), dtheta, (ox, oy)):
  (r, theta, z) = xyz_to_rthetaz(x - ox, y - oy, z)
  (newx, newy, newz) = rthetaz_to_xyz(r, theta + dtheta, z)
  return (newx + ox, newy + oy, z)

def rthetaz_to_xyz((r, theta, z)):
  x = r * math.cos(theta)
  y = r * math.sin(theta)
  return (x, y, z)

if __name__ == "__main__":
  p1 = 1, 0, 0
  p2 = 0, 1, 0
  p3 = -1, 0, 0
  p4 = 0, -1, 0
  p5 = -0.35440000, 3.37140000, 2.45950000

  print str(p1) + " ==> " + str(rthetaz_to_xyz(rotate(xyz_to_rthetaz(p1), math.pi / 6)))
  print str(p2) + " ==> " + str(rthetaz_to_xyz(rotate(xyz_to_rthetaz(p2), math.pi / 6)))
  print str(p3) + " ==> " + str(rthetaz_to_xyz(rotate(xyz_to_rthetaz(p3), math.pi / 6)))
  print str(p4) + " ==> " + str(rthetaz_to_xyz(rotate(xyz_to_rthetaz(p4), math.pi / 6)))
  print str(p5) + " ==> " + str(rthetaz_to_xyz(rotate(xyz_to_rthetaz(p5), math.pi / 6)))
