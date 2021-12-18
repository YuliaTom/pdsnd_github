import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
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

    while True:
        city = input('Please enter one of the following cities: Chicago, New York or Washington:\n').lower()
        if city not in list(CITY_DATA.keys()):
            print('Not a valid city name. Please try again.')
        else:
            break
    while True:
        month = input('To filter by month please enter month (January - June) or type \"all\":\n').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        if month.lower() not in months:
            print('Not a valid month input. Please try again.')
        else:
            break
    while True:
        day = input('To filter by day of week please enter any day of week or type \"all\":\n').lower()
        days = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'}
        if day not in days:
            print('Not a valid day input. Please try again.')
        else:
            break
    print('-' * 40)
    if month == 'all' and day == 'all':
        print('Here is the data for {}.'.format(city.title()))
    elif month == 'all' and day != 'all':
        print('Here is the data for {} filtered by the day of week - {}.'.format(city.title(), day.title()))
    elif month != 'all' and day == 'all':
        print('Here is the data for {} for the month of {}.'.format(city.title(), month.title()))
    else:
        print('Here is the data for {} for the month of {} filtered by day of week - {}.'.format(city.title(),
                                                                                                 month.title(),
                                                                                                 day.title()))

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
    df['Day of Week'] = df['Start Time'].dt.strftime('%A')
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                  'november', 'december']
        month = months.index(month) + 1
        df = df[df['Month'] == month]
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    pop_month = df['Start Time'].dt.strftime('%B').mode()[0]
    # TO DO: display the most common day of week
    pop_day = df['Start Time'].dt.strftime('%A').mode()[0]
    # TO DO: display the most common start hour
    pop_hour = df['Start Time'].dt.hour.mode()[0]
    print(' - The most popular hour is {} o\'clock.'.format(pop_hour))
    print(' - The most common day of week is {}.'.format(pop_day))
    print(' - The most popular month is {}.'.format(pop_month))
    print("\nThis took %s seconds." % (time.time() - start_time).__round__(5))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    pop_start_station = df['Start Station'].mode()[0]
    print(' - {} is the most commonly used start station(s).'.format(pop_start_station))
    pop_end_station = df['End Station'].mode()[0]
    print(' - {} is the most commonly used end station(s).'.format(pop_end_station))
    print("\nThis took %s seconds." % (time.time() - start_time).__round__(5))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = int(df['Trip Duration'].sum() / 60)
    print(' - The total duration of travel is {} minutes.'.format(total_travel.__round__(2)))
    # TO DO: display mean travel time
    mean_travel = int(df['Trip Duration'].mean() / 60)
    print(' - The average duration of travel is {} minutes.'.format(mean_travel.__round__(2)))
    print("\nThis took %s seconds." % (time.time() - start_time).__round__(5))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('\n - There are the following user types and their numbers:\n{}\n'.format(user_type_count.to_string()))
    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\n - The breakdown by gender is:\n{}\n'.format(gender_count.to_string()))
    except:
        print(' - Unfortunately, there is no user gender and DOB data for the city of Washington.')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('\n - The oldest user was born in {}.'.format(int(earliest_year)))
        recent_year = df['Birth Year'].max()
        print(' - The youngest user was born in {}.'.format(int(recent_year)))
        common_year = df['Birth Year'].mode()[0]
        print(' - The most common year of birth of the users is {}.'.format(int(common_year)))
    except:
        print(' ')
    print("\nThis took %s seconds." % (time.time() - start_time).__round__(5))
    print('-' * 40)


def top_data(df):
    """Displays top 5 longest and shortest bikeshare trips."""

    while True:
        top_data_launch = input('\nWould you like to see top 5 longest and shortest trips?\n').lower()
        if top_data_launch in ['no', 'n']:
            break
        elif top_data_launch in ['yes', 'ye', 'y', 'ok']:
            start_time = time.time()
            print('\nCalculating Individual Trip Data...\n')
            print(' - The top 5 longest trips are: \n')
            df_top_five = df.drop('Unnamed: 0', axis=1).sort_values(by=['Trip Duration'],
                                                                    ascending=False).head().to_string(index=False)
            print(df_top_five)
            print('\n - The top 5 shortest trips are: \n')
            df_bottom_five = df.drop('Unnamed: 0', axis=1).sort_values(by=['Trip Duration'],
                                                                       ascending=False).tail().to_string(index=False)
            print(df_bottom_five)
            print("\nThis took %s seconds." % (time.time() - start_time).__round__(5))
            print('-' * 40)
            break
        else:
            print('Not a valid input. Please type \"yes\"/\"y\" or \"no\"/\"n\".')


def raw_data(df):
    """Displays raw data on bikeshare users."""

    while True:
        raw_data_launch = input('\nWould you like to see the raw data for 5 individual trips?\n')
        if raw_data_launch in ['no', 'n']:
            break
        elif raw_data_launch not in ['yes', 'ye', 'y', 'ok']:
            print('Not a valid input. Please type \"yes\"/\"y\" or \"no\"/\"n\".')
        else:
            print('\nCalculating 5 Individual Trips Raw Data...\n')

            def chunker(iterable, size=5):
                for i in range(0, len(iterable), size):
                    yield iterable[i: i + size]

            for chunk in chunker(df.index.values):
                rows = df.iloc[chunk].to_string()
                print(rows)
                checking = input('\nWould you like to see 5 more individual trips?\n')
                if checking not in ['yes', 'ye', 'y', 'ok']:
                    break
                else:
                    continue
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        top_data(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() not in ['yes', 'ye', 'y']:
            print('Thanks for using the script!!!\nGood bye!')
            break


if __name__ == "__main__":
    main()
