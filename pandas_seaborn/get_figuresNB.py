
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import seaborn as sns
sns.set(style="ticks", color_codes=True)


# In[2]:

aviator_data = pd.read_excel('table_reduced.xlsx', skiprows=[0])


# In[3]:

vfr = pd.DataFrame()
vfr['Ability'] = aviator_data["Ability's level"]
vfr['Fixation Dispersion Minimum'] = aviator_data['VFR - Visual Intake Dispersion Minimum [px]']
vfr['Flight Type'] = 'VFR'

ifr1 = pd.DataFrame()
ifr1['Ability'] = aviator_data["Ability's level"]
ifr1['Fixation Dispersion Minimum'] = aviator_data['IFR 1 - Visual Intake Dispersion Minimum [px]']
ifr1['Flight Type'] = 'IFR1'

ep = pd.DataFrame()
ep['Ability'] = aviator_data["Ability's level"]
ep['Fixation Dispersion Minimum'] = aviator_data['EP - Visual Intake Dispersion Minimum [px]']
ep['Flight Type'] = 'EP'

ifr2 = pd.DataFrame()
ifr2['Ability'] = aviator_data["Ability's level"]
ifr2['Fixation Dispersion Minimum'] = aviator_data['IFR 2 - Visual Intake Dispersion Minimum [px]']
ifr2['Flight Type'] = 'IFR2'


# In[4]:

frames = [vfr,ifr1,ep,ifr2]
dispersion_min = pd.concat(frames)
dispersion_min.loc[dispersion_min['Ability'] == 1, 'Ability'] = 'Novice'
dispersion_min.loc[dispersion_min['Ability'] == 2, 'Ability'] = 'Expert'


# In[37]:

plot_dispersion_min = sns.boxplot(x='Flight Type',y='Fixation Dispersion Minimum',
                                    data = dispersion_min, whis=np.inf, width = .5, palette='muted')

plot_dispersion_min = sns.swarmplot(x='Flight Type',y='Fixation Dispersion Minimum',
                                    data = dispersion_min, hue='Ability', palette='Set2', size=8)
                                    
plot_dispersion_min.set_ylabel('Fixation Dispersion Minimum (px)', size = 20)
plot_dispersion_min.set_xlabel('Flight Type', size = 20)
plot_dispersion_min.set_title('Fixation Dispersion Minimum Across All Groups', size = 20)    
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)                
sns.despine()


# In[52]:

vfr = pd.DataFrame()
vfr['Ability'] = aviator_data["Ability's level"]
vfr['Fixation Dispersion Total'] = aviator_data['VFR - Visual Intake Dispersion Total [px]']
vfr['Flight Type'] = 'VFR'

ifr1 = pd.DataFrame()
ifr1['Ability'] = aviator_data["Ability's level"]
ifr1['Fixation Dispersion Total'] = aviator_data['IFR 1 - Visual Intake Dispersion Total [px]']
ifr1['Flight Type'] = 'IFR1'

ep = pd.DataFrame()
ep['Ability'] = aviator_data["Ability's level"]
ep['Fixation Dispersion Total'] = aviator_data['EP - Visual Intake Dispersion Total [px]']
ep['Flight Type'] = 'EP'

ifr2 = pd.DataFrame()
ifr2['Ability'] = aviator_data["Ability's level"]
ifr2['Fixation Dispersion Total'] = aviator_data['IFR 2 - Visual Intake Dispersion Total [px]']
ifr2['Flight Type'] = 'IFR2'


# In[53]:

frames = [vfr,ifr1,ep,ifr2]
dispersion_tot = pd.concat(frames)
dispersion_tot.loc[dispersion_tot['Ability'] == 1, 'Ability'] = 'Novice'
dispersion_tot.loc[dispersion_tot['Ability'] == 2, 'Ability'] = 'Expert'


# In[62]:

plot_dispersion_tot = sns.boxplot(x='Flight Type',y='Fixation Dispersion Total',
                                    data = dispersion_tot, whis=np.inf, width = .3, palette='muted')

plot_dispersion_tot = sns.swarmplot(x='Flight Type',y='Fixation Dispersion Total',
                                    data = dispersion_tot, hue='Ability', palette='Set2', size=8)
                                    
plot_dispersion_tot.set_ylabel('Fixation Dispersion Total (px)', size = 20)
plot_dispersion_tot.set_xlabel('Flight Type', size = 20)
plot_dispersion_tot.set_title('Fixation Dispersion Total Across All Groups', size = 20)    
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)    
plt.ylim(0,500000)
sns.despine()


# In[63]:

vfr = pd.DataFrame()
vfr['Ability'] = aviator_data["Ability's level"]
vfr['Fixation Duration Average'] = aviator_data['VFR - Visual Intake Duration Average [ms]']
vfr['Flight Type'] = 'VFR'

ifr1 = pd.DataFrame()
ifr1['Ability'] = aviator_data["Ability's level"]
ifr1['Fixation Duration Average'] = aviator_data['IFR 1 - Visual Intake Duration Average [ms]']
ifr1['Flight Type'] = 'IFR1'

ep = pd.DataFrame()
ep['Ability'] = aviator_data["Ability's level"]
ep['Fixation Duration Average'] = aviator_data['EP - Visual Intake Duration Average [ms]']
ep['Flight Type'] = 'EP'

ifr2 = pd.DataFrame()
ifr2['Ability'] = aviator_data["Ability's level"]
ifr2['Fixation Duration Average'] = aviator_data['IFR 2 - Visual Intake Duration Average [ms]']
ifr2['Flight Type'] = 'IFR2'


# In[64]:

frames = [vfr,ifr1,ep,ifr2]
dispersion_dur = pd.concat(frames)
dispersion_dur.loc[dispersion_dur['Ability'] == 1, 'Ability'] = 'Novice'
dispersion_dur.loc[dispersion_dur['Ability'] == 2, 'Ability'] = 'Expert'


# In[65]:

plot_dispersion_dur = sns.boxplot(x='Flight Type',y='Fixation Duration Average',
                                    data = dispersion_dur, whis=np.inf, width = .3, palette='muted')

plot_dispersion_dur = sns.swarmplot(x='Flight Type',y='Fixation Duration Average',
                                    data = dispersion_dur, hue='Ability', palette='Set2', size=8)
                                    
plot_dispersion_dur.set_ylabel('Fixation Duration Average (ms)', size = 20)
plot_dispersion_dur.set_xlabel('Flight Type', size = 20)
plot_dispersion_dur.set_title('Fixation Duration Average Across All Groups', size = 20)    
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)    
sns.despine()


# In[67]:

vfr = pd.DataFrame()
vfr['Ability'] = aviator_data["Ability's level"]
vfr['Saccade Duration Average'] = aviator_data['VFR - Saccade Duration Average [ms]']
vfr['Flight Type'] = 'VFR'

ifr1 = pd.DataFrame()
ifr1['Ability'] = aviator_data["Ability's level"]
ifr1['Saccade Duration Average'] = aviator_data['IFR 1 - Saccade Duration Average [ms]']
ifr1['Flight Type'] = 'IFR1'

ep = pd.DataFrame()
ep['Ability'] = aviator_data["Ability's level"]
ep['Saccade Duration Average'] = aviator_data['EP - Saccade Duration Average [ms]']
ep['Flight Type'] = 'EP'

ifr2 = pd.DataFrame()
ifr2['Ability'] = aviator_data["Ability's level"]
ifr2['Saccade Duration Average'] = aviator_data['IFR 2 - Saccade Duration Average [ms]']
ifr2['Flight Type'] = 'IFR2'



# In[68]:

frames = [vfr,ifr1,ep,ifr2]
saccade_dur = pd.concat(frames)
saccade_dur.loc[saccade_dur['Ability'] == 1, 'Ability'] = 'Novice'
saccade_dur.loc[saccade_dur['Ability'] == 2, 'Ability'] = 'Expert'


# In[70]:

plot_saccade_dur = sns.boxplot(x='Flight Type',y='Saccade Duration Average',
                                    data = saccade_dur, whis=np.inf, width = .3, palette='muted')

plot_saccade_dur = sns.swarmplot(x='Flight Type',y='Saccade Duration Average',
                                    data = saccade_dur, hue='Ability', palette='Set2', size=8)
                                    
plot_saccade_dur.set_ylabel('Saccade Duration Average (ms)', size = 20)
plot_saccade_dur.set_xlabel('Flight Type', size = 20)
plot_saccade_dur.set_title('Saccade Duration Average Across All Groups', size = 20)    
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)    
sns.despine()


# In[71]:

vfr = pd.DataFrame()
vfr['Ability'] = aviator_data["Ability's level"]
vfr['Saccade Frequency'] = aviator_data['VFR - Saccade Frequency [count/s]']
vfr['Flight Type'] = 'VFR'

ifr1 = pd.DataFrame()
ifr1['Ability'] = aviator_data["Ability's level"]
ifr1['Saccade Frequency'] = aviator_data['IFR 1 - Saccade Frequency [count/s]']
ifr1['Flight Type'] = 'IFR1'

ep = pd.DataFrame()
ep['Ability'] = aviator_data["Ability's level"]
ep['Saccade Frequency'] = aviator_data['EP - Saccade Frequency [count/s]']
ep['Flight Type'] = 'EP'

ifr2 = pd.DataFrame()
ifr2['Ability'] = aviator_data["Ability's level"]
ifr2['Saccade Frequency'] = aviator_data['IFR 2 - Saccade Frequency [count/s]']
ifr2['Flight Type'] = 'IFR2'


# In[72]:

frames = [vfr,ifr1,ep,ifr2]
saccade_frq = pd.concat(frames)
saccade_frq.loc[saccade_frq['Ability'] == 1, 'Ability'] = 'Novice'
saccade_frq.loc[saccade_frq['Ability'] == 2, 'Ability'] = 'Expert'


# In[ ]:




# In[101]:

plot_saccade_frq = sns.boxplot(x='Flight Type',y='Saccade Frequency',
                                    data = saccade_frq, whis=np.inf, width = .3)

plot_saccade_frq = sns.swarmplot(x='Flight Type',y='Saccade Frequency',
                                    data = saccade_frq, hue='Ability', palette='husl', size=8)
                                    
plot_saccade_frq.set_ylabel('Saccade Frequency (counts/sec)', size = 20)
plot_saccade_frq.set_xlabel('Flight Type', size = 20)
plot_saccade_frq.set_title('Saccade Frequency Across All Groups', size = 20)    
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)    
sns.despine()


# In[ ]:



