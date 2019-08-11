#!/usr/bin/python

import sys
import os
import csv
import math
import coordinates as C

all_pairs = [
 ("33", "88"),
 ("44", "99"),
 ("55", "1010"),
 ("66", "1111"),
 ("77", "1212")
]
all_shifts = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
all_angles = [(math.pi * degree / 180) for degree in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]]

'''
 Description : read data from CSV file
 Requirement : The CSV file should contain data in the following format:
a1, x1, y1, z1 
a2, x2, y2, z2 
a3, x3, y3, z3 
...
...

'''
def read_data(file_name):
  ifile  = open(file_name, "rb")
  csv_xyz = csv.reader(ifile)
  return [row for row in csv_xyz]

# input points in cartesian coordinates.
def shift_z(data, shift):
  return [(atom, float(x), float(y), float(z) + shift) for [atom, x, y, z] in data]

def rotate(data, angle):
  # input points in cartesian coordinates.
  all_xyz = [(atom, (float(x), float(y), float(z))) for [atom, x, y, z] in data]

  # input points in cylindrical coordinates.
  all_rthetaz = [(atom, C.xyz_to_rthetaz((x, y, z))) for (atom, (x, y, z)) in all_xyz]

  # rotated points in cylindrical coordinates.
  all_rthetaz_rotated = [(atom, C.rotate((r, theta, z), angle)) for (atom, (r, theta, z)) in all_rthetaz]

  # rotated points in caresian coordinates.
  all_xyz_rotated = [(atom, C.rthetaz_to_xyz((r, theta, z))) for (atom, (r, theta, z)) in all_rthetaz_rotated]

  return [(atom, x, y, z) for (atom, (x, y, z)) in all_xyz_rotated]

# convert data to string
def string_of_data(data):
  str_rows = [atom + ", " + str(x) + ", " + str(y) + ", " + str(z) + "\n" for [atom, x, y, z]  in data]
  return reduce(lambda x, y: x + y, str_rows)

# write data to a file
def write_data(data, file_name):
  with open(file_name, "w") as fout:
    fout.write(data)

def make_process_pair(transform, ttype, all_delta):
  def process_pair(it, ot):
    it_fname = "data/2019/" + it + "-fin.xyz"
    ot_fname = "data/2019/" + ot + "-fin.xyz"

    it_data = read_data(it_fname)
    ot_data = read_data(ot_fname)

    all_transformed = [transform(it_data, delta) + ot_data for delta in all_delta]
    for i in range(len(all_transformed)):
      out_fname = "data/2019/output/" + ttype + "/" + it + "_" + str(i) + ".xyz"
      write_data(string_of_data(all_transformed[i]), out_fname)

  return process_pair

zshift_pair = make_process_pair(shift_z, "zshift", all_shifts)
rotate_pair = make_process_pair(rotate, "rotate", all_angles)

def make_process_all_pairs(process_pair):
  def process_all_pairs(all_pairs):
    for i, o in all_pairs:
      print("processing " + i + " ...")
      process_pair(i, o)

  return process_all_pairs

zshift_all_pairs = make_process_all_pairs(zshift_pair)
rotate_all_pairs = make_process_all_pairs(rotate_pair)

if __name__ == "__main__":
  print "rotating ..."
  rotate_all_pairs(all_pairs)
  print "done!"
