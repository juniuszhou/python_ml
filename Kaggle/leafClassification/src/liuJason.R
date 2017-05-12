## Classification of leaves
**Statement** Still a Newbie to data mining and machine learning, but I am happy to share my opinion/solution with great kaggle 
community. Eager to hear your advice/suggestion! Thanks!

**Purpose** This Kernel blog serves the purpose of comparing the effectiveness of five different classifiers.

### Read data and load packages
```{r,message=FALSE,warning=FALSE}
# Load Packages
library(ggplot2)
library(readr)
library(magrittr)
library(dplyr)
library(e1071)
library(rpart)
library(Metrics)
library(randomForest)
library(Matrix)
library(methods)
library(MLmetrics)
library(rpart.plot)
library(corrplot)
library(xgboost)
library(caret)
```

```{r load}
# Read Data
train <- read.csv("../input/train.csv")
test <- read.csv("../input/test.csv")
```

As usual, the analysis can be done in five steps:

* Data Exploration/Cleansing
* Descriptive Analysis/Feature Engineering
* Model Comparison
* Conclusion
* Questions 

You may have noticed that the quantity of variables that may put influence on the result is  intimidating! Therefore, maybe we need
to conduct feature engineering before fitting the model. The method I intend to implement is principle component analysis, or PCA since 
the data set is really dimentional.

### Data Exploration/Cleansing

First, we examine types of variables in the dataset.

```{r,message=FALSE,warning=FALSE}
train<- train[,-1]
test<- test
# Type/Class of variables 
```
```{r,message=FALSE,warning=FALSE,eval=FALSE}
sapply(train, class)
```

After getting rid of the 'id' column, I first check how many missing values in training set. If too many missing values are existing in
a column. The variable with to many missing values should be dropped directly. Suprisingly I found the classes of variables are quite neat!

```{r,message=FALSE,warning=FALSE}
Num_NA<-sapply(train,function(y)length(which(is.na(y)==T)))
sum(Num_NA)
```
The integrity of dataset is amazing. So the feature engineering can be started directly.

### Descriptive Analysis/Feature Engineering

Among 193 variables, One can find only three descriptive class: margin, shape and texture. When you examine the correlation among different 
variables in same category, you can find that most of them have strong correlation between each other, which is a sign of feature selection. The corrplot of shape is a proof.
```{r,message=FALSE,warning=FALSE}
correlations<- cor(train %>% select(contains("shape")),use="everything")
corrplot(correlations, method="circle", type="lower",  sig.level = 0.01, insig = "blank")
```

Therefore, I believe that implementing PCA may help us to shrink down the size of variables from 193 to maybe 15 or 16. The problem will be simplified and the overfitting 
problem can be somehow avoided.

```{r,message=FALSE,warning=FALSE}
Margin<-train %>% select(contains("margin"))
pr_Margin<-princomp(Margin)
Shape<- train %>% select(contains('shape'))
pr_shape<-princomp(Shape)
Texture<- train %>% select(contains('texture'))
pr_texture<-princomp(Texture)

```
```{r,message=FALSE,warning=FALSE}
summary(pr_Margin)
```
We can see that the PCA analysis is not feasible enough. The cumulative variance of components of texture and margin are not approximating 80% for the 
first five components. Based on the result of PCA analysis, we prepared the test set for the final prediction as usual.
```{r,message=FALSE,warning=FALSE}
Train_PCA<- data.frame(train$species,pr_Margin$scores[,1:5],pr_shape$scores[,1:3],pr_texture$scores[,1:5])
colnames(Train_PCA)<-c('species','Com1','Com2','Com3','Com4','Com5','Com6','Com7','Com8','Com9','Com10','Com11','Com12','Com13')
Test_Margin<- predict(pr_Margin,newdata=test %>% select(contains("margin")))[,1:5]
Test_Shape<- predict(pr_shape,newdata=test %>% select(contains("shape")))[,1:3]
Test_Texture<- predict(pr_texture,newdata=test %>%select(contains("texture")))[,1:5]
Test<- data.frame(Test_Margin,Test_Shape,Test_Texture)
colnames(Test)<-c('Com1','Com2','Com3','Com4','Com5','Com6','Com7','Com8','Com9','Com10','Com11','Com12','Com13')

```
### Model Comparison
I do not re-split the training set into two sub sets. (***Should I do it?***) Only thing I do is to see the eval-index of the model inside the training set and choose the one that best fit. We start with Naive Bayes.

#### NB Model 

Naive Bayes model is quite basic but always effective when dealing with classification problem. In order to evaluate the effectiveness of classifier, I use the
actual values and fitted values within the training set to make assessment.

```{r,message=FALSE,warning=FALSE}
NaivB<- naiveBayes(species~.,Train_PCA)
pred<- predict(NaivB,newdata=Train_PCA[,2:14],type='raw')
logloss1<-MultiLogLoss(y_true = Train_PCA[,1], y_pred = as.matrix(pred))
```
#### Classification Tree

The second model I tried to fit is classification tree. In order to better train the model, I use the amazing training function in package 'caret' to tune the model.

```{r,message=FALSE,warning=FALSE}
set.seed(1234)
Control<- trainControl(method='repeatedcv',number =10,repeats=3)
Tree<- train(Train_PCA[,2:14],Train_PCA[,1],method='rpart',trControl=Control)
pred<- predict(Tree,newdata= Train_PCA[,2:14],type='prob')
logloss2<- MultiLogLoss(y_true = Train_PCA[,1], y_pred = as.matrix(pred))
```

#### Random Forest

Random forest is always considered as an effective method to perform classification. 

```{r, message=FALSE,warning=FALSE}
set.seed(1234)
Control<- trainControl(method='repeatedcv',number =10,repeats=3)
rf<- train(Train_PCA[,2:14],Train_PCA[,1],method='rf',prox=TRUE,allowParallel=TRUE,trControl=Control)
pred<- predict(rf,newdata= Train_PCA[,2:14],type='prob')
logloss3<-MultiLogLoss(y_true = Train_PCA[,1], y_pred = as.matrix(pred))
```

#### Multinominal Logit Regression

Then, I choose to fit the training set into multinominal logit regression model.
```{r,message=FALSE,warning=FALSE}
set.seed(1234)
Control<- trainControl(method='repeatedcv',number =10,repeats=3)
Grid<- expand.grid(
  decay=c(0.0001,0.0000001,0.00000001)
  )
LG<-train(Train_PCA[,2:14],Train_PCA[,1],method='multinom',prox=TRUE,allowParallel=TRUE,trControl=Control,tuneGrid=Grid,MaxNWts=2000)
pred<- predict(LG,newdata= Train_PCA[,2:14],type='prob')
logloss4<-MultiLogLoss(y_true = Train_PCA[,1], y_pred = as.matrix(pred))
```

#### XGboost
Finally, I choose to try one of the most popular winning receipe of kaggle---XGBoost. Since it took really long time to tune the model **Is that normal?**, so I run the code 
locally and just post the result and skip the running of program.

```{r,message=FALSE,warning=FALSE,eval=FALSE}
set.seed(1234)
cv.ctrl <- trainControl(method = "repeatedcv", repeats = 10,number = 3)

xgb.grid <- expand.grid(nrounds = 100,
                        max_depth = seq(6,10),
                        eta = c(0.01,0.3, 1),
                        gamma = c(0.0, 0.2, 1),
                        colsample_bytree = c(0.5,0.8, 1),
                        min_child_weight= 1
)

xgb_tune <-train(species ~.,
                 data=Train_PCA,
                 method="xgbTree",
                 trControl=cv.ctrl,
                 tuneGrid=xgb.grid
)
pred<- predict(xgb_tune,newdata= Train_PCA[,2:14],type='prob')
logloss5<-MultiLogLoss(y_true = Train_PCA[,1], y_pred = as.matrix(pred))

```

```{r,message=FALSE,warning=FALSE}
logloss5<-0.104116
```

#### Result Comparison

The comparison of the effectiveness of model is displayed on the plot below.

```{r,message=FALSE,warning=FALSE}
Metrics<- data.frame(method=c('NaiveBayes','Classification Tree','Random Forest','Logistic Regression','XGBoost'), Multilogloss=c(logloss1,logloss2,logloss3,logloss4,logloss5))
ggplot(Metrics,aes(x=method,y=Multilogloss))+geom_bar(stat='identity')+theme_bw()+ggtitle('Effectiveness of models')
```

#### Submission

```{r,message=FALSE,warning=FALSE}
Sub<- predict(NaivB,newdata=Test,type='raw')
Sub<- data.frame(id=test$id,Sub)
write.csv(Sub,'Sub10.csv',row.names=FALSE)
```

### Conclusion

In short, we can find: 
  
a. With strong correlations among each variables, feature enginnering is important. PCA is not perfect but it still works.

b. Naive Bayesian is effective when we evaluating the model with multi-log-loss.

c. Classification tree failed to be a good classifier. Maybe the reason is that the number of classes of target is too large.

d. Random Forest and XGBoost are advanced model, I believe my model tunning ability is not good. Maybe they should be more powerful.


### Question

By the end of this blog, I just wanna ask several questions to the talented Kaggle community:

1: Could some parameter tunning experts give me some advice on the parameter tunning using caret package? Please give me some suggestion on that! 

2: Seems that most great scores are achieved by python using logistic regression. I have found that the leaders use different kinds of logistic regression (Maybe) in python, or they can 'solve' the regression effectively
which is (I believe ) different from the one in nnet in R. COULD someone recommend a similar package in R for me?  I REALLY WANT TO LEARN ABOUT IT!!! It looks good when dealing with multiple-class classification.


