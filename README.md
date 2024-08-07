# EG7_2401FTDS_Unsupervised_Learning_Project_Streamlit

# Anime Recommender System Project


![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white) [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](URL_TO_YOUR_APP)

<div id="main image" align="center">
  <img src="https://github.com/PrishaniK/EG7_2401FTDS_Unsupervised_Learning_Project_main/blob/main/Home_banner.jpg" width="950" height="500" alt=""/>
</div>

## Table of contents
* [1. Project Overview](#project-description)
* [2. Dataset](#dataset)
* [3. Packages](#packages)
* [4. Environment](#environment)
* [5. MLFlow](#mlflow)
* [6. Streamlit](#streamlit)
* [7. Team Members](#team-members)

## 1. Project Overview <a class="anchor" id="project-description"></a>

In today’s technology-driven world, recommender systems are socially and economically critical for ensuring that individuals can make appropriate choices surrounding the content they engage with on a daily basis. One application where this is especially true surrounds movie content recommendations; where intelligent algorithms can help viewers find great titles from tens of thousands of options.

…ever wondered how Netflix, Amazon Prime, Showmax, Disney and the likes somehow know what to recommend to you?

Well, you are about to find out! In this project, we require you to use all your skills to build a collaborative and content-based recommender system for a collection of anime titles, capable of accurately predicting how a user will rate an anime title they have not yet viewed, based on their historical preferences. 


## 2. Dataset <a class="anchor" id="dataset"></a>
#### Data Overview

This dataset contains information on anime content (movies, television series, music, specials, OVA, and ONA*), split between a file related to the titles (`anime.csv`) and one related to user ratings of the titles (`training.csv`). The `test.csv` file will be used to create the rating predictions and must be submitted for grading.

*OVA: Original Video Animation - anime film / series made for release in home-video formats, ONA: Original Net Animation is an anime that is directly released onto the Internet.
#### Supplied files:

  - **anime.csv:** This file contains information about the anime content, including aspects such as the id, name, genre, type, number of episodes (if applicable), an average rating based on views, and the number of members in the anime 'group'.
  - **train.csv:** This file contains rating data, supplied by individual users for individual anime titles. It contains user_id information, the anime_id of the title watched, and the rating given (if applicable).
  - **test.csv:** This file will be used to create the final submission. It contains a user_id and an anime_id column only - no rating (that's your task!). These ids will be used to create the rating predictions.


#### Detailed file description:

**Anime.csv**

  - anime_id - myanimelist.net's unique id identifying an anime.
  - name - full name of anime.
  - genre - comma-separated list of genres for this anime.
  - type - movie, TV, OVA, etc.
  - episodes - the number of episodes in the series. (1 if movie).
  - rating - average rating out of 10 for this anime.
  - members - number of community members that are in this anime's "group".

**train.csv**

  - user_id - non-identifiable randomly generated user id.
  - anime_id - the anime that this user has rated.
  - rating - rating out of 10 this user has assigned (-1 if the user watched it but didn't assign a rating).

**test.csv**

  - user_id - non-identifiable randomly generated user id.
  - anime_id - the anime that this user has rated.


## 3. Packages <a class="anchor" id="packages"></a>

To carry out all the objectives for this repo, the following necessary dependencies were loaded:

+ `pandas 2.2.2` - for data manipulation and analysis
+ `numpy 1.26` - for numerical operations and handling arrays
+ `seaborn 0.13.2` - for statistical data visualization
+ `matplotlib 3.8.4` - for plotting graphs and charts
+ `wordcloud 1.9.3` - for creating word clouds
+ `squarify 0.4.4` - for creating treemaps
+ `scikit-learn 1.2.2` - for various machine learning utilities
+ `scipy 1.13.1` - for scientific computations, including sparse matrix operations
+ `mlflow 2.6.0` - for experiment tracking



## 4. Environment <a class="anchor" id="environment"></a>

It's highly recommended to use a virtual environment for your projects, there are many ways to do this; we've outlined one such method below. Make sure to regularly update this section. This way, anyone who clones your repository will know exactly what steps to follow to prepare the necessary environment. The instructions provided here should enable a person to clone your repo and quickly get started.

### Create the new evironment - you only need to do this once

```bash
# create the conda environment
conda create --name <env>
```

### This is how you activate the virtual environment in a terminal and install the project dependencies

```bash
# activate the virtual environment
conda activate <env>
# install the pip package
conda install pip
# install the requirements for this project
pip install -r requirements.txt
```
## 5. MLFlow<a class="anchor" id="mlflow"></a>

MLOps, which stands for Machine Learning Operations, is a practice focused on managing and streamlining the lifecycle of machine learning models. The modern MLOps tool, MLflow is designed to facilitate collaboration on data projects, enabling teams to track experiments, manage models, and streamline deployment processes. For experimentation, testing, and reproducibility of the machine learning models in this project, you will use MLflow. MLflow will help track hyperparameter tuning by logging and comparing different model configurations. This allows you to easily identify and select the best-performing model based on the logged metrics.

- Please have a look here and follow the instructions: https://www.mlflow.org/docs/2.7.1/quickstart.html#quickstart

## 6. Streamlit<a class="anchor" id="streamlit"></a>

### What is Streamlit?

[Streamlit](https://www.streamlit.io/)  is a framework that acts as a web server with dynamic visuals, multiple responsive pages, and robust deployment of your models.

In its own words:
> Streamlit ... is the easiest way for data scientists and machine learning engineers to create beautiful, performant apps in only a few hours!  All in pure Python. All for free.

> It’s a simple and powerful app model that lets you build rich UIs incredibly quickly.

[Streamlit](https://www.streamlit.io/)  takes away much of the background work needed in order to get a platform which can deploy your models to clients and end users. Meaning that you get to focus on the important stuff (related to the data), and can largely ignore the rest. This will allow you to become a lot more productive.  

##### Description of files

For this repository, we are only concerned with a single file:

| File Name              | Description                       |
| :--------------------- | :--------------------             |
| `base_app.py`          | Streamlit application definition. |


#### 6.1 Running the Streamlit web app on your local machine

As a first step to becoming familiar with our web app's functioning, we recommend setting up a running instance on your own local machine. To do this, follow the steps below by running the given commands within a Git bash (Windows), or terminal (Mac/Linux):

- Ensure that you have the prerequisite Python libraries installed on your local machine:

 ```bash
 pip install -U streamlit numpy pandas scikit-learn
 ```

- Navigate to the base of your repo where your base_app.py is stored, and start the Streamlit app.

 ```bash
 cd EG7_2401FTDS_Unsupervised_Learning_Project/Streamlit/
 streamlit run base_app.py
 ```

 If the web server was able to initialise successfully, the following message should be displayed within your bash/terminal session:

```
  You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://192.168.43.41:8501
```
You should also be automatically directed to the base page of our web app. This should look something like:

<div id="s_image" align="center">
  <img src="https://github.com/PrishaniK/EG7_Unsupervised_Learning_Streamlit/blob/main/images/Home_anime_collage.jpg" width="850" height="400" alt=""/>
</div>

Congratulations!

#### 6.2 Deploying your Streamlit web app

- To deploy your app for all to see, click on `deploy`.
  
- Please note: If it's your first time deploying it will redirect you to set up an account first. Please follow the instructions.

## 7. Team Members<a class="anchor" id="team-members"></a>

| Name                                                                                        |  Email              
|---------------------------------------------------------------------------------------------|--------------------             
| [Clement Moshohlo Mphethi](https://github.com/HoOdpHarMxcisT)                                                | clementmphethi@gmail.com
| [Makhutjo Lehutjo](https://github.com/Makhutso98)                                                                                  | makhutjolehutjo8@gmail.com
| [Prishani Kisten](https://github.com/PrishaniK)                                                                            | prishanik135@gmail.com
| [Johannes Malefetsane](https://github.com/johannesmakgetha)                                                | makgethamj@gmail.com
