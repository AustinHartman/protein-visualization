import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches


file = '3nir.pdb'

coords = []
i = 0
with open(file) as pdb_file:
    for row in pdb_file:
        i += 1
        row = row.split()
        if row[0] == "ATOM":
            c = row[6:9]
            c.append(row[-1])
            coords.append(c)

x=[]
y=[]
z=[]
c=[]

for coord in coords:
    x.append(float(coord[0]))
    y.append(float(coord[1]))
    z.append(float(coord[2]))
    c.append(coord[3])

def pickColor(atoms):
    i = 0
    options = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    c_dict = dict()

    for atom in atoms:
        # if new atom encountered move color picker index down
        if (atom not in c_dict):
            if (i+1 < len(options)):
                c_dict[atom] = options[i]
                i += 1
            else:
                print("Ran out of color options")
    return c_dict


def atomColorCodes(c_dict, atoms):
    atom_color_codes = []
    for atom in atoms:
        atom_color_codes.append(c_dict[atom])

    return atom_color_codes


c_dict = pickColor(c)
c = atomColorCodes(c_dict, c)

color_labels = []
for key, value in c_dict.items():
    color_labels.append(mpatches.Patch(color=value, label=key))



fig = plt.figure()
ax = plt.axes(projection='3d')

for i in range(len(x)):
    ax.scatter(x[i], y[i], z[i], color=c[i], s=4)


ax.legend(handles=color_labels)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('PDB 4-digit code ' + file.split('.')[0])

plt.show()
