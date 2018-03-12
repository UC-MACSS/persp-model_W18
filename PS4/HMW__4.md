This is an [R Markdown](http://rmarkdown.rstudio.com) Notebook. When you execute code within the notebook, the results appear beneath the code.

Try executing this chunk by clicking the *Run* button within the chunk or by placing your cursor inside it and pressing *Cmd+Shift+Enter*.

``` r
library(ggplot2)
```

    ## Warning: package 'ggplot2' was built under R version 3.2.5

``` r
library(lattice)
library(caret)
```

    ## Warning: package 'caret' was built under R version 3.2.5

``` r
library(class)
library(GGally)
```

    ## Warning: package 'GGally' was built under R version 3.2.5

``` r
library(SDMTools)
```

    ## 
    ## Attaching package: 'SDMTools'

    ## The following objects are masked from 'package:caret':
    ## 
    ##     sensitivity, specificity

Question 1a): I replace the "?" values with NA values.

``` r
auto<-read.csv("auto.csv", na.strings = "?")
```

Question 1b):

``` r
scatterplot_matrix<-pairs(auto[,1:6], main="Scatterplot Matrix")
```

![](HMW__4_files/figure-markdown_github/unnamed-chunk-3-1.png)

``` r
scatterplot_matrix<-ggpairs(auto[,1:6])
print(scatterplot_matrix)
```

    ## Warning in (function (data, mapping, alignPercent = 0.6, method =
    ## "pearson", : Removed 5 rows containing missing values

    ## Warning in (function (data, mapping, alignPercent = 0.6, method =
    ## "pearson", : Removed 5 rows containing missing values

    ## Warning in (function (data, mapping, alignPercent = 0.6, method =
    ## "pearson", : Removed 5 rows containing missing values

    ## Warning: Removed 5 rows containing missing values (geom_point).

    ## Warning: Removed 5 rows containing missing values (geom_point).

    ## Warning: Removed 5 rows containing missing values (geom_point).

    ## Warning: Removed 5 rows containing non-finite values (stat_density).

    ## Warning in (function (data, mapping, alignPercent = 0.6, method =
    ## "pearson", : Removed 5 rows containing missing values

    ## Warning in (function (data, mapping, alignPercent = 0.6, method =
    ## "pearson", : Removed 5 rows containing missing values

    ## Warning: Removed 5 rows containing missing values (geom_point).

    ## Warning: Removed 5 rows containing missing values (geom_point).

![](HMW__4_files/figure-markdown_github/unnamed-chunk-3-2.png)

Question 1c):

``` r
auto$mpg<-as.numeric(auto$mpg)
auto$cylinders<-as.numeric(auto$cylinders)
auto$displacement<-as.numeric(auto$displacement)
auto$horsepower<-as.numeric(auto$horsepower)
cor_matrix<-cor(auto[,1:8], method="pearson", use="pairwise")
print(cor_matrix)
```

    ##                     mpg  cylinders displacement horsepower     weight
    ## mpg           1.0000000 -0.7762599   -0.8044430 -0.7784268 -0.8317389
    ## cylinders    -0.7762599  1.0000000    0.9509199  0.8429834  0.8970169
    ## displacement -0.8044430  0.9509199    1.0000000  0.8972570  0.9331044
    ## horsepower   -0.7784268  0.8429834    0.8972570  1.0000000  0.8645377
    ## weight       -0.8317389  0.8970169    0.9331044  0.8645377  1.0000000
    ## acceleration  0.4222974 -0.5040606   -0.5441618 -0.6891955 -0.4195023
    ## year          0.5814695 -0.3467172   -0.3698041 -0.4163615 -0.3079004
    ## origin        0.5636979 -0.5649716   -0.6106643 -0.4551715 -0.5812652
    ##              acceleration       year     origin
    ## mpg             0.4222974  0.5814695  0.5636979
    ## cylinders      -0.5040606 -0.3467172 -0.5649716
    ## displacement   -0.5441618 -0.3698041 -0.6106643
    ## horsepower     -0.6891955 -0.4163615 -0.4551715
    ## weight         -0.4195023 -0.3079004 -0.5812652
    ## acceleration    1.0000000  0.2829009  0.2100836
    ## year            0.2829009  1.0000000  0.1843141
    ## origin          0.2100836  0.1843141  1.0000000

Question 1d):

``` r
fit <-lm(auto$mpg~auto$cylinders+auto$displacement+auto$horsepower+auto$weight+auto$acceleration+auto$year+auto$origin)
print(summary(fit))
```

    ## 
    ## Call:
    ## lm(formula = auto$mpg ~ auto$cylinders + auto$displacement + 
    ##     auto$horsepower + auto$weight + auto$acceleration + auto$year + 
    ##     auto$origin)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -9.5903 -2.1565 -0.1169  1.8690 13.0604 
    ## 
    ## Coefficients:
    ##                     Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)       -17.218435   4.644294  -3.707  0.00024 ***
    ## auto$cylinders     -0.493376   0.323282  -1.526  0.12780    
    ## auto$displacement   0.019896   0.007515   2.647  0.00844 ** 
    ## auto$horsepower    -0.016951   0.013787  -1.230  0.21963    
    ## auto$weight        -0.006474   0.000652  -9.929  < 2e-16 ***
    ## auto$acceleration   0.080576   0.098845   0.815  0.41548    
    ## auto$year           0.750773   0.050973  14.729  < 2e-16 ***
    ## auto$origin         1.426141   0.278136   5.127 4.67e-07 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 3.328 on 384 degrees of freedom
    ##   (5 observations deleted due to missingness)
    ## Multiple R-squared:  0.8215, Adjusted R-squared:  0.8182 
    ## F-statistic: 252.4 on 7 and 384 DF,  p-value: < 2.2e-16

1d i) Weight, year, origin and displacement are statistically significant at the 1% signifiance level.

1d ii) Cylinders, horsepower, acceleration are not significant at the 10% significance level.

1d iii) A change in one unit of the year variable - 1 year - corresponds with a 0.75 change in miles per gallon, given that all other variables are controlled for. Question 1e) According to the scatterplot matrix, it looks like acceleration, horsepower and displacement may have a non-linear relationship with mpg.

1e i)

``` r
acc2<-auto$acceleration^2
hors2<-auto$horsepower^2
displacement2<-auto$displacement^2
fit2 <-lm(auto$mpg~auto$cylinders+displacement2+hors2+auto$weight+acc2+auto$year+auto$origin+auto$acceleration+auto$horsepower+auto$displacement)
print(summary(fit2))
```

    ## 
    ## Call:
    ## lm(formula = auto$mpg ~ auto$cylinders + displacement2 + hors2 + 
    ##     auto$weight + acc2 + auto$year + auto$origin + auto$acceleration + 
    ##     auto$horsepower + auto$displacement)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -9.5788 -1.5511 -0.0461  1.5622 11.9010 
    ## 
    ## Coefficients:
    ##                     Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)        6.985e+00  6.004e+00   1.163   0.2454    
    ## auto$cylinders     7.388e-01  3.099e-01   2.384   0.0176 *  
    ## displacement2      1.164e-04  2.847e-05   4.090 5.27e-05 ***
    ## hors2              5.802e-04  1.369e-04   4.237 2.85e-05 ***
    ## auto$weight       -2.925e-03  6.695e-04  -4.368 1.62e-05 ***
    ## acc2               3.306e-02  1.566e-02   2.111   0.0354 *  
    ## auto$year          7.495e-01  4.483e-02  16.716  < 2e-16 ***
    ## auto$origin        5.737e-01  2.683e-01   2.138   0.0332 *  
    ## auto$acceleration -1.352e+00  5.378e-01  -2.514   0.0124 *  
    ## auto$horsepower   -2.221e-01  3.939e-02  -5.638 3.36e-08 ***
    ## auto$displacement -6.999e-02  1.616e-02  -4.332 1.90e-05 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 2.919 on 381 degrees of freedom
    ##   (5 observations deleted due to missingness)
    ## Multiple R-squared:  0.8637, Adjusted R-squared:  0.8602 
    ## F-statistic: 241.5 on 10 and 381 DF,  p-value: < 2.2e-16

1e ii) The adjusted R Square term is 0.8602. This is greater than the initial adjusted R Square term of 0.8182 obtained from the model without square terms.

1e iii) Both displacement and its squared term have coefficients that are statistically significant at a level of 1%. Furthermore, the coefficient value went from being positive to negative of the displacement coeffiecient.

Question 1 f)

``` r
new_df<-data.frame(c(6,200,100,3100, 15.1,1999,1))
predict.lm(fit2, new_df) #fix the predicition part
```

    ## Warning: 'newdata' had 7 rows but variables found have 397 rows

    ##         1         2         3         4         5         6         7 
    ## 14.639453 12.870394 14.267373 13.650758 15.053326 13.192606 15.147593 
    ##         8         9        10        11        12        13        14 
    ## 15.028486 14.432427 14.726152 14.579904 15.655590 15.442992 18.348867 
    ##        15        16        17        18        19        20        21 
    ## 22.061928 18.000170 17.927565 19.693763 24.498205 29.681307 20.981266 
    ##        22        23        24        25        26        27        28 
    ## 22.346951 21.188408 20.831136 19.263087  8.946616  8.566427  9.351586 
    ##        29        30        31        32        33        34        35 
    ##  6.625061 25.247681 21.287382 23.625728        NA 19.133412 15.356422 
    ##        36        37        38        39        40        41        42 
    ## 15.826649 17.261877 16.196361 11.823142 11.982548 11.683579 11.969554 
    ##        43        44        45        46        47        48        49 
    ## 10.105943 10.979931  9.717836 16.596980 22.432493 16.135894 18.098714 
    ##        50        51        52        53        54        55        56 
    ## 23.171733 23.802937 26.937232 26.823504 29.569962 29.535871 28.254423 
    ##        57        58        59        60        61        62        63 
    ## 26.079683 23.664048 25.058512 28.950359 20.836533 23.044787 12.382501 
    ##        64        65        66        67        68        69        70 
    ## 12.675612 12.367067 12.744071 14.738141 13.314407 11.316767 11.254605 
    ##        71        72        73        74        75        76        77 
    ## 12.141432 25.431571 13.536232 13.416389 11.463926 12.315349 19.458631 
    ##        78        79        80        81        82        83        84 
    ## 23.790695 20.892792 26.816496 22.689195 24.288148 22.835788 25.511673 
    ##        85        86        87        88        89        90        91 
    ## 25.430866 12.867160 15.487618 14.287974 13.649964 14.655972 12.692306 
    ##        92        93        94        95        96        97        98 
    ## 14.032523 12.600810 12.392008 14.271696 14.484753 14.926732 17.491532 
    ##        99       100       101       102       103       104       105 
    ## 16.863840 18.543310 19.288766 19.885688 31.603423 11.488925 11.819685 
    ##       106       107       108       109       110       111       112 
    ## 11.483114 11.873870 19.326614 25.211146 23.912381 24.157903 27.578788 
    ##       113       114       115       116       117       118       119 
    ## 23.281886 21.853111 25.133039 14.013034 16.048728 32.837387 26.530080 
    ##       120       121       122       123       124       125       126 
    ## 23.928709 20.038148 16.624025 21.398031 20.869764 15.178602 19.917319 
    ##       127       128       129       130       131       132       133 
    ##        NA 19.421482 17.638458 30.589438 24.640347 31.575141 24.202016 
    ##       134       135       136       137       138       139       140 
    ## 16.336877 15.488520 16.801959 14.130547 12.039036 12.924204 11.956714 
    ##       141       142       143       144       145       146       147 
    ## 12.689009 26.575166 30.717294 27.683006 34.367091 31.116876 28.358670 
    ##       148       149       150       151       152       153       154 
    ## 28.622035 27.587078 24.196162 25.279844 30.453827 19.771536 17.773281 
    ##       155       156       157       158       159       160       161 
    ## 21.149216 21.970081 14.493461 14.005618 13.127563 13.447581 15.598683 
    ##       162       163       164       165       166       167       168 
    ## 15.963889 15.822690 17.663308 19.107853 20.277081 19.433969 29.268172 
    ##       169       170       171       172       173       174       175 
    ## 23.624370 20.132935 24.137884 24.481364 29.290738 24.236089 22.174453 
    ##       176       177       178       179       180       181       182 
    ## 31.126421 20.121948 24.206879 23.447999 23.075573 22.628395 33.542275 
    ##       183       184       185       186       187       188       189 
    ## 26.864220 27.414617 24.109006 27.642046 28.344059 15.874338 15.441998 
    ##       190       191       192       193       194       195       196 
    ## 17.622128 15.635365 20.255161 19.348121 23.064973 21.115157 32.715297 
    ##       197       198       199       200       201       202       203 
    ## 30.436888 31.791981 34.311561 18.440081 20.672953 17.434471 19.852553 
    ##       204       205       206       207       208       209       210 
    ## 32.599915 31.561629 29.952152 27.200948 22.010117 16.076082 22.959288 
    ##       211       212       213       214       215       216       217 
    ## 23.213325 18.226585 14.685802 16.865809 16.683497 16.255074 31.533986 
    ##       218       219       220       221       222       223       224 
    ## 28.765144 34.019433 25.704668 32.489617 17.574347 17.814610 16.264022 
    ##       225       226       227       228       229       230       231 
    ## 16.226230 18.494735 19.399774 19.250981 19.225069 17.354294 16.656966 
    ##       232       233       234       235       236       237       238 
    ## 16.333119 15.412372 30.984401 24.077145 30.005475 24.371230 31.366830 
    ##       239       240       241       242       243       244       245 
    ## 28.839505 32.316529 30.415720 26.142316 25.130472 26.186982 35.277448 
    ##       246       247       248       249       250       251       252 
    ## 33.224576 35.799514 32.546671 34.934615 21.336492 18.713095 19.417839 
    ##       253       254       255       256       257       258       259 
    ## 19.463145 22.364899 24.644081 25.470644 20.684483 22.329057 20.578773 
    ##       260       261       262       263       264       265       266 
    ## 24.087278 18.878625 18.996238 19.303091 17.389401 21.378917 17.472724 
    ##       267       268       269       270       271       272       273 
    ## 31.203853 26.951132 27.900041 30.340120 26.846870 22.579121 24.469722 
    ##       274       275       276       277       278       279       280 
    ## 27.518266 24.979615 22.557490 23.663782 20.352673 32.771897 32.384032 
    ##       281       282       283       284       285       286       287 
    ## 20.906711 24.773610 25.208330 22.736103 20.776797 18.882958 20.088624 
    ##       288       289       290       291       292       293       294 
    ## 19.201181 18.671500 16.400280 18.186030 20.208989 18.797170 34.068291 
    ##       295       296       297       298       299       300       301 
    ## 35.039926 31.714259 28.254616 24.322983 18.825036 27.374173 23.339262 
    ##       302       303       304       305       306       307       308 
    ## 32.434131 31.861463 34.099909 33.370214 25.543196 26.063065 24.873039 
    ##       309       310       311       312       313       314       315 
    ## 26.958906 32.777050 35.588642 32.815081 35.292086 26.130558 25.871056 
    ##       316       317       318       319       320       321       322 
    ## 24.669158 23.197819 32.052247 28.101239 30.535107 29.458265 32.489563 
    ##       323       324       325       326       327       328       329 
    ## 34.699031 24.661748 34.586145 36.499171 36.065998 30.305474 27.767288 
    ##       330       331       332       333       334       335       336 
    ## 36.167462        NA 33.753584 35.857943 25.790493 31.333059 29.000672 
    ##       337       338       339       340       341       342       343 
    ##        NA 32.354596 28.973783 27.759087 27.339106 26.909301 30.418708 
    ##       344       345       346       347       348       349       350 
    ## 38.098839 35.462558 37.882943 34.770720 35.715328 36.033284 35.571589 
    ##       351       352       353       354       355       356       357 
    ## 34.184807 34.290058 32.716336 33.535830        NA 33.743512 32.520086 
    ##       358       359       360       361       362       363       364 
    ## 28.866068 31.013546 26.919125 29.004580 27.150494 26.882728 22.238047 
    ##       365       366       367       368       369       370       371 
    ## 22.371339 25.906004 24.692642 29.125121 29.111747 29.913482 30.150388 
    ##       372       373       374       375       376       377       378 
    ## 29.529725 27.145821 27.273218 34.485267 35.717360 35.979232 35.272185 
    ##       379       380       381       382       383       384       385 
    ## 33.817885 32.375429 34.467970 34.242741 36.850354 36.614497 36.378117 
    ##       386       387       388       389       390       391       392 
    ## 25.291147 26.169976 28.151310 24.859188 29.281243 31.162496 26.646375 
    ##       393       394       395       396       397 
    ## 28.440692 37.391117 32.135898 29.938605 29.240363

Question 2

2 a)

``` r
knn<-data.frame(c(1,2,3,4,5,6))
knn$X1<-c(0,2,0,0,-1,1)
knn$X2<-c(3,0,1,1,0,1)
knn$X3<-c(0,0,3,2,1,1)
knn$Y<-c("Red", "Red", "Red", "Green", "Green", "Red")
knn$dist<-sqrt(knn$X1^2+knn$X2^2+knn$X3^2)
```

2 b) Since the distance is shortest to observation 4 (distance=1.414), I predict that the response variable will be green.

2 c) I will pick those values that correspond to the three closest neighbors to the origin point. This distance is shortest for observation 2 (distance=2), observation 5 (distance=1.414) and observation 6 (distance=1.732).

2 d) A K increases, the patterns of results become more linear. As such, if the Bayes decision boundary is extremely non-linear, a k-value smaller in magnitude will be better.

2 e)

``` r
pred<-c(1,1,1)
labels<-knn$Y
test_pred<-knn(knn[,2:4],pred,cl=labels,k=2)
```

Question 3)

``` r
auto$mpg_high<-0
auto$mpg_high[auto$mpg<median(auto$mpg)]<-0
auto$mpg_high[auto$mpg>median(auto$mpg)]<-1
```

Question 3a)

``` r
fit3<-glm(mpg_high~cylinders+displacement+horsepower+weight+acceleration+year+origin, family=binomial(link='logit'), data=auto)
```

Weight and year are both significant at a level of 10%.

Question 3b)

``` r
set.seed(10)
breakdata<-createDataPartition(auto$mpg, p=0.5, list=FALSE, times=1) 
train<-auto[breakdata,] 
test<-auto[-breakdata,]
```

Question 3c)

``` r
fit4<-glm(mpg_high~cylinders+displacement+horsepower+weight+acceleration+year+origin, family=binomial(link='logit'), data=train)
summary(fit4)
```

    ## 
    ## Call:
    ## glm(formula = mpg_high ~ cylinders + displacement + horsepower + 
    ##     weight + acceleration + year + origin, family = binomial(link = "logit"), 
    ##     data = train)
    ## 
    ## Deviance Residuals: 
    ##      Min        1Q    Median        3Q       Max  
    ## -2.39831  -0.12488  -0.00304   0.25372   2.23403  
    ## 
    ## Coefficients:
    ##                Estimate Std. Error z value Pr(>|z|)    
    ## (Intercept)  -22.636484   8.366129  -2.706  0.00682 ** 
    ## cylinders     -0.640609   0.590332  -1.085  0.27785    
    ## displacement   0.009321   0.017057   0.546  0.58476    
    ## horsepower    -0.014035   0.031119  -0.451  0.65199    
    ## weight        -0.004401   0.001584  -2.779  0.00546 ** 
    ## acceleration  -0.001086   0.171317  -0.006  0.99494    
    ## year           0.489362   0.109314   4.477 7.58e-06 ***
    ## origin         0.338258   0.430314   0.786  0.43182    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## (Dispersion parameter for binomial family taken to be 1)
    ## 
    ##     Null deviance: 272.851  on 196  degrees of freedom
    ## Residual deviance:  86.982  on 189  degrees of freedom
    ##   (2 observations deleted due to missingness)
    ## AIC: 102.98
    ## 
    ## Number of Fisher Scoring iterations: 7

``` r
predicted<-predict(fit4,test,type="response")
actual<-train$mpg_high
actual<-actual[-199]
print(confusion.matrix(actual, predicted))
```

    ## Warning in confusion.matrix(actual, predicted): 3 data points removed due
    ## to missing data

    ##     obs
    ## pred  0  1
    ##    0 70 28
    ##    1 33 64
    ## attr(,"class")
    ## [1] "confusion.matrix"

As the confusion matrix indicates, the model is equally good at classifyig both 0s and 1s. Therefore, it is equally good at classifying the presence or absence of a high mpg.
