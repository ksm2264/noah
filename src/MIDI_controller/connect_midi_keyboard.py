
import mido

def connect_usb() -> mido.MidiDevice:
    """
    Connects to the MIDI keyboard via USB and returns a MidiDevice object.

    Returns:
    mido.MidiDevice: An object representing the MIDI keyboard.
    """
    midi_devices = mido.get_input_names()
    for device in midi_devices:
        if 'MIDI keyboard' in device: 
            return mido.open_input(device)
    raise Exception("MIDI keyboard not found, please connect and try again")
