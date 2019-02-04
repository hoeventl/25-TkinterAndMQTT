# DONE: Copy the code in
#     m1e_mqtt_receiver.py
# as your starting point, pasting its code here.

# Then modify the code so that it receives messages from your
#    m2_tkinter_as_mqtt_sender.py
# module and PRINTS them.
import mqtt_remote_method_calls as com
import time


class DelegateThatReceives(object):

    def forward(self, leftspeed, rightspeed):
        print("Let's move forward", leftspeed, rightspeed)


def main():
    name1 = input("Enter one name (receiver name): ")
    name2 = input("Enter another name (sender name): ")

    my_delegate = DelegateThatReceives()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    while True:
        time.sleep(0.01)  # Time to allow message processing


main()
