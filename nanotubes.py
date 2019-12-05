#!/usr/bin/python

import sys
import os
import csv
import math
import coordinates as C

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
  str_rows = [atom + " " + str(x) + " " + str(y) + " " + str(z) + "\n" for (atom, x, y, z)  in data]
  return reduce(lambda x, y: x + y, str_rows)

# write data to a file
def write_data(data, file_name):
  with open(file_name, "w") as fout:
    fout.write(data)

'''
  This function create a pair processing function.
  Inputs:
    transform: the transformation function; either zshift or rotate
    ttype : stands for transformation type. Actually the name of the output 
      directory to which the output data should be written. "zshift" or "rotate"
    all_delta : list of values by which the transformation has to be done. In
    case of zshift, it's the translational distance, and in case of rotation
    it's the rotation angle.
'''
def make_process_pair(transform, ttype, all_delta, ipath, opath):
  def process_pair(it, ot):
    it_fname = ipath + it + "-fin.xyz-formatted"
    ot_fname = ipath + ot + "-fin.xyz-formatted"

    it_data = read_data(it_fname)
    ot_data = read_data(ot_fname)

    all_transformed = [transform(it_data, delta) + ot_data for delta in all_delta]
#    print "all_transformed"
#    print all_transformed
    for i in range(len(all_transformed)):
      out_fname = opath + ttype + "/" + it + "_" + str(i) + ".xyz"
      try:
        write_data(string_of_data(all_transformed[i]), out_fname)
      except ValueError:
        print "Value Error for i = " + str(i)
        print all_transformed
        sys.exit()

  return process_pair

def make_processors(ipath, opath, all_shifts, all_angles):
  zshift_pair = make_process_pair(shift_z, "zshift", all_shifts, ipath, opath)
  rotate_pair = make_process_pair(rotate, "rotate", all_angles, ipath, opath)
  return (zshift_pair, rotate_pair)


'''
  This function creates the processing function.
'''
def make_process_all_pairs(process_pair):
  def process_all_pairs(all_pairs):
    for i, o in all_pairs:
      print("processing " + i + " ...")
      process_pair(i, o)

  return process_all_pairs

def process(ipath, opath, all_shifts, all_angles, all_pairs):
  zshift_pair, rotate_pair = make_processors(ipath, opath, all_shifts, all_angles)
  zshift_all_pairs = make_process_all_pairs(zshift_pair)
  rotate_all_pairs = make_process_all_pairs(rotate_pair)
  zshift_all_pairs(all_pairs)
  rotate_all_pairs(all_pairs)

def process_mixed():
  input_dir  = "data/2019/mixed/"
  output_dir = "data/2019/mixed/output/"
  d2019_mixed_all_shifts = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
  d2019_mixed_all_angles = [(math.pi * degree / 180) for degree in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]]
  all_pairs = [
    ("33", "88"),
    ("44", "99"),
    ("55", "1010"),
    ("66", "1111"),
    ("77", "1212")
  ]

  process(input_dir, output_dir, all_shifts, all_angles, all_pairs)
def process_long():
  input_dir  = "data/2019/long/"
  output_dir = "data/2019/long/output/"
  all_shifts = range(12)
  all_angles = [(math.pi * degree / 180) for degree in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]]
  all_pairs = [
    ("33", "88"),
    ("44", "99"),
    ("55", "1010"),
    ("66", "1111"),
    ("77", "1212")
  ]

  process(input_dir, output_dir, all_shifts, all_angles, all_pairs)

def process_long2():
  input_dir  = "data/2019/long2/"
  output_dir = "data/2019/long2/output/"
  all_shifts = range(12)
  all_angles = [(math.pi * degree / 180) for degree in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]]
  all_pairs = [
    ("33", "88"),
    ("44", "99"),
    ("55", "1010"),
    ("66", "1111"),
    ("77", "1212")
  ]
  process(input_dir, output_dir, all_shifts, all_angles, all_pairs)

def process_december2019():
  input_dir  = "data/2019/december/"
  output_dir = "data/2019/december/output/"
  all_shifts = range(13)
  all_angles = [(math.pi * degree / 180) for degree in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]]
  all_pairs = [
    ("33", "88"),
    ("44", "99"),
    ("55", "1010"),
    ("66", "1111"),
    ("77", "1212")
  ]
  process(input_dir, output_dir, all_shifts, all_angles, all_pairs)

if __name__ == "__main__":
  print "processing ..."
  process_december2019()
#  process_long2()
  print "done!"
