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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    month = 'all'
    day = 'all'

    while True:
        city_input = input("First, please enter the city name you would like to analyze! Options include 'chicago','new york city', or 'washington': ")
        city = city_input.lower()
        if city == 'chicago'or city == 'new york city' or city =='washington':
            print('Valid input: ' + city + '. Got it!')
            break
        else:
            print('Oops, your input was invalid. Try again!')

    while True:
        filter_option = input("Would you like to filter by 'month', 'day', or 'none'?: ")
        filter = filter_option.lower()   
        if filter == 'month':
            while True:  
                month_input = input("Filtering by month, please enter the month you would like to analyze. Options include 'january', 'february', 'march', 'april', 'may', 'june' or 'all': ")
                month = month_input.lower()
                if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':
                    print('Valid input: ' + month + '. Got it!')
                    break
                else:
                    print('Oops, your input was invalid. Try again!')
        elif filter == 'day':
            while True:
                day_input = input("Filtering by day, please enter the weekday you would like to analyze. Options include 'monday', 'tuesday', 'wednesday', 'thursday','friday','saturday','sunday' or 'all': ")
                day = day_input.lower() 
                if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all':
                    print('Valid input: ' + day + '. Got it!')   
                    break    
                else:
                    print('Oops, your input was invalid. Try again!')
        elif filter == 'none':
            print("No filters will be applied.")
        else:
            print('Oops, your input was invalid. Try again!')
            continue     

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
    df['day_of_week'] = df['Start Time'].dt.strftime('%A').str.lower()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]
    df['hour'] = df['Start Time'].dt.hour


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)
      
    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', common_day.title())

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular start station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular end station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    popular_journey = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('Most popular journey:', popular_journey)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time, 'seconds')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Type Count:', user_types)


    # Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print('Gender Count:', counts_of_gender)
    except:
        print('Gender Count: Apologies, information for the selected city is not available.')
            

    # Display earliest, most recent, and most common year of birth
    try:
        oldest_rider_birth_year = df['Birth Year'].min()
        print('Oldest Rider Birth Year:', oldest_rider_birth_year)
    except:
        print('Oldest Rider Birth Year: Apologies, information for the selected city is not available.')

    try:
        youngest_rider_birth_year = df['Birth Year'].max()
        print('Youngest Rider Birth Year:', youngest_rider_birth_year)
    except:
        print('Youngest Rider Birth Year: Apologies, information for the selected city is not available.')

    try:
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year:', most_common_birth_year)
    except:
        print('Most Common Birth Year: Apologies, information for the selected city is not available.')

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

        #This asks the user if they would like detail from the source file.

        while True:
            individual_trip_data_input = input("Would you like to see individual trip data? Please type 'yes' or 'no': ")
            individual_trip_data = individual_trip_data_input.lower()
            if  individual_trip_data == 'yes':
                for x in range(5,1000000000000,5):
                    print(df.head(x))
                    more_information = input("Would you like to see an additional 5 lines of trip data? Please type 'yes' or 'no': ")
                    if more_information == 'yes':
                        print(df.head(x))
                    elif more_information != 'yes':
                        print("Got it! No more data.")
                        break
                break
            elif individual_trip_data == 'no':
                print('Got it!')
                break
            else:
                print('Oops, your input was invalid. Try again!')
         
        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                print("You are done with this analysis!")
                exit() 
            else:
                print("Let's go!")
                break
            
if __name__ == "__main__":
    main()
    




