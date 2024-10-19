import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key="Put you Open AI api",
)

# should be the same name or number you wanna chat with
def is_last_message_from_sender(chat_log, sender_name="Name ore number"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("]")[-1]
    if sender_name in messages:
        return True
    return False

    # Step 1: Click on the chrome icon at coordinates (1639, 1412)


pyautogui.click(680, 873)

#select the search bar
pyautogui.click(145, 81)
time.sleep(1)

#o search fr the given number ENTER THE NUMBER
pyautogui.typewrite("name or number")
time.sleep(3)

# click on the number
pyautogui.click(184,185)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo( 400, 131)
    pyautogui.dragTo(1168,793, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('command', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(1194, 781)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": " give short responses. do not include senders name in chat You are a person named Gagan who speaks hindi little bit english. You are from Indiaand you are a internationl student. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only) with small text"},
                {"role": "system", "content": "Do not start like this 12/7/2024, 2:39:42PM] Gagan: "},
                {"role": "user", "content": chat_history}
            ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(536, 811)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('command', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')