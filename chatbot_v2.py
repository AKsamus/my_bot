#importing required custom modules
from mode import Mode
from communication import Communication

#invoking classes
speaker = Communication()
listen_to_mode = Mode()

#listens to what mode needs to be invoked
curr_mode = speaker.listen(listen_to_mode)

#if selected mode is not exit below code will run
if curr_mode:
    bot_data = speaker.listen(curr_mode)


