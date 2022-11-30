alert_failure_count = 0
alert_pass_count = 0
total_count = 0 

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    global total_count
    total_count += 1

    return celcius

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        print("An error happend \n")
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        # print(celcius)
        global alert_failure_count
        alert_failure_count += 1

    else:
        print("Exact measurement done \n")
        global alert_pass_count
        alert_pass_count += 1



alert_in_celcius(400.5)
alert_in_celcius(303.6)
alert_in_celcius(392)
alert_in_celcius(650)


total_alerts = alert_pass_count + alert_failure_count
#print(total_alerts)
#print(total_count)
print(f'{total_alerts} total alerts.\n')
print(f'{alert_failure_count} alerts failed. \n')
print(f'{alert_pass_count} alerts Passed. \n')

assert total_count == total_alerts
print('All is well (maybe!)')
