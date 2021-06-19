import time
import pandas as pd
import numpy as np
from tabulate import tabulate

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # city = input(
    #

    while True:
        city = input("\nPlease select one city of these: Chicago, New York city, or Washington',\
that you want to view its data\n").lower()
        if city not in CITY_DATA:
            print("\nIncorrect City!")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(
        "\nPlease select a month between January to June, or all:\n").lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june','all']:
            print("\nIncorrect Month!")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nFor Which day of a week, or enter all: \n").lower()
        if day not in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']:
            print("\nIncorrect Day!")
            continue
        else:
            break

    print('-'*40)
    print(f"You Select {city.title()}, for {month} Month and {day} Day")
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
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    print(f"The most common month is {df['Month'].mode()[0]}")

    # display the most common day of week
    print(f"The most common day of week is {df['Day of Week'].mode()[0]}")

    # display the most common start hour
    print(f"The most common start hour is {df['Hour'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(f"The most commonly used start station is {df['Start Station'].mode()[0]}")

    # display most commonly used end station
    print(f"The most commonly used End station is {df['End Station'].mode()[0]}")

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    print(f"The frequent combination of start and end station trip is {df['combination'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(f"The total travel time is {df['Trip Duration'].sum()}")
    # display mean travel time
    print(f"The mean travel time is {df['Trip Duration'].mean()}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(f"The  counts of user types\n{df['User Type'].value_counts()}")
    # Display counts of gender
    if 'Gender' in df:
        print(f"The counts of gender is\n{df['Gender'].value_counts()}")
    else:
        print("Sorry, there's no gender information for selected city.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print(f"The earliest year is {df['Birth Year'].min()}")
        print(f"The recent year is {df['Birth Year'].max()}")
        print(f"The most common year is {df['Birth Year'].mode()}")
    else:
        print("Sorry, there's no Birth Year information for selected city.")
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if display_data.lower() == 'yes':
            print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
    main()
