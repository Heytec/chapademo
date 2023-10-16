import streamlit as st
import random
import matplotlib.pyplot as plt

class CrashGame:
    def __init(self):
        self.multiplier = 1.00
        self.crashed = False

    def start_game(self):
        self.multiplier = 1.00
        self.crashed = False

    def update(self):
        if self.multiplier >= 100.00:
            self.crashed = True
        else:
            self.multiplier += random.uniform(0.01, 0.1)

        if self.multiplier < 2.00:
            self.crashed = True
        else:
            if random.random() < 0.05:
                self.crashed = True

    def is_crashed(self):
        return self.crashed

    def get_multiplier(self):
        return self.multiplier

def play_crash_game(bet, auto_stop_multiplier):
    game = CrashGame()
    game.start_game()

    multiplier_values = []  # Create an empty list to store multiplier values

    while not game.is_crashed() and game.get_multiplier() < auto_stop_multiplier:
        game.update()
        multiplier_values.append(game.get_multiplier())  # Append the multiplier value

    crash_multiplier = game.get_multiplier()

    exact_winnings = 0

    if crash_multiplier >= auto_stop_multiplier:
        exact_winnings = bet * auto_stop_multiplier

    if crash_multiplier >= auto_stop_multiplier:
        winnings = exact_winnings
    else:
        winnings = -bet
        game.start_game()

    return winnings, crash_multiplier, exact_winnings, multiplier_values

def display_results(bet, winnings, crash_multiplier, exact_winnings, auto_stop_multiplier, multiplier_values):
    if winnings > 0:
        st.write("You cashed out before the crash. You won {:.2f}.".format(winnings))
        if crash_multiplier < auto_stop_multiplier:
            st.write("You crashed out below your desired multiplier. You lost all your money and the game.")
    else:
        st.write("You lost {}.".format(bet))

    remaining_balance = auto_stop_multiplier * bet

    if crash_multiplier >= auto_stop_multiplier:
        st.write("Your remaining balance: {:.2f}".format(remaining_balance))

    st.write("Exact amount won: {:.2f}".format(exact_winnings))

    # Plot the multiplier values
    plt.plot(multiplier_values)
    plt.xlabel("Time")
    plt.ylabel("Multiplier")
    plt.title("Multiplier Over Time (Crash at Multiplier {:.2f})".format(crash_multiplier))

    # Indicate the crash multiplier on the graph
    plt.axhline(y=crash_multiplier, color='red', linestyle='--', label='Crash Multiplier')
    plt.legend()

    st.pyplot(plt)

def main():
    st.title("Chapagame  Game Simulation")

    st.write(" This game demo is designed to test the algorithm. ")

    bet = st.number_input("Enter your bet amount:", min_value=20.0, step=1.0)
    auto_stop_multiplier = st.number_input("Enter your desired auto cash out multiplier:", min_value=1.0, step=0.1)

    if st.button("Play Game"):
        winnings, crash_multiplier, exact_winnings, multiplier_values = play_crash_game(bet, auto_stop_multiplier)
        display_results(bet, winnings, crash_multiplier, exact_winnings, auto_stop_multiplier, multiplier_values)

if __name__ == "__main__":
    main()


