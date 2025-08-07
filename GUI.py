from tkinter import *
class GUI:
    def __init__(self, map, agent):
        self.current_step = 0
        self.map = map
        self.agent = agent
        self.window = Tk()
        self.window.title("Wumpus World")
        self.window.geometry("800x600")
        self.cell_size = 100
        self.canvas = Canvas(self.window, width=800, height=600)
        self.canvas.pack()
        frame = Frame(self.window, bg='white')
        frame.place(relx=1, rely=1, relwidth=0.25, relheight=0.25)

    def draw_agent(self):
        row = 3
        col = 0

        x1 = col * self.cell_size + 10
        y1 = row * self.cell_size + 10
        x2 = x1 + self.cell_size - 20
        y2 = y1 + self.cell_size - 20

        self.agent_shape = self.canvas.create_oval(x1, y1, x2, y2, fill='pink')#agent shape is oval

    def move_agent_step(self):
        if self.current_step < len(self.agent.agent_path):
            x, y = self.agent.agent_path[self.current_step]
            x1 = y * self.cell_size + 10
            y1 = x * self.cell_size + 10
            x2 = x1 + self.cell_size - 20
            y2 = y1 + self.cell_size - 20

            self.canvas.coords(self.agent_shape, x1, y1, x2, y2)
            self.current_step += 1


            self.window.after(1000, self.move_agent_step)

    def agent_move(self):
        self.draw_agent()
        self.window.after(1000, self.move_agent_step)

    def create_map(self):
        for row in range(4):
            for col in range(4):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                tile = self.map[row][col]
                fill_color = 'white'
                if tile.pit:
                    fill_color = 'brown'
                elif tile.wumpus:
                    fill_color = 'purple'
                elif tile.gold:
                    fill_color = 'yellow'

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline='black')

                if tile.wind:
                    self.canvas.create_text(x1 + 25, y1 + 25, text='W', fill='blue', font=('Arial', 20, 'bold'))
                if tile.stench:
                    self.canvas.create_text(x1 + 75, y1 + 25, text='S', fill='green', font=('Arial', 20, 'bold'))
                if tile.glitter:
                    self.canvas.create_text(x1 + 50, y1 + 75, text='G', fill='yellow', font=('Arial', 20, 'bold'))

    def run(self):
        self.create_map()
        self.agent_move()
        self.window.mainloop()
