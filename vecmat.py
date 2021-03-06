# --------------------------------------------------
# Vecmat (Version 1.2)
# by Sha-Chan~
# last version released on the 28 of June.
#
# code provided with licence (CC BY-NC-SA 4.0)
# for more information about licence :
# https://creativecommons.org/licenses/by-nc-sa/4.0/
# --------------------------------------------------

from math import *

class Vector:
  def __init__(self, *coord):
    self.coord = list(coord)
    self.dim = len(coord)
      
  def show(self):
    print(self.coord)
    
  def norm(self):
    return sqrt(sum([i**2 for i in self.coord]))

  def unitV(self):
    return Vector(*[i / self.norm() for i in self.coord])
    
  def dotP(self, vec):
    return sum([self.coord[i] * vec.coord[i] for i in range(len(self.coord))])
  
  def crossP(self, vec):
    if self.dim == 3 and vec.dim == 3: return Vector(self.z*vec.y - self.y*vec.z, self.x*vec.z - self.z*vec.x, self.y*vec.x - self.x*vec.y)

  def det(self, *vec):
    return Matrix([self.coord] + [i.coord for i in vec]).det()
  
  def colinear(self, vec):
    return not self.det(vec)

  def angle(self, vec):
    return round(degrees(acos(self.dotP(vec) / (self.norm()*vec.norm()))), 2)

  def plus(self, vec):
    return Vector(*[self.coord[i] + vec.coord[i] for i in range(self.dim)])

  def minus(self, vec):
    return Vector(*[self.coord[i] - vec.coord[i] for i in range(self.dim)])

  def times_vec(self, vec):
    return Vector(*[self.coord[i] * vec.coord[i] for i in range(self.dim)])

  def times_nb(self, nb):
    return Vector(*[self.coord[i] * nb for i in range(self.dim)])

  def by_vec(self, vec):
    return Vector(*[self.coord[i] / vec.coord[i] for i in range(self.dim)])

  def by_nb(self, nb):
    return Vector(*[self.coord[i] / nb for i in range(self.dim)])

class Matrix:
  def __init__(self, *row):
    self.content = [i for i in row]

  def show(self):
    for i in range(len(self.content)): print(self.content[i])
  
  def get_coef(self, i, j):
    return self.content[i][j]
    
  def get_dim(self):
    return len(self.content), len(self.content[0])
    
  def plus(self, mat):
    return Matrix(*[[self.content[i][j] + mat.content[i][j] for j in range(len(self.content[0]))] for i in range(len(self.content))])
    
  def minus(self, mat):
    return Matrix(*[[self.content[i][j] - mat.content[i][j] for j in range(len(self.content[0]))] for i in range(len(self.content))])
 
  def times_mat(self, mat):
    return Matrix(*[[sum([self.content[j][i] * mat.content[i][j] for i in range(len(self.content[0]))]) for k in range(len(mat.content[0]))] for j in range(len(self.content))])
 
  def times_nb(self, nb):
    return Matrix(*[[self.content[i][j] * nb for j in range(len(self.content[0]))] for i in range(len(self.content))])
    
  def by_mat(self, mat):
    return self.times_mat(mat.inverse())
    
  def by_nb(self, nb):
    return Matrix(*[[self.content[i][j] / nb for j in range(len(self.content[0]))] for i in range(len(self.content))])
    
  def augment(self, mat):
     [self.content[i].append(mat.content[i][j]) for j in range(len(self.content[0])) for i in range(len(self.content))]
        
  def sub(self, row_st, column_st, row_ed, column_ed):
    return Matrix(*[[self.content[i][j] for j in range(column_st, column_ed+1)] for i in range(row_st, row_ed+1)])
  
  def det(self):
    def calc_det(mat):
      rslt = 0
      if mat.get_dim() == (1, 1): rslt += mat.content[0][0]
      else:
        for i in range(len(mat.content[0])): rslt += (mat.content[0][i], -mat.content[0][i])[i % 2] * calc_det(mat.s_mat(i, 0))
      return rslt
    return calc_det(self)
    
  def transpose(self):
    return Matrix(*[[self.content[i][j] for i in range(len(self.content))] for j in range(len(self.content[0]))])
  
  def s_mat(self, jmp_i, jmp_j):
    return Matrix(*[[self.content[j][i] for i in range(len(self.content)) if i != jmp_i] for j in range(len(self.content[0])) if j != jmp_j])  

  def comat(self):
    return Matrix(*[[(-1) ** (i + j) * self.s_mat(i, j).det() for i in range(len(self.content))] for j in range(len(self.content[0]))])

  def inverse(self):
    return self.comat().transpose().times_nb(1 / self.det())

  def switch_row(self, row_1, row_2):
    for j in range(len(self.content[0])): self.content[row_1][j], self.content[row_2][j] = self.content[row_2][j], self.content[row_1][j]

  def switch_column(self, column_1, column_2):
    for i in range(len(self.content)): self.content[i][column_1], self.content[i][column_2] = self.content[i][column_2], self.content[i][column_1]
    
  def write_row(self, index, new_row):
    for j in range(len(self.content[0])): self.content[index][j] = new_row.content[0][j]

  def write_column(self, indef, new_column):
    for i in range(len(self.content)): self.content[i][index] = new_column.content[i][0]
    
def identity(n):
  return Matrix(*[[int(i == j) for i in range(n)] for j in range(n)])
    
    
    
