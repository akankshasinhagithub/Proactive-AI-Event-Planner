from agents.planner_agent import plan_weekend
from agents.search_agent import find_events
from agents.notifier_agent import notify_user
from memory.user_memory import get_user_preferences


def run():
    prefs = get_user_preferences(user_id="akanksha")
    plan = plan_weekend(prefs)
    events = find_events(plan)
    notify_user(events)


if __name__ == "__main__":
    run()
