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

WEEK_DAYS = ['all', 'monday', 'tuesday', 'wedensday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (int) month - name of the month to filter by, or "all" to apply no month filter
        (int) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    while True:
        print('Which city do you want to analyze? Options are: ' + ', '.join(CITY_DATA))
        print(' ')
        city = input()
        if city.lower().strip() not in CITY_DATA.keys():
            print('\nUnavailable data. Please, check for typos.')
        else:
            break
    print('\nYou have selected ' + city.title() + '!')
    print('\t...Loading the database...')

    # get user input for month (all, january, february, ... , june)
    while True:
        print('\nInput month by its number, use 0 for loading all.')
        print(' ')
        try:
            month = int(input())
        except ValueError:
            print('\nPlease, enter a number between 0 and 6')
            continue
        if month not in MONTH_DIC.keys() or month > 6:
            print('\nMonth should be a number ranged from 1 to 6. Use 0 for loading all.')
        else:
            break
    print('\nYou have selected ' + MONTH_DIC[month].capitalize() + ' in ' + city.capitalize())

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('\nInput day of week by its number, use 0 for loading all')
        print(' ')
        try:
            day = int(input())
        except ValueError:
            print('\nPlease, enter a number between 0 and 7')
            continue
        if day not in range(len(WEEK_DAYS)):
            print('\nWeek day should be a number ranged from 1 to 7. Use 0 for loading all.')
        else:
            break
    print('\nYou have selected every ' + WEEK_DAYS[day].capitalize() +  ' of ' + MONTH_DIC[month].capitalize() + ' in ' + city.capitalize())
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (int) month - number of the month to filter by, or "all" to apply no month filter
        (int) day - number of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA.get(city), index_col= 0, parse_dates=['Start Time', 'End Time'])
    if month != 0:
        df = df[df['Start Time'].dt.month == month] # dt pandas date time index
    if day !=0:
        df = df[df['Start Time'].dt.dayofweek == day-1] # dayoftheweek starts on Monday = 0
    return df

def describe_data(df):
    # Shows a general insight about the selected data.

    print("\nDisplaying general insights")
    print('-'*40)
    start_time = time.time()
    
    # Sort the DataFrame by Start Time
    df = df.sort_values(by='Start Time', ascending=True)
    
    # Displays first & last entry
    print("\n    1. First Entry\n")
    print(df.head(1))
    print()
    print("\n    2. Last Entry\n")
    print(df.tail(1))
    print()
    
    # Displays general statistics
    print("\n    3. General Statistics\n")
    print(df.describe())
    
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    
    Usinge the mode of a distribution: value_counts() funtion and idxmax()
    instead of mode() to get only the value without type.
    
    """
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    mode_month = df['Start Time'].dt.month.value_counts().idxmax()
    print('During the selected range the most common month is...\n')
    print('    ' + MONTH_DIC[mode_month].capitalize())

    # display the most common day of week
    mode_day= df['Start Time'].dt.dayofweek.value_counts().idxmax()
    print('\nDuring the selected range the most common day of week is...\n')
    print('    ' + WEEK_DAYS[mode_day + 1].capitalize())

    # display the most common start hour
    mode_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('\nDuring the selected range the most common start hour is...\n')
    if int(mode_hour) < 12:
        print('    ' + str(mode_hour) + ' AM\n')
    else:
        print('    ' + str(mode_hour) + ' PM\n')

    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('During the selected range the most common Start Station is...\n')
    print('    ' + start_station)
    
    # display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('\nDuring the selected range the most common End Station is...\n')
    print('    ' + end_station)
    
    # display most frequent combination of start station and end station trip
    combi_station = df.value_counts(['Start Station', 'End Station']).idxmax()
    print('\nDuring the selected range the most common combination of ')
    print('Start and End stations is...\n')
    print('    ' + ', '.join([str(i) for i in combi_station]))
    
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # Empty dictionaries for total travel time & mean time
    travel_time = {}
    mean_time = {}
    
    # Calculate total travel time
    travel_time['seconds'] = round(df['Trip Duration'].sum(), 2)
    travel_time['minutes'] = round(travel_time['seconds'] / 60, 2)
    travel_time['hours'] = round(travel_time['minutes'] / 60, 2)
    
    # Display total travel time
    print('For the selected range the total travel time is...\n')
    print('-'* max(len(k) for k in travel_time))
    for k in travel_time.keys():
        print('{:<8} {:<8}'.format(k, travel_time[k]))
    print('-'* max(len(k) for k in travel_time))
    
    # Calculate mean travel time
    mean_time['seconds'] = round(df['Trip Duration'].mean(), 2)
    mean_time['minutes'] = round(mean_time['seconds'] / 60, 2)
    mean_time['hours'] = round(mean_time['minutes'] / 60, 2)
    
    # display mean travel time
    print('\nFor the selected range the mean travel time is...\n')
    print('-'* max(len(k) for k in mean_time))
    for k in mean_time.keys():
        print('{:<8} {:<8}'.format(k, mean_time[k]))
    print('-'* max(len(k) for k in mean_time))
    
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('For the selected range the counts of user types are...\n')
    count_types = df.groupby(['User Type'])['User Type'].count()
    print(count_types)

    # Check shape to know if there's data available
    if df.shape[1] < 7:
        print('\nNo data available regarding age nor gender.')
    else:
        # Display counts of gender
        print('\nFor the selected range the counts of gender are...\n')
   
        count_genders = df.groupby(['Gender'])['Gender'].count()
        print(count_genders)

        # Display earliest, most recent, and most common year of birth
        print('\nFor the selected range the year of birth data is...\n')
        oldest_user = df['Birth Year'].min()
        youngest_user = df['Birth Year'].max()
        mode_year = df.groupby(['Birth Year'])['Birth Year'].count().idxmax()
        print('The oldest user born in: ')
        print(oldest_user)
        print('The youngst user born in: ')
        print(youngest_user)
        print('The most common year of birth is: ')
        print(mode_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw(df):
    """
    Displays 5 rows of raw data as user command.
    """

    # Sort the DataFrame by Start Time
    df = df.sort_index(axis=0)
    
    # Start the counter:
    num = 0

    # Ask for input and loop the rows of data
    while num <= df.shape[0]:
        load = input('\nLoad 5 rows of raw data. Enter "y" to continue. Enter anything else to stop.\n')
        if load.lower().strip() != 'y':
            break
        print(df.iloc[0 + num:5 + num])
        num += 5
    if num >= df.shape[0]:
        print('OMG! Have you cycled the data till the end? Please replace the "y" key on your keyboard.')
       
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        func_dict = {describe_data : 'general insights',
                     time_stats : 'travel times', 
                     station_stats : 'station statistics', 
                     trip_duration_stats : 'trips duration',
                     user_stats : 'user',
                     raw: 'raw'}

        for k, f in func_dict.items():
            print('\nDo you want to visualize ' + f + ' data?')
            print('Enter "n" to jump to the next option. Enter any key to continue.\n')
            user_input = input()
            if user_input != 'n':
                k(df)
            else:
                continue

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower().strip() != 'yes':
            break

if __name__ == "__main__":
	main()