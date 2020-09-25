# INDIAN = can only withdraw 200 laddus per month
# NON_INDIAN = can only withdraw 400 laddus per month
# CONTEST_WON rank; rank = range(1,5000) & (rank > 20 -> 300 laddus) & (rank < 20 -> 300 + (20 - rank) laddus)
# TOP_CONTRIBUTOR -> 300 laddus
# BUG_FOUND severity; severity = range(50,1000) & (50 to 1000) laddus
# CONTEST_HOSTED -> 50 laddus

def checkout_amount(origin, accumulated_amount):
    if origin == 'INDIAN':
        number_of_months = accumulated_amount/200
        print(int(number_of_months))
    elif origin == 'NON_INDIAN':
        number_of_months = accumulated_amount/400
        print(int(number_of_months))

def laddu_for_contest_won(rank):
    if int(rank) < 20:
        return 300 + (20 - int(rank))
    elif int(rank) > 20 & int(rank) < 5000:
        return 300

def laddu_for_top_contribution():
    return 300

def laddu_for_bug_found(severity):
    return int(severity)

def laddu_for_contest_hosting():
    return 50

testcases = int(input())
if testcases > 1 & testcases < 100:
    for test in range(testcases):
        activities, origin = input().split()
        if int(activities) > 1 & int(activities) < 100:
            accumulated_amount = 0
            for activity in range(int(activities)):
                list_activities = list(input().split())
                activity_type = list_activities[0]
                if activity_type == 'CONTEST_WON':
                    rank = list_activities[1]
                    accumulated_amount += laddu_for_contest_won(rank)
                elif activity_type == 'TOP_CONTRIBUTOR':
                    accumulated_amount += laddu_for_top_contribution()
                elif activity_type == 'BUG_FOUND':
                    severity = list_activities[1]
                    accumulated_amount += laddu_for_bug_found(severity)
                elif activity_type == 'CONTEST_HOSTED':
                    accumulated_amount += laddu_for_contest_hosting()
            checkout_amount(origin, accumulated_amount)
        else:
            exit()
else:
    exit()