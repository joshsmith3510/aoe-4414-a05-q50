# ray_ellipsoid_intersection.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Brad Denby
# Other contributors: Josh Smith
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
R_E_KM = 6378.1363
E_E=0.081819221456

# helper functions

## function description
def mag(v):
    return math.sqrt(sum(x**2 for x in v))
def smul(s, v):
    return [s*x for x in v]
def add(v1, v2):
    return [x+y for x, y in zip(v1, v2)]
def sub(v1, v2):
    return [x-y for x, y in zip(v1, v2)]
def dot(v1, v2):
    return sum(x*y for x, y in zip(v1, v2))


# initialize script arguments
d_l_x = float('nan')
d_l_y = float('nan')
d_l_z = float('nan')
c_l_x = float('nan')
c_l_y = float('nan')
c_l_z = float('nan')


# parse script arguments
if len(sys.argv)==7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
    ...
else:
    print(\
        'Usage: '\
            'python3 d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z ...'\
                )
    exit()

# write script below this line
d_l=[d_l_x,d_l_y,d_l_z]
c_l=[c_l_x,c_l_y,c_l_z]

#Determining discriminant
a=d_l_x**2+d_l_y**2+(d_l_z**2)/(1-E_E**2)
b=2*(d_l_x*c_l_x+d_l_y*c_l_y+d_l_z*c_l_z/(1-E_E**2))
c=c_l_x**2+c_l_y**2+c_l_z**2/(1-E_E**2)-R_E_KM**2
discr=b*b-4.0*a*c
#Return the intersection point
if discr>=0.0:
    d=(-b-math.sqrt(discr))/(2.0*a)
    if d<0.0:
        d=(-b+math.sqrt(discr))/(2.0*a)
    if d>=0.0:
        l_d=add(smul(d,d_l),c_l)

print(l_d[0]) # x-component of intersection point
print(l_d[1]) # y-component of intersection point
print(l_d[2]) # z-component of intersection point