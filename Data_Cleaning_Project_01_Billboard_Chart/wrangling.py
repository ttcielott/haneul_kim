import pandas as pd
billboard=pd.read_csv('billboard.csv')


#replace the data type of values in the column 'wk1' with float64. 
billboard['wk1']=pd.to_numeric(billboard['wk1'], downcast='float')

#turn the columns of weekly number into rows.
billboard_melt=billboard.melt(
    id_vars=['year','artist','track','time','date.entered'],
    var_name='week',
    value_name='rating'

#drop rows of missing values(rating)
billboard_melt.dropna(inplace=True)

#create new dataframe containing only song information.
billboard_songs=billboard_melt[['year','artist','track','time','date.entered']]

#remove duplicates.
billboard_songs=billboard_songs.drop_duplicates()

#generate the column 'id'
billboard_songs['id']=range(len(billboard_songs))

#export 'billboard_songs.csv'.
billboard_songs.to_csv('billboard_song.csv',index=False)

#merge 'billboard.songs' with 'billboard_melt' and create new dataframe, called 'billboard ratings'.
billboard_ratings=billboard_melt.merge(
    billboard_songs, on=['year','artist','track','time','date.entered']

#select 4 columns that are needed for analysis. 
billboard_ratings=billboard_ratings[['id','date.entered','week','rating']]

# Clean Data View

billboard_ratings.head()

#save clean data file as 'billboard_ratings.csv' 
billboard_ratings.to_csv('billboard_ratings.csv', index=False)

