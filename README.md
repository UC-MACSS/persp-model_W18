# MACS 30100 - Perspectives on Computational Modeling (Winter 2018)

|  | [Dr. Richard Evans](https://sites.google.com/site/rickecon/) | [Chelsea Ernhofer]() (TA) | [Sushmita Gopalan]() (TA) |
|--------------|--------------------------------------------------------------|----------------------------------------------------|----------------------------------------------------------------------------|
| Email | rwevans@uchicago.edu | cernhofer@gmail.com | sushmitavgopalan@uchicago.edu |
| Office | 208 McGiffert House |  |  |
| Office Hours | T 9:30-11:30am | Th 1:00-3:00pm | Th 9:00-11:00am  |
| GitHub | [rickecon](https://github.com/rickecon) | [cernhofer](https://github.com/cernhofer) | [sushmitavgopalan16](https://github.com/sushmitavgopalan16) |

* **Meeting day/time**: MW 11:30am-1:20pm, Saieh Hall, Room 247
* **Lab session**: W 4:30 - 5:20pm, Saieh Hall, Room 247
* Office hours also available by appointment

## Course description

Students are often well trained in the details of specific models relevant to their respective fields. This course presents a generic definition of a model in the social sciences as well as a taxonomy of a wide range of different types of models used. We cover principles of model building, including static versus dynamic models, linear versus nonlinear, simple versus complicated, and identification versus overfitting. Major types of models implemented in this course include systems of nonlinear equations, linear and nonlinear regression, supervised learning (decision trees, random forests, support vector machines, etc.), and unsupervised learning. We will also explore the wide range of computational strategies used to estimate models from data and make statistical and causal inference. Students will study both good examples and bad examples of modeling and estimation. This course will give a quick overview of many topics and applied practice in problem sets with the hope that the students will later pursue deeper study into specific areas we cover.

## Grades

You will have 8 problem sets throughout the term. I will drop everybody's lowest problem set score. For this reason, problem sets will only account for 80 percent of your grade.

| Assignment       | Quantity | Points | Total Points | Percent |
|------------------|----------|--------|--------------|---------|
| Problem Sets     | 8        | 10     | 70           | 77.8%     |
| Midterm exam     | 1        | 20     | 20           | 22.2%     |
| **Total Points** | --       | --     | 90           | 100%    |

Late problem sets will be penalized 2 points for every hour they are late. For example, if an assignment is due on Monday at 11:30am, the following points will be deducted based on the time stamp of the last commit.

| Example PR last commit | points deducted |
| ---------------------- | --------------- |
| 11:31am to 12:30pm     | -2 points       |
| 12:31pm to 1:30pm      | -4 points       |
| 1:31pm to 2:30pm       | -6 points       |
| 2:31pm to 3:30pm       | -8 points       |
| 3:30pm and beyond      | -10 points (no credit) |

## Disability services

If you need any special accommodations, please provide us with a copy of your Accommodation Determination Letter (provided to you by the Student Disability Services office) as soon as possible so that you may discuss with me how your accommodations may be implemented in this course.

## Course schedule

| Date | Day | Topic | Readings | Assignment |
|------------|-------|---------------------------------------------------------|--------------|------------------------------|
| Jan.  3 | W | Model/theory building | [V1997](http://people.ischool.berkeley.edu/~hal/Papers/how.pdf) |  |
| Jan.  8 | M | Data generating process |  | [PS1](https://github.com/UC-MACSS/persp-model_W18/blob/master/ProblemSets/PS1/PS1.pdf) |
| Jan. 10 | W | Maximum likelihood estimation | [Notes](https://github.com/UC-MACSS/persp-model_W18/blob/master/Notebooks/MLE/MLest.ipynb) |  |
| Jan. 15 | M | **No class (Martin Luther King, Jr. Day)** |  |  |
| Jan. 17 | W | Generalized method of moments | [Notes](https://github.com/UC-MACSS/persp-model_W18/blob/master/Notebooks/GMM/GMMest.ipynb) |  |
| Jan. 22 | M | Generalized method of moments |  | [PS2](https://github.com/UC-MACSS/persp-model_W18/blob/master/ProblemSets/PS2/PS2.pdf) |
| Jan. 24 | W | Statistical learning and linear regression | JWHT Ch. 2, 3, [Notes](https://github.com/UC-MACSS/persp-model_W18/blob/master/Notebooks/LinRegress/LinRegress.ipynb) | [PS3](https://github.com/UC-MACSS/persp-model_W18/blob/master/ProblemSets/PS3/PS3.pdf) |
| Jan. 29 | M | Classification and logistic regression | JWHT Chs. 2, 4 |    |
| Jan. 31 | W | Classification and logistic regression | [Notes](https://github.com/UC-MACSS/persp-model_W18/blob/master/Notebooks/Classfcn1/KKNlogitLDA.ipynb) |  |
| **Feb. 5** | **M** | **Evans Midterm** |  | [PS4](https://github.com/UC-MACSS/persp-model_W18/blob/master/ProblemSets/PS4/PS4.pdf) |
| Feb.  7 | W | Generalized linear models | [Notes](https://github.com/UC-MACSS/persp-model_W18/blob/master/Notebooks/GLMs/GLMest.ipynb) |  |
| Feb. 12 | M | Resampling methods (cross-validation and bootstrapping) | JWHT Ch. 5, [Notes](https://github.com/UC-MACSS/persp-model_W18/blob/master/Notebooks/Resampling/Resampling.ipynb) |  |
| Feb. 14 | W | Nonlinear modeling | JWHT Ch. 7, [Notes](https://github.com/UC-MACSS/persp-model_W18/blob/master/Notebooks/Nonlin/Nonlin.ipynb) |     |
| Feb. 19 | M | Tree-based methods | JWHT Ch. 8, [Notes](https://github.com/UC-MACSS/persp-model_W18/blob/master/Notebooks/Trees/Trees.ipynb) | [PS5](https://github.com/UC-MACSS/persp-model_W18/blob/master/ProblemSets/PS5/PS5.pdf) |
| Feb. 21 | W | Tree-based methods | JWHT Ch. 8 |  |
| Feb. 26 | M | Support vector machines | JWHT Ch. 9 | [PS6](https://github.com/UC-MACSS/persp-model_W18/blob/master/ProblemSets/PS6/PS6.pdf) |
| Feb. 28 | W | Support vector machines | [Notes](https://github.com/UC-MACSS/persp-model_W18/blob/master/Notebooks/SVM/SVM.ipynb) |  |
| Mar.  5 | M | Neural networks | HTF Ch. 11, G Ch. 10 | [PS7](https://github.com/UC-MACSS/persp-model_W18/blob/master/ProblemSets/PS7/PS7.pdf) |
| Mar.  7 | W | Neural networks | [Notes](https://github.com/UC-MACSS/persp-model_W18/blob/master/Notebooks/NeuralNet/NeuralNet.ipynb) |     |
| Mar. 12 | M |                 |       | [PS8](https://github.com/UC-MACSS/persp-model_W18/blob/master/ProblemSets/PS8/PS8.pdf) |

## References and Readings ##

All readings are required unless otherwise noted. Adjustments can be made throughout the quarter; be sure to check this repository frequently to make sure you know all the assigned readings.

* Géron, Aurélien, *Hands-On Machine Learning with Scikit-Learn & TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems*, O'Reilly (2017).
* Hastie, Trevor, Robert Tibshirani, and Jerome Friedman, [*The Elements of Statistical Learning: Data Mining, Inference, and Prediction*](https://web.stanford.edu/~hastie/Papers/ESLII.pdf), 2nd Edition, Springer (2009).
* James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). [*An Introduction to Statistical Learning*](http://link.springer.com.proxy.uchicago.edu/book/10.1007%2F978-1-4614-7138-7). New York: Springer.
* VanderPlas, Jake. (2016). [*Python Data Science Handbook*](http://proquestcombo.safaribooksonline.com.proxy.uchicago.edu/book/programming/python/9781491912126). O'Reilly Media, Inc.
* Varian, Hal R., "[How to Build an Economic Model in Your Spare Time](http://people.ischool.berkeley.edu/~hal/Papers/how.pdf)," in *Passion and Craft: Economists at Work*, eds. Michael Szenberg, University of Michigan Press, 1997.
