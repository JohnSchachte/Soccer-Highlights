import librosa
import IPython as ipd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = "avatar.wav"
x, sr = librosa.load(filename, sr = 16000)
length = librosa.get_duration(x, sr)
print(length)


# Creating slices of audio to check for audio changes
max_slice = 5
window_length = max_slice * sr

"""Test Audio Chunk"""
# Audio chunk
# a = x[21*window_length:22*window_length]
# # ipd.display.Audio(a, rate = sr)

# # Energy for the audio chunk
# energy = sum(abs(a**2))
# print(energy)

#Visualizing the audio distribution for the chunk
# fig = plt.figure(figsize=(14, 8))
# ax1 = fig.add_subplot(211)
# ax1.set_xlabel('Splice with time') 
# ax1.set_ylabel('Amplitude') 
# ax1.plot(a)
# plt.show()
"""End of Test Audio Chunk"""


"""Full Audio Distribution"""
# Looking at the distribution of energy
energy = np.array([sum(abs(x[i:i+window_length]**2)) for i in range(0, len(x), window_length)])
print(energy)
plt.hist(energy)
plt.show()



# Defining the threshold 
df = pd.DataFrame(columns=['energy','start','end'])
thresh = 2700
row_index = 0
for i in range(len(energy)):
  value = energy[i]
  if(value >= thresh):
    i = np.where(energy == value)[0]
    print(i)
    df.loc[row_index,'energy'] = value
    df.loc[row_index,'start'] = i[0] * 5
    df.loc[row_index,'end'] = (i[0]+1) * 5
    row_index = row_index + 1

# Merging consecutive time intervals into one
temp = []
i = 0
j = 0
n = len(df) - 2
m = len(df) - 1
while(i <= n):
  j = i + 1
  while(j <= m):
    if(df['end'][i] == df['start'][j]):
      df.loc[i,'end'] = df.loc[j,'end']
      temp.append(j)
      j = j + 1
    else:
      i = j
      break  
df.drop(temp, axis = 0, inplace = True)

print(df)