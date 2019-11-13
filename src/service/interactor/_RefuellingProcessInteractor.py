

class RefuellingProcessInteractor(object):

    def on_rfid_detect(self, identificator: str):
        print(identificator)

    def on_pump_handle(self):
        pass

    def on_pulser_change(self):
        pass
