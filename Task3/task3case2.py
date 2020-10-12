import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import neighbors,tree
from sklearn.preprocessing import OneHotEncoder
#calculate the error and plot the graph


def domodel(x_train,y_train,x_validate,y_validate):

    loss = lambda y, yh: np.mean((y - yh) ** 2)
    K_list = range(1, 200)
    err_train, err_valid ,accuracy=[], [],[]
    for i, K in enumerate(K_list):
        model = neighbors.KNeighborsRegressor(n_neighbors=K)
        #model = tree.DecisionTreeRegressor(min_samples_leaf=K)
        model = model.fit(x_train, y_train)
        err_valid.append(loss(model.predict(x_validate),y_validate))
        err_train.append(loss(model.predict(x_train),y_train))
        accuracy.append(model.score(x_train ,y_train))

    best= np.argmin(err_valid) + 1
    print("BEST K for date split:",best)
    print("Best MSE for date split:",err_valid[best - 1])
    plt.plot(K_list, err_valid, '-', label='unseen')
    plt.plot(K_list, err_train, '-', label='train')
    plt.legend()
    plt.xlabel('K (number of neighbours)')
    plt.ylabel('mean squared error')
    plt.show()

    plt.plot(K_list, accuracy, '-', label='accuracy')
    plt.legend()
    plt.xlabel('K (number of neighbours)')
    plt.ylabel('accuracy')
    plt.show()


mydata = pd.read_csv("./USA_coviddata_clean_50.csv")
#delete useless feature
mydata = mydata.drop(labels=['Unnamed: 0','sub_region_1','hospitalized_cumulative'],axis=1)

#delete the rows that do not have labels
mydata =mydata[mydata['hospitalized_new'].notna()]

#--------------fill the missing data to the average of its column-----------#
for colname,col in mydata.iteritems():
    if 'symptom' in colname:
        symptom_mean = round(mydata[colname].mean(),2)
        mydata[colname].fillna(symptom_mean,inplace=True)
# mydata.fillna(0,inplace=True)

# --------------fill the missing data to the average of its column-----------#


#split into the training set and validation set
mydata_train = mydata[mydata['date']<='2020-08-10'] #use data before ‘2020-08-10’ as training set
mydata_validate = mydata[mydata['date']>'2020-08-10'] #use data after ‘2020-08-10’ as validation set

#delete the region and date features
mydata_train = mydata_train.drop(labels=['date','open_covid_region_code'],axis=1)
mydata_validate = mydata_validate.drop(labels=['date','open_covid_region_code'],axis=1)

# #convert pandas to numpy
mydata_train = mydata_train.values
mydata_validate = mydata_validate.values

#split the data into features and label
x_train,y_train = np.delete(mydata_train,[0],axis=1).astype(np.float),mydata_train[:,0].astype(np.float)
x_validate,y_validate = np.delete(mydata_validate,[0],axis=1).astype(np.float),mydata_validate[:,0].astype(np.float)

domodel(x_train,y_train,x_validate,y_validate)

