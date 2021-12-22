import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington)
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
   
    while True:
        city = str(input('Enter a city (chicago, new york city, washington) : ')).lower()
        if city in ['chicago', 'washington', 'new york city']:
         break
        else:
            print('Invalid City')
              
    while True:
        month = str(input('Enter a month (All, January, February, March, April, June : ')).title()
        if month == 'January':
            break
        elif month == 'February':
            break
        elif month == 'March':
            break
        elif month == 'April':
            break
        elif month == 'May':
            break
        elif month == 'June':
            break       
        elif month == 'All':
            break
        else:
            print ("Invalid month.")
                         
    while True:
        day = str(input('Enter a day (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)? ')).capitalize()
        if day == 'Monday':
            break
        elif day == 'Tuesday':
            break
        elif day == 'Wednesday':
            break
        elif day == 'Thursday':
            break
        elif day == 'Friday':
            break
        elif day == 'Saturday':
            break
        elif day == 'Sunday':
            break
        elif day == 'All':
            break
        else:
            print ("Invalid day.")

    print('City: ' + city + ' Month: ' + month + ' Day: ' +day)
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

    # We create a Pandas DataFrame by passing it a dictionary of Pandas Series
    # We create a DataFrame

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name().str[:20]
    df['day_of_week']= df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'All':
        df = df[df['month'] == month]
    
    if day != 'All':
        df = df[df['day_of_week'] == day]    

    user_input = input('\nDo you want to retrieve 5 rows? (yes or no) : \n').lower()
    i = 0
    while user_input.lower() == 'yes':
        print(df.iloc[i+5])
        i += 5
        user_input = input('Do you want to retrieve 5 rows?  (yes or no) : \n').lower()
        if user_input.lower() != 'yes':
            break
            
    print(df)
    print('-'*40)
    return df     

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month = df['month'].mode()[0]
    print('The most common month is :', most_common_month)

    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is : ',most_common_day)

    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour :', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    commonly_used_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is : ", commonly_used_start_station)

    commonly_used_end_station = df['End Station'].mode()[0]    
    print("The most commonly used end station is : ", commonly_used_end_station)
   
    commonly_used_trip = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("The most frequent combination of start station and end station trip is : ", commonly_used_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum(skipna = True) / 3600
    print('The total travel time is :', total_travel_time.round(), 'hours.')

    mean_travel_time = df['Trip Duration'].mean(skipna = True) / 60
    print('The mean travel time:', mean_travel_time.round(), 'minutes.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    count_of_user_types = df['User Type'].value_counts(dropna=True)
    print('Total number of user types: \n', count_of_user_types)

    if 'Gender' in df.columns :
    
        count_of_gender = df['Gender'].value_counts(dropna=True)
        print('\nTotal number of gender: \n', count_of_gender)

    else:
        print("No gender data!")
        
    if 'Birth Year' in df.columns :        
        
        most_recent_birthyear = int(df['Birth Year'].max())
        print('The most recent birth year:', most_recent_birthyear)
        
        earliest_birthyear = int(df['Birth Year'].min())
        print('The earliest birth year:', earliest_birthyear)
        
        most_common_birthyear = int(df['Birth Year'].mode()[0])
        print('The most common birth year:', most_common_birthyear)

    else:
        print("No birth year data!")
        
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():

    try:
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

    except:
        print("No gender data in washington!")
    
if __name__ == "__main__":
	main()
