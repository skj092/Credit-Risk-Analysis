# Credit Risk Analysis

## What is Credit Risk Analysis

Credit risk analysis is a form of analysis performed by a credit analyst to determine a borrower's ability to meet their debt obligations. The purpose of credit analysis is to determine the creditworthiness of borrowers by quantifying the risk of loss that the lender is exposed to.

## Overview of the problem

In this project you will have to put yourself in the shoes of a loan issuer and manage credit risk by using the past data and deciding whom to give the loan to in the future. The text files contain complete loan data for all loans issued by Lending Club through 2007-2015. The data contains the indicator of default, payment information, credit history, etc.

The data should be divided into train (June 2007 - May 2015) and out-of-time test (June 2015 - Dec 2015) data. You will have to use the training data to build models/analytical solutions and finally apply it to test data to measure the performance and robustness of the models.

## A short primer of underwriting in the credit industry -

In general, whenever an individual/corporation applies for a loan from a bank (or any loan issuer), their credit history undergoes a rigorous check to ensure that whether they are capable enough to pay off the loan (in this industry it is referred to as credit-worthiness).

The issuers have a set of model/s and rule/s in place which take information regarding their current financial standing, previous credit history and some other variables as input and output a metric which gives a measure of the risk that the issuer will potentially take on issuing the loan. The measure is generally in the form of a probability and is the risk that the person will default on their loan (called the probability of default) in the future.
Based on the amount of risk that the issuer is willing to take (plus some other factors) they decide on a cutoff of that score and use it to take a decision regarding whether to pass the loan or not. This is a way of managing credit risk. The whole process collectively is referred to as underwriting.


## Aim :
Our goal in this project is to analyze the data.

## Analysis Reports

**Purpose of the loan :**

![Loan Purpose](/images/purpose.png)

* Debt Consolidation stands as clear winner for loan purpose, with more than 350K loans — or 58% from the total.

Other highlights include:

* Credit Card  — more than 130K (~20%)
* Home Improvement — more than 135K (~6%)
* Other Purposes — less than 30K (~4%)

**Loan issued by regions :**
![Regions](/images/region.png)

Steady rise in loans issued from 2012 till mid of 2014,since then there have been fluctuations. Most loans where issued in south east region followed by west and north east

**Income Category**

![Income Category](/images/incomecategory.png)

* 10k was the loan amount that was issued mostly in the low income category. While 35k was the loan amount that was issued mostly in medium and high income category.

* Defaulters were mostly from low income category as compared to the other two.

* Employment length for low income category is between 3-10years while it is 4-10 years for medium and high income category.

* Interest rate low income category is slightly higher than medium and high income category because they might take longer time to pay and also they are higher risk.

**Yearwise Loan**

![Yearwise Loan](/images/yearwise.png)
* 92.29% of the loans were good loans 7.71% of the loans were bad loans. 2014 and 2015 were the best years as the non-defaulters were way more that the defaulters.

**Clustering Report**

![Similar Fields](/images/cluster.png)
