# demographic_data_analyzer.py

import pandas as pd

def load_data():
    # Load the dataset into a DataFrame
    df = pd.read_csv("adult.data.csv", header=None, 
                     names=["age", "workclass", "fnlwgt", "education", "education-num", 
                            "marital-status", "occupation", "relationship", "race", 
                            "sex", "capital-gain", "capital-loss", "hours-per-week", 
                            "native-country", "salary"])
    return df

def demographic_data_analyzer():
    df = load_data()

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make >50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[advanced_education]['salary'] == '>50K').mean() * 100, 1)

    # 5. What percentage of people without advanced education make more than 50K?
    lower_education_rich = round((df[~advanced_education]['salary'] == '>50K').mean() * 100, 1)

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary >50K?
    min_hours_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers_percentage = round((min_hours_workers['salary'] == '>50K').mean() * 100, 1)

    # 8. What country has the highest percentage of people that earn >50K?
    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_country = df['native-country'].value_counts()
    highest_earning_country = (country_earnings / total_country * 100).idxmax()
    highest_earning_country_percentage = round((country_earnings / total_country * 100).max(), 1)

    # 9. Identify the most popular occupation for those who earn >50K in India.
    india_occupations = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_occupations['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_min_workers_percentage': rich_min_workers_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
