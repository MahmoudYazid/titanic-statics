from keras import layers
from keras import Sequential
import sqlite3 as sql
from matplotlib import pyplot
#
def get_relation_with_dead_or_live(target,predict):
    target_val=[]
    id=[]
    dead_or_not = []
    con=sql.connect("titanic.db")
    con_exe=con.cursor()
    con_exe.execute("""SELECT * FROM train """)
    for result1 in con_exe.fetchall():
        target_val.append(int(float(result1[target])))
        id.append(int(float(result1[0])))


    for result2 in range(0,int(len(target_val))):
        con_exe.execute("""SELECT Survived FROM gender_submission WHERE PassengerId="{}" """.format(id[result2]))
        for result3 in con_exe.fetchall():
            dead_or_not.append(int(float(result3[0])))


    model=Sequential()
    model.add(layers.Dense(1,input_shape=(1,)))
    model.add(layers.Dense(64,activation='relu'))
    model.add(layers.Dense(64,activation='relu'))
    model.add(layers.Dense(64,activation='relu'))

    model.add(layers.Dense(1, activation='relu'))



    model.compile(loss='mean_squared_error' ,optimizer='adam')
    model.fit(target_val,dead_or_not,epochs=1000,verbose=1)
    pre=model.predict([predict])

    pyplot.scatter(target_val,dead_or_not)
    pyplot.show()
    if pre[0]> 0:
        print(1)
    else:
        print(0)

get_relation_with_dead_or_live(6,2)
'''
this script us for only numpers of database like pclass , Age ..etc but the other information wwe will use matlab and we will use the main, medium ... etc bacouse its un countable values or oyou can convert it to numerical values and deal with the same algorethm that did in this script .. 
'''

