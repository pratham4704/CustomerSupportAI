from memory import save_conversation
from memory import get_previous_issue

save_conversation(
    "David",
    "I have a billing issue",
    "Billing Agent responded."
)

print(get_previous_issue("David"))