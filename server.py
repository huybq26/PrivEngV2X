# import pickle
#
#
# with open('NTU_project_map_filled.pkl', 'rb') as f:
#     data = pickle.load(f)
# import pickle
#
#
# with open('NTU_project_map_filled.pkl', 'rb') as f:
#     train_set, valid_set, test_set = pickle.load(f)
#
# train_x = train_set
#
# import matplotlib.cm as cm
# import matplotlib.pyplot as plt
#
#
# plt.imshow(train_x[0].reshape((28, 28)), cmap=cm.Greys_r)
# plt.show()

import pickle

path = 'NTU_project_map_filled.pkl'

f = open(path, 'rb')
data = pickle.load(f)

print(data)
print(len(data))