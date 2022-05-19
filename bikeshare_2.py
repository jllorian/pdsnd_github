import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DIC = { 0 :'all',
              1 :'january',
              2 :'february',
              3 :'march',
              4 :'april',
              5 :'may',
              6 :'june',
              7 :'july',
              8 :'august',
              9 :'september',
              10 :'october',
              11 :'november',
              12 :'december' }

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
    while True:
        print('Which city do you want to analyze? Options are: ' + ', '.join(CITY_DATA))
        print(' ')
        city = input()
        if city not in CITY_DATA.keys():
            print('\nUnavailable data. Please, check for typos.')
        else:
            break
    print('\nYou have selected ' + city.capitalize() + '!')
    print('\t...Loading the database...')

    # get user input for month (all, january, february, ... , june)
    while True:
        print('Input month by its number, use 0 for loading all.')
        print(' ')
        month = int(input())
        if month not in MONTH_DIC.keys():
            print('\nMonth should be a number ranged from 1 to 12. Use 0 for loading all.')
        else:
            break
    print('\nYou have selected ' + MONTH_DIC[month].capitalize() + ' in ' + city.capitalize())

    # get user input for day of week (all, monday, tuesday, ... sunday)
    WEEK_DAYS = ['all', 'monday', 'tuesday', 'wedensday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        print('Input day of week by its number, use 0 for loading all')
        print(' ')
        day = int(input())
        if day not in range(len(WEEK_DAYS)):
            print('\nWeek day should be a number ranged from 1 to 7. Use 0 for loading all.')
        else:
            break
    print('\nYou have selected ' + WEEK_DAYS[day].capitalize() +  ' of ' + MONTH_DIC[month].capitalize() + ' in ' + city.capitalize())

    # convert variables to str, return.
    print('-'*40)
    month = str(MONTH_DIC[month])
    day = str(WEEK_DAYS[day])
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
    df = pd.read_csv(CITY_DATA.get(city).index(''))
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


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
