def main():
    level = int(input('1 - выборы в госдуму, 2 - выборы в облдуму, 3 - выборы в гордуму \n'
                      '11 - выборы в госдуму по спискам, 12 - выборы в облдуму по спискам, 13 - выборы в гордуму по спискам \n'))
    district = 11

    if level == 1:
        level_of_elections = 'federal'
        line_of_candidates = 13
    elif level == 2:
        level_of_elections = 'region'
        line_of_candidates = 12
    elif level == 3:
        level_of_elections = 'city'
        line_of_candidates = 12
    if level == 11:
        level_of_elections = 'federal_parties'
        line_of_candidates = 13
    elif level == 12:
        level_of_elections = 'region_parties'
        line_of_candidates = 12
    elif level == 13:
        level_of_elections = 'city_parties'
        line_of_candidates = 12

    if district == 10:
        polling_stations = ['882', '1411', '1412', '1413', '1414', '1415', '1416', '1417', '1418', '1419', '1420',
                            '1423', '1424', '1426', '1433', '1434', '1435', '1436', '1437', '1438', '1439', '1443',
                            '1444', '1445', '1446']
    elif district == 11:
        polling_stations = ['1425', '1447', '1448', '1449', '1450', '1451', '1452', '1453', '1454', '1455', '1456',
                            '1457', '1458', '1459', '1460', '1461', '1462', '1463', '1464', '1465', '1466', '1467',
                            '1468']

    with open(f'data_{district}\\{level_of_elections}\\resaults.csv', 'w') as f2:
        candidates = []
        votes = []
        for station in polling_stations:
            with open(f'data_{district}\\{level_of_elections}\\{station}.txt', 'r') as f1:
                this_candidate = ['']
                this_votes = [[str(station)]]
                for line in f1:
                    if line[:2].isdecimal():
                        if (int(line[:2]) >= line_of_candidates) & (line[-1] != '%') & (line[-2] != '%'):
                            name, count = line[3:].split(f'\t')
                            if count[-1] == '\n':
                                count = count[:-1]
                            this_candidate.append(name)
                            this_votes[0].append(count)

                if this_candidate in candidates:
                    votes[candidates.index(this_candidate)].append(this_votes[0])
                else:
                    candidates.append(this_candidate)
                    votes.append(this_votes)

        # Запись результатов в файл
        for candidates_list in enumerate(candidates):
            for candidate in enumerate(candidates_list[1]):
                if candidate[0] != len(candidates_list[1]) - 1:
                    f2.write(f'{candidate[1]};')
                else:
                    f2.write(f'{candidate[1]}\n')
            for votes_list in votes[candidates_list[0]]:
                for vote in enumerate(votes_list):
                    if vote[0] != len(votes_list) - 1:
                        f2.write(f'{vote[1]};')
                    else:
                        f2.write(f'{vote[1]}\n')


if __name__ == '__main__':
    main()
