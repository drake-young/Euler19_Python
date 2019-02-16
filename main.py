from timeit import default_timer


# ===========================================================
# FUNCTION: is_leap_year
# ===========================================================
#
# INPUT:    integer containing a year to be evaluated
#
# OUTPUT:   boolean. True if input year is a "leap year", false
#           otherwise
#
# TASK:     validate whether the given year is a leap year and
#           return the results
#
# NOTES:
#       *   Leap Years only occur on years that are multiples
#           of 4
#       *   However, leap years do not occur on years which are
#           also multiples of 100
#       *   However still, if the year is a multiple of 400, it
#           is a leap year, the previous point is disregarded,
#           and the year is a leap year
# ===========================================================
def is_leap_year( year ):
    return year % 4 is 0 and ( year % 100 is not 0 or year % 400 is 0 )



# ===========================================================
# PROBLEM 19 -- Counting Sundays
# ===========================================================
#
#  You are given the following information, but you may prefer
#  to do some research for yourself.
#
#   * 1 Jan 1900 was a Monday
#   * Thirty days has september,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine
#   * A leap year occurs on any year evenly divisible by 4,
#     but not on a century unless it is divisible by 400
#
#  How many Sundays fell on the first of the month during the
#  twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
#  EXTRA RESEARCH:
#   1 Jan 1901  = Tuesday
#   1 Jan 1902  = Wednesday
#   1 Jan 1903  = Thursday
#   1 Jan 1904  = Friday    ** Leap Year
#   1 Jan 1905  = Sunday (2 day shift instead)
#   1 Feb 1901  = Friday (original shift + (31%7))
#
# ===========================================================
def problem_19( ):
    # NOTES BEFORE STARTING
    #   Consider Sunday to be day 0 of the week
    #   Each year shifts one, except after February on leap years which shift two

    # Print Problem Context
    print( "Project Euler Problem 19 -- Counting Sundays" )

    # Set Up Variables
    start_time     =  default_timer( )
    sundays        =  0
    shift          =  2
    month_lengths  =  {
                            'January'   : 31,
                            'February'  : 28,
                            'March'     : 31,
                            'April'     : 30,
                            'May'       : 31,
                            'June'      : 30,
                            'July'      : 31,
                            'August'    : 31,
                            'September' : 30,
                            'October'   : 31,
                            'November'  : 30,
                            'December'  : 31
                      }

    # Calculation Loop: iterate through each month of each year and count if
    # it's a sunday
    for year in range( 1901 , 2001 ):
        for month in month_lengths:
            # Sunday is day 0, if it 0 shift from day 0, it must be sunday
            if shift % 7 is 0:
                sundays  +=  1
            # Every month causes a shift based on its length
            shift  +=  month_lengths[ month ] % 7

            # If it's febuary on a leap year, count the extra day in the month
            if month is 'February' and is_leap_year( year ):
                shift  +=  1

    # Calculate Execution Time
    end_time        =  default_timer( )
    execution_time  =  ( end_time - start_time ) * 1000

    # Display Results
    print( "   Total Sundays:      %d"      %  sundays )
    print( "   Computation Time:   %.3fms"  %  execution_time )
    return



if __name__ == '__main__':
    problem_19( )