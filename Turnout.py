def main():
    level = int(input('1 - выборы в госдуму, 2 - выборы в облдуму, 3 - выборы в гордуму \n'))
    district = 11

    line_of_voters = f'1\t'
    if level == 1:
        level_of_elections = 'federal'
        line_of_turnout_1 = f'7\t'
        line_of_turnout_2 = f'8\t'
    elif level == 2:
        level_of_elections = 'region'
        line_of_turnout_1 = f'8\t'
        line_of_turnout_2 = f'9\t'
    elif level == 3:
        level_of_elections = 'city'
        line_of_turnout_1 = f'8\t'
        line_of_turnout_2 = f'9\t'

    if district == 10:
        polling_stations = ['882', '1411', '1412', '1413', '1414', '1415', '1416', '1417', '1418', '1419', '1420',
                            '1423', '1424', '1426', '1433', '1434', '1435', '1436', '1437', '1438', '1439', '1443',
                            '1444', '1445', '1446']
    elif district == 11:
        polling_stations = ['1425', '1447', '1448', '1449', '1450', '1451', '1452', '1453', '1454', '1455', '1456',
                            '1457', '1458', '1459', '1460', '1461', '1462', '1463', '1464', '1465', '1466', '1467',
                            '1468']

    with open(f'data_{district}\\{level_of_elections}\\turnout_resaults.csv', 'w') as f2:
        voters = []
        bulletins = []
        for station in polling_stations:
            with open(f'data_{district}\\{level_of_elections}\\{station}.txt', 'r') as f1:
                for line in f1:
                    if line[:2] == line_of_voters:
                        voter = line[line.rfind(f'\t') + 1:]
                        if voter[-1] == '\n':
                            voter = voter[:-1]
                        voters.append(voter)

                    if line[:2] == line_of_turnout_1:
                        bulletin_1 = line[line.rfind(f'\t'):]
                        if bulletin_1[-1] == '\n':
                            bulletin_1 = bulletin_1[:-1]

                    if line[:2] == line_of_turnout_2:
                        bulletin_2 = line[line.rfind(f'\t'):]
                        if bulletin_2[-1] == '\n':
                            bulletin_2 = bulletin_2[:-1]
                        bulletins.append(int(bulletin_1) + int(bulletin_2))

        # Запись результатов в файл
        f2.write(f'№ участка;Избирателй;Проголосовало\n')
        for index, voter in enumerate(voters):
            if index != len(voter) - 1:
                f2.write(f'{polling_stations[index]};{voter};{bulletins[index]}\n')
            #else:
            #    f2.write(f'{polling_stations[index]};{voter};{bulletins[index]}')


if __name__ == '__main__':
    main()
