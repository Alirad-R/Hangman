import PySimpleGUI as sg

class Hangman:
    def __init__(self):
        layout = [
            [
                self._build_canvas_frame(),
                # self._build_letters_frame()
            ],
            [
                # self._build_guessed_words_frame()
            ],
            [
                # self._build_buttons_frame()
            ]
        ]
        self._window = sg.Window(
            title="Hangman game",
            layout=layout,
            finalize=True,
            margins=(100,10) #width , height
        )
    
    def _build_canvas_frame(self):
        return sg.Frame(
            "Hangman Game",
            layout=[
                [
                    sg.Graph(
                        key= "_Canvas_",
                        canvas_size=(100, 200),
                        graph_bottom_left=(0,400),
                        graph_top_right=(200,0)
                    )
                ]
            ],
            pad=(0,0)
        )

    def read_event(self):
        event = self._window.read()
        event_id = event[0] if event is not None else None
        return event_id
    
    def close(self):
        self._window.close()
        
game = Hangman()
while True:
    event_id = game.read_event()
    if event_id in {sg.WIN_CLOSED}:
        break
game.close()