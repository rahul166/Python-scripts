'''
Hyperoptimization method I used for tunning the parameters of light gbm

'''



from hyperopt import hp
from hyperopt import fmin, tpe, hp, Trials
import xgboost as xgb
from sklearn.model_selection import cross_val_score,StratifiedKFold


class HyperoptMethod():
    def __init__(self,clf,x_train,y_train):
        self.classifier=clf
        self.x_train=x_train
        self.y_train=y_train

        
    def score(self,params):
        """
        It gives the acuuracy at it each trials
        
        Returns:
            [score(float)] -- [Accuracy score]
        """
        score = cross_val_score(self.classifier, self.x_train, self.y_train , scoring='accuracy', cv=StratifiedKFold()).mean()
        return score

        
    def optimize(self):
        """
        It is the main optimization function 
        Arguments:
            Trials {[type]} -- [description]
        
        Returns:
            [best] -- [optimized params]
        """
        space = {
                 'n_estimators' : hp.choice('n_estimators', [i for i in range(100,1000)]),
                 'max_depth' : hp.choice('max_depth', [i for i in range(1,13)]),
                 'num_leaves': hp.choice('num_leaves', [i for i in range(1,128)]),
                 'colsample_bytree' : hp.quniform('colsample_bytree', 0.5, 1, 0.05),

                 }


        trials=Trials()

        best = fmin(self.score,space=space,algo=tpe.suggest,max_evals=10,trials=trials)
        print(best)
        return best