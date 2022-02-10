import time
import pandas as pd
import numpy as np

CITY_DATA = { "chicago": "chicago.csv",
              "new york city": "new_york_city.csv",
              "washington": "washington.csv" }


Cities = ['chicago', 'new york', 'washington']

Months = ['january', 'february', 'march', 'april', 'may', 'june']

Days = ['monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' , 'sunday' ]

def get_user_input(text, userlist):
    while True:
        data = input(text).lower()
        if data in userlist:
            break
        if data == 'all':
            break

    return data


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
       city = input('which city do you want to explore chicago, new york or washington? \n').lower()
       if city in Cities:
           break



    month = get_user_input("write a month \n"
                           "or just type 'all' to continue without a filter. \n(all, january, february, march, april, may, june) \n> ", Months)



    day = get_user_input("write a day \n"
                    "or just type 'all' to continue without a filter. \n( monday, tuesday ... sunday) \n> ", Days)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour


    if month != 'all':
        month =  Months.index(month) + 1
        df = df[ df['month'] == month ]


    if day != 'all':
        df = df[ df['day_of_week'] == day ]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month = df['month'].value_counts()
    print("The most common month is :", most_common_month)

    most_common_day_of_week = df['day_of_week'].value_counts()
    print("The most common day of week is :", most_common_day_of_week)


    most_common_start_hour = df['hour'].value_counts()
    print("The most common start hour is :", most_common_start_hour)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_commonly_used_start_station = df['Start Station'].value_counts()
    print("The most commonly used start station :", most_commonly_used_start_station)


    most_commonly_used_end_start_station = df['End Station'].value_counts()
    print("The most commonly used end station :", most_commonly_used_end_start_station)


    most_frequent_combination = df['Start Station', 'End Station'].mode
    print("The most commonly used start station and end station : {}, {}".format(most_common_start_end_station[0],     most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time :", total_travel_time)


    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel_time)


    max_travel_time = df['Trip Duration'].max()
    print("Max travel time :", max_travel_time)

    print("Travel time for each user type:\n")
    group_user_trip = df.groupby(['User Type'])['Trip Duration'].sum()
    for i, user_trip in enumerate(group_user_trip):
        print("  {}: {}".format(group_user_trip.index[i], user_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_count = df['User Type'].value_counts()

    for i, user_c in enumerate(user_count):
        print("  {}: {}".format(user_count.index[i], user_c))

    print()

    if 'Gender' in df.columns:
        user_stats_gender(df)

    if 'Birth Year' in df.columns:
        user_stats_birth(df)



def user_birth(df):


    birth_year = df['Birth Year']

    most_common_year = birth_year.value_counts().idxmax()
    print("The most common birth year:", most_common_year)

    most_recent = birth_year.max()
    print("The most recent birth year:", most_recent)

    earliest_year = birth_year.min()
    print("The most earliest birth year:", earliest_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

# bikeshare script 
