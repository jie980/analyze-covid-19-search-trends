import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import neighbors,tree

def split_set(dataset,state_name1, state_name2):
    validate_set = dataset.loc[
        (dataset['open_covid_region_code'] == state_name1) | (dataset['open_covid_region_code'] == state_name2)]
    training_set = dataset.loc[
        (dataset['open_covid_region_code'] != state_name1) & (dataset['open_covid_region_code'] != state_name2)]
    # delete the region and date features
    validate_set = validate_set.drop(labels=['date', 'open_covid_region_code'], axis=1)
    training_set = training_set.drop(labels=['date', 'open_covid_region_code'], axis=1)
    # #convert pandas to numpy
    training_set =training_set.values
    validate_set = validate_set.values

    # split the data into features and label
    x_train, y_train = np.delete(training_set, [0], axis=1).astype(np.float), training_set[:, 0].astype(np.float)
    x_validate, y_validate = np.delete(validate_set, [0], axis=1).astype(np.float), validate_set[:, 0].astype(
        np.float)
    #print(y_validate)

    return x_train,y_train,x_validate,y_validate
#calculate the error and plot the graph
def domodel(x_train,y_train,x_validate,y_validate):
    #define the MSE functioon
    loss = lambda y, yh: np.mean((y - yh) ** 2)
    K_list = range(1, 200)
    err_train, err_valid =[], []
    for i, K in enumerate(K_list):
        model = neighbors.KNeighborsRegressor(n_neighbors=K)
        #model = tree.DecisionTreeRegressor(min_samples_leaf=K)
        model = model.fit(x_train, y_train)
        err_valid.append(loss(model.predict(x_validate),y_validate))
        err_train.append(loss(model.predict(x_train),y_train))
    best= np.argmin(err_valid) + 1
    print("BEST K for region split:",best)
    print("Best MSE for region split:",err_valid[best - 1])
    plt.plot(K_list, err_valid, '-', label='unseen')
    plt.plot(K_list, err_train, '-', label='train')
    plt.legend()
    plt.xlabel('K (number of neighbours)')
    plt.ylabel('mean squared error')
    plt.show()
    return err_valid

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


errorvalid = np.zeros((199, 5)) #use it to store 5 validation error set

#find the 11 states that we are using
regionlist = mydata['open_covid_region_code'].unique()
#print(regionlist.unique())

#do cross validation 5 times
#use 2 states as validation set and 9 states as training set
for i in range(0,len(regionlist)-1,2):
    print("validation set:",regionlist[i],regionlist[i+1])
    x_train,y_train,x_validate,y_validate=split_set(mydata,regionlist[i],regionlist[i+1])

    this_errorvalid = domodel(x_train,y_train,x_validate,y_validate)
    errorvalid[:,i//2] = this_errorvalid


plt.errorbar(range(1, 200), np.mean(errorvalid, 1), np.std(errorvalid, 1), label='validation')

plt.legend()

plt.xlabel('K (number of neighbours)')
plt.ylabel('mean squared error')
plt.show()