def formTeams(students):

    teams = { 1: [], 2: [], 3: [] }

    # encode the students into the dict
    for i in range(len(students)):
        if students[i] == 1:
            teams[1].append(i+1)
        elif students[i] == 2:
            teams[2].append(i+1)
        elif students[i] == 3:
            teams[3].append(i+1)
    
    number_of_teams = min(len(teams[1]), len(teams[2]), len(teams[3]))

    return number_of_teams, teams
    

if __name__ == '__main__':
    n = int(input())

    students = list(map(int, input().split()))

    # print number of teams
    number_of_teams, teams = formTeams(students)
    
    
    # each team consistes of 3 students
    print(number_of_teams)
    
    # print indecies
    for i in range(number_of_teams):
        print(teams[1][i], teams[2][i], teams[3][i])
    print()