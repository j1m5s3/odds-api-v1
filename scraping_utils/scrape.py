import requests
from bs4 import BeautifulSoup


def scrape_nfl_game_lines(url):
    # Make a request to the website
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements containing the game lines
    outcomes = soup.select('.sportsbook-outcome-cell__label-line-container')
    teams = soup.select('.event-cell__name-text')
    odds = soup.select('.sportsbook-odds')

    # Organize outcomes (spread, over/under))
    outcome_arr = []
    for outcome in outcomes:
        current_outcome = outcome.text
        if current_outcome[0] == "O" or current_outcome[0] == "U":
            outcome_over_under = current_outcome[0]
            max_index = len(current_outcome)
            current_outcome = outcome_over_under + ' ' + current_outcome[2:max_index]
            over_under_entry = {"outcome": current_outcome}
            outcome_arr.append({"spread": spread_entry, "over_under": over_under_entry, "money_line": {}})
        else:
            spread_entry = {"outcome": current_outcome}

    # Map odds to outcomes (spread, over/under, money line)
    i = 0
    for outcome in outcome_arr:
        j = 0
        for odd in odds[i:]:
            if j == 0:
                outcome["spread"]["odds"] = odd.text
                i += 1
            if j == 1:
                outcome["over_under"]["odds"] = odd.text
                i += 1
            if j == 2:
                outcome["money_line"]["odds"] = odd.text
                i += 1
                break
            j += 1

    # Map the teams to the odds
    results_dict = {}
    for team, outcome in zip(teams, outcome_arr):
        results_dict[team.text] = outcome

    return results_dict








if __name__ == '__main__':
    scrape_odds()
    pass
