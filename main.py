import sys
import copy
from typing import TYPE_CHECKING

def main():
   init_list = read_file(sys.argv[1])
   bn_list = copy.deepcopy(init_list)
   mg_list = copy.deepcopy(init_list)

   unique = binary_based(bn_list)
   if unique is None:
      # print("WENT TO MERGE")
      unique = merge_based(mg_list)
   if isinstance(unique,list):
      unique = unique[0]
   print(unique)
   

def binary_based(list):
   # print(list)
   length = len(list)
   mid = length // 2
   # print("Mid " + str(mid))
   if length == 1:
      return list[0]
   if length == 2 or length == 0:
      return None
   if list[mid] == list[mid+1] and list[mid] == list[mid-1]:
      return None
   elif list[mid] == list[mid+1]:
      if mid % 2 == 0:
         #left half
         return binary_based(list[mid:])
      else:
         #right half
         return binary_based(list[:mid])

   elif list[mid] == list[mid-1]:
      if mid % 2 == 0:
         #left half
         return binary_based(list[:mid+1])

      else:
         #right half
         return binary_based(list[mid+1:])
   else:
      return list[mid]

   
def merge_based(list):
   length = len(list)
   mid = length // 2
   if length == 1:
      return list
   if length == 2:
      return None
   
   #case where middle element is unique
   if list[mid] != list[mid+1] and list[mid] != list[mid-1]:
      # print("111did\n")
      return list[mid]

   #case where middle element and elements on both sides are the same
   elif list[mid] == list[mid+1] and list[mid] == list[mid-1]:
      # print("222did\n")
      left = merge_based(list[:mid+1])
      right = merge_based(list[mid:])

   #case where middle element and element on the right side are the same
   elif list[mid] == list[mid+1]:
      # print("333did\n")
      left = merge_based(list[:mid])
      right = merge_based(list[mid:])

   #case where middle element and element on the left side are the same list[mid] == list[mid-1]
   else:
      # print("444did\n")
      left = merge_based(list[:mid+1])
      right = merge_based(list[mid+1:])

   # print("left:: " + str(left) + " right:: " + str(right))
   return merge(left, right)
   #for merge, if first element and last element are the same in one of these "subsets" you can discard it
   
def merge(listA, listB):
   # n = len(listA)
   # m = len(listB)
   if listA == None:
      return listB
   elif listB == None:
      return listA
   
   


def read_file(file_name):
    f = open(file_name, 'r')
    line = f.readline()
    #need to make the strings ints
    mapped = map(int, line.split(", "))
    a_list = list(mapped)
    return a_list



main()

