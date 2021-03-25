import calendar as cln
import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input('Please choose a city from "chicago, new york, washington" \n').lower()
        if city not in CITY_DATA:
            print(' " Please choose a correct city name, like --> "chicago", "new york", or "washington"  ')
        else:
            break
    while True:
        month = input('" Please enter a month from " january to june, or type "all" to display all months : " \n').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month != "all" and month not in months:
            print(month)
        else:
            break
    while True:
        day = input('" Please enter a day of the week, or type "all" to display all days : " \n').lower()
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        if day != 'all' and day not in days:
            print(day)
        else:
            break

    print('_' * 40)
    return city, month, day

def load_data(city,month,day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df["Start Time"].dt.day_name()
    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_statist(df):
    print('\nCalculating The Most Frequent Times of Travel....\n')
    start_time = time.time()
    common_month =df['month'].mode()[0]
    print('" The most common month : "',  cln.month_name[common_month])

    day = df['day_of_week'].mode()[0]
    print(f'" The most common day of week is : "  {day}')

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'" The most common start hour is : " {popular_hour}')
    print("\nThis took %s seconds. " % (time.time() - start_time))
    print('_' * 40)

def station_stats_statistices(df):
    print('\nCalculating The Most Popular Stations and trip....\n')
    start_time = time.time()
    common_start_station=df['Start Station'].mode()[0]
    print('" The Most Commonly Station that Used as Start Station is : "',common_start_station)

    common_end_station=df['End Station'].mode()[0]
    print('" The Most Commonly Station that Used as End Station is : "',common_end_station)

    common_start_end=(df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('" The Most Frequent Combination of Start and End Stations : "', common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_' * 40)

def trip_duration_statistices(df):
    print('_'*40)
    print('\nCalculating Trip Duration.....\n')
    print('_' * 40)
    start_time = time.time()
    total_travel_duration = df['Trip Duration'].sum()
    print('" Total Travel Time: ', total_travel_duration, ' seconds, or ', total_travel_duration/3600, 'hours')
    avg_travel_duration=df['Trip Duration'].mean()
    print('" Average Travel Time:', avg_travel_duration, 'seconds, or ', avg_travel_duration/3600, 'hours')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_' * 40)

def user_statistices(df):
    print('\nCalculating User Stats.....\n')
    start_time = time.time()
    user_type= df['User Type'].value_counts()
    print('" Counts Of User Types:\n "', user_type)

    if  'Gender' in df:
        gender=df['Gender'].value_counts()
        print('\n Counts of Gender:\n', gender)
    else:
        print('" There is no gender information in this city."')
    if 'Birth_Year' in df:
        earliest_year =df['Birth_Year'].min()
        print('\n Earliest Year of Birth: \n'. earliest_year)
        recent_year =df['Birth_Year'].max()
        print('\n Recent Year of Birth: \n'. recent_year)
        common_year=df['Birth_Year'].mode()[0]
        print('\n Common Year of Birth: \n'. common_year)
    else:
        print('"There is no birth year information in this city." ')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_' * 40)

def display_dataset(df):
    a = 0
    display_data= input('would you like to display the first 5 rows of the data ? yes/no: ').lower()
    pd.set_option('display.max_columns',None)
    while True:
        if  display_data not in ['yes','no']:
            display_data=input("You entered a wrong choice, Please type 'Yes', or 'No'")
        elif display_data== 'no':
            break
        else:
            print(df[a:a+5])
            display_data=input('Would you like to display the next 5 rows of the data ? yes/no:').lower()
            a+=5


def main():
     while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_dataset(df)
        time_statist(df)
        station_stats_statistices(df)
        trip_duration_statistices(df)
        user_statistices(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if  restart not in ['yes', 'no']:
            display_data = input("You entered a wrong choice, Please type 'Yes', or 'No'")
        elif restart !=  'yes':
            break



if __name__ == "__main__":
    main()