# https://docs.google.com/document/d/194fbAihNt-eGbEEuEMN-mrIsVsrHuvaXISf4kUkyVhA/edit link to project brainstorm

import random
import time
from pygame import mixer
from datetime import datetime

goals_list = []
activities_list = []
breathing_sessions = []


def show_summary():
    print()
    get_summary = str(input("To get your daily summary, press enter "))
    print("On:", datetime.today().strftime("%b-%d-%Y"))
    print("At:", datetime.now().strftime("%H:%M:%S"))
    print()
    print("Goals: ")
    print(goals_list[0])
    print()
    print("Activity Summary")
    print(activities_list[0])
    print()
    print("Breathing session length: ")
    print(str(breathing_sessions[0]) + " Seconds")


def countdown(t):
    mixer.init()
    mixer.music.load("wave_sounds.mp3")
    mixer.music.play()
    while t:
        minutes = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(minutes, secs)
        print(f'\r{timer}')
        time.sleep(1)
        t -= 1
    mixer.music.stop()
    print('Breathing exercise is finished.')


def breathing_exercise():
    print()
    print("Focused breathing is one of the simplest, yet most effective methods of meditation. It allows you to clear \
your mind and refocus your energy.")
    length = int(input("Enter the desired length of time for your breathing session in seconds (recommended >180): "))
    countdown(length)
    breathing_sessions.append(length)


def make_goals():
    print()
    print("It is important to have an idea of what your day schedule will look.")
    goals = str(input("What do you plan to do today? Try to list 3 goals: "))
    goals_list.append(goals)


# def get_quote():


def activities():
    print()
    print("Reflection Activity:")
    fear_question = "Name a fear that is holding you back from doing something you wish to do? If you wish to conquer\n\
this fear, create a list of steps of which may allow you to. If you don't wish to, write down the reasons why. "
    gratitude_question = "Name three things you are grateful for today? "
    death_question = "If you were to die today, what would you spend your last 24 hours doing? "
    act_of_kindness = "Plan one act of kindness you intend on accomplishing today. "
    conflict_question = "Think about a recent conflict you had. What caused this conflict? Try to perceive this\n\
conflict from the other person's point of view. Explain why both parties may have been right from their perspective. "
    stress_question = "Where is your main source of stress derived from? Is it necessary to take on this stress? \n\
How might you be able to reduce it? "
    questions = [fear_question, gratitude_question, death_question, act_of_kindness, conflict_question, stress_question]
    random_question = questions[random.randint(0, (len(questions) - 1))]
    activity_answer = str(input(random_question))
    activities_list.append("Question: " + random_question + "\nAnswer: " + activity_answer)


def run_bot():
    print()
    print()
    print("Meet Reflect Bot, a bot specialized for self-reflection and bringing more productivity into your life.")
    start = str(input("To start, press enter "))
    make_goals()
    activities()
    breathing_exercise()
    show_summary()


if __name__ == '__main__':
    run_bot()
