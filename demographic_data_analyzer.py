import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")  

    # How many of each race are represented in this dataset?
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # People with and without advanced education
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])].shape[0]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])].shape[0]

    # Percentage of people with higher education earning >50K
    higher_education_rich = round(
        (df[(df["education"].isin(["Bachelors", "Masters", "Doctorate"])) & (df["salary"] == ">50K")].shape[0] / higher_education) * 100, 1
    )

    # Percentage of people without higher education earning >50K
    lower_education_rich = round(
        (df[(~df["education"].isin(["Bachelors", "Masters", "Doctorate"])) & (df["salary"] == ">50K")].shape[0] / lower_education) * 100, 1
    )

    # Minimum work hours per week
    min_work_hours = df["hours-per-week"].min()

    # Number of people who work the minimum hours and earn >50K
    num_min_workers = df[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")].shape[0]
    high_income = df[df["hours-per-week"] == min_work_hours].shape[0]

    # Percentage of rich among those who work the minimum hours
    rich_percentage = round((num_min_workers / high_income) * 100, 2)

    # Country with highest percentage of people earning >50K
    highest_earning_country_percentage = (
        df[df["salary"] == ">50K"]["native-country"].value_counts() / df["native-country"].value_counts() * 100
    ).round(1)

    highest_earning_country = highest_earning_country_percentage.idxmax()

    # Most popular occupation for those earning >50K in India
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage.max()}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage.max(),
        'top_IN_occupation': top_IN_occupation
    }
