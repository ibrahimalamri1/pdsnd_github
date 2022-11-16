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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Provide the name of the city: ')
        city = city.lower()
        if city not in ('chicago' , ' new york city' , 'washington' , 'new york city'):
            print('False!, the options are (chicago, new york city, washington)')
            continue 
        else:
            break
        

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Provide the month: ')
        month = month.lower()
        if month not in ('january' , 'february' , 'march' , 'april' , 'may' , 'all'):
            print('False!, please type the month correctly')
            continue 
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Provide the day: ')
        day = day.lower()
        if day not in ('saturday' , 'sunday' , 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday', 'all'):
            print('False!, (please type the day correctly)')
            continue 
        else:
            break


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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ('january' , 'february' , 'march' , 'april' , 'may')
        month = months.index(month) + 1
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('most common month: ' , popular_month)
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('most common day of week: ' , popular_day)
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('most common hour: ' , popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    
    print('most commonly used start station is: ',start_station)
    
    # TO DO: display most commonly used end station
    
    end_station = df['End Station'].value_counts().idxmax()
    
    print('the most common used end station is: ',end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    
    station_combo = df.groupby(['Start Station', 'End Station']).count()
    
    print('most commonly used combination os stations is: ',start_station,'and', end_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time is: ', total_travel_time/2629746,'Months')
    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('average travel time is: ', average_travel_time/60,'Mins')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    
    print('user typs: ' ,user_type)
    
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('gender count :', gender)
    except Exception:
        print('Sorry! gender data is unavilable for this city :)')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        print('earliest year of birth is:',earliest)
        most_recent = df['Birth Year'].max()
        print('most recent year of birth is:',most_recent)
        most_common = df['Birth Year'].value_counts().idxmax()
        print('most common year of birth is:', most_common)
    except Exception:
        print('Sorry! data is unavilable for this city :)')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
    
    

def raw_data(df):
    print('would like to check out the raw data?')
    runs = 0
    ask_user = input('type yes to see 5 rows of raw data, type no to pass..' ).lower()
    if ask_user not in ['yes','no']:
        print('check your spelling :)')
    elif ask_user == 'no':
        print('very well, take care. :)')
    
    
    else:
        while runs+5 < df.shape[0]:
            print(df.iloc[runs:runs+5])
            runs += 5
            ask_user = input('type yes to see 5 more rows of raw data, type no to pass..' ).lower()
            if ask_user == 'no':
                  print('very well, take care. :)')
                  break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

