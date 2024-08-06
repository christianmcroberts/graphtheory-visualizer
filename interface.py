import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import os

class App:
    sidebar: 'Sidebar'

    root  = tk.Tk()
    root.geometry=('600x600')

    def __init__(self, graph_types = {'Cycle': nx.cycle_graph, 'Path': nx.path_graph, 'Complete': nx.complete_graph,
                                      'Wheel': nx.wheel_graph, 'Star': nx.star_graph, 'Ladder': nx.ladder_graph,
                                      'Binomial': nx.binomial_tree, 'Circular Ladder': nx.circular_ladder_graph}):
        self.root.title('Graph Visualizer')
        self.sidebar = Sidebar(self.root, graph_types.keys())
        self.submit_button = tk.Button(self.root,  text='Submit',command = self.create_image).grid(row=4,column=0)
        self.close_button = tk.Button(self.root, text='Close',command=self.root.destroy).grid(row=4,column=1)
        self.root.mainloop()

    def create_image(self): 
        graph_type = None
        num_vertices = None
        for i in self.sidebar.graph_options_listbox.curselection():
            graph_type = self.sidebar.graph_options_listbox.get(i)
        num_vertices = self.sidebar.num_vertices.get()
        if graph_type == None:
            print('Graph type must be provided!')
            pass
        self.image = Images(self.root, graph_type, num_vertices)

class Sidebar:
    # Declare variable for number of vertices
    num_vertices = None

    # Label vertex question and srovide space for Entry

    question_label = None
    num_vertices_entry = None

    # Label graph type question

    graph_options_label: None

    graph_options_listbox = None
                              
    # Create a textbox for the graph visualization
   

    def __init__(self, root, graph_types):
        self.num_vertices = tk.IntVar()
        self.question_label = tk.Label(root,text='How many vertices?').grid(row=0,column=0)
        self.num_vertices_entry = tk.Entry(root, textvariable=self.num_vertices).grid(row=1,column=0)
        self.graph_options_label = tk.Label(root,text='Select Graph Type:').grid(row=2,column=0)
        self.graph_options_listbox = tk.Listbox(root)
        self.graph_options_listbox.grid(row=3, column=0)
        self.add_item(graph_types)

    def add_item(self, items_to_add):
        for idx, item in enumerate(items_to_add):
            self.graph_options_listbox.insert(idx,item)
        
class Images:
    def __init__(self, root, graph_type, num_vertices):
        self.graph_type = graph_type
        self.num_vertices = num_vertices
        self.create_image(root)
        
    def create_image(self, root,graph_types = {'Cycle': nx.cycle_graph, 'Path': nx.path_graph, 'Complete': nx.complete_graph,
                                               'Wheel': nx.wheel_graph, 'Star': nx.star_graph, 'Ladder': nx.ladder_graph,
                                               'Binomial': nx.binomial_tree, 'Circular Ladder': nx.circular_ladder_graph}):
        fig = plt.figure()
        nx.draw_networkx(graph_types[self.graph_type](self.num_vertices),)
        
        image_path = os.path.dirname(__file__)+ '/' + 'Graph.png'
        
        fig.savefig(image_path)

        image = Image.open(image_path)
        image = image.resize((250,250),Image.Resampling.LANCZOS)

        photo_image = ImageTk.PhotoImage(image)

        graph_display = tk.Label(root,image=photo_image,bg='light cyan')
        graph_display.image = photo_image
        graph_display.grid(row=0,column=1,columnspan=1,rowspan=4)

def main():
    app = App()
    
if __name__ == "__main__":
    main()

