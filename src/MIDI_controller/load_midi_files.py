# Define the MIDI_controller module
class MIDI_controller:
    # Define the load_midi_files sub-component
    def load_midi_files(self):
        # Function that loads the desired piano MIDI file to be played as the user's input.
        def select_piano_track():
            # Function that allows the user to select the desired piano track to be played.
            user_input = input("Please select the piano track you want to play: ")
            return user_input
        
        def load_piano_track(piano_track):
            # Function that loads the selected piano track to be played during the game.
            try:
                with open(piano_track, 'r') as file:
                    data = file.read()
                    print(f"{piano_track} loaded successfully!")
                    return data
            except:
                print(f"Unable to load {piano_track}")
                
        # return the functions in a list of dictionaries as requested
        return [{'select_piano_track': select_piano_track}, {'load_piano_track': load_piano_track}]
